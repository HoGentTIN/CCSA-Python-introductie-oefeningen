import pytest
from reeks_5_lijsten_en_tuples.hidato import eerste, opvolger, laatste, hidato

# --- tests voor eerste ---

@pytest.mark.timeout(1)
@pytest.mark.parametrize("oplossing, verwacht", [
    ([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]], (2, 3)),
    ([[8, 14, 13, 12], [15, 1, 2, 11], [5, 3, 10, 16], [4, 6, 7, 9]], (1, 1)),
    (((18, 19, 20, 4, 5), (17, 1, 3, 6, 8), (16, 13, 2, 9, 7), (14, 15, 12, 11, 10)), (1, 1))
])
def test_eerste_voorbeelden_uit_opgave(oplossing, verwacht):
    assert eerste(oplossing) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize("oplossing, verwacht", [
    ([[1, 11, 10, 8], [13, 14, 7, 9], [15, 6, 12, 2], [16, 5, 4, 3]], (0, 0)),
    ([[12, 11, 16, 9, 8], [13, 15, 10, 17, 7], [14, 2, 5, 6, 18], [1, 3, 4, 19, 20]], (3, 0))
])
def test_eerste_middelgrote_roosters(oplossing, verwacht):
    assert eerste(oplossing) == verwacht

@pytest.mark.timeout(1)
def test_eerste_groot_rooster():
    assert eerste([[44, 43, 42, 41, 39, 38],
                   [45, 33, 32, 40, 36, 37],
                   [46, 31, 34, 35, 4, 1],
                   [47, 30, 29, 5, 3, 2],
                   [11, 48, 28, 27, 6, 25],
                   [12, 10, 8, 7, 26, 24],
                   [13, 9, 17, 18, 20, 23],
                   [14, 15, 16, 19, 22, 21]]) == (2, 5)



# --- tests voor opvolger ---

@pytest.mark.timeout(1)
@pytest.mark.parametrize("oplossing, r, k, verwacht", [
    ([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]], 2, 3, (1, 3)),
    ([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]], 1, 3, (1, 2)),
])
def test_opvolger_voorbeelden_uit_opgave_met_opvolger(oplossing, r, k, verwacht):
    assert opvolger(oplossing, r, k) == verwacht

@pytest.mark.timeout(1)
def test_opvolger_voorbeeld_uit_opgave_resultaat_None_None():
    r = [[5, 4, 11, 2], [6, 10, 3, 12], [7, 8, 9, 1]]
    assert opvolger(r, 2, 3) == (None, None)

@pytest.mark.timeout(1)
def test_opvolger_middelgroot_rooster():
    rooster = [[18, 19, 20, 4, 5], [17, 1, 3, 6, 8], [16, 13, 2, 9, 7], [14, 15, 12, 11, 10]]
    assert opvolger(rooster, 1, 2) == (0, 3)

@pytest.mark.timeout(1)
def test_opvolger_groot_rooster():
    rooster = [
        [31, 32, 33, 34, 24, 22, 19, 20],
        [30, 28, 12, 25, 35, 23, 21, 18],
        [29, 62, 27, 40, 39, 36, 37, 17],
        [63, 61, 41, 59, 58, 38, 1, 16],
        [64, 42, 60, 57, 5, 2, 14, 15],
        [43, 44, 45, 56, 6, 4, 3, 13],
        [47, 46, 52, 51, 55, 7, 9, 26],
        [48, 49, 50, 53, 54, 8, 10, 11],
    ]
    assert opvolger(rooster, 4, 7) == (3, 7)


# --- tests voor laatste ---

@pytest.mark.timeout(1)
@pytest.mark.parametrize("oplossing, verwacht", [
    ([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]], (0, 3)),
    ([[8, 14, 13, 12], [15, 1, 2, 11], [5, 3, 10, 16], [4, 6, 7, 9]], (3, 2)),
    (((18, 19, 20, 4, 5), (17, 1, 3, 6, 8), (16, 13, 2, 9, 7), (14, 15, 12, 11, 10)), (0, 2))
])
def test_laatste_voorbeelden_uit_opgave(oplossing, verwacht):
    assert laatste(oplossing) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize("oplossing, verwacht", [
    ([[12, 11, 16, 9, 8],
               [13, 15, 10, 17, 7],
               [14, 2, 5, 6, 18],
               [1, 3, 4, 19, 20]], (3, 4)),
    ([[18, 19, 20, 4, 5],
               [17, 1, 3, 6, 8],
               [16, 13, 2, 9, 7],
               [14, 15, 12, 11, 10]], (0, 2))
])
def test_laatste_middelgrote_roosters(oplossing, verwacht):
    assert laatste(oplossing) == verwacht

