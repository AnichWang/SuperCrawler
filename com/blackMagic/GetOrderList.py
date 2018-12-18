from urllib import request, parse
import json
import sqlite3

if __name__ == "__main__":
    url_getOrderList = "http://172.16.10.90:8066/order/query/getOrderList"

    """
    请求参数：
    businessType: -1
        全部业务:-1，电商:2，业务不明:-2
    state: -1
    channel: -1
    isMerge: false
    pageIndex: 0
        页数，从0开始
    pageSize: 
        页面容量
    sortField: 
    sortOrder: 
    startTime:
        开始时间，示例 Mon Jan 01 2018 00:00:00 GMT+0800    20180101
    endTime:
        结束时间，示例 Fri Nov 30 2018 00:00:00 GMT+0800    20181130
     """
    formData = parse.urlencode([('pageIndex', 0), ('pageSize', 60),
                                ('startTime', 'Mon Jan 01 2018 00:00:00 GMT+0800'),
                                ('endTime', 'Fri Nov 30 2018 00:00:00 GMT+0800')])

    # 获取接口订单数据
    req = request.Request(url_getOrderList)
    with request.urlopen(req, formData.encode('utf-8')) as f:
        orderInfo = f.read().decode('utf-8')
        print(orderInfo)

    # 解析json数据
    format_Data = json.loads(orderInfo)
    results = format_Data['results']
    #
    orderList = results['list']
    print("order number is：", results['total'])
    print(len(orderList))

    conn = sqlite3.connect("BlackMagic.db")
    cursor = conn.cursor()
    cursor.execute("insert into order_info (
    id,
    busTypeName,
    businessType,
    cardNum,
    "dealFee",
    "excelCreated",
    "excelPayTime",
    "favorFee",
    "orderFee",
    "orderStatus",
    "orderStatusName",
    title,
    "totalFee")",
"values (
    :id,
    :busTypeName,
    :businessType,
    :cardNum,
    :dealFee,
    :excelCreated,
    :excelPayTime,
    :favorFee,
    :orderFee,
    :orderStatus,
    :orderStatusName,
    :title,
    :totalFee);"
;")


