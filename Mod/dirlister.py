import os, datetime, random

def run(**args):

    report_name = str(random.randint(1,100000)) + '.txt'
    report_path = os.path.join('E:\\', report_name)
    print "[*] In dirlister module."
    data = os.listdir(".")
    with open(report_path, 'w') as f:
        f.write(str(data))
    
    f.close()
    return report_path, report_name
