import pytest
from reeks_6_dictionaries_en_sets.code39 import omgekeerd, code39, decode39

# --- Tests voor omgekeerd ---

@pytest.mark.timeout(1)
def test_omgekeerd_voorbeeld_uit_opgave():
    sleutel = {
        'U': 'SbSbSbSsS', 'Z': 'SsBsSbBsS', 'P': 'BbSsSsBsS', 'R': 'SsSbBsBsS',
        'H': 'SsBbBsSsS', 'W': 'SbBsSsBsS', 'D': 'SbBsSsSsB', 'K': 'BsSsSsBbS',
        '-': 'SsSbBsSsB', 'M': 'SbSsSbSbS', 'O': 'SsSbSsBsB', '7': 'SsSbSbSbS',
        '+': 'BsSsBbSsS', '1': 'SsSsBbBsS', ' ': 'SsBsBbSsS', '.': 'SsBbSsBsS',
        '/': 'SsSsBsBbS', 'V': 'SbSsBsBsS', 'X': 'SbSbSsSbS', 'C': 'SbSsBsSsB',
        'Y': 'BsSsSbBsS', 'G': 'BsBsSsSbS', '4': 'SsBbSsSsB', 'Q': 'SsBsSbSsB',
        'J': 'SsSsSsBbB', 'F': 'BsSsSbSsB', 'A': 'SsBsSsSbB', '6': 'BsSsSsSbB',
        '2': 'BsBsSbSsS', '$': 'SsSsSbBsB', '0': 'BsSbBsSsS', 'N': 'SsBsBsSbS',
        'I': 'BsSbSsSsB', '9': 'BbSsBsSsS', 'L': 'BsSbSsBsS', ',': 'SsSsBsSbB',
        '5': 'BsSsBsSbS', 'B': 'BbBsSsSsS', '%': 'SsBsSsBbS', 'S': 'BsBbSsSsS',
        '3': 'SbBsBsSsS', 'T': 'BbSsSsSsB', '*': 'SsSsBbSsB', 'E': 'SbSsSsBsB'
    }
    verwacht = {
        'SbSbSbSsS': 'U', 'SsBsSbBsS': 'Z', 'BbSsSsBsS': 'P', 'SsSbBsBsS': 'R', 
        'SsBbBsSsS': 'H', 'SbBsSsBsS': 'W', 'SbBsSsSsB': 'D', 'BsSsSsBbS': 'K', 
        'SsSbBsSsB': '-', 'SbSsSbSbS': 'M', 'SsSbSsBsB': 'O', 'SsSbSbSbS': '7', 
        'BsSsBbSsS': '+', 'SsSsBbBsS': '1', 'SsBsBbSsS': ' ', 'SsBbSsBsS': '.', 
        'SsSsBsBbS': '/', 'SbSsBsBsS': 'V', 'SbSbSsSbS': 'X', 'SbSsBsSsB': 'C', 
        'BsSsSbBsS': 'Y', 'BsBsSsSbS': 'G', 'SsBbSsSsB': '4', 'SsBsSbSsB': 'Q', 
        'SsSsSsBbB': 'J', 'BsSsSbSsB': 'F', 'SsBsSsSbB': 'A', 'BsSsSsSbB': '6', 
        'BsBsSbSsS': '2', 'SsSsSbBsB': '$', 'BsSbBsSsS': '0', 'SsBsBsSbS': 'N', 
        'BsSbSsSsB': 'I', 'BbSsBsSsS': '9', 'BsSbSsBsS': 'L', 'SsSsBsSbB': ',', 
        'BsSsBsSbS': '5', 'BbBsSsSsS': 'B', 'SsBsSsBbS': '%', 'BsBbSsSsS': 'S', 
        'SbBsBsSsS': '3', 'BbSsSsSsB': 'T', 'SsSsBbSsB': '*', 'SbSsSsBsB': 'E'
    }

    assert omgekeerd(sleutel) == verwacht

