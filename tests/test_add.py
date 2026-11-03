import pytest
from entities.monster import Monster

def test_add():
    monster = Monster(name="Vampiro", power=50)
    result = monster.save()
    assert result is True