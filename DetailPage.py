from urllib.request import urlopen

import re
from bs4 import BeautifulSoup

from Tool import Tool


class DetailPage:
    def __init__(self, bs_obj, folder_path):
        self.bsObj = bs_obj
        self.folderPath = folder_path
        self.resourceName = ""
        self.torrentName = ""

    def get_title(self):
        try:
            title = self.bsObj.find("td", {"class": "postcontent"}).find("div", {"class": "postmessage defaultpost"}).find("h2").text
        except:
            print("出现异常")
            title = ""
        self.resourceName = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", title)
        return title

    def get_filtered_title(self):
        title = self.get_title()
        return re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", title)

    def get_image_url(self):
        image_url_list = []
        try:
            tag_list = self.bsObj.find("td", {"class": "postcontent"}).find("div", {"class": "postmessage defaultpost"}).find("div", {"class": "t_msgfont"})
        except:
            print("出现异常")
            tag_list = []
        if tag_list:
            for child in tag_list:
                if child.name == "img" and child["src"].startswith("http"):
                    image_url_list.append(child["src"])
        return image_url_list

    def get_torrent_url(self):
        try:
            torrent_tag = self.bsObj.find("dl", {"class", "t_attachlist"}).find("dt").find("a", {"style": None})
            self.torrentName = torrent_tag.text
        except:
            print("出现异常")
        if self.torrentName == "":
            return None
        else:
            return "http://162.252.9.10/forum/"+torrent_tag["href"]

    def save_resource(self):
        print("保存------------------------------------"+self.get_title()+"--------------------------------------")
        image_url_list = self.get_image_url()
        torrent_url = self.get_torrent_url()
        print("链接获取完成")
        Tool.save_image(image_url_list, self.folderPath + self.resourceName + "\\", self.resourceName, {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"})
        #Tool.save_attachment(torrent_url, self.folderPath + self.resourceName + "\\", self.torrentName, {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"})




if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"}
    prePath = "D:\\_developTool\\SuperCrawler\\resource\\亚洲有码原创-丝袜美腿\\"
    url = "http://38.103.161.140/forum/viewthread.php?tid=10065101&extra=page%3D1%26amp%3Bfilter%3Dtype%26amp%3Btypeid%3D1255"
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    detailPage = DetailPage(bsObj, prePath)
    #print(detailPage.get_title())
    #print(detailPage.resourceName)
    print(detailPage.get_image_url())
    print(detailPage.get_torrent_url())
    #print(detailPage.torrentName)
    detailPage.save_resource()