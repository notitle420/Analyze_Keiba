import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def get_data(file_path):
  df = pd.read_csv(file_path,header=None,index_col=0)
  s = df[1]
  return s


def hit_detection(result):
  hit_detection = False
  if float(result) > 0 :
    hit_detection = True
  return hit_detection

if __name__ == '__main__':
  start = 23
  end = 2080
  x = []
  y = []
  data_num = 0
  all_sum = 0
  all_pay = 0
  x1 = [0,50,100,120,140,160,180,200,220,240,260,280,300]
  a = [0,0,0,0,0,0,0,0,0,0,0,0,0] #合計金額
  b = [0,0,0,0,0,0,0,0,0,0,0,0,0] #出現回数
  c = [0,0,0,0,0,0,0,0,0,0,0,0,0] #当たった回数
  d = [0,0,0,0,0,0,0,0,0,0,0,0,0] #あたり率


  for i in range(start,end):
    for n in range(1,13):
      try:
        path = "Vumacsv/" + str(i) + "_" + str(n) + "_info.csv"
        data = get_data(path)
        data_num += 1
        # all_sum += float(data["result"])
        # all_pay += float(data["payment"])
        if float(data["win_value"]) <= 300:
           x.append(float(data["win_value"]))
           y.append(float(data["result"]))
        if 50 >= float(data["win_value"]) >= 0:
          a[0] += float(data["result"])
          b[0] += 1
          if hit_detection(data["result"]):
            c[0] += 1
        elif 100 >= float(data["win_value"]) > 50:
          a[1] += float(data["result"])
          b[1] += 1
          if hit_detection(data["result"]):
            c[1] += 1
        elif 120 >= float(data["win_value"]) > 100:
          a[2] += float(data["result"])
          b[2] += 1
          if hit_detection(data["result"]):
            c[2] += 1
        elif 140 >= float(data["win_value"]) > 120:
          a[3] += float(data["result"])
          b[3] += 1
          if hit_detection(data["result"]):
            c[3] += 1
        elif 160 >= float(data["win_value"]) > 140:
          a[4] += float(data["result"])
          b[4] += 1
          if hit_detection(data["result"]):
            c[4] += 1
        elif 180 >= float(data["win_value"]) > 160:
          a[5] += float(data["result"])
          b[5] += 1
          if hit_detection(data["result"]):
            c[5] += 1
        elif 200 >= float(data["win_value"]) > 180:
          a[6] += float(data["result"])
          b[6] += 1
          if hit_detection(data["result"]):
            c[6] += 1
        elif 220 >= float(data["win_value"]) > 200:
          a[7] += float(data["result"])
          b[7] += 1
          if hit_detection(data["result"]):
            c[7] += 1
        elif 240 >= float(data["win_value"]) > 220:
          a[8] += float(data["result"])
          b[8] += 1
          if hit_detection(data["result"]):
            c[8] += 1
        elif 260 >= float(data["win_value"]) > 240:
          a[9] += float(data["result"])
          b[9] += 1
          if hit_detection(data["result"]):
            c[9] += 1
        elif 280 >= float(data["win_value"]) > 260:
          a[10] += float(data["result"])
          b[10] += 1
          if hit_detection(data["result"]):
            c[10] += 1
        elif 300 >= float(data["win_value"]) > 280:
          a[11] += float(data["result"])
          b[11] += 1
          if hit_detection(data["result"]):
            c[11] += 1
        else:
          a[12] += float(data["result"])
          b[12] += 1
          if hit_detection(data["result"]):
            c[12] += 1

      except:
          # import traceback
          # traceback.print_exc()
          None


  print("data num = ",data_num)
  # print(all_sum)
  # print(all_pay)
  #角winvalueの合計金額
  #plt.bar(x1, width=-0.4, height=a, align='edge')
  #winvalueのあたら利率
  for k in range(12):
    d[k] = c[k]/b[k]
  plt.bar(x1, width=-0.4, height=d, align='edge')

  #散布図表示
  # plt.ylim(min(y), max(y))
  # plt.xlim(min(x),max(x))
  # plt.yticks([min(y)-10000, -10000, 0,10000,20000,max(y)+10000])
  # plt.xticks([0,100,200,300,400,500])
  # plt.scatter(x, y)
  plt.show()
