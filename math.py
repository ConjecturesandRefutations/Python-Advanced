import statistics
scores = [6,7,2,6,3,5,5,5,2,5,6,1,2]
a = statistics. mean(scores)
print(a)
b = statistics.median(scores)
print(b)
c = statistics.mode(scores)
print(c)

##Low Median (statistics.median_low())
#If the actual median is halfway between two items, the low median is the item immediately lower than the actual median

list_1 = [15,30,45,60]
list_2 = [20,40]
print("Low median of list_1 is:",statistics.median_low(list_1))
print("Low median of list_2 is:",statistics.median_low(list_2))

##High Median (statistics.median_high())
#If the actual median is halfway between two items, the high median is the item immediately higher than the actual median

list_3 = [15,30,45,60]
list_4 = [20,40]
print("High median of list_3 is:",statistics.median_high(list_3))
print("High median of list_4 is:",statistics.median_high(list_4))

import statistics
grades = [70,90,50,85,65,83,94]
grades_mean = statistics.mean(grades)
print("variance of data is:",statistics.variance(grades,grades_mean))

#Variance of data is 246.57

#Let's change the grades to all the same value to see what happens then
grades_2 = [80,80,80,80,80,80,80]
grades_2_mean = statistics.mean(grades_2)
print("variance of data is:",statistics.variance(grades_2,grades_2_mean))

grades = [89,91,95,92,93,94,98,90]
stdevgrades = statistics.stdev(grades)
print("The standard deviation of the list is:", stdevgrades)