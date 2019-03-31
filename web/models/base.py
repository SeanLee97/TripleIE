import pymysql


class Base():
    def __init__(self):
        pass

    def exec_sql(self, sql):
        # 打开数据库连接
        db = pymysql.connect(host='39.107.87.250',
                             port=3306,
                             user='root',
                             passwd='Wj6688',
                             db='kbqa',
                             charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)

        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()

        print("Database version : %s " % data)

        # 关闭数据库连接
        db.close()
