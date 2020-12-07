import time
import pymysql
from decouple import config

def get_time():
    # time_str = time.strftime("%X, %m-%d, %Y")
    time_str = time.strftime("%H:%M, %m/%d/%Y")
    return time_str

def get_conn():
    endpoint = config('ENDPOINT')
    user = config('DB_USER')
    password = config('DB_PASSWORD')
    db = "cov19data"
    charset = "utf8"
    conn = pymysql.connect(endpoint,
                           user=user,
                           password=password,
                           db=db,
                           charset=charset)
    cursor = conn.cursor()
    return conn, cursor

def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def query(sql,*args):

    conn, cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_c1_data():
    sql = "select confirmed, dead, recovered, fatality_rate from history where ds = (select ds from history order by ds desc limit 1)"
    res = query(sql)
    return res[0]

def get_c2_data():
    sql = "select state, confirmed from states_data where date = (select date from states_data order by date desc limit 1)"
    res = query(sql)
    return res

def get_l1_data():
	sql = "select ds, confirmed, recovered, dead from history"
	res = query(sql)
	return res

def get_l2_data():
	sql = "select ds, confirmed_add, dead_add from history where ds != (select ds from history order by ds limit 1)"
	res = query(sql)
	return res

def get_r1_data():
    sql = "select state, confirmed from states_data where date=(select date from states_data order by date desc limit 1) order by confirmed desc limit 5;"
    res = query(sql)
    return res

def get_r2_data():
    sql = 'select content from trending_qs order by id desc limit 5'
    res = query(sql)
    return res

if __name__ =="__main__":
    print(get_time())
    print(get_c1_data())
    print(get_c2_data())
    print(get_l1_data())
    print(get_r1_data())
    print(get_r2_data())
