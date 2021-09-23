from datetime import time
def convert_time(str):
    if 'AM' in str:
        input = str.split(':')
        if len(input) ==2:
            l = input[1].replace('AM','')
            return int(int(input[0])*100 + int(l))
        else:
            return -1
    elif 'PM' in str:
        input = str.split(':')
        if len(input) ==2:
            l = input[1].replace('PM', '')
            return int(int(input[0])+12)*100 + int(l)
        else:
            return -1
    else:
        return -1


def get_time(str):
    if 'AM' in str:
        input = str.split(':')
        if len(input) == 2:
            l = input[1].replace('AM','')
            return time(int(input[0]), int(l), 00)
    elif 'PM' in str:
        input = str.split(':')
        if len(input) == 2:
            l = input[1].replace('PM', '')
            mins = int(l)
            hr = (int(input[0])+ 12)
            if hr == 24 and mins == 0:
                hr = 12
            else:
                hr = hr % 24
            return time(hr, mins, 00)
    return None