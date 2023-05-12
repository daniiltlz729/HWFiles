# def get_shop_list_by_dishes(dishes, person_count):
#     res = {}
#     for dish in dishes:
#         if dish in food:
#             for ingredient in food[dish]:
#                 name = ingredient['Продукт'] 
#                 count = int(ingredient['Кол-во']) * person_count
#                 if name in res:
#                     count += res[name]['quantity']
#                 res[name] = {
#                     'measure': ingredient['Единица измерения'],
#                     'quantity': count} 
#     return res     


# with open('recipes.txt', encoding="utf-8") as file:
#     food = {}
#     for line in file:
#         name_food = line.strip()
#         food_count = int(file.readline())
#         emp = []
#         for i in range(food_count):
#             f = file.readline().strip()
#             name, count, unit = f.split(' | ')
#             emp.append(
#                 {
#                     'Продукт': name,
#                     'Кол-во': count,
#                     'Единица измерения': unit
#                 }
#             )
#         food[name_food] = emp
#         file.readline()
# print(food)

# result = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
# print('КОЛИЧЕСТВО ПРОДУКТОВ ДЛЯ БЛЮД:\n', result)




import os 

def open_file(file):
    with open(f"Files/{file}", encoding='utf-8') as f:
        text = f.readlines()
        count_of_rows = len(text)
        #text = [file, "\n", str(count_of_rows), "\n"] + text + "\n"
        text.insert(0, f"{file}\n")
        text.insert(1, f"{count_of_rows}\n")
        text.extend("\n")
    return text, count_of_rows

result = {}
files = os.listdir("files/")
for filename in files:
       text, lengs = open_file(filename)
       result[lengs] = text

with open('result.txt', 'w', encoding='utf-8') as write_file:
    for key in sorted(result):
        write_file.write(''.join(result[key]))