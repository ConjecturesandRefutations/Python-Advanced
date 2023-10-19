#Below I am creating the path variable and setting the variable to the days.text path

path = 'C:\Users\user\Desktop\Post-Laptop-Programming\Python\Advanced-Python\days.txt'

#In this example, we only want to read from the file, so we will use the 'r' mode

#We will use the open() function to open the days.txt file and assign it to the file object myFile

myFile = open('path', 'r')

#After we have opened the file, we can then read from it, which we will do next