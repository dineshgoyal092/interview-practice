import os
dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
f = open("read.txt","r")
a=0
for line in f:
    print line
    try:
        a += int(line)
    except:
        pass
f.close()
f = open("write.txt","a")
f.writelines(str(a))
f.write("\n")
f.close()
print(a)

