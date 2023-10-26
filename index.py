###Introduction###

#Portability: The open source nature of Python makes it portable and can be ported to many platforms without requiring any changes
#E.g. Linux, Windows, Solaris, Playstation, Sharp Zaurus and more
#High productivity: Python is a good choice if you want to develop complex multi-protocol network applications

#It can connect with database systems and can read and modify files
#It supports rapid prototyping and production completed software development
#It is an interpreted language which means that the interpreter implements the code line by line at a single time
#It can be integrated with languages like C,JAVA,C++, easily
#It is a very easy to learn language,that makes it user-friendly
#It is a dynamically-typed language.This means that the type for a value is decided at runtime, not in advance

#It is used in web-development, data analysis, education

###Files in Python###
#A filename contains two parts - filename and extension
#Python provides us with an important feature for reading data from the file and writing data into a file
#Even though we have various files formats in our computer, the in-built methods of Python can handle two major types of files - 
#Text files and Binary files

#The text and binary files have .txt and .bin as their extensions respectively

#Text files are used to store human readable information whereas the binary files contain computer readable information that is written
#using binary (0s and 1s)

##How Python handles files
#If you are working on an application where you process huge data, then we cannot expected those data to be stored in a variable as the 
#as the variables are volatile in nature
#Hence, to handle such situations, the role of files will come into the picture.
#As files are non-volatile in nature, the data will be stored permanently and using Python we will handle these files in our applications

##File processing
#In Python, file processing takes place in the following order:

#1. Open a file that returns a filehandle (File object)
#2. Use the handle to perform read or write action
#3. Close the file

#Before you can perform any operation on a file in Python, you need to open it first
#And as the read/write transaction completes, you should close it to free the resources tied with the file

###Different File Handling Operations###

##Opening a file in Python
#To open a file in Python, we use its built-in open() function
#This function returns a file object, that would be utilized to call other methods associated with it
#You can you it to read or modify the file

##The Opening Syntax
#The following is the syntax for the open() method:

file_handle = open(file_name, access_mode)

#`file_name`: is the name of the file which needs to be opened
#`access_mode`: specifies the mode in which the file has to be opened, such as read, write and so on. By default,
#it will be in the read-mode

##The File modes
#We can specify the mode while opening a file, to specify whether we want to read(r) write(w) or append(a) to the file
#There are six access modes available in Python to work with a text file

#1. "r" - Read mode is used only to read data from the file. It is also the default mode
#2. "w" - It will create a new file if it does not exist, otherwise it will overwrite the file and allow you to write to it
#3. "a" - It will write data to the end of the file. It does not erase the existing data, and the file must exist for this mode
#4. "r+" - It opens the file to both read and write. The file pointer will be at the beginning of the file
#5. "w+" - The exact same as "r+" but if the file does not exist, a new one is made. Otherwise, the file is overwritten
#6. "a+" - Similar to "w+" as it will create a new file if the file does not exist. Otherwise, the file pointer is at the end of the file if it exists

##Creating a text file
#Before we can begin working in Python, we need to ensure that we have a file to work with
#We can create a text file, and call it `days.txt`
#In this file I have listed the days of the week
#Now that we have a text file to process, we can begin our code!

##Opening a file
#Before we can write our programme, we have to create a Python programming file (like this one).

#Below I am creating the path variable and setting the variable to the days.text path

path = 'C:/Users/user/Desktop/Post-Laptop-Programming/Python/Advanced-Python/days.txt'

#In this example, we only want to read from the file, so we will use the 'r' mode

#We will use the open() function to open the days.txt file and assign it to the file object myFile

myFile = open(path, 'r')

#After we have opened the file, we can then read from it, which we will do next

#To read a file in Python, we must open the file in reading 'r' mode, as we've done above
#Then, you can call any of the methods that Python provides for reading from a file
#There are three functions which we can use to read the files in Python:

#1. read()
#2. readline()
#3. readlines()

##read() function
#It reads the given no. of bytes (N) as a string. If no value is given, then it reads the file til the end
#The following is the syntax of read() function:

file_handle.read(N)

