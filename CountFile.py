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
  x1 = [0,50,100,120,140,160,180,200,220,240,260,280,300]
  a = [0,0,0,0,0,0,0,0,0,0,0,0,0] #合計金額
  b = [0,0,0,0,0,0,0,0,0,0,0,0,0] #出現回数
  c = [0,0,0,0,0,0,0,0,0,0,0,0,0] #当たった回数
  d = [0,0,0,0,0,0,0,0,0,0,0,0,0] #あたり率


  for i in range(start,end):
    for n in range(1,13):
      try:
        path = "Vumacsv/" + str(i) + "_" + str(n) + "_info.csv"
        data_num += 1
      except:
        None

  # for k in range(12):
  #   d[k] = c[k]/b[k]
  print("data num = ",data_num)

  #plt.bar(x1, width=-0.4, height=a, align='edge')
  #plt.bar(x1, width=-0.4, height=d, align='edge')
  # plt.xlim(min(x),max(x))
  # plt.ylim(min(y), max(y))
  # plt.yticks([min(y)-10000, -10000, 0,10000,20000,max(y)+10000])
  #plt.xticks([0,100,200,300,400,500])
  ##plt.scatter(x, y)
  #plt.show()
