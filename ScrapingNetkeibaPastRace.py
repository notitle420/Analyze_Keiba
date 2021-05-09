import csv
import requests
import bs4

RACE_ID = "202005021211"
CSV_DIR = "./csv/"
URL_BASE = "https://db.netkeiba.com/race/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36   '
}

# htmlソース取得
def get_text_from_page(url):
    try:
        res = requests.get(url, headers=HEADERS)
        res.encoding = res.apparent_encoding
        text = res.text
        return text
    except:
        return None

# info取得
def get_info_from_text(header_flg, text):
    try:
        # データ
        info = []
        soup = bs4.BeautifulSoup(text, features='html.parser')
        # レース結果表示用のtable
        base_elem = soup.find(class_="race_table_01 nk_tb_common")
        # 行取得
        elems = base_elem.find_all("tr")
        for elem in elems:
            row_info = []
            # ヘッダーを除外するための情報
            r_class = elem.get("class")
            r_cols = None
            if r_class==None:
                # 列取得
                r_cols = elem.find_all("td")
            else:
                # ヘッダー(先頭行)
                if header_flg:
                    r_cols = elem.find_all("th")
            if not r_cols==None:
                for r_col in r_cols:
                    tmp_text = r_col.text
                    tmp_text = tmp_text.replace("\n", "")
                    row_info.append(tmp_text.strip())
                del row_info[15:18]
                row_info[14:14] = row_info[14].split("(")
                row_info[15] = row_info[15].rstrip(")")
                row_info.pop(16)
                print(row_info)
                info.append(row_info)
        return info

    except:
        print("err")
        return None

def get_odds_from_text(header_flg, text):
    info = []
    info_clean = []
    soup = bs4.BeautifulSoup(text, features='html.parser')
    # レース結果表示用のtable
    base_elem = soup.find(class_="pay_block")
    elems = base_elem.find_all("tr")
    for elem in elems:
        #print(elem)
        temp_row = []
        temp_row.append(elem.find("th"))
        temp_row.extend(elem.find_all("td"))
        row = []
        for text in temp_row:
          #print(text)
          r_class = text.get("class")
          r_text = text.getText("|")
          row.append(r_text)
        info.append(row)
    for row in info:
      if row[0] == "複勝":
        row[1] = row[1].split("|")
        row[2] = row[2].split("|")
        row[3] = row[3].split("|")
        i = 0
        for i in range(3):
          temp_row = []
          temp_row.append("複勝")
          temp_row.append(row[1][i])
          temp_row.append(row[2][i])
          temp_row.append(row[3][i])
          info_clean.append(temp_row)
      elif row[0] == "ワイド":
        row[1] = row[1].split("|")
        row[2] = row[2].split("|")
        row[3] = row[3].split("|")
        i = 0
        for i in range(3):
          temp_row = []
          temp_row.append("ワイド")
          temp_row.append(row[1][i])
          temp_row.append(row[2][i])
          temp_row.append(row[3][i])
          info_clean.append(temp_row)
      else:
        info_clean.append(row)
    return info_clean

if __name__ == '__main__':
    url = URL_BASE + RACE_ID
    text = get_text_from_page(url)
    header = ["着","枠","番","馬","齢","量","騎","時","差","指","通","上","人気","体重","増減","調教","馬主","オッズ","複勝オッズ"]
    #print(text)
    info = get_info_from_text(False, text)
    odds = get_odds_from_text(False, text)
    for i,row in enumerate(info):
      row[2] = int(row[2])
      if i < 3:
        row.insert(13,int(odds[i+1][2])/100)
      else:
        row.insert(13,0)
      row.pop()
      tmp = row.pop(12)
      tmp2 = row.pop(12)
      row.append(tmp)
      row.append(tmp2)
    info_sorted = sorted(info, reverse=False, key=lambda x: x[2])

    # csvファイル
    file_path = CSV_DIR + RACE_ID + ".csv"

    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(info_sorted)
        writer.writerows(odds)
