from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunTestData:
    """Набор тестовых данных для класса Bun"""
    # Позитивные тесты названий
    NAME_CASES = [
        (("black bun", 100), "black bun"),      
        (("white bun", 200.50), "white bun"),   
        (("red bun", 0), "red bun"),            
        (("", 300), ""),                        
        (("a" * 100, 999.99), "a" * 100)       
    ]
   
    PRICE_CASES = [
        (("black bun", 100), 100),              
        (("white bun", 200.50), 200.50),       
        (("red bun", 0), 0),                    
        (("special bun", 999.99), 999.99)       
    ]
 
    INVALID_CASES = [
    (None, 100),                              
    (123, 100),                                
    ("black bun", "100"),                      
    ("black bun", None)                         
    ]


class IngredientTestData:
    """Набор тестовых данных для класса Ingredient"""
    COMMON_CASES = [
        # Формат:(ingredient_type, name, price)
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),       
        (INGREDIENT_TYPE_SAUCE, "", 0),                  
        (INGREDIENT_TYPE_FILLING, "a" * 100, 999.99),    
        (INGREDIENT_TYPE_SAUCE, "sour cream", -1),       
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 999.99), 
        (INGREDIENT_TYPE_FILLING, "sausage", -5)         
    ]
    INVALID_CASES = [
        (None, "hot sauce", 100),                       
        (123, "hot sauce", 100),                        
        (INGREDIENT_TYPE_SAUCE, None, 100),             
        (INGREDIENT_TYPE_SAUCE, 123, 100),            
        (INGREDIENT_TYPE_SAUCE, "hot sauce", "100")     
    ]


class BurgerTestData:
    """Набор тестовых данных для класса Burger"""
    BURGERS_PRICE_DATA = [
        (100.10, [], 200.20),                               
        (250.55, [50.00], 551.10),                          
        (200, [500, 1500, 500, 150, 250], 3300)             
    ]
    """Набор тестовых данных для проверки обработки None в Burger"""
    NONE_PARAMETERS_CASES = [
    ("set_buns", [None], False, False),                 
    ("add_ingredient", [None], False, False),          
    ("remove_ingredient", [None], True, False),        
    ("move_ingredient", [None, 0], True, True),         
    ("move_ingredient", [0, None], True, True)         
]


class ReceiptData:
    EXP_ONLY_BUN = (
        "(==== White ====)\n"
        "(==== White ====)\n\n"
        "Price: 400"
    )
    EXP_DIFF_INGREDS = (
        "(==== White ====)\n"
        "= filling dinosaur =\n"
        "= sauce hot sauce =\n"
        "(==== White ====)\n\n"
        "Price: 700"
    )
    EXP_SAME_INGREDS = (
        "(==== White ====)\n"
        "= filling dinosaur =\n"
        "= filling dinosaur =\n"
        "= sauce hot sauce =\n"
        "(==== White ====)\n\n"
        "Price: 900"
    )
    EXP_EMPTY_NAME = (
        "(====  ====)\n"
        "=   =\n"
        "(====  ====)\n\n"
        "Price: 600"  
    )

class DatabaseData:
    DATABASE_BUNS = [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ]
    DATABASE_INGREDS = [
        (0, 'SAUCE', "hot sauce", 100),
        (1, 'SAUCE', "sour cream", 200),
        (2, 'SAUCE', "chili sauce", 300),
        (3, 'FILLING', "cutlet", 100),
        (4, 'FILLING', "dinosaur", 200),
        (5, 'FILLING', "sausage", 300)
    ]
