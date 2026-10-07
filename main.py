import sys, gui,time
from core import app, data
from threading import Thread

class t(Thread):
    def __init__(self,activity:app.activity) -> None:
        self.a = activity
        super().__init__()
        pass
    def run(self):
        print("hi,test!")
        self.a.addTask("gvbh")
        time.sleep(4)
        print("OK:"+str(self.a.itemGroups().getAll("title"))) # type: ignore
        print(self.a.itemGroups().getAll("bvid")) # type: ignore
        self.a.addTask("exit")

if __name__ == "__main__":
    args = sys.argv[1:]
    if "-t" in args:
        d = data.UData("data")
        vi = data.groups()
        vi.addItems(data.items(['bvid','title','pic','upid'],"_"))
        a = app.activity(gui.guiApp, d, vi)
        print()
    else:
        d = data.UData("data")
        vi = data.groups()
        vi.addItems(data.items(['bvid','title','pic','upid'],"_"))
        a = app.activity(t, d, vi)