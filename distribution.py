import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv

dataFile = pd.read_csv("pro/Normal Distribution/StudentsPerformance.csv")
data = dataFile["math score"].tolist()


# print(data)
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
stddev = statistics.stdev(data)

print("The Mean Of Data = ",mean)
print("The Median Of Data = ",median)
print("The Mode Of Data = ",mode)
print("The Standard Deviation Of Data = ",stddev)

firstStddevStart,firstStddevEnd = mean-stddev,mean+stddev
listOfDataIn1stddev = [result for result in data if result>firstStddevStart and result<firstStddevEnd]
percentageOf1stStdDeviation = len(listOfDataIn1stddev)*100.0/len(data)
print("{}% Of Data Lies Within The First Standard Deviation ".format(percentageOf1stStdDeviation))

secondStddevStart,secondStddevEnd = mean-(2*stddev),mean+(2*stddev)
listOfDataIn2ndStdDev = [result for result in data if result>secondStddevStart and result<secondStddevEnd]
percentageOf2ndStdDeviation = len(listOfDataIn2ndStdDev)*100.0/len(data)
print("{}% Of Data Lies Within The Second Standard Deviation ".format(percentageOf2ndStdDeviation))

thirdStddevStart,thirdStddevEnd = mean-(3*stddev),mean+(3*stddev)
listOfDataIn3rdStdDev = [result for result in data if result>thirdStddevStart and result<thirdStddevEnd]
percentageOf3rdStdDeviation = len(listOfDataIn3rdStdDev)*100.0/len(data)
print("{}% Of Data Lies Within The Third Standard Deviation ".format(percentageOf3rdStdDeviation))

fig = ff.create_distplot([data],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[firstStddevStart,firstStddevStart],y=[0,0.15],mode="lines",name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[firstStddevEnd,firstStddevEnd],y=[0,0.15],mode="lines",name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[secondStddevStart,secondStddevStart],y=[0,0.15],mode="lines",name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[secondStddevEnd,secondStddevEnd],y=[0,0.15],mode="lines",name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.15],mode="lines",name="Mean"))
fig.show()