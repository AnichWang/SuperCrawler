import sqlite3

if __name__ == "__main__":
    #连接数据库，如不存在，则在当前目录创建
    conn = sqlite3.connect('BlackMagic.db')
    cursor = conn.cursor()

    cursor.execute('create table order_info(id INT PRIMARY KEY NOT NULL,'
                   'cardNum varchar(20),'
                   'businessType INT,'
                   'busTypeName varchar(20),'
                   'orderStatus INT,'
                   'orderStatusName varchar(20),'
                   'title varchar(20),'
                   'totalFee varchar(20),'
                   'dealFee varchar(20),'
                   'orderFee varchar(20),'
                   'favorFee varchar(20),'
                   'excelPayTime varchar(20),'
                   'excelCreated varchar(20))')

    cursor.close()
    conn.commit()
    conn.close()
