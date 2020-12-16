import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime 
import calendar
import statistics
import main
import csv

file = pd.read_csv('activity.csv')

def day(date): 
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    the_date = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    if calendar.day_name[the_date] in weekdays:
        return 'weekday'
    else:
        return 'weekend'

file['day'] = file['date'].apply(day)

interval = []
weekday = []
weekend = []
for i in file['interval'].unique():
    interval.append(i)
    weekday.append(file.loc[(file['interval']==i) & (file['day']=='weekday'), 'steps'].dropna().mean())
    weekend.append(file.loc[(file['interval']==i) & (file['day']=='weekend'), 'steps'].dropna().mean())

final_file = pd.DataFrame({'Interval':interval, 'Weekday':weekday, 'Weekend':weekend})

final_file.plot(x ='Interval')
plt.title('Weekday weekend')
plt.ylabel('Steps')
plt.show()