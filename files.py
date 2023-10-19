#Below I am creating the path variable and setting the variable to the days.text path

path = r'C:\Users\user\Desktop\Post-Laptop-Programming\Python\Advanced-Python\days.txt'

#In this example, we only want to read from the file, so we will use the 'r' mode

#We will use the open() function to open the days.txt file and assign it to the file object myFile

myFile = open(path, 'r')

#After we have opened the file, we can then read from it, which we will do next

file_contents = myFile.read()

print(file_contents)

# Don't forget to close the file when you're done with it
myFile.close()

file_input = open("read.txt",'r')
data = file_input.readline()
print(data)

#The output of the above (print(data)) is `Hello!`
#Here we are opening the file 'read.txt' in a read only mode
#We can see that it read one line at a time

#file_input.readlines() returns a list of the lines in the file, where each itmes of the list represents a single line
#The examplde below reads the same file but this time with the parameter set to 20 bytes
#Hence, only the elements until 20 bytes are read from the file

file_input = open("read.txt",'r')
list = file_input.readlines(20)
print(list)

#The above has the output ['Hello!\n', 'Wagwanning fam?\n']. We can see how it is a list with each line taking up an element in the list

##write() function
#Let's first use write() for writing to a file in Python. This function puts the given text in a single line

file_object = open("read.txt",'w')
file_object.write("Python is awesome!")

new_content = open("days.txt",'a')
new_content.write("Bonjour")