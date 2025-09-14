import pytest
from data import DatabaseData


class TestDatabase:

    @pytest.mark.parametrize('index, name, price', DatabaseData.DATABASE_BUNS)
    def test_buns_values_true(self, database_fixture, index, name, price):
        """Проверка данных булочек в базе"""
        buns = database_fixture.available_buns()
        assert buns[index].name == name
        assert buns[index].price == price

    @pytest.mark.parametrize('index, type, name, price', DatabaseData.DATABASE_INGREDS)
    def test_ingredients_values_true(self, database_fixture, index, type, name, price):
        """Проверка данных ингредиентов в базе"""
        ingredient = database_fixture.available_ingredients()
        assert ingredient[index].type == type
        assert ingredient[index].name == name
        assert ingredient[index].price == price

    def test_available_buns_returns_list_type(self, database_fixture):
        """Проверка что available_buns возвращает список"""
        buns = database_fixture.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_returns_non_empty_list(self, database_fixture):
        """Проверка что available_buns возвращает непустой список"""
        buns = database_fixture.available_buns()
        assert len(buns) > 0

    def test_available_ingredients_returns_list_type(self, database_fixture):
        """Проверка что available_ingredients возвращает список"""
        ingredients = database_fixture.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_returns_non_empty_list(self, database_fixture):
        """Проверка что available_ingredients возвращает непустой список"""
        ingredients = database_fixture.available_ingredients()
        assert len(ingredients) > 0