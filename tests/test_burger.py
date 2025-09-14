import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import BurgerTestData, ReceiptData
from helpers import InvalidIngredient 


class TestBurger:

    def test_bun_should_be_none_by_default(self):
        """Проверка отсутствия булочки по умолчанию"""
        burger = Burger()
        assert burger.bun is None

    def test_ingredients_should_be_empty_list_by_default(self):
        """Проверка пустого списка ингредиентов по умолчанию"""
        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns_updates_bun_correctly(self, mock_bun, burger_fixture):
        """Проверка корректной установки булочки"""
        burger_fixture.set_buns(mock_bun)
        assert burger_fixture.bun == mock_bun

    def test_add_ingredient_appends_to_ingredients_list(self, mock_ingredient_filling, burger_fixture):
        """Проверка добавления ингредиента в список"""
        initial_length = len(burger_fixture.ingredients)
        burger_fixture.add_ingredient(mock_ingredient_filling)
        assert len(burger_fixture.ingredients) == initial_length + 1
        assert burger_fixture.ingredients[-1] == mock_ingredient_filling

    def test_add_ingredient_multiple_same_correctly(self, mock_ingredient_filling, burger_fixture):
        """Проверка корректного добавления нескольких одинаковых ингредиентов"""
        for _ in range(5):
            burger_fixture.add_ingredient(mock_ingredient_filling)
        assert len(burger_fixture.ingredients) == 5
        assert all(ingredient == mock_ingredient_filling for ingredient in burger_fixture.ingredients)

    def test_remove_ingredient_decreases_ingredients_count(self, burger_with_ingredient):
        """Проверка удаления ингредиента по индексу"""
        initial_length = len(burger_with_ingredient.ingredients)
        burger_with_ingredient.remove_ingredient(0)
        assert len(burger_with_ingredient.ingredients) == initial_length - 1

    def test_move_ingredient_changes_positions_correctly(self, burger_fixture, mock_ingredient_filling, mock_ingredient_sauce):
        """Проверка перемещения ингредиента"""
        burger_fixture.add_ingredient(mock_ingredient_filling)
        burger_fixture.add_ingredient(mock_ingredient_sauce)
        
        assert burger_fixture.ingredients[0] == mock_ingredient_filling
        assert burger_fixture.ingredients[1] == mock_ingredient_sauce
        
        burger_fixture.move_ingredient(0, 1)
        
        assert burger_fixture.ingredients[0] == mock_ingredient_sauce
        assert burger_fixture.ingredients[1] == mock_ingredient_filling

    @pytest.mark.parametrize('bun_price, ingredients_prices, expected_price', BurgerTestData.BURGERS_PRICE_DATA)
    def test_get_price_with_multiple_ingredients_correctly(
        self, mock_bun, burger_fixture, bun_price, ingredients_prices, expected_price):
        """Проверка расчета цены с разным количеством ингредиентов"""
        mock_bun.get_price.return_value = bun_price
        burger_fixture.set_buns(mock_bun)
        
        for price in ingredients_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger_fixture.add_ingredient(mock_ingredient)
            
        assert burger_fixture.get_price() == expected_price

    def test_get_price_with_none_bun_raises_error(self, mock_ingredient_filling, burger_fixture):
        """Проверка вызова ошибки при расчете цены без булочки"""
        burger_fixture.add_ingredient(mock_ingredient_filling)
        with pytest.raises(AttributeError):
            burger_fixture.get_price()

    def test_get_receipt_structure_with_only_bun(self, burger_fixture, mock_bun):
        """Проверка формата чека для бургера только с булочкой"""
        burger_fixture.set_buns(mock_bun)
        assert burger_fixture.get_receipt() == ReceiptData.EXP_ONLY_BUN

    def test_get_receipt_with_ingredients_of_different_type(
            self, burger_fixture, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        """Проверка формата чека с разными типами ингредиентов"""
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient_filling)
        burger_fixture.add_ingredient(mock_ingredient_sauce)
        assert burger_fixture.get_receipt() == ReceiptData.EXP_DIFF_INGREDS

    def test_get_receipt_with_multiple_ingredients_of_same_type(
        self, burger_fixture, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        """Проверка формата чека с повторяющимися ингредиентами"""
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient_filling)
        burger_fixture.add_ingredient(mock_ingredient_filling)
        burger_fixture.add_ingredient(mock_ingredient_sauce)
        assert burger_fixture.get_receipt() == ReceiptData.EXP_SAME_INGREDS
        
    def test_get_receipt_with_empty_names(self, burger_fixture):
        """Проверка формата чека с пустыми названиями"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = ""
        mock_bun.get_price.return_value = 300
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ""
        mock_ingredient.get_name.return_value = ""
        mock_ingredient.get_price.return_value = 300
        
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient)
        
        receipt = burger_fixture.get_receipt()
        expected_receipt = (
            "(====  ====)\n"
            "=   =\n"  
            "(====  ====)\n\n"
            "Price: 900"
        )
        assert receipt == expected_receipt

    def test_get_receipt_with_no_bun_raises_error(self, burger_fixture, mock_ingredient_filling):
        """Проверка вызова ошибки при генерации чека без булочки"""
        burger_fixture.add_ingredient(mock_ingredient_filling)
        with pytest.raises(AttributeError):
            burger_fixture.get_receipt()

    def test_get_receipt_with_none_ingredient_raises_error(self, burger_fixture, mock_bun):
        """Проверка вызова ошибки при None-ингредиенте в чеке"""
        burger_fixture.set_buns(mock_bun)
        burger_fixture.ingredients.append(None)
        with pytest.raises(AttributeError):
            burger_fixture.get_receipt()

    def test_get_receipt_with_invalid_ingredient_object_raises_error(self, burger_fixture, mock_bun):
        """Проверка вызова ошибки при невалидном ингредиенте"""
        invalid_ingredient = InvalidIngredient()
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(invalid_ingredient)
        
        with pytest.raises(AttributeError):
            burger_fixture.get_receipt()

    def test_get_receipt_with_long_names_contains_name(self, burger_fixture):
        """Проверка что длинное название содержится в чеке"""
        long_name = "б" * 100
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = long_name
        mock_bun.get_price.return_value = 200
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "FILLING"
        mock_ingredient.get_name.return_value = long_name
        mock_ingredient.get_price.return_value = 100
        
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient)
        
        receipt = burger_fixture.get_receipt()
        assert long_name in receipt

    def test_get_receipt_with_long_names_contains_type(self, burger_fixture):
        """Проверка что длинный тип содержится в чеке"""
        long_type = "т" * 100
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булочка"
        mock_bun.get_price.return_value = 200
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = long_type
        mock_ingredient.get_name.return_value = "Ингредиент"
        mock_ingredient.get_price.return_value = 100
        
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient)
        
        receipt = burger_fixture.get_receipt()
        assert long_type.lower() in receipt

    def test_get_receipt_with_long_names_contains_correct_price(self, burger_fixture):
        """Проверка что цена с длинными названиями рассчитывается правильно"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булочка"
        mock_bun.get_price.return_value = 200
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "FILLING"
        mock_ingredient.get_name.return_value = "Ингредиент"
        mock_ingredient.get_price.return_value = 100
        
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient)
        
        receipt = burger_fixture.get_receipt()
        assert "Price: 500" in receipt

    def test_remove_ingredient_with_none_parameters_raises_error(self, burger_fixture):
        """Проверка вызова ошибки при None параметрах в remove_ingredient"""
        with pytest.raises((TypeError, IndexError)):
            burger_fixture.remove_ingredient(0)

    def test_move_ingredient_with_none_parameters_raises_error(self, burger_fixture):
        """Проверка вызова ошибки при None параметрах в move_ingredient"""
        with pytest.raises((TypeError, IndexError)):
            burger_fixture.move_ingredient(0, 1)

    def test_set_buns_with_none_parameter(self, burger_fixture):
        """Проверка установки None булочки"""
        burger_fixture.set_buns(None)
        assert burger_fixture.bun is None

    def test_add_ingredient_with_none_parameter(self, burger_fixture):
        """Проверка добавления None ингредиента"""
        burger_fixture.add_ingredient(None)
        assert burger_fixture.ingredients[-1] is None