@pytest.mark.timeout(1)
def test_omgekeerd_voorbeeld_1():
    assert omgekeerd({'T': 'SsSsBsBbS', '2': 'SsBbSsSsB', '%': 'SsSbSbSbS', '8': 'BsSbSsBsS', '-': 'SbSsSsBsB',
                      'Y': 'BbSsBsSsS', 'V': 'SbBsSsSsB', 'I': 'SsBsSbBsS', ' ': 'SbBsSsBsS', 'X': 'SbSsBsSsB'}) \
        == {'SsSsBsBbS': 'T', 'SsBbSsSsB': '2', 'SsSbSbSbS': '%', 'BsSbSsBsS': '8', 'SbSsSsBsB': '-', 'BbSsBsSsS': 'Y',
            'SbBsSsSsB': 'V', 'SsBsSbBsS': 'I', 'SbBsSsBsS': ' ', 'SbSsBsSsB': 'X'}

@pytest.mark.timeout(1)
def test_omgekeerd_voorbeeld_2():
    assert omgekeerd({'D': 'SbBsSsBsS', 'U': 'BsBbSsSsS', 'M': 'SbSsBsBsS', 'C': 'BsBsSbSsS', 'Y': 'SsBsBbSsS',
                      '.': 'BsSsBbSsS', 'V': 'SbSbSbSsS', '2': 'BbBsSsSsS', 'E': 'SsBbBsSsS'}) \
        == {'SbBsSsBsS': 'D', 'BsBbSsSsS': 'U', 'SbSsBsBsS': 'M', 'BsBsSbSsS': 'C', 'SsBsBbSsS': 'Y',
            'BsSsBbSsS': '.', 'SbSbSbSsS': 'V', 'BbBsSsSsS': '2', 'SsBbBsSsS': 'E'}

@pytest.mark.timeout(1)
def test_omgekeerd_voorbeeld_3():
    assert omgekeerd({'A': 'SsSsBbSsB', '+': 'BsSsSsSbB', 'J': 'BsSsSbSsB', 'S': 'BbSsBsSsS', 'U': 'SsBsSsBbS',
                      '/': 'SsBsBbSsS', '6': 'SsBbBsSsS', 'I': 'SsBbSsBsS'}) \
        == {'SsSsBbSsB': 'A', 'BsSsSsSbB': '+', 'BsSsSbSsB': 'J', 'BbSsBsSsS': 'S', 'SsBsSsBbS': 'U',
            'SsBsBbSsS': '/', 'SsBbBsSsS': '6', 'SsBbSsBsS': 'I'}
    
@pytest.mark.timeout(1)
def test_omgekeerd_voorbeeld_4():
    assert omgekeerd({'G': 'SsSsSbBsB', '.': 'BbSsSsBsS', 'H': 'BsSsSbBsS', 'T': 'SsSsBsBbS', 'I': 'SsBsSbBsS', 
                      '$': 'SbSbSbSsS', 'E': 'BsSsBbSsS', '8': 'BsSbSsBsS', 'C': 'BsBsSbSsS', 'X': 'SbSsBsSsB', 
                      'Q': 'SsSsSsBbB'}) \
        == {'SsSsSbBsB': 'G', 'BbSsSsBsS': '.', 'BsSsSbBsS': 'H', 'SsSsBsBbS': 'T', 'SsBsSbBsS': 'I', 
            'SbSbSbSsS': '$', 'BsSsBbSsS': 'E', 'BsSbSsBsS': '8', 'BsBsSbSsS': 'C', 'SbSsBsSsB': 'X', 
            'SsSsSsBbB': 'Q'}

@pytest.mark.timeout(1)
def test_omgekeerd_randgeval_kleinste():
    assert omgekeerd({'A': 'SsSsBbSsB'}) == {'SsSsBbSsB': 'A'}


# --- Tests voor code39 ---

@pytest.mark.timeout(1)
def test_code39_kleinste_case():
    sleutel = {'A': 'SsSsBbSsB'}
    assert code39('a', sleutel) == 'SsSsBbSsB'

@pytest.mark.timeout(1)
def test_code39_spatie():
    sleutel = {' ': 'SsBsBbSsS', 'A': 'SsSsBbSsB'}
    assert code39(' a', sleutel) == 'SsBsBbSsS' + 's' + 'SsSsBbSsB'

