import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime 
import statistics
import main
import csv

average_daily_list = []
def count_missing_values():
    result = 0
    diction = main.dataAssigner(1)
    for key in diction:
            if "NA" in diction[key]:
                result += diction[key].count("NA")
            else:
                continue
    print("There are {} missing values in the data.".format(result//2))
    print("The strategy to fill the missing value is to fill every missing value with the average of each interval(Question 2)\n")

def daily_pattern():
    diction2 = main.dataAssigner(2)
    for key in diction2:
        for i in range(len(diction2[key])):
            # In this part we assume that every missing values are filled with zero
            if diction2[key][i] == "NA":
                diction2[key][i] = "0"
        diction2[key] = [int(s) for s in diction2[key]]
        mean_daily = np.mean(diction2[key])
        average_daily_list.append(mean_daily)

def input_missing_values():
    average_in_int = [int(s) for s in average_daily_list]
    average_in_str = [str(i) for i in average_in_int]
    diction = main.dataAssigner(1)
    for key in diction:
        if 'NA' in diction[key]:
            diction[key] = average_in_str
    del diction['date']
    for key in diction:
            diction[key] = [int(s) for s in diction[key]]
            plt.hist(diction[key], color="green")
            plt.title("{}".format(key))
            plt.xlabel('Steps', fontsize=18)
            plt.ylabel('Frequency', fontsize=16)
            mean_per_day = np.mean(diction[key])
            median_per_day = np.median(diction[key])
            print("Date {}: {} Steps\nAverage at date {}: {} Steps\nMedian at date {}: {} Steps\n".format(key, sum(diction[key]), key, mean_per_day, key, median_per_day)) 
            plt.show()

daily_pattern()
count_missing_values()
input_missing_values()