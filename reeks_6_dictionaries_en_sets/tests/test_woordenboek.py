import pytest
from reeks_6_dictionaries_en_sets.woordenboek import vertaling_toevoegen, vertaling

# --- Before each test ---

@pytest.fixture(scope="function")
def woordenboek():
    # Aanmaken van een woordenboek met enkele vertalingen
    # Deze fixture wordt voor elke test uitgevoerd en geeft een woordenboek terug
    d = {}
    vertaling_toevoegen('plerzs', 'vrouw', d)
    vertaling_toevoegen('nirtu', 'bloem', d)
    vertaling_toevoegen('klinzoj', 'dorst', d)
    vertaling_toevoegen('tilza', 'hond', d)
    vertaling_toevoegen('zraidi', 'tijd', d)
    return d

# --- Tests voor vertaling_toevoegen ---

@pytest.mark.timeout(1)
def test_vertaling_toevoegen_levert_juist_woordenboek(woordenboek):
    # Verwachte dictionary na alle toevoegingen
    verwacht = {
        'plerzs': 'vrouw',
        'nirtu': 'bloem',
        'klinzoj': 'dorst',
        'tilza': 'hond',
        'zraidi': 'tijd',
    }
    assert woordenboek == verwacht # woordenboek uit de fixture

# --- Tests voor vertaling ---

@pytest.mark.timeout(1)
def test_vertaling_bestaand_woord_geeft_juiste_vertaling(woordenboek):
    assert vertaling('tilza', woordenboek) == 'hond' # woordenboek uit de fixture

@pytest.mark.timeout(1)
def test_vertaling_onbekend_woord_geeft_vraagtekens(woordenboek):
    assert vertaling('guoles', woordenboek) == '???' # woordenboek uit de fixture

# --- Uitgebreid gecombineerd testscenario met vertaling_toevoegen en vertaling ---

@pytest.mark.timeout(1)
def test_woordenboek_uitgebreid_scenario_dat_vertaling_toevoegen_en_vertaling_gebruikt():
    woordenboek = {
        'aaa':'aaa', 
        'aaba':'baaa', 
        'aabakka':'kkabaaa'
    }

    vertaling_toevoegen('zymurgyz', 'ygrumyzz', woordenboek)
    vertaling_toevoegen('zyzzyvaz', 'avyzzyzz', woordenboek)
    vertaling_toevoegen('zyzzyvasz', 'savyzzyzz', woordenboek)

    vertaling_toevoegen('eevalure', 'rulaveee', woordenboek)
    assert vertaling('eevalure', woordenboek) == 'rulaveee'

    assert vertaling('gtrivinsa', woordenboek) == '???'
    assert vertaling('gellintc', woordenboek) == '???'
    assert vertaling('elegizec', woordenboek) == '???'

    vertaling_toevoegen('carrc', 'rracc', woordenboek)
    assert vertaling('carrc', woordenboek) == 'rracc'

    vertaling_toevoegen('frownerf', 'renworff', woordenboek)
    assert vertaling('frownerf', woordenboek) == 'renworff'

    assert vertaling('senulouvg', woordenboek) == '???'

    vertaling_toevoegen('inarmedi', 'demranii', woordenboek)
    assert vertaling('inarmedi', woordenboek) == 'demranii'

    assert vertaling('oilesimmc', woordenboek) == '???'

    vertaling_toevoegen('ealoshge', 'ghsolaee', woordenboek)
    assert vertaling('ealoshge', woordenboek) == 'ghsolaee'

    vertaling_toevoegen('achesa', 'sehcaa', woordenboek)
    assert vertaling('achesa', woordenboek) == 'sehcaa'

    vertaling_toevoegen('damnabled', 'elbanmadd', woordenboek)
    assert vertaling('damnabled', woordenboek) == 'elbanmadd'

    vertaling_toevoegen('cursc', 'srucc', woordenboek)
    assert vertaling('cursc', woordenboek) == 'srucc'

    assert vertaling('sruiddg', woordenboek) == '???'

    vertaling_toevoegen('elexurfe', 'fruxelee', woordenboek)
    assert vertaling('elexurfe', woordenboek) == 'fruxelee'
    assert vertaling('inarmedi', woordenboek) == 'demranii'
    assert vertaling('aaa', woordenboek) == 'aaa'

