import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from helpers import create_mock_ingredient, create_mock_bun 

@pytest.fixture
def bun_fixture(request):
    """Фикстура для создания экземпляра Bun с параметрами из теста"""
    name, price = request.param
    return Bun(name, price)

@pytest.fixture
def ingredient_fixture(request):
    """Фикстура для создания экземпляра Ingredient с параметрами из теста"""
    ingredient_type, name, price = request.param
    return Ingredient(ingredient_type, name, price)

@pytest.fixture
def burger_fixture():
    """Фикстура для создания экземпляра Burger"""
    burger = Burger()
    return burger

@pytest.fixture
def burger_with_ingredient(burger_fixture, mock_ingredient_filling):
    """Фикстура бургера с одним добавленным ингредиентом"""
    burger_fixture.add_ingredient(mock_ingredient_filling)
    return burger_fixture

@pytest.fixture
def database_fixture():
    """Фикстура для создания экземпляра Database"""
    database = Database()
    return database

@pytest.fixture
def mock_bun():
    return create_mock_bun('White', 200)  

@pytest.fixture
def mock_ingredient_filling():
    return create_mock_ingredient('FILLING', 'dinosaur', 200)  

@pytest.fixture
def mock_ingredient_sauce():
    return create_mock_ingredient('SAUCE', 'hot sauce', 100) 
