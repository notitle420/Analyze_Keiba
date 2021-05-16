import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter



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
  #出現回数
  yNum = []
  #あたり率
  y = []
  for i in range(start,end):
    for n in range(1,13):
      try:
        path = "Vumacsv/" + str(i) + "_" + str(n) + "_info.csv"
        data = get_data(path)
        hit_boolean = hit_detection(data["result"])
        yNum.append(data["place"])
        if hit_boolean:
          y.append(data["place"])
      except:
        None
  c1 = Counter(yNum)
  c2 = Counter(y)
  print(c1.most_common())
  print(c2.most_common())
  # for i in range(10):
  #   y[i] = y[i] / yNum[i]



  # plt.bar(place, width=-0.4, height=y, align='edge')
  # plt.show()
