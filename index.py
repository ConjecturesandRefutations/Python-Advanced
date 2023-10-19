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
#Python provides us with an important feature for rearing data from the file and writing data into a file
#Even though we have various files formats in our computer, the in-built methods of python can handle two major types of files - 
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