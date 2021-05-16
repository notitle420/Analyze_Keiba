import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def get_data(file_path):
  df = pd.read_csv(file_path,header=None,index_col=0)
  s = df[1]
  return s


def hit_detection(result):
  hit_detection = False
  if int(result) > 0 :
    hit_detection = True
  return hit_detection

if __name__ == '__main__':
  start = 23
  end = 2080
  place = ['Tokyo', 'Hanshin', 'Hakodate', 'Fukushima', 'Chukyo', 'Sapporo', 'Nigata', 'Ogura', 'Nakayama', 'Kyoto']
  places = []
  data_num = 0
  y = []  #あたり率
  yNum = [] #出現回数
  for i in range(start,end):
    for n in range(1,13):
      try:
        path = "Vumacsv/" + str(i) + "_" + str(n) + "_info.csv"
        data = get_data(path)
        hit_boolean = hit_detection(data["result"])
        data_num +=1
        if data["place"] not in places:
          places.append(data["place"])
          yNum.append(0)
          y.append(0)
        for k, place in enumerate(places):
          if place == data["place"]:
            yNum[k] += 1
            if hit_boolean:
              y[k] += 1

      except:
          # import traceback
          # traceback.print_exc()
          None


  for i in range(len(places)):
    y[i] = y[i] / yNum[i]

  print(data_num)
  print(places)
  print(y[i])


  # plt.bar(place, width=-0.4, height=y, align='edge')
  # plt.show()
