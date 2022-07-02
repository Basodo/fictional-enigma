num_list = []

def letters_naar_cijfers():

    secret_message = input("type secret message: ")

    secret_message = secret_message.lower()
    for x in secret_message:
        num_list.append(ord(x)-96)
        
    ## hier zie je de cijfer code
    #print(num_list)

