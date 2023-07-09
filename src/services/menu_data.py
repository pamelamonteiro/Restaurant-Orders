import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        menu = dict()
        with open(source_path) as file:
            data = csv.DictReader(file)
            for row in data:
                name = row['dish']
                # price = float(row['price'])
                # ingredient = Ingredient(row['ingredient'])
                # amount = int(row['recipe_amount'])
                if name not in menu.keys():
                    menu[name] = Dish(
                        name,
                        float(row['price'])
                    )
                menu[name].add_ingredient_dependency(
                    Ingredient(row['ingredient']),
                    int(row['recipe_amount'])
                )
            #     dishes = dishes.get(name)
            #     if not dishes:
            #         dish = Dish(name, price)
            #         dishes[name] = dish
            #         self.dishes.add(dish)
            # dishes[name].add_ingredient_dependency(ingredient, amount)
        self.dishes = set(menu.values())
                
# https://www.w3schools.com/python/ref_func_dict.asp
# https://docs.python.org/3/library/csv.html#csv.DictReader
# https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
# https://opensource.com/article/23/1/fix-indexerror-python#:~:text=The%20only%20solution%20to%20fix,()%20an%20len()%20functions.
