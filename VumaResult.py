import csv
import requests
import json
import pandas as pd
import time

CSV_DIR = "./VumacsvToday/"
URL_BASE = "https://api.vuma.ai/api/races/"
MARK = "/mark"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Authorization':'BearereyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkudnVtYS5haVwvYXBpXC9sb2dpbiIsImlhdCI6MTYyMDMwMDA1MywiZXhwIjoxNjIyODkyMDUzLCJuYmYiOjE2MjAzMDAwNTMsImp0aSI6IlJURktKTlFWOW1KUmJidloiLCJzdWIiOjIwOTk0LCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.KqexvF6u71jyKvt1Ayekwk4xhIp5ggN6gUVrb5FD44k',
    'Accept-Encoding':	'gzip, deflate, br',
    'Accept-Language':	'ja,en-US;q=0.9,en;q=0.8'
}

class ObjectLike(dict):
    __getattr__ = dict.get

def flatten_list_tuple_range(l):
    for el in l:
        if isinstance(el, (list, tuple, range)):
            yield from flatten_list_tuple_range(el)
        else:
            yield el


def get_data_from_page(url):
    res = requests.get(url, headers=HEADERS)
    res.encoding = res.apparent_encoding
    text = res.text.encode('utf-8')
    return text

def get_prediction_data(data):
    try:
      data = json.loads(data, object_hook=ObjectLike)
      place = data.place_name
      race = data.race_name
      horse_num = data.horse_num
      course = data.course
      just_tickets = data.just_tickets.result
      info = []
      info.append(place)
      info.append(race)

      for course_info in course.values():
        info.append(course_info)

      info.append(horse_num)

      for ticket in just_tickets.values():
        info.append(ticket)
      return info
    except:
      import traceback
      traceback.print_exc()
      return None



if __name__ == '__main__':
    start = 2083
    end = 2086
    for i in range(start,end):
      for n in range(1,13):
        RACE_ID = str(i) + "/" + str(n)
        print(RACE_ID)
        url = URL_BASE + RACE_ID + MARK
        data = get_data_from_page(url)
        info1 = get_prediction_data(data)
        header1 = ["place","e_name","type","distance","wether","condisiton","horse_num","v_num","win_value","payment","payout","result"]
        if info1 != None:
          df1 = pd.DataFrame(info1,index=header1)
          file_path1 = CSV_DIR + str(i) + "_" + str(n)  + "_info" + ".csv"
          df1.to_csv(file_path1)
        # else:
          # df1 = pd.DataFrame(["Nodata"])
          # file_path1 = CSV_DIR + str(i) + "_" + str(n)  + "_info_Nodata" + ".csv"
          # df1.to_csv(file_path1)
