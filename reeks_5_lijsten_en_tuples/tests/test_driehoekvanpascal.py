import pytest
from reeks_5_lijsten_en_tuples.driehoekvanpascal import driehoek, zeshoek, kwadraat

# === Tests voor driehoek ===

@pytest.mark.timeout(1)
def test_driehoek_0_rijen_geeft_lege_lijst():
    assert driehoek(0) == []

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, verwacht", [
        (1, [[1]]),
        (2, [[1], [1, 1]]),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
    ]
)
def test_driehoek_kleine_cases_geven_juiste_rijen(r, verwacht):
    assert driehoek(r) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r", [
        -1, 
        3.14,
        'shrubbery',
    ]
)
def test_driehoek_ongeldige_input_assertionerror(r):
    with pytest.raises(AssertionError, match='ongeldig aantal rijen'):
        driehoek(r)

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, verwacht", [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (6, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]),
        (7, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]),
    ]
)
def test_driehoek_middelgrote_cases_geven_juiste_rijen(r, verwacht):
    assert driehoek(r) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, verwacht", [
        (8, [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1]
        ]),
        (11, [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1],
            [1, 8, 28, 56, 70, 56, 28, 8, 1],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
            [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
        ]),
    ]
)
def test_driehoek_grote_cases_geven_juiste_rijen(r, verwacht):
    assert driehoek(r) == verwacht

# === Tests voor zeshoek ===

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, k, verwacht", [
        (5, 3, [3, 3, 4, 10, 10, 4]),
        (8, 4, [15, 20, 35, 70, 56, 21]),
        (4, 2, [1, 2, 3, 6, 4, 1]),
    ]
)
def test_zeshoek_kleine_cases_geven_juiste_output(r, k, verwacht):
    assert zeshoek(r, k) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, k, verwacht", [
        (11, 3, [9, 36, 120, 165, 55, 10]),
        (11, 5, [84, 126, 252, 462, 330, 120]),
        (14, 13, [12, 1, 1, 14, 91, 78]),
        (15, 9, [1716, 1287, 2002, 5005, 6435, 3432]),
    ]
)
def test_zeshoek_middelgrote_cases_geven_juiste_output(r, k, verwacht):
    assert zeshoek(r, k) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, k, verwacht", [
        (16, 7, [2002, 3003, 6435, 11440, 8008, 3003]),
        (17, 11, [5005, 3003, 4368, 12376, 19448, 11440]),
        (18, 6, [1820, 4368, 12376, 18564, 8568, 2380]),
        (19, 6, [2380, 6188, 18564, 27132, 11628, 3060]),
        (20, 2, [1, 18, 171, 190, 20, 1]),
    ]
)
def test_zeshoek_grote_cases_geven_juiste_output(r, k, verwacht):
    assert zeshoek(r, k) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, k", [
        (3, 3), 
        (1, 6), 
        (2, 1), 
        (1, 1), 
        (2, 15)
    ]
)
def test_zeshoek_ongeldige_input_assertionerror(r, k):
    with pytest.raises(AssertionError, match='ongeldige interne positie'):
        zeshoek(r, k)

# === Tests voor kwadraat ===

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, k, verwacht", [
        (4, 2, '1 x 2 x 3 x 6 x 4 x 1 = 144 = 12 x 12'),
        (5, 4, '3 x 1 x 1 x 5 x 10 x 6 = 900 = 30 x 30'),
        (7, 3, '5 x 10 x 20 x 35 x 21 x 6 = 4410000 = 2100 x 2100'),
        (9, 4, '21 x 35 x 70 x 126 x 84 x 28 = 15247310400 = 123480 x 123480'),
    ]
)
def test_kwadraat_kleine_gevallen_geven_juiste_output(r, k, verwacht):
    assert kwadraat(r, k) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, k, verwacht", [
        (10, 3, '8 x 28 x 84 x 120 x 45 x 9 = 914457600 = 30240 x 30240'),
        (10, 6, '70 x 56 x 84 x 210 x 252 x 126 = 2195612697600 = 1481760 x 1481760'),
        (12, 11, '10 x 1 x 1 x 12 x 66 x 55 = 435600 = 660 x 660'),
        (13, 6, '330 x 462 x 924 x 1716 x 1287 x 495 = 154002906018561600 = 392432040 x 392432040'),
        (15, 11, '715 x 286 x 364 x 1365 x 3003 x 2002 = 610837252834208400 = 781560780 x 781560780'),
        (15, 14, '13 x 1 x 1 x 15 x 105 x 91 = 1863225 = 1365 x 1365'),
    ]
)
def test_kwadraat_middelgrote_gevallen_geven_juiste_output(r, k, verwacht):
    assert kwadraat(r, k) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, k, verwacht", [
        (16, 5, '364 x 1001 x 3003 x 4368 x 1820 x 455 = 3957821539024953600 = 1989427440 x 1989427440'),
        (19, 16, '680 x 136 x 153 x 969 x 3876 x 3060 = 162617853341721600 = 403259040 x 403259040'),
        (20, 2, '1 x 18 x 171 x 190 x 20 x 1 = 11696400 = 3420 x 3420'),
    ]
)
def test_kwadraat_grote_gevallen_geven_juiste_output(r, k, verwacht):
    assert kwadraat(r, k) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "r, k", [
        (3, 3), 
        (1, 6), 
        (2, 1)
    ]
)
def test_kwadraat_ongeldige_input_geeft_assertionerror(r, k):
    with pytest.raises(AssertionError, match='ongeldige interne positie'):
        kwadraat(r, k)
