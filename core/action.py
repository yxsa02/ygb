from .app import data

class action:
    def __init__(self,activity): 
        self.activity = activity
        self.uim = activity.uim
        self.udata:data.UData = activity.udata
        self.ig:data.groups = activity.itemGroups
        self.geter = activity.geter
        self.meta = {"exit":{"desc":"退出程序","f":self.exit},
            "test":{"desc":"测试功能","f":self.test},"gvbi":{"desc":"getVideoByBvid","f":self.getVideoByBvid}}
    def test(self,p):
        if  self.ig() == None:
            self.activity.status = "没有项组"
            return
        for i in self.geter.VG():
            self.activity.status = f"正在添加第{i}个视频"
            self.ig().addItem(i) # type: ignore
        self.uim.Wmain.updateList()
    def exit(self,p):
        self.activity.status = "exit"
    def getVideoByBvid(self,p):
        vi = self.geter.videoInfo(p['bvid'])
        i = self.ig()
        if i:
            i.addItem(vi)
            self.uim.Wmain.updateList()

