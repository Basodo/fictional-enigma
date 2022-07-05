#lamps is de output functie die num_list weer omzet in letters

from keyboard import num_list

def translate():
     secret_message = ("")
     for x in range(len(num_list)):
          secret_message = secret_message + (chr(num_list[x]+96))
     print(secret_message)
