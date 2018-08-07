import os, datetime, random

def run(**args):

    data = ""
    report_name = str(random.randint(1,100000)) + '.txt'
    report_path = os.path.join('E:\\', report_name)
    print "[*] In dirlister module."
    for parent, directories, filenames in os.walk("C:\\"):
        for filename in filenames:
            data += str(os.path.join(parent, filename)) + "/n"
        
        for directory in directories:
            data += str(os.path.join(parent, directory)) + "/n"
        
    with open(report_path, 'w') as f:
        f.write(str(data))
    
    f.close()
    return report_path, report_name
