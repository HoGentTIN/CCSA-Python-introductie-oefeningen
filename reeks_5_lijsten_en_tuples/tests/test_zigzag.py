import pytest
from reeks_5_lijsten_en_tuples.zigzag import iszigzag, zigzag_traag, zigzag_snel

# --- Tests voor iszigzag ---

@pytest.mark.timeout(1)
def test_iszigzag_3_2_is_zigzag():
    assert iszigzag((3, 2)) is True

@pytest.mark.timeout(1)
def test_iszigzag_10_13_is_niet_zigzag():
    assert iszigzag([10, 13]) is False

@pytest.mark.timeout(1)
@pytest.mark.parametrize("reeks", [
    (10, 5, 6, 2, 20, 3, 100, 80),
    [20, 5, 10, 2, 80, 6, 100, 3],
    [9, 8, 9, 8, 9, 8],
])
def test_iszigzag_lijst_enkel_positieve_getallen_is_zigzag(reeks):
    assert iszigzag(reeks) is True

@pytest.mark.timeout(1)
@pytest.mark.parametrize("reeks", [
    [10, 5, 6, 3, 2, 20, 100, 80],
    (10, 5, 6, 2, 1),
    [1, 2, 10, 5, 49, 23, 90],
    (10, 49, 1, 5, 2, 23),
])
def test_iszigzag_lijst_enkel_positieve_getallen_niet_zigzag(reeks):
    assert iszigzag(reeks) is False

@pytest.mark.timeout(1)
@pytest.mark.parametrize("reeks", [
    (1, -50, 100, -1, 0, -200, 100, 5),
    (-20, -50, 38, -4, 62, -10, 22, 12),
    [-23, -44, -7, -17, 81, 19, 73, -25, 88, -30, 98, -42, 1, -1, 84],
])
def test_iszigzag_lijst_met_negatieve_getallen_is_zigzag(reeks):
    assert iszigzag(reeks) is True

@pytest.mark.timeout(1)
@pytest.mark.parametrize("reeks", [
    [-13, -43, -23, -39, -15, -42, 14, -35, -15, -40, -39, 12],
    (-26, 99, 30, 52, 34, 39, -4, 40, -37, 83),
    [98, 98, 98, -11, 82, 29, 72, 33, 39, 51],
    [1, 94, 68, -47, -36],
])
def test_iszigzag_lijst_met_negatieven_getallen_niet_zigzag(reeks):
    assert iszigzag(reeks) is False

@pytest.mark.timeout(1)
def test_iszigzag_lijst_allemaal_zelfde_is_zigzag():
    assert iszigzag((8, 8, 8, 8, 8, 8, 8, 8)) is True



# --- Tests voor zigzag_traag ---

@pytest.mark.timeout(1)
def test_zigzag_traag_voorbeeld_uit_opgave():
    reeks = [10, 90, 49, 2, 1, 5, 23]
    zigzag_traag(reeks)
    assert reeks == [2, 1, 10, 5, 49, 23, 90]

@pytest.mark.timeout(1)
def test_zigzag_traag_kortste_reeks():
    reeks = [100, 200]
    zigzag_traag(reeks)
    assert reeks == [200, 100]

@pytest.mark.timeout(1)
def test_zigzag_traag_middellange_reeks():
    reeks = [79, 68, 73, -27, 16, -3, 45, 62, -12, -13, 35, 49, -31]
    zigzag_traag(reeks)
    assert reeks == [-27, -31, -12, -13, 16, -3, 45, 35, 62, 49, 73, 68, 79]

@pytest.mark.timeout(1)
def test_zigzag_traag_langste_reeks():
    reeks = [-45, -9, -24, 66, 88, 32, 57, 21, -40, 55, 31, 18, 37, -50, 19, 39, -3, -45, -36, 28]
    zigzag_traag(reeks)
    assert reeks == [-45, -50, -40, -45, -24, -36, -3, -9, 19, 18, 28, 21, 32, 31, 39, 37, 57, 55, 88, 66]

@pytest.mark.timeout(1)
def test_zigzag_traag_allemaal_dezelfde_waarden():
    reeks = [5, 5, 5, 5]
    zigzag_traag(reeks)
    assert reeks == [5, 5, 5, 5]



# --- Tests voor zigzag_snel ---

@pytest.mark.timeout(1)
def test_zigzag_snel_voorbeeld_uit_opgave():
    reeks = [10, 90, 49, 2, 1, 5, 23]
    zigzag_snel(reeks)
    assert reeks == [90, 10, 49, 1, 5, 2, 23]

@pytest.mark.timeout(1)
def test_zigzag_snel_kortste_reeks():
    reeks = [100, 200]
    zigzag_snel(reeks)
    assert reeks == [200, 100]

@pytest.mark.timeout(1)
def test_zigzag_snel_middellange_reeks():
    reeks = [79, 68, 73, -27, 16, -3, 45, 62, -12, -13, 35, 49, -31]
    zigzag_snel(reeks)
    assert reeks == [79, 68, 73, -27, 16, -3, 62, -12, 45, -13, 49, -31, 35]

@pytest.mark.timeout(1)
def test_zigzag_snel_langste_reeks():
    reeks = [-45, -9, -24, 66, 88, 32, 57, 21, -40, 55, 31, 18, 37, -50, 19, 39, -3, -45, -36, 28]
    zigzag_snel(reeks)
    assert reeks == [-9, -45, 66, -24, 88, 32, 57, -40, 55, 21, 31, 18, 37, -50, 39, -3, 19, -45, 28, -36]

@pytest.mark.timeout(1)
def test_zigzag_snel_allemaal_dezelfde_waarden():
    reeks = [2, 2, 2, 2]
    zigzag_snel(reeks)
    assert reeks == [2, 2, 2, 2]