import pathlib
from pprint import pprint
def read_recipes(filename):
    cook_book = {}
    with open(filename, 'rt', encoding = 'utf-8') as file:
        new_dish = True
        amount = False
        ingredients = False
        for line in file:
            line = line.strip()
            line = line.strip(' ')
            if line:
                if new_dish:
                    current_dish = line
                    cook_book.update({current_dish: []})
                    new_dish = False
                    amount = True
                    continue
                if amount:
                    #cook_book[current_dish] += [{'ingredient_name': '', 'quantity': '', 'measure': ''}] * int(line)
                    amount = False
                    ingredients = True
                    continue
                if ingredients:
                    lis = line.split('|')
                    lis = [str.strip(' ') for str in lis]
                    cook_book[current_dish] += [{'ingredient_name': lis[0], 'quantity': int(lis[1]), 'measure': lis[2]}]
                    continue
            else:
                new_dish = True
                ingredients = False
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list.update({ingredient['ingredient_name']: {"measure": ingredient['measure'],
                                                                     'quantity': ingredient['quantity'] * person_count}})
        else:
            print(f"Блюдо {dish} отсутсвует в книге рецептов")
    return shop_list

cook_book = read_recipes('recipes.txt')
pprint(cook_book)

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

def file_lenghs(file):
    len = 0
    f = open(file, 'r', encoding = 'utf-8')
    for line in f:
        len += 1
    f.close()
    return len
dict_files_len = {}
for filename in pathlib.Path('files').iterdir():
    dict_files_len.update({filename.name: file_lenghs(filename)})
sorted_list_of_files_by_len = sorted(dict_files_len, key=dict_files_len.get)
with open('result.txt', 'w', encoding = 'utf-8') as f:
    for file in sorted_list_of_files_by_len:
        f.write(file + '\n')
        f.write(str(dict_files_len[file]) + '\n')
        with open(pathlib.Path('files', file), 'r', encoding = 'utf-8') as f1:
            for line in f1.readlines():
                f.write(line)
with open('result.txt', 'r', encoding = 'utf-8') as f:
    print(f"\n{f.read()}")