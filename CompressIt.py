#!/us/bin/python
import zipfile
import sys

__author__ = 'Prayance'


def mycompression():
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED

    modes = {zipfile.ZIP_DEFLATED: 'delated',
             zipfile.ZIP_STORED: 'stored',
             }

    print "creating archive"
    zf = zipfile.ZipFile("/home/elly/sqlBackups/mySecondZip.zip", mode='w')
    print 'Raw size: ', sys.getsizeof('/home/elly/sqlBackups/01102015_105631/EllyTest.sql')
    try:
        print 'adding ellytest.sql with compression mode', modes[compression]
        zf.write('/home/elly/sqlBackups/01102015_105631/EllyTest.sql', compress_type=compression)
    finally:
        print 'closing'
        zf.close()
    print '9 compressed size:', sys.getsizeof(zf)


def main():
    mycompression()


main()
'''
mypath = '/home/elly/sqlBackups/01102015_105631/'
myfile = mypath + 'EllyTest.sql'
print 'Raw size: ',sys.getsizeof(myfile)
with open(myfile, 'rb') as f_in, gzip.open(myfile + '.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)

assert isinstance(f_out, object)
print '9 compressed size:',sys.getsizeof(f_out)



def reset():
    tar = tarfile.open(".", "test.tar.gz", "w:gz")
    tar.add("/home/elly/sqlBackups/01102015_105631/EllyTest.sql")
    tar.close()


def archive_log():
    src = '/home/elly/sqlBackups/01102015_121958/EllyTest.sql'
    dst = '/home/elly/sqlBackups/EllyTest.sql.gz'
    zip = zipfile.ZipFile(dst, 'w')
    zip.write(src, os.path.basename(src), zipfile.ZIP_DEFLATED)
    zip.close()
    '''

'''
def reset():
    tar = tarfile.open('/home/elly/sqlBackups/sample.tar.gz', "w:gz")
    tar.add('/home/elly/sqlBackups/01102015_105631/EllyTest.sql', filter=reset)
    tar.close()


def myzips():
    mypath = '/home/elly/sqlBackups/01102015_121958/'
    zip = zipfile.ZipFile('EllyTest.sql', 'w')
    zip.write(mypath, os.path.basename(mypath), zipfile.ZIP_DEFLATED)
    zip.close()
    print "Job done!"



def main():
    reset()

    main()
      '''
'''
myfile = open('/home/elly/sqlBackups/01102015_105631/EllyTest.sql', 'r').read()
compressed = base64.b64encode(zlib.compress(myfile, 9))

print compressed

output = open('encodecomp.txt', 'a')
output.write(compressed)
output.close()

readFile = open('encodecomp.txt', 'r').read

decompressed = zlib.decompress(base64.b64decode(readFile))


print 'Raw size: ',sys.getsizeof(myfile)

compressed = zlib.compress(myfile, 9)
print '9 compressed size:',sys.getsizeof(compressed)

savecomp = open('compdata.txt', 'a')
savecomp.write(compressed)
savecomp.close()

decompressed = zlib.decompress(compressed)'''
