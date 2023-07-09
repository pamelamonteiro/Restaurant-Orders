from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    lasanha = Dish('lasanha', 35.00)
    pizza = Dish('pizza', 40.00)

    # atributo name
    assert lasanha.name == 'lasanha'
    assert pizza.name == 'pizza'
    # hash ingredientes iguais
    assert hash(lasanha) == hash(lasanha)
    assert hash(pizza) == hash(pizza)
    # hash ingredientes diferentes
    assert hash(lasanha) != hash(pizza)
    assert hash(pizza) != hash(lasanha)
    # implementação repr
    assert repr(lasanha) == "Dish('lasanha', R$35.00)"
    assert repr(pizza) == "Dish('pizza', R$40.00)"
    # adicionando ingredientes
    lasanha.add_ingredient_dependency(Ingredient("queijo mussarela"), 5)
    lasanha.add_ingredient_dependency(Ingredient("presunto"), 5)
    lasanha.add_ingredient_dependency(Ingredient("massa de lasanha"), 1)
    pizza.add_ingredient_dependency(Ingredient("farinha"), 1)
    pizza.add_ingredient_dependency(Ingredient("bacon"), 3)
    pizza.add_ingredient_dependency(Ingredient("queijo parmesão"), 3)
    # atributo restriction
    assert lasanha.get_restrictions() == set({
        Restriction.ANIMAL_MEAT: 'ANIMAL_MEAT',
        Restriction.GLUTEN: 'GLUTEN',
        Restriction.ANIMAL_DERIVED: 'ANIMAL_DERIVED',
        Restriction.LACTOSE: 'LACTOSE',
    })
    assert pizza.get_restrictions() == set({
        Restriction.ANIMAL_DERIVED: 'ANIMAL_DERIVED',
        Restriction.GLUTEN: 'GLUTEN',
        Restriction.LACTOSE: 'LACTOSE',
        Restriction.ANIMAL_MEAT: 'ANIMAL_MEAT',
    })
    # atributo ingredientes
    assert lasanha.get_ingredients() == {
        Ingredient("massa de lasanha"),
        Ingredient("queijo mussarela"),
        Ingredient("presunto")
    }
    assert pizza.get_ingredients() == {
        Ingredient("farinha"),
        Ingredient("bacon"),
        Ingredient("queijo parmesão"),
    }
    # operador igualdade
    assert lasanha.__eq__(Dish('lasanha', 35.00)) is True
    assert pizza.__eq__(Dish('pizza', 40.00)) is True
    # implementando erros
    with pytest.raises(TypeError):
        Dish('burguer', '35.00')
    with pytest.raises(ValueError):
        Dish('pizza', -40.00)
