import pytest
from reeks_5_lijsten_en_tuples.alfabetisch import alfabetisch

@pytest.mark.timeout(1)
def test_alfabetisch_zin_met_pet():
    zin = 'een pet met een platte klep is een plattekleppet'
    verwacht = 'een een een is klep met pet platte plattekleppet'
    assert alfabetisch(zin) == verwacht

@pytest.mark.timeout(1)
def test_alfabetisch_alle_woorden_in_zin_beginnen_met_z():
    zin = 'zeven zatte zaventemse zotten zullen zeven zomerse zondagen zwemmen zonder zwembroek'
    verwacht = 'zatte zaventemse zeven zeven zomerse zondagen zonder zotten zullen zwembroek zwemmen'
    assert alfabetisch(zin) == verwacht

@pytest.mark.timeout(1)
def test_alfabetisch_zin_met_vliegen():
    zin = 'je ziet een boel vliegen vliegen maar er is geen een bij bij'
    verwacht = 'bij bij boel een een er geen is je maar vliegen vliegen ziet'
    assert alfabetisch(zin) == verwacht


@pytest.mark.timeout(1)
def test_alfabetisch_spreiding_woorden_van_a_tot_z():
    zin = 'elke zebra eet wel graag een sappige appel of vijg'
    verwacht = 'appel een eet elke graag of sappige vijg wel zebra'
    assert alfabetisch(zin) == verwacht