import pytest
from reeks_4_functies.cijfertruukje import even_oneven, volgende, stappen

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "getal, verwacht", [
        (886328712442992, (10, 5)),    # groot getal met veel cijfers (voorbeeld uit de opgave)
        (10515, (1, 4)),               # Getal met 1 even en 4 oneven cijfers
        (145, (1, 2)),                 # Getal met 1 even en 2 oneven cijfers
    ]
)
def test_even_oneven_voorbeelden_uit_opgave(getal, verwacht):
    assert even_oneven(getal) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "getal, verwacht", [
        (15733825158586986342986668147679694682184078045209438, (31, 22)),   # Zeer groot getal (lange int)
        (546463143476755325179388001666783978334140665948078643, (28, 26)),
    ]
)
def test_even_oneven_grote_getallen(getal, verwacht):
    assert even_oneven(getal) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "getal, verwacht", [
        (24680, (5, 0)),   # Alle cijfers even
        (13579, (0, 5)),   # Alle cijfers oneven
        (0, (1, 0)),       # Nul is alleen even
    ]
)
def test_even_oneven_randgevallen(getal, verwacht):
    assert even_oneven(getal) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "getal, verwacht", [
        (886328712442992, 10515),   # Voorbeeld uit de opgave, drie opeenvolgende stappen
        (10515, 145),
        (145, 123),
    ]
)
def test_volgende_voorbeeld_uit_opgave(getal, verwacht):
    assert volgende(getal) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "getal, verwacht", [
        (789647685678390492092579414560016810984761704433048, 292251),
        (546463143476755325179388001666783978334140665948078643, 282654),
    ]
)
def test_volgende_grote_getallen(getal, verwacht):
    assert volgende(getal) == verwacht

@pytest.mark.timeout(1)
def test_volgende_kleine_getallen():
    assert volgende(123) == 123   # 123 blijft zichzelf

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "getal, verwacht", [
        (886328712442992, 3),
        (1217637626188463187643618416764317864, 4),
        (0, 2),
        (1, 5),
    ]
)
def test_stappen_voorbeelden_uit_opgave(getal, verwacht):
    assert stappen(getal) == verwacht

@pytest.mark.timeout(1)
def test_stappen_123_0():
    # 123 is eindpunt, dus 0 stappen
    assert stappen(123) == 0
    

@pytest.mark.timeout(1)
def test_stappen_groot_getal():
    assert stappen(10153431604305257821343758067907) == 3

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "getal, verwacht", [
        (2468, 3),    # Enkel even of oneven cijfers, om het gedrag met nullen te testen
        (1357, 4),
    ]
)
def test_stappen_alleen_even_of_oneven_getallen(getal, verwacht):
    assert stappen(getal) == verwacht