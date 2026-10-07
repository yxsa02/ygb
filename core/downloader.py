import threading,requests,os,re,subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import activity as ActivityType

class dlThread:
    """下载线程"""
    def __init__(self,app:ActivityType) -> None:
        self.app = app
        self.task = []
        self.config = {"tempDir":"","downloadPath":"","isReecode":False,"isMerge":True}
        try:
            subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
            self.ff = True
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.ff = False
        self.threads = ThreadPoolExecutor(max_workers=4)
        #self.threads.
    
class dlVideoItem:
    """视频下载"""
    def __init__(self,thread:dlThread,bvid:str,st:str,name=None,cid:int|None=None) -> None:
        self.bvid = bvid
        self.thread = thread
        self.title = name
        self.cid = cid
        self.st = st
        self.did = []
        self.now = ""
        self.dealPath()
        self.readTask()
    def readTask(self):
        self.task:list = [self.getURL]
        if "a" in self.st or "w" in self.st:
            self.task.append(self.downloadAudio)
            if self.thread.config["isReecode"]:
                self.task.append(self.recodeAudio)
        if "v" in self.st or "w" in self.st:
            self.task.append(self.downloadVideo)
        if "w" in self.st:
            self.task.append(self.mergeVideo)
    def dealPath(self): 
        if self.title is None or self.cid is None:
            i = self.thread.app.geter.videoInfo(self.bvid)
            if self.title is None:
                self.title = i['title']
            self.cid = i['cid']
        if "a" in self.st:
            if self.thread.config['isReecode']:
                self.aPath = os.path.join(self.thread.config['tempDir'],make_filename(f"{self.title}.mp3"))
            else:
                self.aPath = os.path.join(self.thread.config['downloadPath'],make_filename(f"{self.title}.mp3"))
        else:
            self.aPath = os.path.join(self.thread.config['tempDir'],make_filename(f"{self.title}.mp3"))
        if "v" in self.st:
            self.vPath = os.path.join(self.thread.config['downloadPath'],make_filename(f"{self.title}.mp4"))
        else:
            self.vPath = os.path.join(self.thread.config['tempDir'],make_filename(f"{self.title}.mp4"))
    def getURL(self):
        self.now = "getURL"
        i = self.thread.app.geter.Vurl(self.did,self.cid)
        if 'dash' in i:
            v = i['dash']['video']
            v.sort(key=lambda x: x.get('bandwidth', 0), reverse=True)
            if v:
                self.vUrl = v[0].get('baseUrl')
        elif 'durl' in i:
            if i['durl']:
                self.vUrl = i['durl'][0].get('url')
            else:
                self.vUrl = None
        else:
            self.vUrl = None
        #获取最佳质量的音频URL
        if 'dash' in i:
            audios = i['dash']['audio']
            audios.sort(key=lambda x: x.get('bandwidth', 0), reverse=True)
            if audios:
                self.aUrl = audios[0].get('baseUrl')
            else:
                self.aUrl = None
        self.did.append("getURL")
    def downloadVideo(self):
        self.now = "downloadVideo"
        if self.vUrl is None:
            return
        response = self.thread.app.geter.session.get(self.vUrl, stream=True)
        response.raise_for_status()
        totalSize = int(response.headers.get('content-length', 0))
        downloadedSize = 0
        with open(self.vPath,'wb') as file:
            toLastUpdateP = 0
            for data in response.iter_content(chunk_size=2048):
                downloadedSize += file.write(data)
                toLastUpdateP += 1
                if totalSize > 0 and toLastUpdateP > 5:
                    progress = int((downloadedSize / totalSize) * 100)
                    #self.pg_update(self.pgg,progress)
    def downloadAudio(self):
        self.now = "downloadAudio"
        if self.aUrl is None:
            return
        response = self.thread.app.geter.session.get(self.aUrl, stream=True)
        response.raise_for_status()
        totalSize = int(response.headers.get('content-length', 0))
        downloadedSize = 0
        with open(self.aPath,'wb') as file:
            toLastUpdateP = 0
            for data in response.iter_content(chunk_size=2048):
                downloadedSize += file.write(data)
                toLastUpdateP += 1
                if totalSize > 0 and toLastUpdateP > 5:
                    progress = int((downloadedSize / totalSize) * 100)
                    #self.pg_update(self.pgg,progress)
    def recodeAudio(self):
        """音频处理"""
        cmd = ['ffmpeg','-i',self.aPath,os.path.join(self.thread.config['downloadPath'],make_filename(f"{self.title}.mp3"))]
        result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            #os.remove(path)
            print(f"[I]音频处理完成:{self.title}.mp3")
        else:
            print(f"[E]音频处理失败，返回码: {result.returncode}")
    def mergeVideo(self):
        #合并视频和音频
        try:
            # 使用ffmpeg合并，并忽略所有输出
            cmd = [
                'ffmpeg', '-y',  # -y 覆盖输出文件
                '-i', self.vPath,'-i', self.aPath,
                '-c', 'copy',  # 直接复制流，不重新编码
                os.path.join(self.thread.config['downloadPath'],make_filename(f"{self.title}.mp4"))
            ]
            # 重定向输出到NULL，避免编码问题
            result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result.returncode == 0:
                print(f"[I]合并完成:{self.title}.mp4")
                return True
            else:
                print(f"[E]合并失败,返回码: {result.returncode}")
                return False
        except Exception as e:
            print(f"[E]合并视频音频时出错: {e}")
            return False

def make_filename(filename):
    """创建安全的文件名（解决中文路径问题）"""
    # 移除Windows文件名中的非法字符
    illegal_chars = r'[<>:"/\\|?*\x00-\x1f]'
    filename = re.sub(illegal_chars, '_', filename)
    # 移除首尾空格和点
    filename = filename.strip().strip('.')
    # 限制文件名长度（Windows路径最大260字符，但要留空间给路径）
    if len(filename) > 100:
        filename = filename[:100]
    return filename

