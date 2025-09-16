import pytest
from reeks_4_functies.bovensteboven import bovensteboven, volgende

@pytest.mark.parametrize(
    "getal", [
        181,    # Voorbeelden met korte bovensteboven-getallen
        609,
        619,
        689,
        818,
        1111,
        6009,   # Grotere getallen die zichzelf blijven bij omdraaiing
        10801,
        88888,
    ]
)
def test_bovensteboven_resultaat_true(getal):
    assert bovensteboven(getal) is True

@pytest.mark.parametrize(
    "getal", [
        187,    # Bevatten niet-toegestane cijfers (zoals 2, 3, 4, 5 of 7)
        745,
        121,
        303,
        151,
        555,
        123,
        707,
        8884888
    ]
)
def test_bovensteboven_resultaat_false(getal):
    assert bovensteboven(getal) is False

@pytest.mark.parametrize(
    "n, verwacht", [
        (100, 101),   # Klein bereik: eenvoudige opvolging controleren
        (101, 111),
        (111, 181),
    ]
)
def test_volgende_kleine_getallen(n, verwacht):
    assert volgende(n) == verwacht

@pytest.mark.parametrize(
    "n, verwacht", [
        (181, 609),   # Test getallen waarbij 6 en 9 in spiegeling betrokken worden
        (609, 619),
        (619, 689),
    ]
)
def test_volgende_naar_getallen_met_6_en_9(n, verwacht):
    assert volgende(n) == verwacht

def test_volgende_springen_naar_getal_met_meer_cijfers():
    # Overschakeling naar een nieuw getal met 4 cijfers
    assert volgende(986) == 1001

@pytest.mark.parametrize(
    "n, verwacht", [
        (1001, 1111),     # Lange getallen (4 cijfers)
        (6009, 6119),
        (6889, 6969),
        (8008, 8118),
        (9886, 9966),
    ]
)
def test_volgende_getallen_met_4_cijfers(n, verwacht):
    assert volgende(n) == verwacht

@pytest.mark.parametrize(
    "n, verwacht", [
        (9966, 10001),    # Springt over naar 5- of 6-cijferige bovensteboven-getallen
        (10801, 11011),
    ]
)
def test_volgende_bij_grens_naar_meer_cijfers(n, verwacht):
    assert volgende(n) == verwacht
