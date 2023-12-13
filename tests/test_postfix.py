from CalCoolUs.preprocess import ShuntingYard

myShunt = ShuntingYard()


def test_postfix():
    assert myShunt.getPostfix("x+2") == ["x", "2", "+"]
    assert myShunt.getPostfix("2^-x") == ["2", "x", "-1", "*", "^"]
    
