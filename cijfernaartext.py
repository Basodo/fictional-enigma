
from lettersnaarcijfer import num_list

geheime_text = ("")
for x in range(len(num_list)):
     geheime_text = geheime_text + (chr(num_list[x]+96))
print(geheime_text)