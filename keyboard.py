#Keyboard wordt aan het begin aangeroepen en neemt een input van letters die daarna wordt omgezet naar een lijst van cijfers

#num_list is de lijst met cijfers die door enigma wordt versleutelt
num_list = []
volgordestring = ""

def vercijfer():

    volgordestring = input("order of the rotors: ")
    secret_message = input("type secret message: ")

    secret_message = secret_message.lower()
    for x in secret_message:
        num_list.append(ord(x)-96)
        
    ## hier zie je de cijfer code
    #print(num_list)
