import csv
import re

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
sub = r'+7(\2)-\3-\4-\5 \6\7'

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)


def contact_name(contact_list: list):
    new_contact_list = list()
    for item in contact_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  re.sub(pattern, sub, item[5]),
                  item[6]]
        new_contact_list.append(result)
    return name(new_contact_list)


def name(contacts: list):
    for c in contacts:
        first_name = c[0]
        last_name = c[1]
        for n_c in contacts:
            n_first_name = n_c[0]
            n_last_name = n_c[1]
            if first_name == n_first_name and last_name == n_last_name:
                if c[2] == '':
                    c[2] = n_c[2]
                if c[3] == '':
                    c[3] = n_c[3]
                if c[4] == '':
                    c[4] = n_c[4]
                if c[5] == '':
                    c[5] = n_c[5]
                if c[6] == '':
                    c[6] = n_c[6]

    result_list = list()
    for i in contacts:
        if i not in result_list:
            result_list.append(i)

    return result_list


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contact_name(contacts_list))
