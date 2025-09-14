from unittest.mock import Mock


def create_mock_ingredient(ingredient_type, name, price):
    """Создает mock-объект ингредиента с заданными параметрами"""
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = ingredient_type
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_price.return_value = price
    return mock_ingredient


def create_mock_bun(name, price):
    """Создает mock-объект булочки с заданными параметрами"""
    mock_bun = Mock()
    mock_bun.get_name.return_value = name
    mock_bun.get_price.return_value = price
    return mock_bun


def create_burger_with_ingredients(burger, bun, ingredients):
    """Создает бургер с заданными ингредиентами"""
    burger.set_buns(bun)
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    return burger


class InvalidIngredient:
    """Невалидный класс ингредиента для тестирования обработки ошибок"""
    pass