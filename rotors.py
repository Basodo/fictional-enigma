from keyboard import num_list
from keyboard import vercijfer
from settings import volgordelijst
from settings import rotations
from settings import rotornotch

    
def rotor1():
        
    wires = [[6,19,22,20,6,7,20,15,10,4,20,6,19,22,1,25,9,20,16,2,7,24,11,6,4,17], [23,8,10,7,16,19,11,7,3,18,19,23,16,12,19,6,2,15,24,3,10,20,23,3,7,14], 
    [12,23,6,15,7,23,1,8,2,22,12,21,15,4,9,5,14,8,21,23,9,5,25,22,16,10]]
    #wires2 = [23,8,10,7,16,19,11,7,3,18,19,23,16,12,19,6,2,15,24,3,10,20,23,3,7,14]
    
    for x in range(len(num_list)):
        if num_list[x] != -64:
            for i in range(len(volgordelijst)):
                inputwire = num_list[x] + rotations[i]
                if inputwire >= len(wires[i]):
                    inputwire = inputwire - len(wires[i])
                num_list[x] = num_list[x] + wires[volgordelijst[i]][inputwire]
                print(num_list[x])
                if num_list[x] > 26:
                    num_list[x] = num_list[x] - 26
            


            rotations[0] = rotations[0] + 1
            for r in range(len(volgordelijst)):
                if r > 0:
                    if rotations[(r-1)] == rotornotch[r]:
                        rotations[r] = rotations[r] + 1
                if rotations[r] >= 26:
                    rotations[r] = rotations[r] - 26
    print(rotations)


    
#rotor 1 vercijfering:
"""
26 <-> 17

9 <-> 19

1 <-> 7

21 <-> 2

13 <-> 6

16 <-> 15

25 <-> 3

18 <-> 12

20 <-> 22

24 <-> 4

11 <-> 5

23 <-> 8

14 <-> 10
"""