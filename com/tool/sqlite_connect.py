import sqlite3

if __name__ == "__main__":
    #连接数据库，如不存在，则在当前目录创建
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    #