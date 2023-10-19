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
#Before we can write our programme, we have to create a Python programming file (like this one). I have created a new one in this repository
