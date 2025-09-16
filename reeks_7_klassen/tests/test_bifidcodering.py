import pytest
from reeks_7_klassen.bifidcodering import Bifid

# --- Fixture voor standaard Bifid-rooster ---
@pytest.fixture
# wordt uitgevoerd vóór elke test die 'standaard_bifid' als argument heeft
def standaard_bifid():
    return Bifid(9, ('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdef'
                     'ghijklmnopqrstuvwxyz .,;:?!"\'-()[]{}$=%'))

# --- Tests voor __init__ en inputvalidatie ---

def test_init_grootte_te_groot():
    with pytest.raises(AssertionError, match='er moet gelden dat 2 <= n <= 10'):
        Bifid(20, '...')

def test_init_grootte_net_te_groot():
    with pytest.raises(AssertionError, match='er moet gelden dat 2 <= n <= 10'):
        Bifid(11, '...')

def test_init_grootte_te_klein():
    with pytest.raises(AssertionError, match='er moet gelden dat 2 <= n <= 10'):
        Bifid(0, '...')

def test_init_grootte_net_te_klein():
    with pytest.raises(AssertionError, match='er moet gelden dat 2 <= n <= 10'):
        Bifid(1, '...')

def test_init_te_veel_symbolen():
    with pytest.raises(AssertionError, match='aantal symbolen komt niet overeen met grootte van het rooster'):
        Bifid(3, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def test_init_te_weinig_symbolen():
    with pytest.raises(AssertionError, match='aantal symbolen komt niet overeen met grootte van het rooster'):
        Bifid(3, 'ABC')

# --- Tests voor symbool() ---

@pytest.mark.parametrize("rij, kolom, symbool", [
    (2, 1, 'T'),  # 'T' is op positie (2, 1)
    (0, 0, 'A'),  # 'A' is op positie (0, 0)
    (8, 8, '%'),  # '%' is op positie (8, 8)
])
def test_symbool_geldige_positie_geeft_juist_symbool(standaard_bifid, rij, kolom, symbool):
    assert standaard_bifid.symbool(rij, kolom) == symbool

@pytest.mark.parametrize("rij, kolom", [
    (-2, 5),
    (-7, 8),
    (7, 10),
    (12, 3),
    (3, -1),
    (9, 9),
    (10, 0),
    (5, 11),
    (12, 12),
])
def test_symbool_foutieve_positie_werpt_assertionerror(standaard_bifid, rij, kolom):
    with pytest.raises(AssertionError, match="ongeldige positie in rooster"):
        standaard_bifid.symbool(rij, kolom)

# --- Tests voor positie() ---

@pytest.mark.parametrize("rij, kolom, symbool", [
    (2, 1, 'T'),  # 'T' is op positie (2, 1)
    (0, 0, 'A'),  # 'A' is op positie (0, 0)
    (8, 8, '%'),  # '%' is op positie (8, 8)
])
def test_positie_geldig_symbool_geeft_juiste_positie(standaard_bifid, rij, kolom, symbool):
    assert standaard_bifid.positie(symbool) == (rij, kolom)

@pytest.mark.parametrize("symbool, fout", [
    ('', "symbool moet uit 1 karakter bestaan"),
    ('FOUT', "symbool moet uit 1 karakter bestaan"),
    ('~', "onbekend symbool: '~'"),
])
def test_positie_ongeldig_symbool_werpt_assertionerror(standaard_bifid, symbool, fout):
    with pytest.raises(AssertionError, match=fout):
        standaard_bifid.positie(symbool)

# --- Tests voor codeer() en decodeer() ---

def test_codeer_korte_zin_uit_opgave(standaard_bifid):
    assert standaard_bifid.codeer('This is a dead parrot!') == 'WgwygeexfozQ(%II5D$I}O'

def test_decodeer_korte_zin_uit_opgave(standaard_bifid):
    assert standaard_bifid.decodeer('WgwygeexfozQ(%II5D$I}O') == 'This is a dead parrot!'

def test_codeer_decodeer_enkel_teken(standaard_bifid):
    assert standaard_bifid.codeer("A") == standaard_bifid.codeer("A")
    assert standaard_bifid.decodeer(standaard_bifid.codeer("A")) == "A"

@pytest.mark.parametrize("zin, gecodeerd", [
    (
        'Human thigh bones are stronger than concrete.',
        "Gnpwegfnyfgyonfyepfnnw'VE)-z)na({(Rnw%QE[n0ba"
    ),
    (
        'Your heart beats over 100,000 times a day!',
        'Xxwepweyxwp3ZUYwnygezx0=a))aJ}5%I)%%R5II1x'
    ),
    (
        "It's against the law to have a pet dog in Iceland!",
        'G"wefyyexgypewwxgwnwpEffh).(s{B)?[E)r.5($b]p%i[cE6'
    ),
    (
        'Dolphins sleep with one eye open!',
        'Foepynfyggogggof:lz{ICe iQ}e{w}wf'
    ),
])
def test_codeer_decodeer_meerdere_korte_zinnen(standaard_bifid, zin, gecodeerd):
    assert standaard_bifid.codeer(zin) == gecodeerd
    assert standaard_bifid.decodeer(gecodeerd) == zin

@pytest.mark.parametrize("zin, gecodeerd", [
    (
        'The word "queue" is the only word in the English language that is still pronounced the same way when the last four letters are removed.',
        'Wgxnzpghwywgopyogfyesnnwxfgegwgwyyfpoopneyeyfgwywfyexgyfxxgwpwnxfpe,?{r9zWW ()?}c f]%iQieu(-SgSw).R((RU$}fWW9QiA5{G{?iQiSB}l%WKiIIi{651',
    ),
    (
        'Beetles taste like apples, wasps like pine nuts, and worms like fried bacon.',
        "EgnywygnnwonzygpxfgnnxyzwnyopxfgfegefqNbWIJBi0N(yWB{As[)i e{TB(d{r1[)ir{9JXa",
    ),
    (
        "Of all the words in the English language, the word 'set' has the most definitions!",
        'NwoyeyogwpwgFfggnnwe"wgxnzwzwgyexpyeenwozo(U)?{r1%iQieu(-SgSwRQif]=EQ=A)?]jR5riRnF',
    ),
    (
        'What is called a "French kiss" in the English speaking world is known as an "English kiss" in France.',
        'WgwyeoewzFfexgzwpwgFfggxennyonwyoppgwp.nnwxgzwpFfe?.R([CW9Ix{c-RA {)?{g0H(wB{ f[9()fe(IE$eu(-RA {}(ca'
    ),
    (
        '"Almost" is the longest word in the English language with all the letters in alphabetical order.',
        '.opzwywgongyxnwpwgFfggnnweyggfpwgnyfyfwoeewepoeqsVjP%IQiXgaRf]%iQieu(-SgSw{)-C0QiWKiI{(Y.NRS0r5('
    ),
])
def test_codeer_decodeer_meerdere_lange_zinnen(standaard_bifid, zin, gecodeerd):
    assert standaard_bifid.codeer(zin) == gecodeerd
    assert standaard_bifid.decodeer(gecodeerd) == zin