## MIN / MAX
#temperatures_arr = [21, 23, 26, 22, 25, 20, 19, 23]

#i = 0
#max = 0
#while i < 8:
#  temp = temperatures_arr[i]
#   i = i + 1
#   if temp > max:
#       max = temp
#print("maximum is", max)
import statistics

def get_max_value(temperatures_arr):
    return max(temperatures_arr)

#
#min = max
#while i < len(temperatures_arr):
#    temperature = temperatures_arr[i]
#    i = i + 1
#    if temperature < min:
#        min = temperature
#print("minimun is", min)
def get_min_value(temperatures_arr):
    return min(temperatures_arr)

#
## MEAN
#pressure_arr = [80, 90, 100, 150, 120, 110, 160, 110, 100]
#
#sum = 0
#for pressure in pressure_arr:
#    sum = pressure + sum
#    length = len(pressure_arr)
#    mean = sum / length
#print("The mean is", mean)
def get_mean(pressure_arr):
    return statistics.mean(pressure_arr)
#
## MEDIAN
#power_arr = [4, 5, 2, 6, 3, 7, 8, 9, 6, 5, 2]
#
#power_arr.sort()
#
#a = int(input("please enter a number : "));
#if (a % 2 == 0):
#    print("This number is even")
#else:
#    print("This number is odd")
#
#a = len(power_arr)
#print("the number of items inside list is", a)
#
#def find_middle(input_list):
#    middle = float(len(input_list))/2
#    return (input_list[int(middle)], input_list[int(middle-1)])
#
#middle_value = 0
#if (a % 2):
#    print("This number is even")
#    x, y = find_middle(power_arr)
#    middle_value = (x + y) / 2
#else:
#    print("This number is odd")
#    middle_index = float(len(power_arr))/2
#    print("The middle index is", middle_index)
#    middle_value = power_arr[int(middle_index - .5)]
#print("The median is", middle_value)

def get_median(power_arr):
    return statistics.median(power_arr)
#
#
# mode values
#import statistics

#values = [8,  11,  9,  14,  9,  15,  18,  6,  9,  10]
#mode = statistics.mode(values)
#print(mode) # Answer 9

def get_mode(values):
    return statistics.mode(values)
#
# Standard deviation
#import statistics
#
#sample = [5, 4, 3, 2, 1]
#value = statistics.stdev(sample)
#print("Standard Deviation of sample is % s" % value) # answer 1.5811388300841898

def get_stdeviation(sample):
    return statistics.stdev(sample)

# Variance
#
#import statistics
#
#sample = [10, 9, 8, 7, 6, 5, 4]
#value = statistics.variance(sample)
#print("Variance of sample is % s " % value) # Answer 4.666666666666667

def get_variance(sample):
    return statistics.variance(sample)
