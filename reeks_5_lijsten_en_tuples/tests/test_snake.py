import pytest
from reeks_5_lijsten_en_tuples.snake import beweeg, teruggekeerd, laatste_levende_positie

# --- tests voor beweeg ---

@pytest.mark.parametrize("coordinaten, toets, verwacht", [
    ((-6, -6), '<', (-7, -6)),
    ((7, 3), '^', (7, 4))
])
def test_beweeg_voorbeelden_opgave(coordinaten, toets, verwacht):
    assert beweeg(coordinaten, toets) == verwacht

@pytest.mark.parametrize("coordinaten, toets, verwacht", [
    ((0, 0), '>', (1, 0)),
    ((0, 0), '^', (0, 1)),
    ((-10, -6), '>', (-9, -6)),
    ((10, -4), '>', (11, -4)),
    ((-2, 5), '^', (-2, 6)),
    ((-7, -10), '^', (-7, -9))
])
def test_beweeg_andere_inputs(coordinaten, toets, verwacht):
    assert beweeg(coordinaten, toets) == verwacht


# --- tests voor teruggekeerd ---

def test_teruggekeerd_voorbeeld_opgave_boven_onder_geeft_true():
    assert teruggekeerd(['^', 'v']) is True

def test_teruggekeerd_voorbeeld_opgave_rechts_onder_geeft_false():
    assert teruggekeerd(['>', 'v']) is False

@pytest.mark.parametrize("lijst_twee_toetsen, verwacht", [
    (['<', '<'], False),
    (['^', '^'], False),
    (['<', '^'], False),
    (['^', '>'], False),
    (['v', '<'], False)
])
def test_teruggekeerd_andere_voorbeelden_geven_false(lijst_twee_toetsen, verwacht):
    assert teruggekeerd(lijst_twee_toetsen) is verwacht

@pytest.mark.parametrize("lijst_twee_toetsen", [
    ['<', '>'],
    ['^', 'v'],
    ['>', '<'],
    ['v', '^']
])
def test_teruggekeerd_andere_voorbeelden_geven_true(lijst_twee_toetsen):
    assert teruggekeerd(lijst_twee_toetsen) is True

# --- tests voor laatste_levende_positie ---

@pytest.mark.timeout(1)
def test_laatste_levende_positie_voorbeeld_uit_opgave_met_dood():
    assert laatste_levende_positie(['>', '<', '^']) == (1, 1, 0)

@pytest.mark.timeout(1)
def test_laatste_levende_positie_voorbeeld_uit_opgave_niet_dood():
    assert laatste_levende_positie(['v', '>', 'v', '<', '^', '^']) == (6, 0, 0)

@pytest.mark.timeout(1)
def test_laatste_levende_positie_kort_voorbeeld_meteen_dood():
    assert laatste_levende_positie(['^', 'v']) == (1, 0, 1)

@pytest.mark.timeout(1)
@pytest.mark.parametrize("lijst_toetsen, verwacht", [
    (['>', 'v', '>', '<', '<', '^', 'v', '<', '>', '>', '>', '^'], (3, 2, -1)),
    (['v', '<', '^', '<', '<', '>', 'v'], (5, -3, 0)),
    (['<', '>', '^'], (1, -1, 0)), 
    (['<', '>', '^', 'v', '<', 'v', '^', '^', '>', 'v', '<', '^', 'v', '<', '>', '<', 'v', '^'], (1, -1, 0)),
    (['<', '^', '>', '>', '^', '^', 'v', '<', 'v', '>', '<', '<', 'v', '^', '^', '>', '^', '<', '>', '>'], (6, 1, 3)),
    (['v', 'v', '<', '^', '>', 'v', '<', '<', '<', 'v', '^', '>', '<'], (10, -3, -3))
])
def test_laatste_levende_positie_meerdere_stappen_wel_dood(lijst_toetsen, verwacht):
    assert laatste_levende_positie(lijst_toetsen) == verwacht

@pytest.mark.timeout(1)
def test_laatste_levende_positie_lange_reeks_niet_dood():
    assert laatste_levende_positie(['>', '^', '>', '^', '>', '>', '^', '^', '<', '<', '<', '<', '<', '<', '<', '^']) == (16, -3, 5)
