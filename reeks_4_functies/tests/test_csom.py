import pytest
from reeks_4_functies.csom import csom

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
@pytest.mark.parametrize(
    "n, verwacht", [
        (0, 0),     # Enkelcijferige getallen vormen hun eigen c-som
        (5, 5),
        (8, 8),
    ]
)
def test_csom_eencijferige_getallen(n, verwacht):
    assert csom(n) == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
@pytest.mark.parametrize(
    "n, verwacht", [
        (1923, 6),          # Getallen waarbij 2 tussenstappen nodig zijn (1+9+2+3 = 15 → 1+5 = 6)
        (712719, 9),        # 7+1+2+7+1+9 = 27 → 2+7 = 9
        (840800, 2),        # eerste som = 20 → 2+0 = 2
    ]
)
def test_csom_getallen_met_twee_lagen(n, verwacht):
    assert csom(n) == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
@pytest.mark.parametrize(
    "n, verwacht", [
        (377096267, 2),     # Grote samengestelde getallen met meerdere reductiefasen
        (897593, 5),
        (826732, 1),
    ]
)
def test_csom_getallen_met_veel_cijfers(n, verwacht):
    assert csom(n) == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
@pytest.mark.parametrize(
    "n, verwacht", [
        (712719, 9),        # Interessant wiskundig geval: als som deelbaar is door 9 → uitkomst is 9
        (849222, 9),
        (284850, 9),
    ]
)
def test_csom_uitkomst_is_9(n, verwacht):
    assert csom(n) == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
@pytest.mark.parametrize(
    "n, verwacht", [
        (949654, 1),
        (734779, 1),
        (290395, 1),
    ]
)
def test_csom_uitkomst_is_1(n, verwacht):
    assert csom(n) == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
@pytest.mark.parametrize(
    "n, verwacht", [
        (926997, 6),
        (506105, 8),
        (309585, 3),
        (855583, 7),
    ]
)
def test_csom_uitkomst_niet_1_of_9(n, verwacht):
    assert csom(n) == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
@pytest.mark.parametrize(
    "n, verwacht", [
        (111111, 6),    # Getallen die veel herhaling bevatten (6x1 = 6)
        (222222, 3),    # 6x2 = 12 → 1+2 = 3
        (999999, 9),    # 6x9 = 54 → 5+4 = 9
    ]
)
def test_csom_repetitieve_cijfers(n, verwacht):
    assert csom(n) == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
@pytest.mark.parametrize(
    "n, verwacht", [
        (1, 1),         # Getallen met enkel enen en nullen
        (10, 1),        # 1+0 = 1
        (1001, 2),      # 1+0+0+1 = 2
        (1000000, 1),   # 1+0+0+0+0+0+0 = 1
    ]
)
def test_csom_enen_en_nullen(n, verwacht):
    assert csom(n) == verwacht
