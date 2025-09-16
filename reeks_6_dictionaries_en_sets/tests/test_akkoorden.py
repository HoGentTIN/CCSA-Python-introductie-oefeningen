import pytest
from reeks_6_dictionaries_en_sets.akkoorden import ontleding, noten, akkoord

# --- Tests voor ontleding ---

@pytest.mark.timeout(1)
def test_ontleding_opgavevoorbeeld_1():
    assert ontleding('F') == ('F', '')

@pytest.mark.timeout(1)
def test_ontleding_opgavevoorbeeld_2():
    assert ontleding('Gm7') == ('G', 'm7')

@pytest.mark.timeout(1)
def test_ontleding_opgavevoorbeeld_3():
    assert ontleding('D#M7') == ('D#', 'M7')

@pytest.mark.timeout(1)
def test_ontleding_grondnoot_kruis_overmatig():
    assert ontleding('F#+') == ('F#', '+')

@pytest.mark.timeout(1)
def test_ontleding_grondnoot_overmatig():
    assert ontleding('A+') == ('A', '+')

@pytest.mark.timeout(1)
def test_ontleding_grondnoot_M7():
    assert ontleding('AM7') == ('A', 'M7')

@pytest.mark.timeout(1)
def test_ontleding_grondnoot_kruis_overmatig7():
    assert ontleding('F#+7') == ('F#', '+7')

@pytest.mark.timeout(1)
def test_ontleding_grondnoot_mM7():
    assert ontleding('EmM7') == ('E', 'mM7')

@pytest.mark.timeout(1)
def test_ontleding_grondnoot_kruis_overmatig7_b():
    assert ontleding('G#+7') == ('G#', '+7')

@pytest.mark.timeout(1)
def test_ontleding_grondnoot_verminderd():
    assert ontleding('G°') == ('G', '°')

@pytest.mark.timeout(1)
def test_ontleding_grondnoot_C_verminderd():
    assert ontleding('C°') == ('C', '°')


# --- Tests voor noten ---

@pytest.mark.timeout(1)
def test_noten_opgavevoorbeeld_1():
    assert noten('F', [0, 4, 7]) == ['F', 'A', 'C']

@pytest.mark.timeout(1)
def test_noten_opgavevoorbeeld_2():
    assert noten('G', [0, 3, 7, 10]) == ['G', 'A#', 'D', 'F']

@pytest.mark.timeout(1)
def test_noten_opgavevoorbeeld_3():
    assert noten('D#', [0, 4, 7, 11]) == ['D#', 'G', 'A#', 'D']

@pytest.mark.timeout(1)
def test_noten_kruis_overmatig():
    assert noten('F#', [0, 4, 8]) == ['F#', 'A#', 'D']

@pytest.mark.timeout(1)
def test_noten_A_overmatig():
    assert noten('A', [0, 4, 8]) == ['A', 'C#', 'F']

@pytest.mark.timeout(1)
def test_noten_A_majeur7():
    assert noten('A', [0, 4, 7, 11]) == ['A', 'C#', 'E', 'G#']

@pytest.mark.timeout(1)
def test_noten_F_kruis_overmatig7():
    assert noten('F#', [0, 4, 8, 10]) == ['F#', 'A#', 'D', 'E']

@pytest.mark.timeout(1)
def test_noten_E_majeur7():
    assert noten('E', [0, 4, 7, 11]) == ['E', 'G#', 'B', 'D#']

@pytest.mark.timeout(1)
def test_noten_G_kruis_overmatig7():
    assert noten('G#', [0, 4, 8, 10]) == ['G#', 'C', 'E', 'F#']


# --- Tests voor akkoord ---

@pytest.mark.timeout(1)
def test_akkoord_opgavevoorbeeld_1():
    # akkoord('F', akkoordtypes, akkoordsymbolen)
    akkoordtypes = {'majeur': [0, 4, 7], 'mineur': [0, 3, 7], 'dominant septiem': [0, 4, 7, 10], 'mineur septiem': [0, 3, 7, 10], 'majeur septiem': [0, 4, 7, 11]}
    akkoordsymbolen = {'': 'majeur', 'm': 'mineur', '7': 'dominant septiem', 'm7': 'mineur septiem', 'M7': 'majeur septiem'}
    assert akkoord('F', akkoordtypes, akkoordsymbolen) == ('F', 'A', 'C')

@pytest.mark.timeout(1)
def test_akkoord_opgavevoorbeeld_2():
    akkoordtypes = {'majeur': [0, 4, 7], 'mineur': [0, 3, 7], 'dominant septiem': [0, 4, 7, 10], 'mineur septiem': [0, 3, 7, 10], 'majeur septiem': [0, 4, 7, 11]}
    akkoordsymbolen = {'': 'majeur', 'm': 'mineur', '7': 'dominant septiem', 'm7': 'mineur septiem', 'M7': 'majeur septiem'}
    assert akkoord('Gm7', akkoordtypes, akkoordsymbolen) == ('G', 'A#', 'D', 'F')

@pytest.mark.timeout(1)
def test_akkoord_opgavevoorbeeld_3():
    akkoordtypes = {'majeur': [0, 4, 7], 'mineur': [0, 3, 7], 'dominant septiem': [0, 4, 7, 10], 'mineur septiem': [0, 3, 7, 10], 'majeur septiem': [0, 4, 7, 11]}
    akkoordsymbolen = {'': 'majeur', 'm': 'mineur', '7': 'dominant septiem', 'm7': 'mineur septiem', 'M7': 'majeur septiem'}
    assert akkoord('D#M7', akkoordtypes, akkoordsymbolen) == ('D#', 'G', 'A#', 'D')

