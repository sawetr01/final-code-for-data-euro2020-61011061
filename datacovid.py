# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:07:14 2021

@author: angpa
"""

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
df_perform = pd.read_csv('data/performance.csv') #test per thousand population
df_daily = pd.read_csv('data/daily test.csv') #daily test
df_positive = pd.read_csv('data/positive.csv') #positive per test
df_confirm = pd.read_csv('data/test per confirm.csv') # confirm case per test
df_hospital = pd.read_csv('data/hospital.csv')

hospital_den = df_hospital.iloc[4550:4610,3]
hospital_uk = df_hospital.iloc[17492:17552,3]
hospital_italy = df_hospital.iloc[9072:9132,3]
date = df_daily.iloc[16373:16433,2]
x = hospital_den
y = date
z = hospital_italy
u = hospital_uk 
fig,axes = plt.subplots(1,1)
plt.plot(y,x)
plt.plot(y,z)
plt.plot(y,u)
plt.title("population in hospital")
plt.xlabel("date")
plt.ylabel("population")
plt.legend(['denmark','italy','uk'])
plt.xticks(rotation=90)
axes.xaxis.set_major_locator(MaxNLocator(43))
plt.show()

daily_den = df_daily.iloc[12371:12431,3]
daily_uk = df_daily.iloc[53193:53253,3]
daily_italy = df_daily.iloc[22534:22594,3]
date = df_daily.iloc[16373:16433,2]
x = daily_den 
y = date
z = daily_italy
u = daily_uk
fig,axes = plt.subplots(1,1)
plt.plot(y,x)
plt.plot(y,z)
plt.plot(y,u)
plt.title("daily test")
plt.xlabel("date")
plt.ylabel("value of test")
plt.legend(['denmark','italy','uk'])
plt.xticks(rotation=90)
axes.xaxis.set_major_locator(MaxNLocator(43))
plt.show()

perform_den = df_perform.iloc[14816:14876,3]
perform_italy = df_perform.iloc[27802:27862,3]
perform_uk = df_perform.iloc[63607:63667,3]
x1 = perform_den 
y1 = date
z1 = perform_italy
u1 = perform_uk
fig,axes = plt.subplots(1,1)
plt.plot(y1,x1)
plt.plot(y1,z1)
plt.plot(y1,u1)
plt.title("test per thousand population")
plt.xlabel('date')
plt.ylabel('test perform')
plt.legend(['denmark','italy','uk'])
plt.xticks(rotation=90)
axes.xaxis.set_major_locator(MaxNLocator(43))

plt.show()

positive_den = df_positive.iloc[14459:14519,3]
positive_italy = df_positive.iloc[25583:25643,3]
positive_uk = df_positive.iloc[60121:60181,3]
x2 = positive_den
y2 = date
z2 = perform_italy
u2 = perform_uk
fig,axes = plt.subplots(1,1)
plt.plot(y2,x2)
plt.plot(y2,z2)
plt.plot(y2,u2)
plt.title("positive per test")
plt.xlabel('date')
plt.ylabel('positive rate')
plt.legend(['denmark','italy','uk'])
plt.xticks(rotation=90)
axes.xaxis.set_major_locator(MaxNLocator(43))
plt.show()

confirm_den = df_confirm.iloc[14392:14452,3]
confirm_italy = df_confirm.iloc[25302:25362,3]
confirm_uk = df_confirm.iloc[59495:59555,3]
x3 = confirm_den
y3 = date 
z3 = confirm_italy
u3 = confirm_uk
fig,axes = plt.subplots(1,1)
plt.plot(y3,x3)
plt.plot(y3,z3)
plt.plot(y3,u3)
plt.title("confirm per test")
plt.xlabel('date')
plt.ylabel('confirm rate')
plt.legend(['denmark','italy','uk'])
plt.xticks(rotation=90)
axes.xaxis.set_major_locator(MaxNLocator(43))
plt.show()













































