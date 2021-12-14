import os

def read_file(name_file):
    cook_book = {}
    ingredient = []
    file_path = os.getcwd()
    path_to_file = os.path.join(file_path, name_file)
    with open(path_to_file, 'rt', encoding='utf-8') as recipes:
        for line in recipes:
            meals = line.strip()
            count = int(recipes.readline().strip())
            for line in range(count):
                record = recipes.readline().strip().split(' | ')
                ingredient.append({'ingredient_name': record[0], 'quantity': record[1], 'measure': record[2]})
                cook_book[meals] = ingredient    
            recipes.readline().strip()
            ingredient = []    
    return cook_book  


def get_list_by_dishes(dishes, cook_book):
    shop_list = []
    for dish in dishes:
        if dish not in cook_book:
            print(f'Рецепта {dish} нет в кулинарной книге')
            return -1    
        for i, item in enumerate(cook_book[dish]):
            if len(shop_list) == 0:
                shop_list.append(item)
            elif item not in shop_list:
                shop_list.append(item)    
            else:
                shop_list[shop_list.index(item)]['quantity'] = str(int(shop_list[shop_list.index(item)]['quantity'])+int(item['quantity']))               
    return shop_list 
    
    

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list_dishes = {}
    shop_list = get_list_by_dishes(dishes, cook_book)
    for ingredient in shop_list:    
        volume_for_persons = int(ingredient['quantity']) * person_count
        shop_list_dishes[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': str(volume_for_persons)}
    return shop_list_dishes



shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2, read_file("recipes.txt"))
# print(*shop_list.items(), sep = "\n")
print(shop_list)