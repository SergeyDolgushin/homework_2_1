import os

def read_file(name_file):
    all_recipes = {}
    ingredient = []
    file_path = os.getcwd()
    path_to_file = os.path.join(file_path, name_file)
    # print(f'путь {path_to_file}')
    with open(path_to_file, 'rt', encoding='utf-8') as recipes:
        for line in recipes:
            meals = line.strip()
            # print("Название", meals)
            count = int(recipes.readline().strip())
            # print(count)
            for line in range(count):
                record = recipes.readline().strip().split(' | ')
                ingredient.append({'ingredient_name': record[0], 'quantity': record[1], 'measure': record[2]})
                all_recipes[meals] = ingredient    
                # print("Ингредиент:", ingredient)
            recipes.readline().strip()
            ingredient = []    
    return all_recipes  

print()
print(read_file('recipes.txt'))