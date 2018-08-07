import os, datetime, random, fnmatch


def run(**args):

    doc_path = ""
    doc_type = ".doc"
    report_name = str(random.randint(1, 100000)) + '.txt'
    report_path = os.path.join('E:\\', report_name)
    print "[*] In dirlister module."
    for parent, directories, filenames in os.walk("C:\\"):
        for filename in fnmatch.filter(filenames, "*%s" % doc_type):
            doc_path += str(os.path.join(parent, filename))

    with open(report_path, 'w') as f:
        f.write(str(datetime.datetime.now()))
        f.write(str(doc_path))

    f.close()
    return report_path, report_name
