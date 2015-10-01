#!/usr/bin/python
import os

__author__ = 'Prayance'

# this is the directory that the file will be copied from.
# fileDirectory = "/home/mysqlbackups/latest"
fileDirectory = "/home/elly/sqlBackups/"

# TODO need to import and initialise logger
logDirectory = "/home/elly/myLogs/"
logName = "logFile.log"


# returns a list of filenames that are in the directory
def getfiles():
    filenames = []
    try:
        mylist = os.listdir(fileDirectory)
        for myfile in mylist:
            if myfile.endswith(".zip"):
                filenames.append(myfile)
    except Exception as e:
        print "Error encountered. The error is: {0}".format(e)
    return filenames


# returns a list of filenames that are in the directory
def getfolders():
    filenames = []
    try:
        mylist = os.listdir(fileDirectory)
        for myfile in mylist:
            if not myfile.endswith(".zip"):
                filenames.append(myfile)
    except Exception as e:
        print "Error encountered. The error is: {0}".format(e)
    return filenames


# returns the number of elements in an array
def countfiles(myarray):
    counter = 0
    for item in myarray:
        counter += 1
    return counter


# from the directory, choose the last modified - latest file to zip it after
def choosemyfile(directory):
    return max([os.path.join(directory, d) for d in os.listdir(directory)], key=os.path.getmtime)


# ----------------------------------------------------------------------------------------------------------------------
def main():
    myarray = getfiles()
    print "My list has: " + str(countfiles(myarray)) + " elements."
    for item in myarray:
        print "My Files are: " + item

    print "My chosen file is: " + choosemyfile(fileDirectory)

main()
