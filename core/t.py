import requests,os
"""
class tempPool:
    def __init__(self):
        self.pool = {}
    def get(self,key):
        return self.pool.get(key)
    def set(self,key,value):
        self.pool[key] = value
"""
def dl_pic(url):
    filename = url.split("/")[-1]
    try:
        with open(os.path.join("data","temp",filename), 'rb') as f:
            return f.read()
    except FileNotFoundError:
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
            with open(os.path.join("data","temp",filename), 'wb') as f:
                f.write(response.content)
            return response.content  # 返回图片的二进制数据
        except requests.RequestException as e:
            print(f"下载图片失败: {e}")
            return b""  # 返回空字节串表示下载失败
