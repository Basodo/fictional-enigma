from secretmessage import num_list

def encrypt():
    for x in range(len(num_list)):
        if num_list[x] != -64:
            num_list[x] = num_list[x]+3
            if num_list[x] > 26:
                num_list[x]=num_list[x]-26
