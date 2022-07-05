#deze functie is een test en past een caeser cipher toe op num_list

from keyboard import num_list

def caesar_cipher():
    for x in range(len(num_list)):
        if num_list[x] != -64:
            num_list[x] = num_list[x]+3
            if num_list[x] > 26:
                num_list[x]=num_list[x]-26
