from keyboard import num_list

letters = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

def plugboard():
    for x in range(len(num_list)):
        if num_list[x] == letters[(ord("a")-96)]:
            num_list[x] = letters[(ord("b")-96)]
        elif num_list[x] == letters[(ord("b")-96)]:
            num_list[x] = letters[(ord("a")-96)]
        elif num_list[x] == letters[(ord("c")-96)]:
            num_list[x] = letters[(ord("d")-96)]
        elif num_list[x] == letters[(ord("d")-96)]:
            num_list[x] = letters[(ord("c")-96)]
        elif num_list[x] == letters[(ord("e")-96)]:
            num_list[x] = letters[(ord("f")-96)]

def plugtest():
    plugs = ["ae", "rt"]
    for x in range(len(plugs)):
        for i in range(len(num_list)):
            if num_list[i] == ord((plugs[x[1]])-96):
                num_list[i] = ord((plugs[x[2]])-96)
    