@pytest.mark.timeout(1)
def test_code39_voorbeeld_uit_opgave():
    sleutel = {
        'U': 'SbSbSbSsS', 'Z': 'SsBsSbBsS', 'P': 'BbSsSsBsS', 'R': 'SsSbBsBsS',
        'H': 'SsBbBsSsS', 'W': 'SbBsSsBsS', 'D': 'SbBsSsSsB', 'K': 'BsSsSsBbS',
        '-': 'SsSbBsSsB', 'M': 'SbSsSbSbS', 'O': 'SsSbSsBsB', '7': 'SsSbSbSbS',
        '+': 'BsSsBbSsS', '1': 'SsSsBbBsS', ' ': 'SsBsBbSsS', '.': 'SsBbSsBsS',
        '/': 'SsSsBsBbS', 'V': 'SbSsBsBsS', 'X': 'SbSbSsSbS', 'C': 'SbSsBsSsB',
        'Y': 'BsSsSbBsS', 'G': 'BsBsSsSbS', '4': 'SsBbSsSsB', 'Q': 'SsBsSbSsB',
        'J': 'SsSsSsBbB', 'F': 'BsSsSbSsB', 'A': 'SsBsSsSbB', '6': 'BsSsSsSbB',
        '2': 'BsBsSbSsS', '$': 'SsSsSbBsB', '0': 'BsSbBsSsS', 'N': 'SsBsBsSbS',
        'I': 'BsSbSsSsB', '9': 'BbSsBsSsS', 'L': 'BsSbSsBsS', ',': 'SsSsBsSbB',
        '5': 'BsSsBsSbS', 'B': 'BbBsSsSsS', '%': 'SsBsSsBbS', 'S': 'BsBbSsSsS',
        '3': 'SbBsBsSsS', 'T': 'BbSsSsSsB', '*': 'SsSsBbSsB', 'E': 'SbSsSsBsB'
    }
    assert code39('Sulfur, so good.', sleutel) == (
        'BsBbSsSsSsSbSbSbSsSsBsSbSsBsSsBsSsSbSsBsSbSbSbSsSsSsSbBsBsSsSsSsBsSbBsSsBsBbSsSsBsBb'
        'SsSsSsSsSbSsBsBsSsBsBbSsSsBsBsSsSbSsSsSbSsBsBsSsSbSsBsBsSbBsSsSsBsSsBbSsBsS'
    )

@pytest.mark.timeout(1)
def test_code39_langer_voorbeeld_engels():
    sleutel = {
        '3': 'BsBbSsSsS', 'X': 'SbSsSbSbS', 'T': 'BsSsSbBsS', 'O': 'BbSsSsBsS', 
        'B': 'BsSsBbSsS', 'A': 'SsSsSbBsB', '2': 'SbSsBsBsS', '9': 'BsSbSsBsS', 
        '*': 'BsSbBsSsS', 'K': 'SsSbBsSsB', 'C': 'SbSbSbSsS', '.': 'BsBsSbSsS', 
        'W': 'SsBsBbSsS', '$': 'BsSsSsBbS', '-': 'SsBbBsSsS', 'J': 'SsBsBsSbS', 
        'S': 'BsSsSbSsB', 'N': 'SsSsBbBsS', 'H': 'BbBsSsSsS', '4': 'SsSsBbSsB', 
        '5': 'SbSsSsBsB', 'E': 'SsSsSsBbB', 'D': 'SbBsSsSsB', 'L': 'SbBsSsBsS', 
        'G': 'BsSsSsSbB', '/': 'SsSbBsBsS', 'F': 'BsBsSsSbS', '8': 'SsSsBsBbS', 
        '1': 'SsBbSsSsB', 'V': 'BbSsSsSsB', '+': 'SsSsBsSbB', '0': 'SsBsSbSsB', 
        '7': 'SbSbSsSbS', 'M': 'SsBsSsBbS', 'Y': 'BbSsBsSsS', '%': 'SbSsBsSsB', 
        'U': 'SbBsBsSsS', 'Q': 'SsBsSsSbB', '6': 'SsSbSbSbS', ' ': 'BsSsBsSbS', 
        'Z': 'SsSbSsBsB', 'P': 'SsBsSbBsS', 'R': 'SsBbSsBsS', 'I': 'BsSbSsSsB'
    }
    assert code39('The police caught the robbers after their radon the bank.', sleutel) == (
        "BsSsSbBsSsBbBsSsSsSsSsSsSsBbBsBsSsBsSbSsSsBsSbBsSsBbSsSsBsSsSbBsSsBsSsBsSbSsSsBsSbSbSbS"
        "sSsSsSsSsBbBsBsSsBsSbSsSbSbSbSsSsSsSsSbBsBsSbBsBsSsSsBsSsSsSbBsBbBsSsSsSsBsSsSbBsSsBsSs"
        "BsSbSsBsSsSbBsSsBbBsSsSsSsSsSsSsBbBsBsSsBsSbSsSsBbSsBsSsBbSsSsBsSsBsSsBbSsSsBsSsBbSsSsS"
        "sSsSsBbBsSsBbSsBsSsBsSsSbSsBsBsSsBsSbSsSsSsSbBsBsBsBsSsSbSsBsSsSbBsSsSsSsSsBbBsSsBbSsBs"
        "SsBsSsBsSbSsBsSsSbBsSsBbBsSsSsSsSsSsSsBbBsBsSbSsSsBsSsBbSsBsSsBsSsBsSbSsSsBbSsBsSsSsSsS"
        "bBsBsSbBsSsSsBsBbSsSsBsSsSsSsBbBsSsBsSsBsSbSsBsSsSbBsSsBbBsSsSsSsSsSsSsBbBsBsSsBsSbSsBs"
        "SsBbSsSsSsSsSbBsBsSsSsBbBsSsSsSbBsSsBsBsBsSbSsS"
    )

