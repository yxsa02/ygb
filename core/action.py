from typing import TYPE_CHECKING
from . import data
import re
if TYPE_CHECKING:
    from app import activity as ActivityType
    from gui import uio as UIOType

class action:
    def __init__(self,activity:"ActivityType"): 
        self.activity = activity
        self.uio:"UIOType" = activity.uio
        self.udata:data.UData = activity.udata
        self.ig:data.groups = activity.itemGroups
        self.geter = activity.geter
        self.meta = {"exit":{"desc":"退出程序","f":self.exit},"gvbh":{"desc":"推荐","f":self.getVideoByH},
            "test":{"desc":"测试功能","f":self.test},"gvbi":{"desc":"getVideoByBvid","f":self.getVideoByBvid},
            "info":{"desc":"显示信息","f":self.showInfo},"seav":{"desc":"搜索视频","f":self.searchVideo}}
    def test(self,p):
        if  self.ig() == None:
            self.activity.status = "没有项组"
            return
        ta = self.geter.VG()
        if ta == None:
            return
        for i in ta:
            self.activity.status = f"正在添加第{i}个视频"
            self.ig().addItem(i) # type: ignore
        self.uio.Wmain.updateList()
    def exit(self,p):
        self.activity.status = "exit"
    def getVideoByBvid(self,p):
        if p["bvid"][:2] == "BV" and len(p["bvid"]) == 12:
            bvid = p["bvid"]
        else:
            bvid = re.search(r"BV[0-9A-Za-z]{10}",p["bvid"])
        vi = self.geter.videoInfo(bvid)
        self.ig().addItem({"bvid":bvid,"title":vi['title'],"desc":vi['desc'],"pic":vi['pic'],"upname":vi['owner']['name'],"upid":vi['owner']['mid']})
        self.uio.Wmain.updateList()
    def getVideoByH(self,p):
        for i in self.geter.VG(p.get("ps",10)): # type: ignore
            self.ig().addItem(i) # type: ignore
        self.uio.Wmain.updateList()
    def showInfo(self,p):
        self.uio.Wmain.ui.info.clear()
        self.ig().setChosing(p['key'])
        r = self.ig().indexItem(p['key'])
        if r == None:
            self.activity.status = f"没有找到bvid:{p['key']}的项"
            return
        #self.uio.Wmain.ui.info.addItems([f""])
        self.uio.Wmain.ui.info.addItem(f"标题:{r['title']}")
        self.uio.Wmain.ui.info.addItem(f"作者:{r['upname']}(作者ID:{r['upid']})")
        #self.ui.info.addItem(str(api.get_Vtag(self.Vitems.chosingVi,headers=self.config.headers)))
        #self.uio.Wmain.ui.info.addItem(f"简介:{r['desc']}")
        #self.uio.Wmain.ui.info.addItem(f"时长:{r['duration']}|观看次数:{r['view']}")
        self.uio.Wmain.ui.info.addItem(f"bvid:{p['key']}")
        self.uio.Wmain.showpic(self.ig().indexItem(p['key'],"pic"))
    def searchVideo(self,p):
        if p.get("keyword") == None:
            self.activity.status = "没有输入搜索关键字"
            return
        r = self.geter.search(p["keyword"],p.get("pn",1))
        print(r)
        for i in r:
            self.ig().addItems(i) # type: ignore
        self.uio.Wmain.updateList()
    
