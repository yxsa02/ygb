from . import get

class activity:
    def __init__(self,uim,udata,vi):
        """activity class
        """
        self.uim = uim(self)
        self.udata = udata
        self.vi = vi
        self.geter = get.get(udata.getConfig())
        self.action = action(self)
        self.uim.start()
        self.status = "running"
        self.event = []
        self.loop()
    def loop(self):
        while self.status == "running":
            for e in self.event:
                self.doTask(e)
                self.event.remove(e)
            #self.uim.loop()
    def doTask(self, task):
        try:
            if task['id'] in self.action.meta:
                self.action.meta[task['id']]["f"](self.action)
            else:
                print(f"[E]未知任务: {task}")
        except Exception as e:
            print("[E]失败"+e)
    def addTask(self, task):
        self.event.append({"id":task})
    
class action:
    
    def __init__(self,activity):
        self.activity = activity
        self.uim = activity.uim
        self.udata = activity.udata
        self.vi = activity.vi
        self.geter = activity.geter
        self.meta = {"exit":{"desc":"退出程序","f":self.exit},"test":{"desc":"测试功能","f":self.test}}
    def test(self):
        print("test")
    def exit(self):
        self.activity.status = "exit"
    def getVideoByBvid(self,bvid):
        #self.vi.
        pass