@pytest.mark.timeout(1)
def test_code39_nog_een_lang_voorbeeld():
    sleutel = {
        'R': 'SbBsBsSsS', 'O': 'BbSsBsSsS', '-': 'SsSsSsBbB', 'L': 'SsSsSbBsB', '/': 'SbBsSsSsB', 
        '+': 'SsSbSbSbS', 'F': 'SbSsBsBsS', '1': 'SsSsBbSsB', 'B': 'SsBsSbSsB', '5': 'SbSbSsSbS', 
        'C': 'BsBsSsSbS', 'K': 'BsSbSsBsS', 'P': 'SsSsBsSbB', 'E': 'SbSsSbSbS', '%': 'BsBsSbSsS', 
        'W': 'BsSbBsSsS', '0': 'BsSsSsBbS', '$': 'SsBsBbSsS', 'I': 'SsBsSsBbS', '2': 'BsSbSsSsB', 
        '4': 'SsBsSbBsS', ' ': 'SsBbSsSsB', 'V': 'SsSbSsBsB', 'Y': 'SsBbBsSsS', '3': 'BsBbSsSsS', 
        'Z': 'SbBsSsBsS', '*': 'SsSsBsBbS', 'G': 'SbSsSsBsB', 'X': 'SbSbSbSsS', '9': 'BsSsBbSsS', 
        'U': 'SsBsSsSbB', 'M': 'SsSbBsBsS', '.': 'BbSsSsBsS', 'J': 'SsBsBsSbS', 'Q': 'SbSsBsSsB', 
        'D': 'SsSbBsSsB', "'": 'SsBbSsBsS', 'T': 'BsSsSbBsS', 'H': 'BsSsBsSbS', 'A': 'BsSsSbSsB', 
        '7': 'BbSsSsSsB', '6': 'BbBsSsSsS', 'S': 'SsSsBbBsS', 'N': 'BsSsSsSbB'
    }
    assert code39("I can't wait until he's dead so we can barium in the krypton the hill.", sleutel) == (
        'SsBsSsBbSsSsBbSsSsBsBsBsSsSbSsBsSsSbSsBsBsSsSsSbBsSsBbSsBsSsBsSsSbBsSsSsBbSsSsBsBsSbBsSs'
        'SsBsSsSbSsBsSsBsSsBbSsBsSsSbBsSsSsBbSsSsBsSsBsSsSbBsBsSsSsSbBsBsSsSbBsSsSsBsSsBbSsSsSsSb'
        'BsBsSsBbSsSsBsBsSsBsSbSsSbSsSbSbSsSsBbSsBsSsSsSsBbBsSsSsBbSsSsBsSsSbBsSsBsSbSsSbSbSsBsSs'
        'SbSsBsSsSbBsSsBsSsBbSsSsBsSsSsBbBsSsBbSsBsSsSsSsBbSsSsBsBsSbBsSsSsSbSsSbSbSsSsBbSsSsBsBs'
        'BsSsSbSsBsSsSbSsBsBsSsSsSbBsSsBbSsSsBsSsBsSbSsBsBsSsSbSsBsSbBsBsSsSsSsBsSsBbSsSsBsSsSbBs'
        'SsSbBsBsSsSsBbSsSsBsSsBsSsBbSsBsSsSsSbBsSsBbSsSsBsBsSsSbBsSsBsSsBsSbSsSbSsSbSbSsSsBbSsSs'
        'BsBsSbSsBsSsSbBsBsSsSsSsBbBsSsSsSsSsBsSbBsBsSsSbBsSsBbSsBsSsSsBsSsSsSbBsSsBbSsSsBsBsSsSb'
        'BsSsBsSsBsSbSsSbSsSbSbSsSsBbSsSsBsBsSsBsSbSsSsBsSsBbSsSsSsSbBsBsSsSsSbBsBsBbSsSsBsS'
    )

