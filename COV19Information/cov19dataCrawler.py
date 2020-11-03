import requests
import json
import re
import pymysql
import time 
import traceback
from selenium.webdriver import Chrome,ChromeOptions
from decouple import config


endpoint = config('ENDPOINT')
user = config('DB_USER')
password = config('DB_PASSWORD')
db = "cov19data"
charset = "utf8"
historyData = config('HISTORY_DATA_URL')
statesData = config('STATES_DATA_URL')


def get_conn():
    conn = pymysql.connect(endpoint, user = user, password = password, db = db, charset = charset)
    cursor = conn.cursor()  
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def get_covid19_data():
    url = historyData
    res = requests.get(url)
    data_dic = json.loads(res.text)
    data_total = data_dic["Data"]["CountryDict"]["US"]
    # data_total
    history = {}
    confirmed_yesterday=0
    dead_yesterday=0
    for key in data_total:   
        tup = time.strptime(key, "%Y%m%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirmed = data_total[key]["Confirmed"]
        death = data_total[key]["Deaths"]
        recovered = data_total[key]["Recovered"]
        
        confirmed_add = confirmed - confirmed_yesterday
        confirmed_yesterday = confirmed
        dead_add = death - dead_yesterday
        dead_yesterday = death
        
        fatality_rate = round(death/confirmed, 4)
        
        history[ds] = {"confirmed": confirmed, "recovered": recovered, "death": death, "confirmed_add":confirmed_add, "dead_add":dead_add, "fatality_rate":fatality_rate}
    return history


def get_covid19_states_data():
    url = statesData
    res = requests.get(url)
    data = re.search(r'({[\s\S]*})',res.text).group(0)
    d = json.loads(data)
    data_dic = json.loads(d["data"])
    dic = {"美军":"US Army", "纳瓦霍族保留地":"Navajo Reservation", "至尊公主号邮轮":"Grand Princess", "钻石公主号邮轮":"Diamond Princess", "北马里亚纳群岛":"Northern Mariana Islands", "撤回侨民":"Evacuee", "地区待确认":"Region to be confirmed", "联邦监狱局":"Federal Prison"}
    for country in data_dic["foreignList"]:
        if "美国" == country["name"]:
            data_state = country["children"]
            states_data = []
            for state_info in data_state:
                date = "2020." + state_info["date"]
                tup = time.strptime(date, "%Y.%m.%d")
                date = time.strftime("%Y-%m-%d", tup)
                if(state_info["nameMap"] == ''):
                    state = dic[state_info["name"]]
                else:
                    state = state_info["nameMap"]
                confirmed = state_info["confirm"]
                dead = state_info["dead"]
                recovered = state_info["heal"]   
                states_data.append([date, state, confirmed, dead, recovered])
    return states_data    


def insert_history():
    cursor = None
    conn = None
    try:
        dic = get_covid19_data()  
        print(f"{time.asctime()}begin")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s)"
        for k, v in dic.items():
            cursor.execute(sql, [k, v.get("confirmed"), v.get("recovered"), v.get("death"), v.get("confirmed_add"), v.get("dead_add"), v.get("fatality_rate")])
        conn.commit()  
        print(f"{time.asctime()}finish")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_history(): 
    cursor = None
    conn = None
    try:
        dic = get_covid19_data() 
        print(f"{time.asctime()}begin")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirmed from history where ds=%s"
        for k, v in dic.items():
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get("confirmed"), v.get("recovered"), v.get("death"), v.get("confirmed_add"), v.get("dead_add"), v.get("fatality_rate")])
        conn.commit()  
        print(f"{time.asctime()}finish")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_states_data():   
    cursor = None
    conn = None
    try:
        li = get_covid19_states_data() 
        conn, cursor = get_conn()
        sql = "insert into states_data(date,state,confirmed,dead,recovered) values(%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select date from states_data order by date desc limit 1)' 
        cursor.execute(sql_query,li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}begin")
            for item in li:
                cursor.execute(sql, item)
            conn.commit()  
            print(f"{time.asctime()}finish")
        else:
            print(f"{time.asctime()}already updated")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def get_google_qs():
    url = "https://trends.google.com/trends/story/US_cu_4Rjdh3ABAABMHM_en"
    option = ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    browser = Chrome(options=option)
    browser.get(url)
    data=browser.find_elements_by_xpath("/html/body/div[2]/div[2]/md-content/div/div/div[6]/trends-widget/ng-include/widget/div/div/ng-include/div/div/span/a")
    content = [i.text for i in data]
    browser.close()
    return content


def update_google_qs():
    cursor = None
    conn = None
    try:
        context = get_google_qs()
        print(f"{time.asctime()}begin")
        conn, cursor = get_conn()
        sql = "insert into trending_qs(date,content) values(%s,%s)"
        ts = time.strftime("%Y-%m-%d %X")
        for i in context:
            cursor.execute(sql, (ts, i))  
        conn.commit()  
        print(f"{time.asctime()}finish")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == "__main__":
    update_history()
    update_states_data()
    update_google_qs()


# get_covid19_data()
# get_covid19_states_data()
# insert_history()
# update_history()
# update_states_data()
# get_google_qs()
# update_google_qs()

