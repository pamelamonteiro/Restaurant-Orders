from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    manteiga = Ingredient('manteiga')
    ovo = Ingredient('ovo')
    carne = Ingredient('carne')

    # hash ingredientes iguais
    assert hash(manteiga) == hash(manteiga)
    assert hash(ovo) == hash(ovo)
    assert hash(carne) == hash(carne)
    # hash ingredientes diferentes
    assert hash(manteiga) != hash(ovo)
    assert hash(ovo) != hash(carne)
    assert hash(carne) != hash(manteiga)
    # implementação repr
    assert repr(manteiga) == "Ingredient('manteiga')"
    assert repr(ovo) == "Ingredient('ovo')"
    assert repr(carne) == "Ingredient('carne')"
    # atributo restriction
    assert manteiga.restrictions == set({Restriction.LACTOSE, Restriction.ANIMAL_DERIVED})
    assert ovo.restrictions == set({Restriction.ANIMAL_DERIVED})
    assert carne.restrictions == set({Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED})
    # operador igualdade certo
    assert manteiga.__eq__(Ingredient('manteiga')) is True
    assert ovo.__eq__(Ingredient('ovo')) is True
    assert carne.__eq__(Ingredient('carne')) is True
    # atributo name
    assert manteiga.name == 'manteiga'
    assert ovo.name == 'ovo'
    assert carne.name == 'carne'
