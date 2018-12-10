from urllib import request


class RequestClient:

    def __init__(self, url, headers, url_param, post_data):

        self.url = url
        self.headers = headers
        self.urlParam = url_param
        self.postData = post_data

    @staticmethod
    def request_get(self):
        req = request.Request(url='%s%s%s' % (self.url, '?', self.urlParam), headers=self.headers)
        res = request.urlopen(req)
        res = res.read()
        return res

    @staticmethod
    def request_post(self):
        req = request.Request(url=self.url, data=self.postData, headers=self.headers)
        res = request.urlopen(req)
        res = res.read()
        return res

