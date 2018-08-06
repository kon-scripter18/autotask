import os, datetime

def run(**args):

    report_name = str(datetime.datetime.now().isoformat()) + '.txt'
    report_path = os.path.join('C:', os.sep, 'Windows', os.sep, 'System32', report_name)
    print "[*] In dirlister module."
    data = os.listdir(".")
    with open(report_path, 'w') as f:
        f.write(str(data))

    return report_path, report_name
