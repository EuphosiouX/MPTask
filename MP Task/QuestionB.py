import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime 
import statistics
import main

def average_daily_pattern():
    average_daily_list = []
    diction2 = main.dataAssigner(2)
    for key in diction2:
        for i in range(len(diction2[key])):
            # In this part we assume that every missing values are filled with zero
            if diction2[key][i] == "NA":
                diction2[key][i] = "0"
        diction2[key] = [int(s) for s in diction2[key]]
        mean_daily = np.mean(diction2[key])
        average_daily_list.append(mean_daily)
        interval = [int(s) for s in diction2.keys()]
        for i in range(len(average_daily_list)):
            diction2[key] = [average_daily_list[i]]
    arr_x = np.array(interval)
    arr_y = np.array(average_daily_list)
    plt.plot(arr_x, arr_y)
    plt.title("Daily Average Pattern")
    plt.xlabel('Interval', fontsize=16)
    plt.ylabel('Average steps', fontsize=16)
    print("Maximum number of steps: {} at interval: {}\n".format(max(average_daily_list), max(diction2, key=diction2.get)))
    plt.show()

average_daily_pattern()