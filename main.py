import sys, gui
from core import app, data

if __name__ == "__main__":
    args = sys.argv[1:]
    if "-t" in args:
        d = data.UData("data")
        vi = data.items(['bvid','title','pic','autor'],"videoItems")
        a = app.activity(gui.guiApp, d, vi)
        print()