# --- Tests voor decode39 ---

@pytest.mark.timeout(1)
def test_decode39_kleinste():
    sleutel = {'A': 'SsSsBbSsB'}
    gecodeerd = 'SsSsBbSsB'
    assert decode39(gecodeerd, sleutel) == 'A'

@pytest.mark.timeout(1)
def test_decode39_twee_letters():
    sleutel = {'A': 'SsSsBbSsB', 'B': 'BbBsSsSsS'}
    gecodeerd = 'SsSsBbSsBsBbBsSsSsS'
    assert decode39(gecodeerd, sleutel) == 'AB'

@pytest.mark.timeout(1)
def test_decode39_voorbeeld_uit_opgave():
    sleutel = {
        'U': 'SbSbSbSsS', 'Z': 'SsBsSbBsS', 'P': 'BbSsSsBsS', 'R': 'SsSbBsBsS',
        'H': 'SsBbBsSsS', 'W': 'SbBsSsBsS', 'D': 'SbBsSsSsB', 'K': 'BsSsSsBbS',
        '-': 'SsSbBsSsB', 'M': 'SbSsSbSbS', 'O': 'SsSbSsBsB', '7': 'SsSbSbSbS',
        '+': 'BsSsBbSsS', '1': 'SsSsBbBsS', ' ': 'SsBsBbSsS', '.': 'SsBbSsBsS',
        '/': 'SsSsBsBbS', 'V': 'SbSsBsBsS', 'X': 'SbSbSsSbS', 'C': 'SbSsBsSsB',
        'Y': 'BsSsSbBsS', 'G': 'BsBsSsSbS', '4': 'SsBbSsSsB', 'Q': 'SsBsSbSsB',
        'J': 'SsSsSsBbB', 'F': 'BsSsSbSsB', 'A': 'SsBsSsSbB', '6': 'BsSsSsSbB',
        '2': 'BsBsSbSsS', '$': 'SsSsSbBsB', '0': 'BsSbBsSsS', 'N': 'SsBsBsSbS',
        'I': 'BsSbSsSsB', '9': 'BbSsBsSsS', 'L': 'BsSbSsBsS', ',': 'SsSsBsSbB',
        '5': 'BsSsBsSbS', 'B': 'BbBsSsSsS', '%': 'SsBsSsBbS', 'S': 'BsBbSsSsS',
        '3': 'SbBsBsSsS', 'T': 'BbSsSsSsB', '*': 'SsSsBbSsB', 'E': 'SbSsSsBsB'
    }
    gecodeerd = (
        'BsBbSsSsSsSbSbSbSsSsBsSbSsBsSsBsSsSbSsBsSbSbSbSsSsSsSbBsBsSsSsSsBsSbBsSsBsBbSsSsBsBb'
        'SsSsSsSsSbSsBsBsSsBsBbSsSsBsBsSsSbSsSsSbSsBsBsSsSbSsBsBsSbBsSsSsBsSsBbSsBsS'
    )
    assert decode39(gecodeerd, sleutel) == 'SULFUR, SO GOOD.'