@pytest.mark.timeout(1)
def test_akkoord_kruis_overmatig():
    akkoordtypes = {'overmatig 7th': [0, 4, 8, 10], 'mineur 7th': [0, 3, 7, 10], 'majeur 7th': [0, 4, 7, 11], 'mineur': [0, 3, 7], 'overmatig': [0, 4, 8]}
    akkoordsymbolen = {'m': 'mineur', 'm7': 'mineur 7th', '+7': 'overmatig 7th', 'M7': 'majeur 7th', '+': 'overmatig'}
    assert akkoord('F#+', akkoordtypes, akkoordsymbolen) == ('F#', 'A#', 'D')

@pytest.mark.timeout(1)
def test_akkoord_overmatig():
    akkoordtypes = {'mineur 7th': [0, 3, 7, 10], 'dominant 7th': [0, 4, 7, 10], 'verminderd': [0, 3, 6], 'mineur-majeur 7th': [0, 4, 7, 11], 'mineur': [0, 3, 7], 'overmatig': [0, 4, 8]}
    akkoordsymbolen = {'mM7': 'mineur-majeur 7th', 'm': 'mineur', '°': 'verminderd', 'm7': 'mineur 7th', '7': 'dominant 7th', '+': 'overmatig'}
    assert akkoord('A+', akkoordtypes, akkoordsymbolen) == ('A', 'C#', 'F')

@pytest.mark.timeout(1)
def test_akkoord_M7():
    akkoordtypes = {'verminderd 7th': [0, 3, 6, 9], 'majeur 7th': [0, 4, 7, 11], 'dominant 7th': [0, 4, 7, 10], 'overmatig 7th': [0, 4, 8, 10], 'mineur': [0, 3, 7], 'mineur-majeur 7th': [0, 4, 7, 11]}
    akkoordsymbolen = {'°7': 'verminderd 7th', 'mM7': 'mineur-majeur 7th', 'm': 'mineur', 'M7': 'majeur 7th', '+7': 'overmatig 7th', '7': 'dominant 7th'}
    assert akkoord('AM7', akkoordtypes, akkoordsymbolen) == ('A', 'C#', 'E', 'G#')

@pytest.mark.timeout(1)
def test_akkoord_kruis_overmatig7():
    akkoordtypes = {'overmatig 7th': [0, 4, 8, 10], 'dominant 7th': [0, 4, 7, 10], 'verminderd': [0, 3, 6], 'mineur': [0, 3, 7], 'mineur-majeur 7th': [0, 4, 7, 11]}
    akkoordsymbolen = {'°': 'verminderd', 'mM7': 'mineur-majeur 7th', 'm': 'mineur', '+7': 'overmatig 7th', '7': 'dominant 7th'}
    assert akkoord('F#+7', akkoordtypes, akkoordsymbolen) == ('F#', 'A#', 'D', 'E')

@pytest.mark.timeout(1)
def test_akkoord_mM7():
    akkoordtypes = {'mineur-majeur 7th': [0, 4, 7, 11], 'verminderd 7th': [0, 3, 6, 9], 'overmatig': [0, 4, 8]}
    akkoordsymbolen = {'+': 'overmatig', 'mM7': 'mineur-majeur 7th', '°7': 'verminderd 7th'}
    assert akkoord('EmM7', akkoordtypes, akkoordsymbolen) == ('E', 'G#', 'B', 'D#')

@pytest.mark.timeout(1)
def test_akkoord_kruis_overmatig7_b():
    akkoordtypes = {'overmatig 7th': [0, 4, 8, 10], 'majeur': [0, 4, 7], 'dominant 7th': [0, 4, 7, 10], 'overmatig': [0, 4, 8]}
    akkoordsymbolen = {'': 'majeur', '+': 'overmatig', '+7': 'overmatig 7th', '7': 'dominant 7th'}
    assert akkoord('G#+7', akkoordtypes, akkoordsymbolen) == ('G#', 'C', 'E', 'F#')

@pytest.mark.timeout(1)
def test_akkoord_verminderd():
    akkoordtypes = {'majeur': [0, 4, 7], 'verminderd': [0, 3, 6], 'mineur': [0, 3, 7], 'overmatig': [0, 4, 8]}
    akkoordsymbolen = {'': 'majeur', '°': 'verminderd', '+': 'overmatig', 'm': 'mineur'}
    assert akkoord('G°', akkoordtypes, akkoordsymbolen) == ('G', 'A#', 'C#')

@pytest.mark.timeout(1)
def test_akkoord_C_verminderd():
    akkoordtypes = {'majeur': [0, 4, 7], 'verminderd': [0, 3, 6], 'majeur 7th': [0, 4, 7, 11], 'mineur-majeur 7th': [0, 4, 7, 11]}
    akkoordsymbolen = {'': 'majeur', '°': 'verminderd', 'M7': 'majeur 7th', 'mM7': 'mineur-majeur 7th'}
    assert akkoord('C°', akkoordtypes, akkoordsymbolen) == ('C', 'D#', 'F#')
