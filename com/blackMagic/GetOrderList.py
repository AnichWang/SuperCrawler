from urllib import parse
import json
from com.tool.request_client import RequestClient

if __name__ == "__main__":
    url_getOrderList = "http://172.16.10.90:8066/order/query/getOrderList"

    textMod = {"businessType": "-1", "state": "-1", "channel": "-1", "isMerge": "false", "pageIndex": 0}
    #textmod = json.dumps(textMod).encode(encoding='utf-8')

    textmod = json.JSONEncoder().encode(textMod)
    
    #textmod = parse.urlencode(textmod).encode(encoding='utf-8')
    print(textMod)

    headers_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"}
    request_client = RequestClient(url_getOrderList, headers_dict, '', textMod)
    response = request_client.request_post(request_client)

