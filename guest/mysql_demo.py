from pymysql import cursors, connect
from pymysql.err import OperationalError

try:
    # 连接数据库
    conn = connect(host='127.0.0.1',
               user='root',
               password='passw0rd',
               db='guest',
               charset='utf8mb4',
               cursorsclass=cursors.DictCursor)
    with conn.cursor() as cursor:
        # 创建嘉宾数据
        sql = 'INSERT INTO sign_guest (id,realname,phone,email,sign,create_time,event_id) VALUES ' \
              '("1","alen","13511001100","alen@mail.com","0","2020-12-19 06:33:06","1")'
        # 提交事务
        conn.commit()

        with conn.cursor() as cursor:
            # 查询添加的嘉宾
            sql = 'SELECT realname, phone, email, sign FROM sign_guest WHERE phone=%s'
            cursor.execute(sql, ('13312341237',))
            result = cursor.fetchone()
            print(result)
except OperationalError as e:
    print('MySQL Error %d: %s' % (e.args[0], e.args[1]))
finally:
    conn.close()