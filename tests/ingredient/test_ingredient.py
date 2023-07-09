from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    camarao = Ingredient("camarão")
    ovo = Ingredient("ovo")
    carne = Ingredient("carne")

    assert hash(camarao) == hash("camarão")
    assert hash(ovo) == hash("ovo")
    assert hash(carne) == hash("carne")
