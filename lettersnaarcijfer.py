

num_list = []

letter_naar_cijfer = input("type secret message: ")

for c in letter_naar_cijfer:
    num_list.append(ord(c)-95)

print(num_list)



