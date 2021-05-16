import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter


def get_data(file_path):
    df = pd.read_csv(file_path)
    return df


def numStr(num):
    if num >= 10:
        return str(num)
    else:
        return '0' + str(num)


if __name__ == '__main__':
    ninki = []
    payback = []
    ninki_sum = []
    ninki_payback = []
    free_ninki = []
    free_ninki_sum = []
    free_ninki_payback = []
    free_data_num = 0
    grade_list = []
    baba_list = []

    data_num = 0
    y = []  # あたり率
    yNum = []  # 出現回数
    # for i in range(start, end):
    #   for n in range(1, 13):
    for year in range(2020, 2021):
        for placeCode in range(1, 11):
            for kaisai in range(1, 8):
                for nitime in range(1, 13):
                    for raceNum in range(1, 13):
                        RACE_ID = str(year) + numStr(placeCode) + \
                            numStr(kaisai) + numStr(nitime) + \
                            numStr(raceNum)
                        print(RACE_ID)
                        try:
                            tmp_data = get_data(
                                "Paybackcsv/" + RACE_ID + "_RaceInfo.csv")
                            g = tmp_data["レース"].values[0]
                            b = tmp_data["馬場"].values[0]
                            p = tmp_data["場所"].values[0]
                            # if "G3" in g or "G2" in g or "G1" in g:
                            # if b == "良":
                            path = "Paybackcsv/" + RACE_ID + "_RaceResult.csv"
                            data = get_data(path)
                            free_data_num += 1
                            s = int(data.query('買い方 == "三連複"')
                                    ["人気"].values)
                            d = int(data.query('買い方 == "三連複"')[
                                "払い戻し"].values[0].replace(",", ""))
                            z = int(data.query('買い方 == "単勝"')[
                                "払い戻し"].values[0].replace(",", ""))
                            l = int(data.query('買い方 == "三連複"')
                                    ["人気"].values)
                            free_ninki.append(s)
                            if s not in free_ninki_sum:
                                free_ninki_sum.append(s)
                                free_ninki_payback.append([s, d])
                            for k1, n1 in enumerate(free_ninki_sum):
                                if n1 == s:
                                    free_ninki_payback[k1][1] += d
                            if (p == "東京" or p == "札幌" or p == "阪神") and b == "良":
                                data_num += 1
                                # s = int(data.query('買い方 == "三連複"')
                                #         ["人気"].values)
                                # d = int(data.query('買い方 == "三連複"')[
                                #     "払い戻し"].values[0].replace(",", ""))
                                ninki.append(s)
                                if s not in ninki_sum:
                                    ninki_sum.append(s)
                                    ninki_payback.append([s, d])
                                for k, n in enumerate(ninki_sum):
                                    if n == s:
                                        ninki_payback[k][1] += d
                        except:
                            import traceback
                            traceback.print_exc()
                            None
    print(free_data_num)
    print(data_num)
    # print(ninki)
    # print(payback)
    # print(ninki_sum)
    # print(ninki_payback)

    # 制限なし
    f_counter = Counter(free_ninki)
    f_count = f_counter.most_common()  # N番目人気のあたり回数をカウント
    f_sorted_data = sorted(f_count, key=lambda x: x[0])  # N番目人気のあたり回数を人気純にそーと
    # N番目人気のあたり合計金額を人気順にそーと
    f_sorted_data2 = sorted(free_ninki_payback, key=lambda x: x[0])

    f_x = [f_x[0] for f_x in f_sorted_data]  # N番目人気を横軸
    f_y1 = [f_y[1] for f_y in f_sorted_data]   # N番目人気のあたり回数を縦軸
    f_y2 = [f_y[1] for f_y in f_sorted_data2]   # N番目人気のあたり合計金額を縦軸
    f_y3 = np.array(f_y2)/np.array(f_y1)  # N番目人気の平均あたり金額
    f_y4 = np.array([f_y[1] for f_y in f_sorted_data]) / \
        free_data_num   # N番目人気のあたり率
    f_y5 = np.array(f_y4)*np.array(f_y3)  # N番目人気のあたり率＊平均あたり金額

    f_y_sum = []
    f_y_pay_sum = []
    f_y_pay_out = []
    for i in range(1, 11):
        f_y_sum.append(sum(f_y1[:i*10]))  # N*十番人気までのあたり回数
        f_y_pay_sum.append(sum(f_y2[:i*10]))  # N*十番人気までのあたり金額
        f_y_pay_out.append(i*10)

    f_y6 = np.array(f_y_pay_sum)/np.array(f_y_sum)  # N*10番目まで買った時のあたり平均金額
    f_y7 = np.array(f_y_sum)/free_data_num  # N*10番目まで買った時のあたり率
    f_y8 = np.array(f_y7)*np.array(f_y6)  # y番目人気まで買った時のあたり率＊平均あたり金額
    f_y9 = np.array(f_y8)/np.array(f_y_pay_out)  # あたり期待値/払う金額

    # なんらかのせいげんをつけた値

    counter = Counter(ninki)
    count = counter.most_common()  # N番目人気のあたり回数をカウント
    sorted_data = sorted(count, key=lambda x: x[0])  # N番目人気のあたり回数を人気純にそーと
    # N番目人気のあたり合計金額を人気順にそーと
    sorted_data2 = sorted(ninki_payback, key=lambda x: x[0])

    x = [x[0] for x in sorted_data]  # N番目人気を横軸
    y1 = [y[1] for y in sorted_data]   # N番目人気のあたり回数を縦軸
    y2 = [y[1] for y in sorted_data2]   # N番目人気のあたり合計金額を縦軸
    y3 = np.array(y2)/np.array(y1)  # N番目人気の平均あたり金額
    y4 = np.array([y[1] for y in sorted_data])/data_num   # N番目人気のあたり率
    y5 = np.array(y4)*np.array(y3)  # N番目人気のあたり率＊平均あたり金額

    y_sum = []
    y_pay_sum = []
    y_pay_out = []
    for i in range(1, 11):
        y_sum.append(sum(y1[:i*10]))  # N*十番人気までのあたり回数
        y_pay_sum.append(sum(y2[:i*10]))  # N*十番人気までのあたり金額
        y_pay_out.append(i*10)

    y6 = np.array(y_pay_sum)/np.array(y_sum)  # N*10番目まで買った時のあたり平均金額
    y7 = np.array(y_sum)/data_num  # N*10番目まで買った時のあたり率
    y8 = np.array(y7)*np.array(y6)  # y番目人気まで買った時のあたり率＊平均あたり金額
    y9 = np.array(y8)/np.array(y_pay_out)  # あたり期待値/払う金額

    # plt.xticks(fontsize=8)
    print(y6)
    plt.bar(x[:10], width=-0.4, height=y8, align='edge')
    plt.bar(x[:10], width=0.4, height=f_y8, align='edge')

    # # plt.plot(x, y7)
    plt.show()