#Since our file has been opened, we can now manipulate it (ie read from it) through the file object we assigned to it

myFile.read()

#Output:

#Monday
#Tuesday
#Wednesday
#Thursday
#Friday
#Saturday
#Sunday

##readline() function
#Python file method readling() reads one entire line from the file
#Have a look at the syntax of readline() function:

fileObj.readline()

#Simply put, this operation will read the file line-by-line

##readlines() function
#readlines() method will return all the lines in a file in the format of a Python list where each element is a line in the file
#Have a look at the syntax of readlines() function:

fileObj.readlines()

#The function returns a list of all the lines which can then be used for further manipulation or simply printed
#If we specify the parameter, the lines exceeding the number of bytes from the hint parameter will not be returned by the readlines method

##Writing to a file in Python
#Python provides the write() method to write a string or sequence of bytes to a file
#When using this function, any information inside the file will be overwritten
#To do that, Python provides a built-in method write() which writes any string to an open file

##write() function
#Let's first use write() for writing to a file in Python. This function puts the given text in a single line

file_object.write("some text")

#Let's consider the same sample text file: read.txt

file_input = open("read.text","w")
file_input.write("Python is amazing!")

#Output:

Python is amazing!

#In the previous example, file_input is the file object. We have opened the file "read.txt" in the 'w' mode (write)
#When we open the file in write mode and write to a file, we know that the content gets overwritten
#Thus, now the read.txt file has the content: `Python is amazing`

#Now, most of the time you will be writing to a file without destroying the existing content
#To write to a file while preserving the previous content is called appending to a file
#In the append mode, the file pointer is at the end of the file, thus we can continue writing from teh end of the previous content

#For this example, let's append to the same file that we already created (read.txt).

file_input = open("read.txt",'a')
file_input.write("Bonjour")

#We can see that 'Bonjour' is added to the end
#We have opened the file 'read.txt' using append mode
#This tells Python not to overwrite the data but start writing from the last line

##Closing a file
#It's always the best practice to close a file when your works gets finished
#Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python
#Python has a garbage collector to clean up unreferenced objects but we must not rely on it to clos the file

#The sytax to use the close() method is:

fileObj.close()

#After closing the file we cannot perform any operation on the file

#An example
#Here we are opening a file for reading and closing it properly at the end:

file_input = open("read.txt",'r')
print(file_input.read())
file_input.close()

###Python Modules
#To use the functionality present in any module, you have to import it into your current program (like in ReactJS)
#You need to use the `import` keyword along with the desired module name

import module_name

#When the interpreter comes across an import statement, it imports the module to your current program
#You can use the functions insude a module by using a dot(.) operator which allows us to call the function by first 
#specifying the module name, and then the name of the function

module_name.functionName()

##Random Module
#Python offers a random module that can generate random numbers
#The random module is a built-in module to generate the pseudo-random variables
#It can be used to perform some action randomly such as to get a random number, selecting a random element from a list,
#shuffle elements randomly, etc
#The most important method of the random module is the random() method
#Most of the other functions depend on it. The random() method generates a random float in range (0.0,1.0)

##Seeding Random Numbers
#The random module takes a number as input and generates a random number for it.
#This initial value is known as a seed, and the procedure is known as seeding
#The numbers we generate through pseudo-random number generators are deterministic
#This means they can be replicated using the same seed
#Let's understand this through an example:

import random
print('RandomNumber 1=>',random.random())
print('RandomNumber 2=>',random.random())

#Notice here that we haven't mentioned the value of the seed. By default, the current system time in milliseconds is used as a seed

#Let's have a look at the output:

Random Number 1=> 0.929588880056842
Random Number 2=> 0.152223695233975

#Both numbers are different because of the change in time during execution from the first statement to the second statement

##random.randint()

import random
print(random.randint(3,9))

#Output:
5

#The random.randint() method takes two arguments describing the range from which the method draws a random integer

##random.randrange(start,stop,step)
#Syntax: random.range(start,stop,step)
#The random.randrange() function returns a random integer within the given range, ie start and stop
#The random.randrange() function takes three parameters as input: start, stop and step. Out of these parameters,
#the two parameters, start and step and optional

