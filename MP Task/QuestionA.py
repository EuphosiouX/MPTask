import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime 
import statistics
import main

def mean_per_day():
    diction = main.dataAssigner(1)
    for key in diction:
        if 'NA' not in diction[key]:
            diction[key] = [int(s) for s in diction[key]]
            plt.hist(diction[key], color="r")
            plt.title("{}".format(key))
            plt.xlabel('Steps', fontsize=18)
            plt.ylabel('Frequency', fontsize=16)
            mean_per_day = np.mean(diction[key])
            median_per_day = np.median(diction[key])
            print("Date {}: {} Steps\nAverage at date {}: {} Steps\nMedian at date {}: {} Steps\n".format(key, sum(diction[key]), key, mean_per_day, key, median_per_day)) 
            plt.show()
        else: 
            print("Date {}: {}\nAverage at date {}: {}\nMedian at date {}: {}\n".format(key,"NA", key, "NA", key, "NA"))

mean_per_day()