import pytest
from reeks_5_lijsten_en_tuples.achterhoede import zien, zeggen

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "personen, verwacht", [
        (('R', 'B', 'R', 'R', 'B'), ('B', 'R', 'R', 'B', 'R')),
        (['R', 'B', 'R', 'B', 'R', 'R'], ('B', 'R', 'R', 'B', 'B', 'R')),
        (['B', 'B', 'R', 'R', 'B', 'B', 'R', 'R'], ('B', 'B', 'B', 'R', 'B', 'B', 'B', 'R')),
    ]
)
def test_zien_korte_tuple_of_list(personen, verwacht):
    assert zien(personen) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "personen, verwacht", [
        ('BRRRRB', ('B', 'B', 'R', 'B', 'R', 'B')),
        ('RBBRB', ('B', 'R', 'R', 'R', 'B')),
        ('RRBBRR', ('B', 'R', 'B', 'B', 'B', 'R')),
        ('RRRRRRRRRR', ('B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R')),
    ]
)
def test_zien_korte_string(personen, verwacht):
    assert zien(personen) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "personen, verwacht", [
        (('R', 'R', 'R', 'B', 'R', 'B', 'B', 'B', 'B', 'R', 'R', 'R', 'B', 'R', 'R', 'B', 'R', 'R', 'R', 'B'), 
         ('B', 'R', 'B', 'R', 'R', 'B', 'B', 'B', 'B', 'B', 'R', 'B', 'R', 'R', 'B', 'R', 'R', 'B', 'R', 'B')),
        ('RRBRRBBBRBRBBBBB', 
         ('B', 'R', 'B', 'B', 'R', 'B', 'B', 'B', 'B', 'R', 'R', 'B', 'B', 'B', 'B', 'B')),
        (['B', 'B', 'B', 'B', 'R', 'R', 'B', 'B', 'B', 'R', 'B', 'B', 'B', 'B', 'R', 'B', 'R', 'B', 'R', 'R'],
         ('B', 'B', 'B', 'B', 'B', 'R', 'B', 'B', 'B', 'B', 'R', 'R', 'R', 'R', 'R', 'B', 'B', 'R', 'R', 'B')  
       )
    ]   
)
def test_zien_lange_invoer_tuple_list_en_string(personen, verwacht):
    assert zien(personen) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "personen, verwacht", [
        (('B', 'B', 'R', 'B', 'R', 'B'), ('B', 'R', 'R', 'R', 'R', 'B')),
        (('B', 'R', 'R', 'R', 'B'), ('R', 'B', 'B', 'R', 'B')),
        (['B', 'R', 'R', 'B', 'B', 'R'], ('R', 'B', 'R', 'B', 'R', 'R')),
        (['B', 'R', 'B', 'R', 'B', 'R', 'B'], ('R', 'R', 'R', 'R', 'R', 'R', 'B')),
    ]
)
def test_zeggen_korte_tuple_of_list(personen, verwacht):
    assert zeggen(personen) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "personen, verwacht", [
        ('BBBBBBB', ('B', 'B', 'B', 'B', 'B', 'B', 'B')),
        ('RBBBBBB', ('R', 'B', 'B', 'B', 'B', 'B', 'B')),
        ('BRRBR', ('R', 'B', 'R', 'R', 'R')),
    ]
)
def test_zeggen_korte_string(personen, verwacht):
    assert zeggen(personen) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "personen, verwacht", [
         (('B', 'R', 'B', 'B', 'R', 'B', 'B', 'R', 'R', 'B'),
             ('R', 'R', 'B', 'R', 'R', 'B', 'R', 'B', 'R', 'B')),
         (['B', 'B', 'B', 'R', 'R', 'B', 'B', 'R', 'R', 'R', 'B', 'B'],
             ('B', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'B', 'R', 'B', 'B')),
         ('BRRBRBRRRR',
             ('R', 'B', 'R', 'R', 'R', 'R', 'B', 'B', 'B', 'R'))
]
)
def test_zeggen_langere_invoer_tuple_list_en_string(personen, verwacht):
    assert zeggen(personen) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "personen, verwacht", [
        (('B', 'R', 'B', 'B', 'R', 'R', 'R', 'R', 'R', 'R', 'B', 'B', 'R', 'B', 'B', 'R', 'B', 'B', 'R', 'B'), 
         ('R', 'R', 'B', 'R', 'B', 'B', 'B', 'B', 'B', 'R', 'B', 'R', 'R', 'B', 'R', 'R', 'B', 'R', 'R', 'B')),
        (['B', 'R', 'B', 'R', 'R', 'R', 'B', 'B', 'R', 'B', 'R', 'B', 'B', 'B', 'B'], 
         ('R', 'R', 'R', 'B', 'B', 'R', 'B', 'R', 'R', 'R', 'R', 'B', 'B', 'B', 'B')),
        ('BRBRBBBBRBBRRRBRBR', 
         ('R', 'R', 'R', 'R', 'B', 'B', 'B', 'R', 'R', 'B', 'R', 'B', 'B', 'R', 'R', 'R', 'R', 'R')),
    ]
)
def test_zeggen_langste_invoer_tuple_list_en_string(personen, verwacht):
    assert zeggen(personen) == verwacht
