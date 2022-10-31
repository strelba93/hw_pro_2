from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for items in contacts_list:
    b = items[0].split(" ")
    c = items[1].split(" ")
    if len(b) == 3:
        items[0] = b[0]
        items[1] = b[1]
        items[2] = b[2]
    if len(b) == 2:
        items[0] = b[0]
        items[1] = b[1]
    if len(c) == 2:
        items[1] = c[0]
        items[2] = c[1]

for items in contacts_list:
    for i, n in enumerate(items):
        pat_1 = re.compile('(\+?)(7|8)(\ ?)(\(?)(\d{3})(\)?)(\-?)(\ ?)(\d{3})(\-?)(\d{2})(\-?)(\d{2})')
        res_1 = re.sub(pat_1, r'+7(\5)\9-\11-\13', n)
        items[i] = res_1

for items in contacts_list:
    for i, n in enumerate(items):
        pat_2 = r'(\ )?(\,)?(\()?(доб.)(\ )?(\d*)(\))?'
        if 'доб' in n:
            res_2 = re.sub(pat_2, r'доб.\6', n)
            items[i] = res_2


head = contacts_list[0]
contacts_list.pop(0)

fl_dict = {}
for items in contacts_list:
    fl_dict[items[0], items[1]] = dict({'surname': items[2], 'organization': items[3], 'position': items[4], 'phone': items[5], 'email': items[6]})

new_list = []
new_list.append(head)
print(new_list)
for keys, values in fl_dict.items():
    for n in contacts_list:
        if values['surname'] == '' and keys[0] == n[0] and n[2] != '':
            values['surname'] = n[2]
        if values['organization'] == '' and keys[0] == n[0] and n[3] != '':
            values['organization'] = n[3]
        if values['position'] == '' and keys[0] == n[0] and n[4] != '':
            values['position'] = n[4]
        if values['phone'] == '' and keys[0] == n[0] and n[5] != '':
            values['phone'] = n[5]
        if values['email'] == '' and keys[0] == n[0] and n[6] != '':
            values['email'] = n[6]
    a = keys[0], keys[1], values['surname'], values['organization'], values['position'], values['phone'], values['email']
    new_list.append(a)

# pprint(fl_dict)
# pprint(new_list)











with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=";")
    datawriter.writerows(new_list)
