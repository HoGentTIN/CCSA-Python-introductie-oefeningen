import pytest
from reeks_6_dictionaries_en_sets.dubbels import dubbel, dubbels

# --- Tests voor dubbel ---

@pytest.mark.timeout(1)
def test_dubbel_opgavevoorbeeld_1():
    assert dubbel([1, 2, 3, 4, 2]) == 2

@pytest.mark.timeout(1)
def test_dubbel_opgavevoorbeeld_2():
    assert dubbel([1, 2, 3, 4]) is None

@pytest.mark.timeout(1)
def test_dubbel_opgavevoorbeeld_3():
    assert dubbel([1, 2, 3, 4, 5, 6, 100, -234, 15, 0, -20000, 15]) == 15

@pytest.mark.timeout(1)
def test_dubbel_beide_in_midden():
    assert dubbel([194, -241, -185, 31, 137, 85, 137, -242, 215, -277, -238, 273]) == 137

@pytest.mark.timeout(1)
def test_dubbel_eerste_vooraan_tweede_in_midden():
    assert dubbel([306, 189, -32, -210, 306, 127, -88, 66, -352, 132, -372, -344, -240, 329, -118, 388, -308, 219]) == 306

@pytest.mark.timeout(1)
def test_dubbel_eerste_vooraan_tweede_achteraan():
    assert dubbel([56, 189, -32, -210, 306, 127, -88, 66, -352, 132, -372, -344, -240, 329, -118, 388, -308, 219, 56]) == 56

@pytest.mark.timeout(1)
def test_dubbel_negatief_getal():
    assert dubbel([298, 174, -5, -130, 369, 63, -242, -201, 173, 391, -113, -130]) == -130

@pytest.mark.timeout(1)
def test_dubbel_kleinste_lijst_1element():
    assert dubbel([42]) is None

@pytest.mark.timeout(1)
def test_dubbel_lege_lijst():
    assert dubbel([]) is None

@pytest.mark.timeout(1)
def test_dubbel_lange_lijst_zonder_dubbels():
    assert dubbel([-63, 90, -298, 212, -10, 94, -59, -132, -194, -306, 185, 42, -365, -270, -356, 88, 169, -159, -247, -346]) is None


# --- Tests voor dubbels ---

@pytest.mark.timeout(1)
def test_dubbels_opgavevoorbeeld_1():
    assert dubbels([1, 2, 3, 4, 2]) == ({1, 3, 4}, {2})

@pytest.mark.timeout(1)
def test_dubbels_opgavevoorbeeld_2():
    assert dubbels([2, 8, 8, 6, 10, -20, -4, -2, -4]) == ({2, 6, 10, -20, -2}, {8, -4})

@pytest.mark.timeout(1)
def test_dubbels_opgavevoorbeeld_3():
    assert dubbels([1, 3, 5, 7, 2, 4, 6]) == ({1, 2, 3, 4, 5, 6, 7}, set())

@pytest.mark.timeout(1)
def test_dubbels_meer_dan_twee_keer_zelfde_getal():
    assert dubbels([-2, -2, -2, 3, 4]) == ({3, 4}, {-2})

@pytest.mark.timeout(1)
def test_dubbels_vier_dubbels():
    assert dubbels([-153, -222, 296, -153, 297, 31, -222, -63, -222, 303, 327, 312, 136, 327, 297, 8, -220, -222, 297, -99, 142, 204, -222, -276]) \
        == ({-63, -220, 296, 136, 8, 204, -276, 142, 303, 312, -99, 31}, {297, -222, 327, -153})

@pytest.mark.timeout(1)
def test_dubbels_lange_lijst_enkel_dubbels():
    assert dubbels([202, 33, 358, 25, 170, -37, 257, 389, -142, 170, -113, 257, 101, -101, 33, -101, 358, 25, -142, 202, -37, -113, 389, 101]) \
        == (set(), {257, 33, 101, 389, 358, -37, 170, 202, -113, -142, 25, -101})

@pytest.mark.timeout(1)
def test_dubbels_alles_uniek():
    assert dubbels([8, 9, 10]) == ({8, 9, 10}, set())

@pytest.mark.timeout(1)
def test_dubbels_minimaal():
    assert dubbels([42]) == ({42}, set())

@pytest.mark.timeout(1)
def test_dubbels_lege_lijst():
    assert dubbels([]) == (set(), set())
