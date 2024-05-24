from sets_categories_data import ALCOHOLS


def clean_ingredients(dish_name, dish_ingredients):
    my_set = set(dish_ingredients)
    return (dish_name, my_set)

def check_drinks(drink_name, drink_ingredients):
    for i in drink_ingredients:
        if i in ALCOHOLS:
            return f"{drink_name} Cocktail"
        else:
            return f"{drink_name} Mocktail"
