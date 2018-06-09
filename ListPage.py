from urllib.request import urlopen
from bs4 import BeautifulSoup

from DetailPage import DetailPage


class ListPage:
    def __init__(self, bs_obj):
        self.bsObj = bs_obj
        self.url_list = []

    def get_url_list(self):
        url_table = self.bsObj.find_all("table", {"id": "forum_230"})[1]
        for child in url_table.children:
            if child.name == 'tbody':
                detail_url = child.find("tr").find("th").find("span", {"id": str(child['id'][6:])}).find("a")
                self.url_list.append("http://38.103.161.140/forum/" + detail_url["href"])
        return self.url_list

if __name__ == "__main__":
    prePath = "D:\\_developTool\\SuperCrawler\\resource\\亚洲有码原创-丝袜美腿\\"

    url_sis001_stocking = "http://38.103.161.140/forum/forumdisplay.php?fid=230&filter=type&typeid=1255"
    list_html = urlopen(url_sis001_stocking)
    list_bsObj = BeautifulSoup(list_html, "html.parser")
    pageList = ListPage(list_bsObj)
    url_list = pageList.get_url_list()
    print("本页共 %d 个资源"% len(url_list))

    i = 0
    for url in url_list:
        i += 1
        print("准备第 %d 次采集" % i)
        print(url)
        html = urlopen(url)
        bsObj = BeautifulSoup(html, "html.parser")
        detailPage = DetailPage(bsObj, prePath)
        print("开始采集")
        detailPage.save_resource()