#!/usr/bin/env python3

##From the error log file, use Python regular expressions to extract the
##IP addresses. Then use Python to write the IP addresses to a text file.
##The addresses should be listed in a column.

import re


# Making a function to read the error log file w/error handling.
def readFile():
    try:
        print()
        print("---------------------------------")
        print("Welcome to the IP address finder!")
        print("---------------------------------")
        print()
        filepath = input("Please enter the filepath of log file: ")
        # filepath = "error_log.txt" # File is in current working directory.
        print()
        newFile = input("Please enter a name for the new log file: ")
        print()
        
        fileObject = open(filepath, "r")
        line = fileObject.readline()
        IPlogFile = open(newFile, "a")
        
        while(line != ""):
            # print(line, end="") # Error file spaces are actually read as str.
            line = fileObject.readline()
            # Read IP, a slash is needed for "."
            data = re.search("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", line)
            if data != None:
                print(data.group()) # Testing the console data before write to file
                IPlogFile.write(data.group() + "\n" + "\n")
                print()
        fileObject.close()
        IPlogFile.close()
        print()
        print("The following data was written to log file: " + newFile )
        print()
    except Exception as e:
        print()
        print(" *** ERROR HAS OCCURRED *** ")
        print("Error Type:", type(e))
        print("Error:", e)
        print("Error Arguments:", e.args)

# Calling the readFile() function.
readFile()







            