@pytest.mark.timeout(1)
def test_decode39_volledige_zin_lang():
    sleutel = {'A': 'SbSsBsBsS', 'N': 'SsBsBbSsS', 'V': 'SsBbSsSsB', '%': 'BsBsSsSbS', 
               'F': 'SsSsSsBbB', '2': 'BsSbSsSsB', 'H': 'SsBsSsBbS', 'T': 'BsSbSsBsS', 
               '7': 'SbSsBsSsB', '/': 'SbSsSsBsB', 'K': 'SbBsSsSsB', ';': 'BbSsSsSsB', 
               'L': 'BsSsBsSbS', '4': 'SsSbSbSbS', 'X': 'BsSsSsBbS', 'O': 'SbSbSsSbS', 
               '5': 'SsBbBsSsS', '3': 'SbSsSbSbS', 'J': 'BbSsSsBsS', 'Z': 'BsSsSsSbB', 
               '1': 'BsBbSsSsS', '+': 'BsSbBsSsS', 'P': 'SsBsSsSbB', 'D': 'BsSsSbSsB', 
               'S': 'SsBsSbBsS', 'E': 'SsSbBsSsB', '0': 'SsSbSsBsB', '6': 'SsSsSbBsB', 
               'I': 'BbSsBsSsS', 'M': 'BsSsSbBsS', 'G': 'SsBbSsBsS', 'B': 'BbBsSsSsS', 
               ' ': 'SsSsBbBsS', '$': 'SsSsBsSbB', '.': 'SsSsBbSsB', 'U': 'SsSbBsBsS', 
               ',': 'BsSsBbSsS', '-': 'SbSbSbSsS', 'R': 'BsBsSbSsS', '*': 'SsSsBsBbS', 
               'W': 'SbBsSsBsS', 'C': 'SbBsBsSsS', 'Y': 'SsBsSbSsB', 'Q': 'SsBsBsSbS'
            }
    gecodeerd = (
        'BbSsBsSsSsSsSsBbBsSsBbBsSsSsSsSbSbSsSbSsSsSbBsBsSsSsBbSsBsSsSsBsSsBbSsBsSbSs'
        'BsSsSsSsBbBsSsBsSbSsBsSsSbBsSsBsSsSsSbBsSsBsBsSsBsSbSsSsBbSsSsBsSsSbBsSsBsSs'
        'SsBbBsSsSbBsBsSsSsSbSbSsSbSsSbSbSsSbSsSbBsSsSsBsBbSsBsSsSsSsSbBsSsBsSsBsSbBs'
        'SsBsSsBbSsSsSsSsBbBsSsBbBsSsSsSsSsSbBsBsSsBsSbSsBsSsSsSsBbBsSsBbSsBsSsSsSsSs'
        'BbBsSsSbSsBsBsSsBsSbSsBsSsSsSbBsSsBsSsSsBbBsSsSsBsSsBbSsSbSsBsBsSsSsSsSsBbBs'
        'SsBsBbSsSsBbSsBsSsSsSsSbBsBsSsBsSsSbBsSsSsSsBbSsBsSsSsBbBsSsBsSbSsBsSsSsBsSs'
        'BbSsSsSbBsSsBsSsBsBbSsSsSsSsBbBsSsBbSsBsSsSsSsSsBbBsSsSbSsBsBsSsBsSbSsBsSsSs'
        'SbBsSsBsSsSsBbBsSsBsSbSsBsSsSsBsSsBbSsSsSbBsSsBsSsSsBbBsSsSbSbSsSbSsBsSbSsBs'
        'SsSsBsSsBbSsSsSbBsSsBsBsBsSbSsSsSsSsBbBsSsSsBsSbBsSsBbSsBsSsSsBsSsSsBbSsBbSs'
        'SsSsBsSsSsBbBsSsSsBsBbSsSsSbSbSsSbSsSbBsSsBsSsSsSsBbBsSsBsSbSsBsSsSsBsSsBbSs'
        'SsSbBsSsBsSsBsSbSsBsSsSsBbBsSsSbSsBsBsSsBsBsSbSsSsSsBbSsBsSsSbSbSsSbSsSsBsBb'
        'SsSsSsSsBbSsB'
    )
    assert decode39(gecodeerd, sleutel) == ( 'I BOUGHT TWELVE COOKIES, BUT I ATE '
    'HAFNIUM. THEN I ATE THE OTHER SIX; NOW THEY ARGON.' )

