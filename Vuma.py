import csv
import requests
import json
import pandas as pd

RACE_ID = "2081/12"
CSV_DIR = "./Vumacsv/"
URL_BASE = "https://api.vuma.ai/api/races/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Authorization':'XXXXX,
    'Accept-Encoding':	'gzip, deflate, br',
    'Accept-Language':	'ja,en-US;q=0.9,en;q=0.8'
}

class ObjectLike(dict):
    __getattr__ = dict.get


def get_data_from_page(url):
    res = requests.get(url, headers=HEADERS)
    res.encoding = res.apparent_encoding
    text = res.text.encode('utf-8')
    return text

def get_prediction_data(data):
    data = json.loads(data, object_hook=ObjectLike)
    round_horses = data.just_prediction.round_horses
    horses_array = []
    for round_horse in round_horses:
      horse_info = []
      for info in round_horse.mark_prediction.values():
        # info = str(info).encode('utf-8')
        # info = info.decode('unicode-escape')
        if info != None and not isinstance(info, int):
          if "　" in info:
            info  = ''.join(info.split())
        horse_info.append(info)
      del horse_info[22:28]
      horse_info.pop(3)
      horses_array.append(horse_info)
    print(horses_array)
    return horses_array



if __name__ == '__main__':
    start = 2000
    end = 2020
    for i in range(start,end):
      for n in range(1,12):
        RACE_ID = str(i) + "/" + str(n)
        print(RACE_ID)
        url = URL_BASE + RACE_ID
        data = get_data_from_page(url)
        info = get_prediction_data(data)
        header = ["mark","枠","番","馬","性","齢","騎","量","父","爺","牧","調教","人気","オッズ","体重","増減","馬主","牧場","勝率","連率","複率"]
        df = pd.DataFrame(info,columns=header)
        # csvファイル
        file_path = CSV_DIR + str(i) + "_" + str(n) + ".csv"
        df.to_csv(file_path)


    # with open(file_path, "w", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     writer.writerows(info)
