import pytest
from reeks_4b_recursieve_functies.ggd import ggd

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "a, b, verwacht", [
        (13, 17, 1),        # ggd van twee priemgetallen is 1
        (67, 71, 1),
        (39829, 59063, 1),
    ]
)
def test_beide_getallen_priem(a, b, verwacht):
    assert ggd(a, b) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "a, b, verwacht", [
        (14359, 92237, 1),   # Eén priemgetal, ander getal niet priem → ggd is 1 (92237 is priem)
        (52369, 28470, 1),   # 52369 is priem
        (68187, 40039, 1),   # 40039 is priem
    ]
)
def test_een_getal_is_priem_ander_getal_niet(a, b, verwacht):
    assert ggd(a, b) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "a, b, verwacht", [
        (84070, 57969, 1),   # Beiden samengesteld, maar geen gem. delers → ggd is 1
        (78910, 52059, 1),
        (2013, 13528, 1),
        (18736, 96951, 1),
        (24213, 3436, 1),
        (52377, 57796, 1),
    ]
)
def test_geen_priemgetallen_maar_onderling_priem(a, b, verwacht):
    assert ggd(a, b) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "a, b, verwacht", [
        (70115, 46010, 5),   # ggd is klein (≠ 1)
        (71066, 93056, 2),
        (40994, 49214, 2),
        (71658, 56949, 3),
        (71511, 90129, 3),
    ]
)
def test_kleine_gemeenschappelijke_delers(a, b, verwacht):
    assert ggd(a, b) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "a, b, verwacht", [
        (10, 205, 5),            # ggd 4 of groter
        (35564, 80138, 34),
        (58446, 52164, 18),
        (58430, 2240, 10),
        (12640, 43068, 4),
        (83804, 38988, 4),
    ]
)
def test_grote_gemeenschappelijke_delers(a, b, verwacht):
    assert ggd(a, b) == verwacht