@pytest.mark.timeout(1)
def test_decode39_tweede_zin_lang():
    sleutel = {'L': 'BbSsSsSsB', 'G': 'BsSbBsSsS', ',': 'BsBsSbSsS', 'Y': 'BbBsSsSsS', 
               '2': 'SsSsBsSbB', '1': 'SsBbSsSsB', 'P': 'SsBsBsSbS', 'E': 'BsBbSsSsS', 
               '*': 'SsSbSsBsB', 'J': 'BsSsBsSbS', '0': 'SbSbSsSbS', '7': 'SsBsSsSbB', 
               'O': 'BsSbSsBsS', 'A': 'SsBsSbBsS', 'Z': 'SbSbSbSsS', 'M': 'SbBsSsSsB', 
               'R': 'SsBbBsSsS', '%': 'BsSsSbBsS', 'U': 'BsBsSsSbS', 'H': 'SbBsSsBsS', 
               ' ': 'SsBsSsBbS', 'T': 'BsSsSsBbS', 'N': 'BsSsSbSsB', '9': 'SbSsSsBsB', 
               'C': 'SsSsSsBbB', '6': 'SbSsBsSsB', 'W': 'SsSsBsBbS', 'D': 'SbSsBsBsS', 
               'F': 'SbBsBsSsS', 'X': 'BsSsBbSsS', '/': 'SsSsBbSsB', '3': 'SsSsBbBsS', 
               'V': 'SsBsSbSsB', 'B': 'SsSsSbBsB', '$': 'SsBbSsBsS', 'S': 'BsSbSsSsB', 
               '-': 'BbSsSsBsS', '5': 'BsSsSsSbB', '+': 'SbSsSbSbS', '.': 'BbSsBsSsS', 
               '4': 'SsSbBsSsB', 'Q': 'SsBsBbSsS', 'K': 'SsSbSbSbS', 'I': 'SsSbBsBsS'
            }
    gecodeerd = (
        'BsSsSsBbSsSbBsSsBsSsBsBbSsSsSsSsBsSsBbSsSsSbSbSbSsSsSbBsBsSsSbSsBsBs'
        'SsBsSsSbSsBsSsBsSbBsSsSsBsBsSbSsSsBsBsSbSsBsBbSsSsSsSsBbBsSsSsSsBsSsBbSsBsSsSsBb'
        'SsSsBbBsSsSsSsSbBsBsSsBsBbSsSsSsSbSsBsBsSsSsBsSsBbSsBsSsSsBbSsBsSbSsBsSsSsBsSsBb'
        'SsBbSsSsSsBsBsBbSsSsSsSsBsSbBsSsSsBsSbSsBsBsBbSsSsSsSsBsSsBbSsBsSsSsBbSsSbBsSsBs'
        'SsBsBbSsSsSsSsBsSsBbSsSsSsSsBbBsBsSbSsBsSsBsBsSsSbSsBsSsSbSsBsBsSsSsBbSsSsBbBsSs'
        'SsBbBsSsSsSsBsBsSbSsSsSsBsSsBbSsSsSsSbBsBsBsBsSsSbSsBsSsSsBbSsSsBsSsBbSsBsSsSsBb'
        'SsSbBsSsBsSsBsBbSsSsSsSsBsSsBbSsBsSsSsBbSsSbBsSsBsSsBsBbSsSsSsSsBsSsBbSsSbBsBsSs'
        'SsSsSsSbBsBsSsSbBsBsSsSsBsSsBbSsSsSsBsBbSsBsBbSsSsSsBsSsSbSsBsBsSsSsBbSsSsBsSsBb'
        'SsBsSsSsBbSsBsSbSsBsSsSsBsSsBbSsBsSsSsBbSsSbBsSsBsSsBsBbSsSsSsSsBsSsBbSsSsBsSbBs'
        'SsSsSbBsBsSsSsBbBsSsSsSsBsBsSbSsBsSbSsBsSsSsBbBsSsSsBsSsSsBbSsSsBsSsBbSsBsSsSsBb'
        'SsBsSbSsBsSsSsBsSsBbSsSsSsSsBbBsBsBbSsSsSsBsSbSsSsBsSsSbBsBsSsBsBsSsSbSsSbBsSsSs'
        'BsBbSsBsSsS'
        )
    assert decode39(gecodeerd, sleutel) == ('THE KIDNAPPER TRIED TO LEAVE THE COUNTRY, '
    'BUT THE THE FBI WENT TO THE AIRPORT TO CESIUM.')