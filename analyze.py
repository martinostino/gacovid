import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#get data
inp = input("Do you want GA or Fulton data? (type g or f)")
if inp == "g":
	myfile = open("ga_dat.csv","r")
if inp == "f":
	myfile = open("fulton.csv","r")
header = myfile.readline()
everything = myfile.readlines()
date = []
num_pos = []
rate_pos = []
for data in everything:
	piece = data.split(",")
	date.append(piece[0])
	num_pos.append(float(piece[1]))
	rate_pos.append(float(piece[2]))
myfile.close()
#print(date)
#print(num_pos)
#print(rate_pos)


#7-Day Moving Average Calculations:
ave_num = [None,None,None,None,None,None]
aseries1 = pd.Series(num_pos)
windows1 = aseries1.rolling(7)
mov_ave1 = windows1.mean()
mov_ave_list1 = mov_ave1.tolist()
without_nans1 = mov_ave_list1[7-1:]
for each in without_nans1:
	ave_num.append(each)

ave_rate = [None,None,None,None,None,None]
aseries2 = pd.Series(rate_pos)
windows2 = aseries2.rolling(7)
mov_ave2 = windows2.mean()
mov_ave_list2 = mov_ave2.tolist()
without_nans2 = mov_ave_list2[7-1:]
for each in without_nans2:
	ave_rate.append(each)

#Calculations
max_loc = num_pos.index(max(num_pos)) #location
#print(max_loc)
weight_list = []
tot_val = num_pos[max_loc]/(rate_pos[max_loc]/100)
for each in rate_pos:
	aweight = (each/100)*tot_val
	weight_list.append(aweight)

ave_weight = [None,None,None,None,None,None]
aseries3 = pd.Series(weight_list)
windows3 = aseries3.rolling(7)
mov_ave3 = windows3.mean()
mov_ave_list3 = mov_ave3.tolist()
without_nans3 = mov_ave_list3[7-1:]
for each in without_nans3:
	ave_weight.append(each)


#make plots
#Raw Numbers
fig, ax1 = plt.subplots()
color = "blue"
ax1.set_xlabel('date')
for tick in ax1.get_xticklabels():
    tick.set_rotation(45)
ax1.set_ylabel('Number of Postive Cases', color=color)
ax1.plot(date, num_pos, color=color)
#ax1.plot(date, ave_num, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'red'
ax2.set_ylabel('Postive Rate', color=color)
ax2.plot(date, rate_pos, color=color)
#ax2.plot(date, ave_rate, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax1.xaxis.set_major_locator(plt.MaxNLocator(25))
fig.tight_layout()
#plt.show()

#7-Day Rolling Average
fig,ax3 = plt.subplots()
color = "blue"
ax3.set_xlabel('date')
for tick in ax3.get_xticklabels():
    tick.set_rotation(45)
ax3.set_ylabel('Number of Postive Cases', color=color)
ax3.plot(date, ave_num, color=color)
ax3.tick_params(axis='y', labelcolor=color)
ax4 = ax3.twinx()
color = 'red'
ax4.set_ylabel('Postive Rate', color=color)
ax4.plot(date, ave_rate, color=color)
ax4.tick_params(axis='y', labelcolor=color)
ax3.xaxis.set_major_locator(plt.MaxNLocator(25))
fig.tight_layout()
#plt.show()

#Weighted
fig, ax5 = plt.subplots()
color = "blue"
ax5.set_xlabel('date')
for tick in ax5.get_xticklabels():
    tick.set_rotation(45)
ax5.set_ylabel('Weighted Positive Cases', color=color)
ax5.plot(date, weight_list, color=color, label="Number of 'Real' Cases")
ax5.tick_params(axis='y', labelcolor=color)
#ax6 = ax5.twinx()
color = 'red'
ax5.plot(date,ave_weight,color=color, label="7-Day Moving Average")
ax5.legend(loc = "upper left")
ax5.xaxis.set_major_locator(plt.MaxNLocator(25))
fig.tight_layout()
plt.show()
