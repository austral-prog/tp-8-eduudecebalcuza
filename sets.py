from sets_categories_data import ALCOHOLS


def clean_ingredients(dish_name, dish_ingredients):
    my_set = set()
    for element in dish_ingredients:
        if element not in my_set:
            my_set.add(element)
    return (dish_name, my_set)

def check_drinks(drink_name, drink_ingredients):
    for ingridient in drink_ingredients:
        if ingridient in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"
