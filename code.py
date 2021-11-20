import csv
import plotly.figure_factory as ff
import pandas as pd 
import statistics

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data)/len(data)
print(mean)

median = statistics.median(data)
print(median)

mode = statistics.mode(data)
print(mode)

standard_deviation = statistics.stdev(data)
print(standard_deviation)

first_stdev_start, first_stdev_end = mean-standard_deviation, mean+standard_deviation
list_data_1_stdev = [result for result in data if result > first_stdev_start and result < first_stdev_end]
print("{}% of data lies within 1 standard deviation".format(len(list_data_1_stdev)*100/len(data)))

two_stdev_start, two_stdev_end = mean-(standard_deviation*2), mean+(standard_deviation*2)
list_data_2_stdev = [result for result in data if result > two_stdev_start and result < two_stdev_end]
print("{}% of data lies within 2 standard deviation".format(len(list_data_2_stdev)*100/len(data)))

three_stdev_start, three_stdev_end = mean-(standard_deviation*3), mean+(standard_deviation*3)
list_data_3_stdev = [result for result in data if result > three_stdev_start and result < three_stdev_end]
print("{}% of data lies within 3 standard deviation".format(len(list_data_3_stdev)*100/len(data)))