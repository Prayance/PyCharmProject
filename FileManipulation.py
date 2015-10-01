#!/usr/bin/python
import os

__author__ = 'Prayance'

# this is the directory that the file will be copied from.
fileDirectory = "/home/mysqlbackups/latest"

# TODO need to import and initialise logger
logDirectory = "/home/elly/myLogs/"
logName = "logFile.log"


def getfiles():
    filenames = []
    try:
        mylist = os.listdir(fileDirectory)
        for myfile in mylist:
            if myfile.endswith(".gz"):
                filenames.append(myfile)
    except Exception as e:
        print "Error encountered. The error is: {0}".format(e)
    return filenames


def countfiles(myarray):
    counter = 0
    for item in myarray:
        counter += 1
    return counter


# ---------------------------------------------------------------------------------------

def main():
    myarray = getfiles()
    print "My list has: " + str(countfiles(myarray)) + " elements."
    for item in myarray:
        print "My Files are: " + item


main()
