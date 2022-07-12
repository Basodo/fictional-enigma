from keyboard import num_list
from keyboard import vercijfer
from keyboard import volgordestring

    
def rotor1():
        
    wires = [6,19,22,20,6,7,20,15,10,4,20,6,19,22,1,25,9,20,16,2,7,24,11,6,4,17]
    rotation = 0
    for x in range(len(num_list)):
        inputwire = rotation + num_list[x]
        if inputwire > 26:
            inputwire = inputwire-26
        num_list[x] = num_list[x] + wires[inputwire]
        if num_list[x]>26:
            num_list[x] = num_list[x] - 26
        rotation = rotation + 1

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