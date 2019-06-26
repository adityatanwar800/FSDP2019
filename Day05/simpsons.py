
import re

phone_book_dict = {}
result_contacts = []
with open('simpsons_phone_book.txt', mode='rt') as phone_book:
    for line in phone_book:
        temp_list = line.split()
        phone_book_dict[ " ".join(temp_list[:-1]) ] = temp_list[-1].replace("\n","")
    
    for contact_name in phone_book_dict.keys():
        if re.match(r'J.*Neu', contact_name):
            result_contacts.append( contact_name )
        
print(result_contacts)