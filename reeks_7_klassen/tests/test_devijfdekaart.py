import pytest
from reeks_7_klassen.devijfdekaart import Kaart, vijfde_kaart

# --- Tests voor Kaart: correcte initialisatie, __str__ en __repr__ ---

def test_kaart_repr_voorbeeld_opgave():
    assert repr(Kaart('aas', 'schoppen')) == "Kaart(rang='aas', kleur='schoppen')"

def test_kaart_str_voorbeeld_opgave():
    assert str(Kaart('aas', 'schoppen')) == "schoppen aas"

def test_kaart_assertionerror_foute_kleur():
    with pytest.raises(AssertionError, match="ongeldige kaart"):
        Kaart('aas', 'pijkens')

def test_kaart_repr_6_schoppen():
    assert repr(Kaart('6', 'schoppen')) == "Kaart(rang='6', kleur='schoppen')"

def test_kaart_str_6_schoppen():
    assert str(Kaart('6', 'schoppen')) == "schoppen 6"

def test_kaart_repr_4_ruiten():
    assert repr(Kaart('4', 'ruiten')) == "Kaart(rang='4', kleur='ruiten')"

def test_kaart_str_4_ruiten():
    assert str(Kaart('4', 'ruiten')) == "ruiten 4"

def test_kaart_repr_2_klaveren():
    assert repr(Kaart('2', 'klaveren')) == "Kaart(rang='2', kleur='klaveren')"

def test_kaart_str_2_klaveren():
    assert str(Kaart('2', 'klaveren')) == "klaveren 2"

def test_kaart_repr_boer_ruiten():
    assert repr(Kaart('boer', 'ruiten')) == "Kaart(rang='boer', kleur='ruiten')"

def test_kaart_str_boer_ruiten():
    assert str(Kaart('boer', 'ruiten')) == "ruiten boer"

def test_kaart_repr_8_schoppen():
    assert repr(Kaart('8', 'schoppen')) == "Kaart(rang='8', kleur='schoppen')"

def test_kaart_str_8_schoppen():
    assert str(Kaart('8', 'schoppen')) == "schoppen 8"

def test_kaart_repr_vrouw_klaveren():
    assert repr(Kaart('vrouw', 'klaveren')) == "Kaart(rang='vrouw', kleur='klaveren')"

def test_kaart_str_vrouw_klaveren():
    assert str(Kaart('vrouw', 'klaveren')) == "klaveren vrouw"

def test_kaart_repr_3_ruiten():
    assert repr(Kaart('3', 'ruiten')) == "Kaart(rang='3', kleur='ruiten')"

def test_kaart_str_3_ruiten():
    assert str(Kaart('3', 'ruiten')) == "ruiten 3"

def test_kaart_repr_3_schoppen():
    assert repr(Kaart('3', 'schoppen')) == "Kaart(rang='3', kleur='schoppen')"

def test_kaart_str_3_schoppen():
    assert str(Kaart('3', 'schoppen')) == "schoppen 3"

# --- Tests voor vergelijkingsoperatoren Kaart ---

def test_kaart_kleiner_dan_kleinere_rang_true():
    assert Kaart('aas', 'schoppen') < Kaart('boer', 'harten')

def test_kaart_kleiner_dan_kleinere_rang_randgeval_true():
    assert Kaart('4', 'schoppen') < Kaart('5', 'harten')

def test_kaart_groter_gelijk_kleinere_rang_false():
    assert not (Kaart('aas', 'schoppen') >= Kaart('boer', 'harten'))

def test_kaart_groter_gelijk_kleinere_rang_randgeval_false():
    assert not (Kaart('4', 'schoppen') >= Kaart('5', 'harten'))

def test_kaart_gelijk_verschillende_rang_false():
    assert not (Kaart('5', 'schoppen') == Kaart('6', 'klaveren'))

def test_kaart_gelijk_verschillende_kleur_false():
    assert not (Kaart('6', 'schoppen') == Kaart('6', 'klaveren'))

def test_kaart_gelijk_true():
    assert Kaart('boer', 'klaveren') == Kaart('boer', 'klaveren')

def test_kaart_6_ruiten_groter_dan_4_klaveren_true():
    assert Kaart('6', 'ruiten') > Kaart('4', 'klaveren')

def test_kaart_boer_klaveren_groter_dan_5_klaveren_true():
    assert Kaart('boer', 'klaveren') > Kaart('5', 'klaveren')

def test_kaart_10_harten_kleiner_gelijk_aas_ruiten_false():
    assert not (Kaart('10', 'harten') <= Kaart('aas', 'ruiten'))

def test_kaart_kleiner_gelijk_met_zichzelf_true():
    assert Kaart('boer', 'klaveren') <= Kaart('boer', 'klaveren')

def test_kaart_groter_gelijk_met_zichzelf_true():
    assert Kaart('3', 'harten') >= Kaart('3', 'harten')

def test_kaart_verschillend_verschillende_kleur_true():
    assert Kaart('3', 'klaveren') != Kaart('3', 'schoppen')

def test_kaart_verschillend_zelfde_kleur_true():
    assert Kaart('3', 'klaveren') != Kaart('9', 'klaveren')

