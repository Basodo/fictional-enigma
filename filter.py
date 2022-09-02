#zorgt dat alleen letters worden ingevult

from keyboard import num_list
from settings import volgordelijst

def filter():
    detected = False
    for x in range(len(num_list)):
        if detected == False:
            if (num_list[x] <= 0 and num_list[x] != -64)or num_list[x] > 26:
                print("the message contains characters that can't be encrypted")
                detected = True
        else:
            quit()
