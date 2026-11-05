import pytest
from entities.monster import Monster

def test_add():
    monster = Monster(name="Vampiro", power="Sangre")
    result = monster.save()
    assert result is True
