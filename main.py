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

pprint(contacts_list)
pprint(head)

fl_dict = {}
fl_list = []
for items in contacts_list:
    fl_list.append(dict({items[0], items[1]: f'surname {items[2]}, organization {items[3]}, position {items[4]}, phone {items[5]}, email {items[6]}'}}))

for i in fl_list:
    for k, v in i.items():
        if v[0] == contacts_list[0][0]:
            i['sfsdf'] = contacts_list[0][3]

pprint(fl_list)
# contacts_dict = []
# keys = contacts_list[0]
# values = contacts_list[1:]
# for num, vals in enumerate(values):
#     contacts_dict.append({})
#     for key, val in zip(keys, vals):
#         contacts_
#           dict[num].update({key: val})


# pprint(contacts_dict)


# for items in contacts_dict:
#     fls_dict = {}
# pprint(fls_dict)


# for i in contacts_dict:
#     for k, v in i.items():
#         fl_dict = {'firstname_lastname': [i['firstname'], i['lastname']], 'surname': i['surname'], 'organization': i['organization'], 'phone': i['phone'], 'position': i['position']}
# pprint(fl_dict)



# with open("phonebook.csv", "w", encoding="utf-8") as f:
#     # datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     # datawriter.writerows(result_2)
# write_csv("phonebook.csv", contacts_dict)

