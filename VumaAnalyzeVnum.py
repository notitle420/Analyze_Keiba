import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def get_data(file_path):
  df = pd.read_csv(file_path,header=None,index_col=0)
  s = df[1]
  return s


def hit_detection(result):
  hit_detection = False
  print(result)
  if int(result) > 0 :
    hit_detection = True
  return hit_detection

if __name__ == '__main__':
  start = 23
  end = 2080
  x = [1,2,3]
  yNum = [0,0,0]
  y = [0,0,0]
  for i in range(start,end):
    for n in range(1,13):
      try:
        path = "Vumacsv/" + str(i) + "_" + str(n) + "_info.csv"
        data = get_data(path)
        hit_boolean = hit_detection(data["result"])
        if data["v_num"] == "1":
            yNum[0] += 1
        elif data["v_num"] == "2":
            yNum[1] += 1
        elif data["v_num"] == "3":
            yNum[2] += 1
        else:
          x.append(0)
          yNum.append(0)
          y.append(0)

        if hit_boolean:
          if data["v_num"] == "1":
            y[0] += 1
          elif data["v_num"] == "2":
            y[1] += 1
          elif data["v_num"] == "3":
            y[2] += 1

      except:
        print("None")
  y[0] = y[0] / yNum[0]
  y[1] = y[1] / yNum[1]
  y[2] = y[2] / yNum[2]
  print(yNum)
  print(y)
  plt.bar(x, width=-0.4, height=y, align='edge')




  # x = np.linspace(0, 1, 100)
  # plt.figure(0)
  # plt.gca().set_aspect('equal', adjustable='box')
  # plt.title('logistic map')
  # plt.grid(True)
  # plt.plot(x, 4*x*(1-x))
  # plt.plot(x, x*(1-x))
  # plt.xlabel('$x$', fontsize=20)
  # plt.ylabel('$y(x)$', fontsize=20)
  # plt.legend(["r=4", "r=1"])
  plt.show()
