import requests, re, time, urllib.parse, hashlib
from http.cookies import SimpleCookie

User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def w_rid(param):
    e = "7cd084941338484aae1ad9425b84077c4932caff0ff746eab6f01bf08b70ac45"
    c = ''.join([e[i] for i in
                 [46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49, 33, 9, 42, 19, 29, 28, 14,
                  39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40, 61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56,
                  59, 6, 63, 57, 62, 11, 36, 20, 34, 44, 52]])
    c = c[:32]
    u = int(time.time())
    param["wts"] = u
    f = [f"{urllib.parse.quote(str(k).encode('utf-8'))}={urllib.parse.quote(str(v).encode('utf-8'))}" for k, v in
         sorted(param.items())]
    y = '&'.join(f)
    return hashlib.md5((y + c).encode(encoding='utf-8')).hexdigest(), u


class get:
    def __init__(self, config=None):
        self.session = requests.Session()
        if config and config.get("cookie", ""):
            self.cookies(config.get("cookie", ""))
        self.session.headers['User-Agent'] = User_Agent
    def cookies(self, cookie):
        """
        设置cookies
        :param cookie: 字符串形式的cookie，例如 "key1=value1; key2=value2"
        """
        cookie_obj = SimpleCookie()
        cookie_obj.load(cookie)
        for key, morsel in cookie_obj.items():
            self.session.cookies.set(key, morsel.value)
    def check(self, response):
        if response.status_code == 200:
            return True
        else:
            return False
    # ========== 原有方法 ==========
    def VG(self, clear=True):
        """推荐视频"""
        Url = "https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd?ps=10&web_location=1430650&y_num=3&fresh_type=4&feed_version=V8&fresh_idx_1h=1&fetch_row=4&fresh_idx=1&brush=1&device=win&homepage_ver=1&last_y_num=4&screen=329-565&seo_info=&tt_exp=&uniq_id=1314743959197"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            data = req.json()
            if data['code'] == 0:
                row = [{"title": item['title'], "bvid": item['bvid'], "pic": item['pic'], "upname": item['owner']['name'], "upid":item['owner']['mid'], "cid":item['cid']} for item in data['data']['item']]
                return row
        else:
            return req.json()
    def videoInfo(self, bvid, clear=True):
        """视频信息"""
        Url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            data = req.json()
            if data['code'] == 0:
                row = data['data']
                return {"title": row['title'], "aid": row["aid"], "pic": row['pic'], 
                       "owner": row['owner']['name'], "upid": row['owner']['mid'], 
                       "duration": row['duration'], "desc": row['desc'], 
                       "view": row['stat']['view'], "cid": row['cid']}
        else:
            return req.json()
    # ========== 新增方法（从 api.py 迁移） ==========
    def search(self, keyword, page=1, clear=True):
        """
        搜索视频
        :param keyword: 搜索关键词
        :param page: 页码
        :param clear: 是否返回精简数据
        """
        Url = "https://api.bilibili.com/x/web-interface/search/type"
        params = {"keyword": keyword, "search_type": "video", "page": page}
        req = self.session.get(Url, params=params)
        self.check(req)
        if clear:
            row = []
            if req.json()['code'] == 0:
                for item in req.json()['data']['result']:
                    t = re.sub(r'<[^>]+>', "", item['title'])
                    row.append({"title": t, "bvid": item['bvid'], "pic": item['pic'], "upname": item['author']})
            return row
        else:
            return req.text
    def anl(self, upmid, clear=True):
        """
        获取用户收藏夹列表
        :param upmid: 用户ID
        :param clear: 是否返回精简数据
        """
        Url = f"https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid={upmid}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            row = []
            if req.json()['code'] == 0 and req.json()['data'] is not None:
                items = req.json()['data']['list']
                for i, item in enumerate(items, 1):
                    row.append({"title": item['title'], "id": item['id'], 
                               "count": item["media_count"], "type": "mb"})
            else:
                row = None
            return row
        else:
            return req.json()
    def sl(self, mid, pn=1, keyword="", ps=25, clear=True):
        """
        获取收藏夹内容
        :param mid: 收藏夹ID
        :param pn: 页码
        :param keyword: 关键词过滤
        :param ps: 每页数量
        :param clear: 是否返回精简数据
        """
        Url = f"https://api.bilibili.com/x/v3/fav/resource/list?media_id={mid}&pn={pn}&ps={ps}&keyword={keyword}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            return req.json()['data']
        else:
            return req.json()
    def send_vc(self, oid, message, csrf, clear=True):
        """
        发送评论
        :param oid: 视频ID
        :param message: 评论内容
        :param csrf: CSRF令牌
        :param clear: 是否返回精简数据
        """
        Url = "https://api.bilibili.com/x/v2/reply/add"
        params = {"oid": oid, "type": 1, "message": message, "csrf": csrf}
        req = self.session.post(Url, params=params)
        self.check(req)
        row = req.json()
        if clear:
            if row['code'] == 0:
                return {"status": row['data']['success_toast'], 
                       "message": row['data']['reply']['content']['message'], "oid": oid}
        else:
            return row
    def aw(self, clear=True):
        """稍后再看列表"""
        Url = "https://api.bilibili.com/x/v2/history/toview"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            if req.json()['code'] == 0:
                return [
                    {
                        "title": item['title'], "bvid": item['bvid'],
                        "pic": item['pic'], "upname": item['owner']['name'],
                        "cid": item.get('cid'), "aid": item.get('aid'),
                    } for item in req.json()['data']['list']]
        else:
            return req.json()['data']['list']
    def Uinfo(self, uid, clear=True):
        """
        获取用户信息
        :param uid: 用户ID
        :param clear: 是否返回精简数据
        """
        params = {"mid": uid, "token": "", "platform": "web", "web_location": 1550101, 
                 "dm_img_list": "[]", "dm_img_str": "V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ", 
                 "dm_cover_img_str": "QU5HTEUgKEludGVsLCBJbnRlbChSKSBVSEQgR3JhcGhpY3MgNjMwICgweDAwMDAzRTlCKSBEaXJlY3QzRDExIHZzXzVfMCBwc181XzAsIEQzRDExKUdvb2dsZSBJbmMuIChJbnRlbC", 
                 "dm_img_inter": "{\"ds\":[],\"wh\":[3256,5442,64],\"of\":[495,990,495]}"}
        wrid, wts = w_rid(params)
        Url = f"https://api.bilibili.com/x/space/wbi/acc/info?mid={uid}&token=&platform=web&web_location={params['web_location']}&dm_img_list={params['dm_img_list']}&dm_img_str={params['dm_img_str']}&dm_cover_img_str={params['dm_cover_img_str']}&dm_img_inter={params['dm_img_inter']}&w_rid={wrid}&wts={wts}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            return req.json()['data']
        else:
            return req.json()
    def like(self, uid, clear=True):
        """获取用户点赞视频列表"""
        Url = f"https://api.bilibili.com/x/space/like/video?vmid={uid}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            return [{
                "bvid": item['bvid'],
                "title": item['title'],
                "pic": item['pic'],
                "upname": item['owner']['name'],
                "upid": item['owner']['mid'],
                "aid": item['aid'],
                "tag": None
            } for item in req.json()['data']['list']]
        else:
            return req.json()
    def coin(self, uid, clear=True):
        """获取用户投币视频列表"""
        Url = f"https://api.bilibili.com/x/space/coin/video?vmid={uid}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            return [{
                "bvid": item['bvid'],
                "title": item['title'],
                "pic": item['pic'],
                "upname": item['owner']['name'],
                "upid": item['owner']['mid'],
                "aid": item['aid'],
                "tag": None
            } for item in req.json()['data']]
        else:
            return req.json()
    def follow(self, uid, page=1, ps=50, clear=True):
        """
        获取用户关注列表
        :param uid: 用户ID
        :param page: 页码
        :param ps: 每页数量
        :param clear: 是否返回精简数据
        """
        Url = f"https://api.bilibili.com/x/relation/followings?vmid={uid}&pn={page}&ps={ps}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            get_data = req.json()
            if get_data['code'] == 0:
                row = {}
                for i in get_data['data']['list']:
                    row[i['mid']] = i['uname']
                return row
        else:
            return req.json()
    def fans(self, uid, page=1, ps=50, clear=True):
        """
        获取用户粉丝列表
        :param uid: 用户ID
        :param page: 页码
        :param ps: 每页数量
        :param clear: 是否返回精简数据
        """
        Url = f"https://api.bilibili.com/x/relation/fans?vmid={uid}&ps={ps}&pn={page}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            get_data = req.json()
            if get_data['code'] == 0:
                row = {}
                for i in get_data['data']['list']:
                    row[i['mid']] = i['uname']
                return row
        else:
            return req.json()
    def uv(self, uid, page=1, clear=True):
        """
        获取用户作品列表
        :param uid: 用户ID
        :param page: 页码
        :param clear: 是否返回精简数据
        """
        params = {"mid": uid, "pn": page, "ps": "50", "order": "pubdate"}
        wrid, wts = w_rid(params)
        Url = f"https://api.bilibili.com/x/space/wbi/arc/search?mid={uid}&pn={page}&ps=50&order=pubdate&w_rid={wrid}&wts={wts}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            get_data = req.json()
            if get_data['code'] == 0:
                return [{'bvid': i['bvid'], 'title': i['title'], 'aid': i['aid']} 
                       for i in get_data['data']['list']['vlist']]
        else:
            return req.json()
    def Vtag(self, bvid, clear=True):
        """获取视频标签"""
        Url = f"https://api.bilibili.com/x/web-interface/view/detail/tag?bvid={bvid}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            return [tag["tag_name"] for tag in req.json()['data']]
        else:
            return req.json()
    def send_C(self, aid, mid, csrf, type=True):
        """
        收藏/取消收藏
        :param aid: 视频ID
        :param mid: 收藏夹ID
        :param csrf: CSRF令牌
        :param type: True=收藏，False=取消收藏
        """
        Url = "https://api.bilibili.com/medialist/gateway/coll/resource/deal"
        if not type:
            params = {"rid": aid, "type": 2, "del_media_ids": mid, "csrf": csrf}
        else:
            params = {"rid": aid, "type": 2, "add_media_ids": mid, "csrf": csrf}
        req = self.session.post(Url, params=params)
        if req.status_code != 200:
            return req.status_code
        return req.json()
    def su2u(self, url, clear=True):
        """
        短链转BV号
        :param url: 短链URL
        :param clear: 是否返回精简数据
        """
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        req = self.session.get(url, allow_redirects=False)
        if clear:
            match = re.search(r'href="([^"]+)"', req.text)
            if match:
                video_url = match.group(1)
                decoded_url = urllib.parse.unquote(video_url)
                bv_match = re.search(r'/video/(BV[0-9A-Za-z]+)', decoded_url)
                if bv_match:
                    bvid = bv_match.group(1)
                    return bvid
            else:
                return None
        else:
            return req.text
    def history(self, max_id=0, view_at=0, ps=30, type="all", clear=True):
        """
        获取历史记录
        :param max_id: 最大历史记录ID（用于分页）
        :param view_at: 最后观看时间戳
        :param ps: 每页数量
        :param type: 类型（all=全部，live=直播，article=专栏等）
        :param clear: 是否返回精简数据
        """
        Url = f"https://api.bilibili.com/x/web-interface/history/cursor?max={max_id}&view_at={view_at}&ps={ps}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            row = req.json()['data']
            rl = [{"title": i['title'], "bvid": i['history']['bvid'], 
                  "cid": i['history']['cid'], "upname": i['author_name'], 
                  "upid": i['author_mid'], "pic": i['cover']} for i in row['list']]
            return {"max_id": row['cursor']['max'], "view_at": row['cursor']['view_at'], 
                   "list": rl, "business": row['cursor']['business'], "ps": row['cursor']['ps']}
        else:
            return req.json()
    def followinfo(self, uid):
        """获取用户关注统计信息"""
        Url = f"https://api.bilibili.com/x/relation/stat?vmid={uid}"
        req = self.session.get(Url)
        self.check(req)
        if req.json()['code'] == 0:
            return req.json()['data']
    def Vurl(self, bvid, cid, clear=True):
        """获取视频播放地址"""
        Url = f"https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&fnval=16&fourk=1"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            return req.json()['data']
        else:
            return req.json()
    def readList(self, id, clear=True):
        """
        获取专栏文集
        :param id: 文集ID
        :param clear: 是否返回精简数据
        """
        Url = f"https://api.bilibili.com/x/article/list/web/articles?id={id}"
        req = self.session.get(Url)
        self.check(req)
        if clear:
            data = req.json()['data']
            return {"name": data['list']['name'], "pic": data['list']['image_url'], 
                   "upid": data['list']['mid'], "list": data['articles']}
        else:
            return req.json()
    def uReadList(self, uid, clear=True):
        """
        获取用户专栏文集列表
        :param uid: 用户ID
        :param clear: 是否返回精简数据
        """
        params = {"mid": uid}
        params['w_rid'], params['wts'] = w_rid(params)
        Url = "https://api.bilibili.com/x/article/up/lists"
        req = self.session.get(Url, params=params)
        self.check(req)
        if clear:
            return req.json()['data']['lists']
        else:
            return req.json()

if __name__ == "__main__":
    g = get()
    for i in g.VG():
        print(i)
    # 测试示例
    # info = g.videoInfo("BV1xx411c7mD")
    # print(info)