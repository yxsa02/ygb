import json, os, sqlite3
#from typing import Any

class UData:
    """用户数据类，用于管理用户配置数据"""
    configTemplate = {
            "defaultDir": "~",
            "downloadPath": "",
            "usedDownloadPath": [],
            "downloadSaveType": "",
            "transcodeAudio": True
        }
    def __init__(self,path):
        self.path = path
        self.loadConfig()
        self.loadBox()
    def loadBox(self):
        """加载数据"""
        self.box = sqlite3.connect(os.path.join(self.path, 'box.db'))
        with self.box:
            self.box.execute('''CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )''')
            self.box.execute('''CREATE TABLE IF NOT EXISTS mBox (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )''')
    def loadConfig(self):
        """加载配置数据"""
        try:
            with open(os.path.join(self.path, 'config.json'), 'r', encoding='utf-8') as f:
                fd = json.load(f)
            for key, value in self.configTemplate.items():
                fd.setdefault(key, value)  
        except json.decoder.JSONDecodeError:
            raise ValueError(f"[E] 配置文件格式错误: {self.path}/config.json")       
        except FileNotFoundError:
            fd = self.configTemplate.copy()
            with open(os.path.join(self.path, 'config.json'), 'w', encoding='utf-8') as f:
                json.dump(fd,f, indent=4, ensure_ascii=False)
        self.__config = fd
    def saveConfig(self):
        """保存配置数据"""
        with open(os.path.join(self.path, 'config.json'), 'w', encoding='utf-8') as f:
            json.dump(self.__config,f, indent=4, ensure_ascii=False)
    def getConfig(self, key=None):
        """获取配置数据"""
        if key is None:
            return self.__config
        return self.__config.get(key, None)
    def setConfig(self, key, value):
        """设置配置数据"""
        self.__config[key] = value
    def getBox(self):
        """获取数据"""
        return self.box
    
