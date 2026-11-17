from . import get,data,downloader
from .action import action
import time
#from functools import wraps

class activity:
    def __init__(self,uio,udata:data.UData,ig:data.groups):
        """activity class
        """
        self.uio = uio(self)
        self.udata = udata
        self.itemGroups = ig
        self.geter = get.get(udata.getConfig())
        self.downloader = downloader.dlThreads(self)
        self.action = action(self)
        self.uio.start()
        self.status = "running"
        self.event = []
        self.loop()
    def loop(self):
        while self.status == "running":
            for e in self.event:
                try:
                    self.doTask(e)
                    self.event.remove(e)
                except Exception as e:
                    print(f"[E]任务失败:{e}")
            time.sleep(0.01)
            #self.uim.loop()
    def doTask(self, task:dict):
        try:
            if task['id'] in self.action.meta:
                self.action.meta[task['id']]["f"](task.get("p",{}))
            else:
                print(f"[E]未知任务: {task}")
        except Exception as e:
            print(f"[E]失败:{e}")
    def addTask(self, task:str,p:dict={}):
        self.event.append({"id":task,"p":p})

    
