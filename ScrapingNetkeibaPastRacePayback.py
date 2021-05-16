import csv
import requests
import bs4
import pandas as pd

# RACE_ID = "202005021211"
CSV_DIR = "./Paybackcsv/"
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


def numStr(num):
    if num >= 10:
        return str(num)
    else:
        return '0' + str(num)


def get_race_from_text(text):
    info = []
    info_clean = []
    soup = bs4.BeautifulSoup(text, features='html.parser')
    # レース結果表示用のtable
    try:
        base_elem = soup.find(class_="mainrace_data")
        elem1 = base_elem.find("h1").getText()
        elem2 = base_elem.find("span").getText()
        elem3 = base_elem.find(class_="smalltxt").getText()
        elem2 = elem2.split("/")
        elem3 = elem3.split(" ")
        cleanElem = []
        cleanElem.append(elem1)
        for i, elem in enumerate(elem2):
            if i == 0:
                elem = elem.replace("\xa0", "")
                cleanElem.append(elem[:1])
                cleanElem.append(elem[1:2])
                cleanElem.append(elem[2:])
            if i == 1:
                elem = elem.replace("\xa0", "")
                cleanElem.append(elem[-1:])
            if i == 2:
                elem = elem.replace("\xa0", "")
                cleanElem.append(elem[-1:])
        for k, elem in enumerate(elem3):
            if k == 0:
                cleanElem.append(elem)
            if k == 1:
                cleanElem.append(elem[2:4])
            if k == 2:
                elem = elem.replace("\xa0", "")
                cleanElem.append(elem)
            # if k == 3:
            #     elem = elem.replace("\xa0", "")
            #     cleanElem.append(elem)
        return cleanElem
    except:
        import traceback
        traceback.print_exc()
        None


def get_odds_from_text(text):
    info = []
    info_clean = []
    soup = bs4.BeautifulSoup(text, features='html.parser')
    # レース結果表示用のtable
    try:
        base_elem = soup.find(class_="pay_block")
        elems = base_elem.find_all("tr")
        for elem in elems:
            # print(elem)
            temp_row = []
            temp_row.append(elem.find("th"))
            temp_row.extend(elem.find_all("td"))
            row = []
            for text in temp_row:
                # print(text)
                r_class = text.get("class")
                r_text = text.getText("|")
                row.append(r_text)
            info.append(row)
        print(info)
        for row in info:
            print(row)
            if row[0] == "複勝":
                row[1] = row[1].split("|")
                row[2] = row[2].split("|")
                row[3] = row[3].split("|")
                i = 0
                for i in range(len(row[1])):
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
    except:
        return None


def deback():
    RACE_ID = "202005021211"
    url = URL_BASE + RACE_ID
    text = get_text_from_page(url)
    odds = get_race_from_text(text)
    # df = pd.DataFrame(odds, columns=header)
    # file_path = "deback.csv"
    df.to_csv(file_path)


if __name__ == '__main__':
    header1 = ["買い方", "番号", "払い戻し", "人気"]
    header2 = ["レース", "コース", "周り", "距離", "天気", "馬場", "日付", "場所", "グレード"]
    for year in range(2001, 2020):
        for placeCode in range(1, 11):
            for kaisai in range(1, 8):
                for nitime in range(1, 13):
                    for raceNum in range(1, 13):
                        RACE_ID = str(year) + numStr(placeCode) + \
                            numStr(kaisai) + numStr(nitime) + \
                            numStr(raceNum)
                        print(RACE_ID)
                        url = URL_BASE + RACE_ID
                        text = get_text_from_page(url)
                        odds = get_odds_from_text(text)
                        race = [get_race_from_text(text)]
                        print(race)
                        if odds != None:
                            df1 = pd.DataFrame(odds, columns=header1)
                            df2 = pd.DataFrame(race, columns=header2)
                            file_path1 = CSV_DIR + str(year) + numStr(placeCode) + numStr(
                                kaisai) + numStr(nitime) + numStr(raceNum) + "_RaceResult.csv"
                            file_path2 = CSV_DIR + str(year) + numStr(placeCode) + numStr(
                                kaisai) + numStr(nitime) + numStr(raceNum) + "_RaceInfo.csv"
                            df1.to_csv(file_path1)
                            df2.to_csv(file_path2)
