import csv
import requests
import json
import pandas as pd

RACE_ID = "2081/12"
CSV_DIR = "./Vumacsv/"
URL_BASE = "https://api.vuma.ai/api/races/"
MARK = "/mark"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Authorization':'XXXXX'
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


def get_tickets_data(data):
    data = json.loads(data, object_hook=ObjectLike)
    just_tickets = data.just_tickets.tickets
    tickets_infos = []
    for ticket in just_tickets:
      ticket_info = []
      for info in ticket.values():
        ticket_info.append(info)
      ticket_info.pop(2)
      ticket_info.pop(1)
      tickets_infos.append(ticket_info)

    clean_tickets = []

    for ticket in tickets_infos:
      ticket = list(flatten_list_tuple_range(ticket))
      if ticket[0] == "単勝" or ticket[0] == "複勝":
        ticket[4:4] = ["",""]
        ticket[7:7] = ["",""]
      elif ticket[0] == "馬単" or ticket[0] == "ワイド" or ticket[0] == "馬連":
        ticket[5:5] = [""]
        ticket[8:8] = [""]
        del ticket[9]
      elif ticket[0] == "3連複" or ticket[0] == "3連単":
         del ticket[9]
      clean_tickets.append(ticket)
      print(clean_tickets)
    return clean_tickets

if __name__ == '__main__':
    start = 2000
    end = 2020
    for i in range(start,end):
      for n in range(1,12):
        RACE_ID = str(i) + "/" + str(n)
        print(RACE_ID)
        url = URL_BASE + RACE_ID + MARK
        data = get_data_from_page(url)
        info2 = get_tickets_data(data)
        header2 = ["買い方","payment","payout","馬","馬","馬","番","番","番"]
        df2 = pd.DataFrame(info2,columns=header2)
        # csvファイル
        file_path2 = CSV_DIR + str(i) + "_" + str(n) + "_tickets.csv"
        df2.to_csv(file_path2)