class items:
    """项组类，用于管理一组具有相同结构的项"""
    def __init__(self,key,tag):
        """
        初始化项组
        :param key: 项组的键表，第一个键为主键
        :param tag: 项组的标签
        """
        self.tag = tag
        if len(set(key)) != len(key):
            raise ValueError(f"[E][{self.tag}]项组有键重复")
        for k in key:
            if not k:  # 空字符串检查
                raise ValueError(f"[E][{self.tag}]项组有键为空")
            if k[0].isdigit():
                raise ValueError(f"[E][{self.tag}]项组键不能以数字开头: {k}")
            # 可选：检查是否包含特殊字符
            if not k.isidentifier():  # Python内置方法，检查是否为合法标识符
                raise ValueError(f"[E][{self.tag}]项组键无效: {k}")
        self.__key = key
        self.__allItem = {}
        self.__chosenItem = []
        self.__chosingItem = ""
    def __repr__(self):
        return f"<Items tag={self.tag} count={len(self.__allItem)}>"
    def __iter__(self):
        return iter(self.__allItem.values())
    def __len__(self):
        return len(self.__allItem)
    def addItem(self, item):
        """
        添加项到项组
        :param item: 项，必须是字典，且包含所有键
        """
        if not isinstance(item, dict):
            raise ValueError(f"[E][{self.tag}]项必须是字典")
        for k in self.__key:
            if k not in item:
                raise ValueError(f"[E][{self.tag}]项缺少键: {k}")
        main_key = item[self.__key[0]]
        if main_key in self.__allItem:
            raise ValueError(f"[E][{self.tag}]项主键重复: {main_key}")
        self.__allItem[main_key] = item
    def clear(self):
        """
        清空项组
        """
        self.__allItem.clear()
        self.__chosenItem.clear()
        self.__chosingItem = ""
    def choose(self, item=None, dotype=None):
        """
        选择项
        :param item: 项的主键，或项的索引，或项的列表
        :param dotype: True表示选择，False表示取消选择，None表示切换选择状态
        """
        if item is None:
            # 如果没有传入item，全选/全不选
            if len(self.__chosenItem) == len(self.__allItem):
                # 如果已经全选，则全不选
                self.__chosenItem.clear()
            else:
                # 否则全选
                self.__chosenItem = list(self.__allItem.keys())
            return
        if isinstance(item, int):
            # 如果是索引，获取对应的主键
            main_key = list(self.__allItem.keys())[item]
            self.choose(main_key, dotype)
        elif isinstance(item, list):
            for i in item:
                self.choose(i, dotype)
        elif isinstance(item, str):
            if dotype is False:
                # 明确取消选择
                if item in self.__chosenItem:
                    self.__chosenItem.remove(item)
            elif dotype is True:
                # 明确选择
                if item not in self.__chosenItem:
                    self.__chosenItem.append(item)
            else:
                # 默认切换选择状态
                if item in self.__chosenItem:
                    self.__chosenItem.remove(item)
                else:
                    self.__chosenItem.append(item)
    def delete(self, item=None):
        """
        删除项
        :param item: 项的主键，或项的索引，或项的列表
        """
        if item is None:
            # 删除全部项中主键在被选项中的所有项
            if self.__chosingItem in self.__chosenItem:
                self.__chosingItem = ""
            self.__allItem = {k: v for k, v in self.__allItem.items() if k not in self.__chosenItem}
            self.__chosenItem.clear()
            return
        if isinstance(item, int):
            # 如果是索引，获取对应的主键
            main_key = list(self.__allItem.keys())[item]
            self.delete(main_key)
        elif isinstance(item, list):
            for i in item:
                self.delete(i)
        elif isinstance(item, str):
            if item in self.__allItem:
                del self.__allItem[item]
                if item in self.__chosenItem:
                    self.__chosenItem.remove(item)
                if item == self.__chosingItem:
                    self.__chosingItem = ""
    def getChosen(self, key=None):
        """
        获取被选项的值
        :param key: 键，或键的索引，或None表示获取所有被选项
        :return: 被选项的值列表
        """
        if key is None:
            return [self.__allItem[k] for k in self.__chosenItem]
        if isinstance(key, int):
            key = self.__key[key]
        if key not in self.__key:
            raise ValueError(f"[E][{self.tag}]键无效: {key}")
        return [self.__allItem[k][key] for k in self.__chosenItem]
    def getAll(self, key=None):
        """
        获取所有项的值
        :param key: 键，或键的索引，或None表示获取所有项
        :return: 所有项的值列表
        """
        if key is None:
            return list(self.__allItem.values())
        if isinstance(key, int):
            key = self.__key[key]
        if key not in self.__key:
            raise ValueError(f"[E][{self.tag}]键无效: {key}")
        return [v[key] for v in self.__allItem.values()]
    def getChosing(self):
        """
        获取当前正在选择的项的主键
        :return: 当前正在选择的项的主键
        """
        return self.__chosingItem
    def setChosing(self, item):
        """
        设置当前正在选择的项的主键
        :param item: 项的主键
        """
        if item not in self.__allItem:
            raise ValueError(f"[E][{self.tag}]项不存在: {item}")
        self.__chosingItem = item
    def update(self, main_key, key, value):
        """更新指定项的字段"""
        if main_key not in self.__allItem:
            raise ValueError(f"[E][{self.tag}]项不存在: {main_key}")
        if key not in self.__key:
            raise ValueError(f"[E][{self.tag}]键无效: {key}")
        self.__allItem[main_key][key] = value

class groups:
    """组类，用于管理一组项组"""
    def __init__(self):
        self.__now = ""
        self.__all = {}
    def __repr__(self):
        return f"<Groups count={len(self.__all)}>"
    def __call__(self, tag=None) -> items|None:
        if tag ==None:
            tag = "_"
        return self.__all.get(tag)
    def __getitem__(self,key) -> items|None:
        return self.__all.get(key)
    def addItems(self,i:items,tag=None):
        """
        添加项组到组
        :param i: 项组
        """
        if not isinstance(i, items):
            #raise ValueError("[E][Groups]添加的对象不是项组")
            return False
        if i.tag in self.__all:
            raise ValueError(f"[E][Groups]项组标签重复: {i.tag}")
        if tag == None:
            self.__all[i.tag] = i
        else:
            self.__all[tag] = i
    def getItems(self, tag):
        """
        获取指定标签的项组
        :param tag: 项组的标签
        :return: 指定标签的项组
        """
        return self.__all.get(tag,False)
    def changeNow(self,tag):
        if tag in self.__all:
            self.__now = tag


if __name__ == "__main__":
    u =UData("D:/y/pj/p/ygbp/data")
    u.saveConfig()
    i = items([''],'')
    