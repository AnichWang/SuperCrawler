import os
from urllib.error import HTTPError
from urllib.request import urlretrieve, urlopen


class Tool:

    @staticmethod
    def save_image(urlList, folderPath, title, headers={}):
        '''
        :param urlList: 图片地址的list
        :param folderPath: 保存本地文件夹地址
        :return:
        '''
        if urlList:
            i = 0
            for url in urlList:
                i += 1
                # 创建文件夹
                if not os.path.exists(folderPath):
                    os.mkdir(folderPath)
                if not os.path.exists(folderPath + title + str(i) + ".gif"):
                    try:
                        urlretrieve(url, folderPath + title + str(i) + ".gif", Tool.report_hook, headers)
                        print(title + str(i) + ".gif" + "----------保存完成")
                    except HTTPError as e:
                        print(e)
                        print("保存 "+title + str(i) + ".gif 出错")


    @staticmethod
    def save_attachment(url, folderPath, title, headers={}):
        '''
        :param url: 下载地址
        :param folderPath: 保存本地文件夹地址
        :return:
        '''
        if url:
            if not os.path.exists(folderPath):
                os.mkdir(folderPath)
            if not os.path.exists(folderPath + title + '.torrent'):
                # print(request.info()['Content-Disposition'])
                try:
                    urlretrieve(url, folderPath + title + '.torrent', Tool.report_hook, (None, headers))
                    print(title + ".torrent" + "----------保存完成")
                except HTTPError:
                    print("保存"+title + ".torrent 出错")

    @staticmethod
    def save_attachment_old(url, folderPath, title):
        '''
        :param url: 下载地址
        :param folderPath: 保存本地文件夹地址
        :return:
        '''
        if url:
            request = urlopen(url)
            data = request.read()
            if not os.path.exists(folderPath):
                os.mkdir(folderPath)
            if not os.path.exists(folderPath + title + '.torrent'):
                # print(request.info()['Content-Disposition'])
                print(title + ".torrent" + "----------保存中")
                file = open(folderPath + title + '.torrent', 'wb')
                file.write(data)
                file.close()

    @staticmethod
    def report_hook(block_num, bs, size):
        '''
        :param block_num: 已经下载的数据块
        :param bs: 数据块大小
        :param size: 远程文件总大小
        :return:
        '''
        per = 100.0*block_num*bs/size
        if per > 100:
            per = 100
        print("下载进度-----%.1f%%" % per)



if __name__ == "__main__":
    pre = "D:\\_developTool\\SuperCrawler\\resource\\"
    Tool.save_image(['http://imagizer.imageshack.com/img922/9004/QZMA7r.jpg', 'http://imagizer.imageshack.com/img924/9363/Q21Tr6.jpg'], pre+"\\aaa\\", "fuck", {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"})
    #Tool.save_attachment('http://162.252.9.10/forum/attachment.php?aid=2981766', pre+"\\aaa\\", "fuck")