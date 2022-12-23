# import re
# import csv

# with open("phonebook_raw.csv", encoding='utf-8') as f:
#     rows = csv.reader(f, delimiter=",")
#     contacts_list = list(rows)

# # TODO 1: выполните пункты 1-3 ДЗ
# dict_info = {}
# for i in range(len(contacts_list)):
#     j = ' '.join(contacts_list[i])
#     pattern = r"(\+7|7|8)?\s*\(*(\d{3})\)*[\s|-]*(\d+)[\s|-]*(\d{2})[\s|-]*(\d{2})\s*\(*([а-яА-Я]*\.*)\s*(\d{0,4})\)*"
#     pattern_2 = r"^([а-яА-Я]*)[\s|\,]+?([а-яА-Я]*)[\s|\,]+?([а-яА-Я]*)"
#     result = re.sub(pattern, r'+7(\2)\3-\4-\5 \6\7', j)
#     result_2 = re.sub(pattern_2, r'\1 \2 \3', result)
#     p = result_2.split()
#     for h in range(len(p)):
#         if h > 1:
#             dict_info[p[0] + ' ' + p[1]] = dict_info.get(p[0] + ' ' + p[1], []) + [p[h]]
# list_cont = []   
# for key, v in dict_info.items():
#     v_2 = list(dict.fromkeys(v))
#     cont = [key] + v_2
#     j_j = " ".join(cont)
#     pattern_3 = r'(\+7?\(*\d{3}\)*[-]?\d{3}[-]*\d{2}[-]*\d{2})\s?(\D{19,}[^a-zA-Z\n]$)'
#     result_3 = re.sub(pattern_3, r'\2 \1', j_j)
#     p_2 = result_3.split()
#     list_cont.append([" ".join(p_2)])

# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding='utf-8') as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(list_cont)