import random
print(random.randrange(3,9))

#Output:
4

#In the script above, the random.randrang() method is similar to random.randint() but it also lets us define the third argument, 
#which is the step point of the defined range
#If the start parameter is not passed in, it takes the default value 0
#On the other hand, step parameters are optional. It takes the default value 1

##random.shuffle()
#This funciton is used to shuffle a given sequence randomly
#The shuffle function shuffles a list in-place. The most common example is suffling cards

import random 
list = [10,6,4,11,1]
random.shuffle(list)
print("Printing shuffled list", list)

#Output
Printing shuffled list [4,10,1,11,6]

##random.choices()
#Do you want to choose single or multiple elements from the list randomly with a different probability?
#If yes, this method will give you a choice to choose more than one element from the sequence randomly
#This function basically takes a sequence as a parameter and returns random values from it
#Let's have a look at the syntax of this function:

random.choices(population, weights=None,*,cum_weights=None,k=1)

#The random.choices() return a k sized list of elements chosen from the population with replacement
#Weights or cum_weights are used to define the selection probability for each element
#If a weights sequence is specified, random selections are made according to the relative weights
#Alternatively, if a cum_weights sequence is given, the random selections are made according to the cumulative weights
#If neither weights nor cum_weights are specified, selections are made with equal probability
#You cannot specify both weights and cumulative weights

#Example:

import random
numberList = [151,251,351,451,551]
print(random.choices(numberList, weights =(10,20,30,40,50),k=5))

#Output:
[551,331,551,251,551]

#As you can see in the output, we got 551 three times because we specified the highest weight for it. So it has
#the highest probablity to be selected
#We specified k=5 to choose 5 elements. You can specify any number you want

##Statistics Modules
# To use the statistics module, our first step is to import the statistics module provided by Python

import statistics

#In Python, we don't have to manually calculate the mean, median and mode
#We simply yse the functions provided by the statistics module and are good to go
#Example:

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

import statistics
list_1 = [15,30,45,60]
list_2 = [20,40]
print("Low median of list_1 is:",statistics.median_low(list_1))
print("Low median of list_2 is:",statistics.median_low(list_2))

##High Median (statistics.median_high())
#If the actual median is halfway between two items, the high median is the item immediately higher than the actual median

import statistics
list_3 = [15,30,45,60]
list_4 = [20,40]
print("High median of list_3 is:",statistics.median_high(list_3))
print("High median of list_4 is:",statistics.median_high(list_4))

##Variance
#Variance in statistics refers to the average of the squared distances from the mean
#In other words, how varied in the data? Does it vary a lot, in that we have one grade of say 20, another that's 99,
#and another that's 50? Are the grades very varied, or are they all fairly close together?

##Implementing the Variance Method (statistics.variance())
#So let's try the variance function on our current list of grades, and then we will change the grades to get a different result
#Also, to better understand what the value we calculate is, a variance value of zero means that all of the data values
#are identical. All non-zero variances are positive

import statistics
grades = [70,90,50,85,65,83,94]
grades_mean = statistics.mean(grades)
print("variance of data is:",statistics.variance(grades,grades_mean))

#Output:
variance of data is 246.57

#Let's change the grades to all the same value to see what happens then
grades_2 = [80,80,80,80,80,80,80]
grades_2_mean = statistics.mean(grades_2)
print("variance of data is:",statistics.variance(grades_2,grades_2_mean))

#Output:
variance of data is 0

#Sure enough, that gives us a variance of zero. Since all of the grades are the same, they do not vary at all

##Standard Deviation (statistics.stdev.())
#Standard deviation is used to show how much variation from the mean exists. You can think of it as a typical variation from the mean
#A low standard deviation indicates that the values tend to be close to the mean of the set, while a high standard deviation indicates
#indicates that the values are spread out over a wider range

import statistics
grades = [89,91,95,92,93,94,98,90]
stdevgrades = statistics.stdev(grades)
print("The standard deviation of the list is:", stdevgrades)

#Output:

The standard deviation of the list is: 2.915474226504

#Fun fact: the standard deviation is actually the square root of the variance


