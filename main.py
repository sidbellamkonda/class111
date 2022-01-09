import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")

data = df["Math_score"].tolist()

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean

mean_list = []
for i in range(0,1000):
    setOfMeans = randomSetOfMean(100)
    mean_list.append(setOfMeans)

mean = statistics.mean(mean_list)
std_dev = statistics.stdev(mean_list)

print("Mean of Sampling:", mean)
print("Standard Deviation of Sampling", std_dev)

first_sd_start, first_sd_end = mean - std_dev, mean + std_dev
second_sd_start, second_sd_end = mean - 2*std_dev, mean + 2*std_dev
third_sd_start, third_sd_end = mean - 3*std_dev, mean + 3*std_dev

df = pd.read_csv("School1.csv")
data1 = df["Math_score"].tolist()
mean_sample1 = statistics.mean(data1)
print("Mean of School 1 scores: ", mean_sample1)
fig = ff.create_distplot([mean_list], ["student_marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_sample1, mean_sample1], y = [0, 0.17], mode = "lines", name = "Mean of Students who had math lab"))

fig.add_trace(go.Scatter(x = [first_sd_start, first_sd_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 1 start"))
fig.add_trace(go.Scatter(x = [first_sd_end, first_sd_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 1 end"))

fig.add_trace(go.Scatter(x = [second_sd_start, second_sd_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 2 start"))
fig.add_trace(go.Scatter(x = [second_sd_end, second_sd_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 2 end"))

fig.add_trace(go.Scatter(x = [third_sd_start, third_sd_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 start"))
fig.add_trace(go.Scatter(x = [third_sd_end, third_sd_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 end"))
fig.show()



df = pd.read_csv("School2.csv")
data2 = df["Math_score"].tolist()
mean_sample2 = statistics.mean(data2)
print("Mean of School 2 scores: ", mean_sample2)
fig = ff.create_distplot([mean_list], ["student_marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_sample2, mean_sample2], y = [0, 0.17], mode = "lines", name = "Mean of Students who used the app"))

fig.add_trace(go.Scatter(x = [first_sd_start, first_sd_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 1 start"))
fig.add_trace(go.Scatter(x = [first_sd_end, first_sd_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 1 end"))

fig.add_trace(go.Scatter(x = [second_sd_start, second_sd_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 2 start"))
fig.add_trace(go.Scatter(x = [second_sd_end, second_sd_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 2 end"))

fig.add_trace(go.Scatter(x = [third_sd_start, third_sd_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 start"))
fig.add_trace(go.Scatter(x = [third_sd_end, third_sd_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 end"))
fig.show()



df = pd.read_csv("School3.csv")
data3 = df["Math_score"].tolist()
mean_sample3 = statistics.mean(data3)
print("Mean of School 3 scores: ", mean_sample3)
fig = ff.create_distplot([mean_list], ["student_marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_sample3, mean_sample3], y = [0, 0.17], mode = "lines", name = "Mean of Students who were enforced with registers"))

fig.add_trace(go.Scatter(x = [first_sd_start, first_sd_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 1 start"))
fig.add_trace(go.Scatter(x = [first_sd_end, first_sd_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 1 end"))

fig.add_trace(go.Scatter(x = [second_sd_start, second_sd_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 2 start"))
fig.add_trace(go.Scatter(x = [second_sd_end, second_sd_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 2 end"))

fig.add_trace(go.Scatter(x = [third_sd_start, third_sd_start], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 start"))
fig.add_trace(go.Scatter(x = [third_sd_end, third_sd_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 end"))
fig.show()



zScore1 = (mean_sample1 - mean)/std_dev
print("ZScore1: ", zScore1)

zScore2 = (mean_sample2 - mean)/std_dev
print("ZScore2: ", zScore2)

zScore3 = (mean_sample3 - mean)/std_dev
print("ZScore3: ", zScore3)