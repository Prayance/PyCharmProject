#!/us/bin/python
import sys
import MySQLdb

__author__ = 'elly'

try:
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="1234",  # your password
                         db="EllyTest")  # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM person")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print row[0]
    # we can use print row to print the entire thing

    # returs the current version of the MySQL database
    cur.execute("SELECT VERSION()")

    # fetch the data
    myVersion = cur.fetchall()

    # print the database version
    print "Database version : %s " % myVersion

except MySQLdb.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)
# release the resources.
finally:

    if db:
        db.close()
