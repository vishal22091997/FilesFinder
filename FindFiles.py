import os
from shutil import copy
count = 0
def find(parent, format, output_dir):
    if parent == output_dir:
        return
    global count
    try:
        files = os.listdir(parent)
    except:
        return
    for i in files:
        print i
        if os.path.isdir(parent + "\\" + i):
            find(parent + "\\" + i, format, output_dir)
        elif i.endswith(format):
            src = parent + "\\" + i
            des = output_dir + "\\" + "file" + "_" + str(count) + ".rwr"
            file = open(des, 'w')
            copy(src, des)
            file.close()
            count += 1
def main():
    global count
    parent_dir = "C:\\Users"
    format = ".rwr"
    output_dir = "C:\\Users\\1000255626\\Desktop\\Sample"
    if os.path.exists(output_dir) and os.path.exists(parent_dir):
        print os.listdir(parent_dir)
        find(parent_dir, format, output_dir)
        print "Total Files: " + str(count)
        print "Done ! ! !"
    else:
        print "Some Path Error"

main()