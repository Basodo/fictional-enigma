from keyboard import num_list
from settings import plugs

def plugtest():
    for x in range(len(plugs)):
        for i in range(len(num_list)):
            if num_list[i] == ord(plugs[x][0])-96:
                num_list[i] = ord(plugs[x][1])-96
            elif num_list[i] == ord(plugs[x][1])-96:
                num_list[i] = ord(plugs[x][0])-96