def test_kaart_verschillend_zelfde_kaart_false():
    assert not (Kaart('9', 'ruiten') != Kaart('9', 'ruiten'))

# --- Tests voor vijfde_kaart ---
# alle volgordes van de vier kaarten komen minstens 1 keer voor

def test_vijfde_kaart_voorbeeld_opgave():
    assert vijfde_kaart([Kaart('7', 'schoppen'), Kaart('vrouw', 'harten'), Kaart('8', 'klaveren'), Kaart('3', 'ruiten')]) == Kaart(rang='heer', kleur='schoppen')

def test_vijfde_kaart_tuple():
    assert vijfde_kaart((Kaart('4', 'harten'), Kaart('aas', 'schoppen'), Kaart('heer', 'klaveren'), Kaart('heer', 'harten'))) == Kaart(rang='5', kleur='harten')

def test_vijfde_kaart_lijst():
    assert vijfde_kaart([Kaart('boer', 'harten'), Kaart('6', 'ruiten'), Kaart('9', 'klaveren'), Kaart('aas', 'harten')]) == Kaart(rang='2', kleur='harten')

def test_vijfde_kaart_verschillende_rangschikkingen_vb1():
    assert vijfde_kaart((Kaart('4', 'ruiten'), Kaart('vrouw', 'schoppen'), Kaart('2', 'schoppen'), Kaart('7', 'ruiten'))) == Kaart(rang='9', kleur='ruiten')

def test_vijfde_kaart_verschillende_rangschikkingen_vb2():
    assert vijfde_kaart((Kaart('vrouw', 'schoppen'), Kaart('6', 'ruiten'), Kaart('9', 'harten'), Kaart('6', 'klaveren'))) == Kaart(rang='3', kleur='schoppen')

def test_vijfde_kaart_verschillende_rangschikkingen_vb3():
    assert vijfde_kaart((Kaart('3', 'schoppen'), Kaart('8', 'klaveren'), Kaart('9', 'harten'), Kaart('4', 'harten'))) == Kaart(rang='7', kleur='schoppen')

def test_vijfde_kaart_verschillende_rangschikkingen_vb4():
    assert vijfde_kaart(([Kaart('3', 'schoppen'), Kaart('6', 'harten'), Kaart('9', 'ruiten'), Kaart('7', 'klaveren')])) == Kaart(rang='5', kleur='schoppen')

def test_vijfde_kaart_verschillende_rangschikkingen_vb5():
    assert vijfde_kaart([Kaart('7', 'klaveren'), Kaart('8', 'harten'), Kaart('4', 'ruiten'), Kaart('vrouw', 'harten')]) == Kaart(rang='10', kleur='klaveren')

def test_vijfde_kaart_verschillende_rangschikkingen_vb6():
    assert vijfde_kaart([Kaart('5', 'ruiten'), Kaart('8', 'schoppen'), Kaart('boer', 'schoppen'), Kaart('7', 'ruiten')]) == Kaart(rang='9', kleur='ruiten')

def test_vijfde_kaart_verschillende_rangschikkingen_vb7():
    assert vijfde_kaart([Kaart('7', 'ruiten'), Kaart('vrouw', 'klaveren'), Kaart('vrouw', 'ruiten'), Kaart('heer', 'ruiten')]) == Kaart(rang='8', kleur='ruiten')

def test_vijfde_kaart_verschillende_rangschikkingen_vb8():
    assert vijfde_kaart([Kaart('7', 'harten'), Kaart('10', 'klaveren'), Kaart('7', 'ruiten'), Kaart('8', 'klaveren')]) == Kaart(rang='vrouw', kleur='harten')

def test_vijfde_kaart_verschillende_rangschikkingen_vb9():
    assert vijfde_kaart((Kaart('3', 'klaveren'), Kaart('5', 'klaveren'), Kaart('9', 'schoppen'), Kaart('4', 'schoppen'))) == Kaart(rang='7', kleur='klaveren')

def test_vijfde_kaart_verschillende_rangschikkingen_vb10():
    assert vijfde_kaart([Kaart('3', 'schoppen'), Kaart('vrouw', 'klaveren'), Kaart('aas', 'klaveren'), Kaart('7', 'ruiten')]) == Kaart(rang='8', kleur='schoppen')

def test_vijfde_kaart_verschillende_rangschikkingen_vb11():
    assert vijfde_kaart([Kaart('10', 'ruiten'), Kaart('boer', 'ruiten'), Kaart('3', 'ruiten'), Kaart('5', 'harten')]) == Kaart(rang='2', kleur='ruiten')

def test_vijfde_kaart_verschillende_rangschikkingen_vb12():
    assert vijfde_kaart([Kaart('5', 'schoppen'), Kaart('heer', 'klaveren'), Kaart('boer', 'harten'), Kaart('9', 'harten')]) == Kaart(rang='boer', kleur='schoppen')

def test_vijfde_kaart_enkel_klaveren():
    assert vijfde_kaart([Kaart('3', 'klaveren'), Kaart('6', 'klaveren'), Kaart('7', 'klaveren'), Kaart('9', 'klaveren')]) == Kaart(rang='4', kleur='klaveren')