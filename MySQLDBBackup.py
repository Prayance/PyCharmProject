#!/us/bin/python
import os
import time

__author__ = 'Prayance'


# the mysql database details
DB_Host = 'localhost'
DB_User = 'root'
DB_User_Password = '1234'
DB_Name = 'EllyTest'
Backup_Path = '/home/elly/sqlBackups/'

# get current date/time to name the backup
Current_Datetime = time.strftime('%d%m%Y_%H%M%S')

FinalPath = Backup_Path + Current_Datetime

# check if backup folder already exists and create it if not
if not os.path.exists(FinalPath):
    os.makedirs(FinalPath)

# Check if you want to take single database backup or assinged multiple backups in DB_NAME.
print "checking for databases names file."
if os.path.exists(DB_Name):
    file1 = open(DB_Name)
    multi = 1
    print "Databases file found..."
    print "Starting backup of all dbs listed in file " + DB_Name
else:
    print "Databases file not found..."
    print "Starting backup of database " + DB_Name
    multi = 0

# Starting actual database backup process.
if multi:
    in_file = open(DB_Name, "r")
    flength = len(in_file.readlines())
    in_file.close()
    p = 1
    dbfile = open(DB_Name, "r")

    while p <= flength:
        db = dbfile.readline()  # reading database name from file
        db = db[:-1]  # deletes extra line
        dumpcmd = "mysqldump -u " + DB_User + " -p" + DB_User_Password + " -h " + DB_Host + " " + db + " > " + FinalPath + "/" + db + ".sql"
        os.system(dumpcmd)
        p += 1
    dbfile.close()
else:
    db = DB_Name
    dumpcmd = "mysqldump -u " + DB_User + " -p" + DB_User_Password + " " + db + " > " + FinalPath + "/" + db + ".sql"
    os.system(dumpcmd)

print "Backup script completed"
print "Your backups has been created in '" + FinalPath + "' directory"
