
with open("sample.txt",'r') as f:
    f.readline()
    for i in f:
        input = i.split()
        print(str(input[0]))