@pytest.mark.timeout(1)
def test_laatste_groot_rooster():
    rooster = [
        [31, 32, 33, 34, 24, 22, 19, 20],
        [30, 28, 12, 25, 35, 23, 21, 18],
        [29, 62, 27, 40, 39, 36, 37, 17],
        [63, 61, 41, 59, 58, 38, 1, 16],
        [64, 42, 60, 57, 5, 2, 14, 15],
        [43, 44, 45, 56, 6, 4, 3, 13],
        [47, 46, 52, 51, 55, 7, 9, 26],
        [48, 49, 50, 53, 54, 8, 10, 11],
    ]
    assert laatste(rooster) == (7, 7)


# --- tests voor hidato ---

@pytest.mark.timeout(1)
@pytest.mark.parametrize("oplossing", [
    ([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]]),
    ((18, 19, 20, 4, 5), (17, 1, 3, 6, 8), (16, 13, 2, 9, 7), (14, 15, 12, 11, 10))
])
def test_hidato_voorbeelden_opgave_resultaat_true(oplossing):
    assert hidato(oplossing) is True

@pytest.mark.timeout(1)
def test_hidato_voorbeeld_opgave_resultaat_false():
    assert hidato([[8, 14, 13, 12], [15, 1, 2, 11], [5, 3, 10, 16], [4, 6, 7, 9]]) is False

@pytest.mark.timeout(1)
def test_hidato_ander_voorbeeld_resultaat_true():
    assert hidato([[28, 29, 24, 31, 32], [27, 25, 30, 23, 33], [26, 20, 10, 22, 34],
                   [19, 11, 21, 9, 35], [18, 12, 8, 6, 5], [17, 13, 7, 4, 3], [16, 15, 14, 2, 1]]) is True

@pytest.mark.timeout(1)
@pytest.mark.parametrize("oplossing", [
    ([[8, 14, 13, 12], [15, 1, 2, 11], [5, 3, 10, 16], [4, 6, 7, 9]]),
    ([[1, 11, 10, 8], [13, 14, 7, 9], [15, 6, 12, 2], [16, 5, 4, 3]]),
    ([[18, 17, 22, 23], [19, 21, 16, 24], [20, 14, 15, 25], [28, 6, 26, 11],
      [29, 27, 12, 10], [30, 3, 9, 8], [4, 31, 2, 7], [32, 5, 13, 1]])
])
def test_hidato_andere_voorbeelden_resultaat_false(oplossing):
    assert hidato(oplossing) is False

@pytest.mark.timeout(1)
def test_hidato_groot_rooster_resultaat_true():
    rooster = [
        [26, 27, 28, 31, 32],
        [24, 25, 30, 29, 33],
        [22, 23, 37, 34, 35],
        [21, 19, 38, 36, 16],
        [20, 39, 18, 17, 15],
        [40, 3, 8, 9, 14],
        [4, 2, 7, 13, 10],
        [5, 6, 1, 12, 11],
    ]
    assert hidato(rooster) is True  

@pytest.mark.timeout(1)
def test_hidato_groot_rooster_resultaat_false():
    rooster = [
        [31, 32, 33, 34, 24, 22, 19, 20],
        [30, 28, 12, 25, 35, 23, 21, 18],
        [29, 62, 27, 40, 39, 36, 37, 17],
        [63, 61, 41, 59, 58, 38, 1, 16],
        [64, 42, 60, 57, 5, 2, 14, 15],
        [43, 44, 45, 56, 6, 4, 3, 13],
        [47, 46, 52, 51, 55, 7, 9, 26],
        [48, 49, 50, 53, 54, 8, 10, 11],
    ]
    assert hidato(rooster) is False  