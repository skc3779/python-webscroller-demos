import pymysql.cursors

# mysql connect
conn = pymysql.connect(host='192.168.0.46', user='root', passwd='^^qkek123',
                       db='books', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
try:
    with conn.cursor() as cursor:
        cursor.execute("USE books")
        cursor.execute("SELECT * FROM pages WHERE col01 in ('1','2')")
        print(cursor.fetchall())
finally:
    cursor.close()
    conn.close()
