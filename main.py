from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
print(contacts_list)
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
some_list = []
some_list2 = []

for i in range(0,len(contacts_list),1):
    for j in range(0,len(contacts_list[0]),1):
        if i == 0:
            some_list.append(contacts_list[i][j])
        else:
            if j == 0:
                print(re.compile("[а-яёА-ЯЁ]+").findall(contacts_list[i][j]))
                patt = re.compile("[а-яёА-ЯЁ]+").findall(contacts_list[i][j])
                if len(patt) >= 1:
                    some_list.append(patt[0])
                else:
                    some_list.append(contacts_list[i][j])
            if j == 1:
                patt2 = re.compile("[а-яёА-ЯЁ]+").findall(contacts_list[i][j])
                if len(patt2) == 2 and len(patt) == 1:
                    some_list.append(patt2[0])
                if len(patt) == 1 and len(patt2) < 2:
                    some_list.append(contacts_list[i][j])
                if len(patt) >= 2:
                    some_list.append(patt[1])

            print(len(patt))
            if j == 2:
                if len(patt) >= 3:
                    some_list.append(patt[2])
                else:
                    if len(patt2) == 2:
                        some_list.append(patt2[1])
                    some_list.append(contacts_list[i][j])
            if j == 3:
                if i == 3:
                    some_list.append("ФСН")
                else:
                    some_list.append("СССР")
            if j == 4:
                some_list.append((contacts_list[i][j]))
            if j == 5:
                some_list.append((contacts_list[i][j]))
            if j == 6:
                some_list.append(contacts_list[i][j])
    some_list2.append(some_list)
    some_list = []

#TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w",encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
# Вместо contacts_list подставьте свой список
    datawriter.writerows(some_list2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
