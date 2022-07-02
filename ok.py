import pandas as pd
import statistics
import csv

df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds"].to_list()

#Mean for height and Weight
height_mean = statistics.mean(height_list)
Weight_mean = statistics.mean(Weight_list)

# Median for height and weight
height_median = statistics.median(height_median)
Weight_median = statisttics.median(weight_median)

# Mode for height and weight

height_mode = staistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

#Printing mean, median and mode to validate


print("Mean, Median and Mode of height is {}, {} and {} respectively".format(height_mean, height_median, height_mode))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(weight_mean, weight_median, weight_mode))

#Standard deviation for height and weight
height_std_deviation = statistics.stdev(height_list)
weight_std_deviation = statistics.stdev(weight_list)

#1, 2 and 3 Standard Deviations for height
height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation

height_first_std_deviation_start, height_second_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation

height_first_std_deviation_start, height_third_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation


#Percentage of data within 1, 2 and 3 Standard Deviations for Height
weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_first_std_deviation_start and result < height_first_std_deviation_end]

weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end]

weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_third_std_deviation_start and result < weight_thir_std_deviation_end]

#Printing data for height and weight (Standard Deviation)
print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))

print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))

print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))