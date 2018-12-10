from urllib.request import *
from json
from com.tool.request_client import RequestClient

if __name__ == "__main__":
    url_getOrderList = "http://172.16.10.90:8066/order/query/getOrderList"
    dataForm = ""
    headers_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"}
    urlRequest = Request(url=url_getOrderList, data=dataForm, headers=headers_dict)
    response = urlopen(urlRequest)
    print(response)
    request_client = RequestClient(url_getOrderList, headers_dict,'',post_data)

