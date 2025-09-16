import pytest
from reeks_4_functies.varkenslatijn import varkenswoord, varkenslatijn

# === Tests voor varkenswoord ===

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "woord, verwacht", [
        ('egg', 'eggway'),                      # Voorbeeld uit opgave waar woord begint met klinker
        ('AUDiEnCe', 'AUDiEnCeway'),
    ]
)
def test_varkenswoord_begin_klinker(woord, verwacht):
    assert varkenswoord(woord) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "woord, verwacht", [
        ('trash', 'ashtray'),                   # Voorbeelden uit opgave waar medeklinker(s) verplaatst worden
        ('quit', 'itquay'),
        ('whistle', 'istlewhay'),
    ]
)
def test_varkenswoord_begin_medeklinker(woord, verwacht):
    assert varkenswoord(woord) == verwacht


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "woord, verwacht", [
        ('Pig', 'Igpay'),                       # Begin hoofdletter + medeklinker, dus aangepaste hoofdletter
        ('Latin', 'Atinlay'),
        ('CurTAin', 'UrTAincay'),
    ]
)
def test_varkenswoord_begin_medeklinker_hoofdletter(woord, verwacht):
    assert varkenswoord(woord) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "woord, verwacht", [
        ('plover', 'overplay'),                 # Woorden met meerdere medeklinkers aan het begin
        ('plunder', 'underplay'),
    ]
)
def test_varkenswoord_meerdere_medeklinkers(woord, verwacht):
    assert varkenswoord(woord) == verwacht


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "woord, verwacht", [
        ('gRuMbLe', 'uMbLegRay'),               # Voorbeelden met hoofdletters midden in het woord
        ('sEVeReLy', 'EVeReLysay'),
        ('teRmiNAL', 'eRmiNALtay'),
        ('BaNaNa', 'ANaNabay'),
        ('DNa', 'AdNay'),
        ('CiViliZEd', 'IViliZEdcay'),
    ]
)
def test_varkenswoord_hoofdletters_in_midden(woord, verwacht):
    assert varkenswoord(woord) == verwacht

# === Tests voor varkenslatijn ===

@pytest.mark.timeout(1)
def test_varkenslatijn_eerste_zin_uit_opgave():
    assert varkenslatijn('And now for something completely different!') == \
           'Andway ownay orfay omethingsay ompletelycay ifferentday!'

@pytest.mark.timeout(1)
def test_varkenslatijn_tweede_zin_uit_opgave_met_interpunctie():
    assert varkenslatijn('Stwike him, centuwion, stwike him vewy wuffly') == \
           'Ikestway imhay, entuwioncay, ikestway imhay ewyvay ufflyway'

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "zin, verwacht", [
        ("Now, you listen here: he is not the Messiah, he is a very naughty boy!",
         'Ownay, ouyay istenlay erehay: ehay isway otnay ethay Essiahmay, ehay isway away eryvay aughtynay oybay!'),     # Inputzin met dubbelpunt
        ('Honk if you love Brian!', 'Onkhay ifway ouyay ovelay Ianbray!'),                                           # Kortere zin eindigend op uitroepteken
    ]
)
def test_varkenslatijn_andere_voorbeelden(zin, verwacht):
    assert varkenslatijn(zin) == verwacht


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "zin, verwacht", [
        ("No, I'm only pulling your leg, it's crucifixion really!",
         "Onay, Iway'may onlyway ullingpay ouryay eglay, itway'say ucifixioncray eallyray!"),
        ("There's something you've forgotten", "Erethay'say omethingsay ouyay'evay orgottenfay"),
    ]
)
def test_varkenslatijn_met_apostrof(zin, verwacht):
    assert varkenslatijn(zin) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "zin, verwacht", [
        ("(Come on guys, cheer up!)", "(Omecay onway uysgay, eerchay upway!)"),
        ("(I mean - what have you got to lose?)", "(Iway eanmay - atwhay avehay ouyay otgay otay oselay?)"),
    ]
)
def test_varkenslatijn_met_haakjes(zin, verwacht):
    assert varkenslatijn(zin) == verwacht