import pytest
from reeks_5_lijsten_en_tuples.faroshuffle import nieuw_kaartspel, splits_kaartspel, faro_shuffle

# --- Tests voor nieuw_kaartspel ---

def test_nieuw_kaartspel_opgavevoorbeeld_1():
    assert nieuw_kaartspel(['dood ', 'liefde ', 'tijd '], ['0', '1']) == [
        'dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1'
    ]

def test_nieuw_kaartspel_opgavevoorbeeld_2():
    assert nieuw_kaartspel(['blad ', 'steen ', 'schaar '], ['1', '2', '3']) == [
        'blad 1', 'blad 2', 'blad 3', 'steen 1', 'steen 2', 'steen 3',
        'schaar 1', 'schaar 2', 'schaar 3'
    ]

def test_nieuw_kaartspel_opgavevoorbeeld_3():
    assert nieuw_kaartspel(['James '], ['7']) == ['James 7']

def test_nieuw_kaartspel_standaard_kaartspel():
    assert nieuw_kaartspel(
        ['H', 'R', 'K', 'S'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'B', 'D', 'H']
    ) == [
        'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HB', 'HD', 'HH',
        'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'RB', 'RD', 'RH',
        'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'KB', 'KD', 'KH',
        'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SB', 'SD', 'SH'
    ]

def test_nieuw_kaartspel_4_kleuren_8_waarden():
    assert nieuw_kaartspel(
        ['H', 'R', 'K', 'S'],
        ['1', '7', '8', '9', '10', 'B', 'D', 'H']
    ) == [
        'H1', 'H7', 'H8', 'H9', 'H10', 'HB', 'HD', 'HH',
        'R1', 'R7', 'R8', 'R9', 'R10', 'RB', 'RD', 'RH',
        'K1', 'K7', 'K8', 'K9', 'K10', 'KB', 'KD', 'KH',
        'S1', 'S7', 'S8', 'S9', 'S10', 'SB', 'SD', 'SH'
    ]

def test_nieuw_kaartspel_6_kleuren_9_waarden():
    assert nieuw_kaartspel(
        ['Y', 'R', 'B', 'G', 'O', 'P'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    ) == [
        'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9',
        'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9',
        'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
        'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
        'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9',
        'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9'
    ]


# --- Tests voor splits_kaartspel ---

def test_splits_kaartspel_opgavevoorbeeld_1():
    lijst = ['dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1']
    assert splits_kaartspel(lijst) == (
        ['dood 0', 'dood 1', 'liefde 0'],
        ['liefde 1', 'tijd 0', 'tijd 1']
    )

def test_splits_kaartspel_opgavevoorbeeld_2():
    lijst = ['blad 1', 'blad 2', 'blad 3', 'steen 1', 'steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3']
    assert splits_kaartspel(lijst) == (
        ['blad 1', 'blad 2', 'blad 3', 'steen 1'],
        ['steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3']
    )

def test_splits_kaartspel_opgavevoorbeeld_3():
    assert splits_kaartspel(['James 7']) == ([], ['James 7'])

def test_splits_kaartspel_standaard_kaartspel():
    lijst = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HB', 'HD', 'HH', 
             'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'RB', 'RD', 'RH', 
             'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'KB', 'KD', 'KH', 
             'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SB', 'SD', 'SH'
             ]
    assert splits_kaartspel(lijst) == (
        ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HB', 'HD', 'HH', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'RB', 'RD', 'RH'],
        ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'KB', 'KD', 'KH', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SB', 'SD', 'SH']
    )

def test_splits_kaartspel_4_kleuren_8_waarden():
    lijst = ['H1', 'H7', 'H8', 'H9', 'H10', 'HB', 'HD', 'HH', 
             'R1', 'R7', 'R8', 'R9', 'R10', 'RB', 'RD', 'RH', 
             'K1', 'K7', 'K8', 'K9', 'K10', 'KB', 'KD', 'KH', 
             'S1', 'S7', 'S8', 'S9', 'S10', 'SB', 'SD', 'SH'
             ]
    assert splits_kaartspel(lijst) == (
        ['H1', 'H7', 'H8', 'H9', 'H10', 'HB', 'HD', 'HH', 'R1', 'R7', 'R8', 'R9', 'R10', 'RB', 'RD', 'RH'],
        ['K1', 'K7', 'K8', 'K9', 'K10', 'KB', 'KD', 'KH', 'S1', 'S7', 'S8', 'S9', 'S10', 'SB', 'SD', 'SH']
    )

def test_splits_kaartspel_6_kleuren_9_waarden():
    lijst = [
        'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9',
        'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9',
        'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
        'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
        'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9',
        'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9'
    ]
    assert splits_kaartspel(lijst) == (
        ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'],
        ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9']
    )


# --- Tests voor faro_shuffle ---

def test_faro_shuffle_opgavevoorbeeld_1():
    assert faro_shuffle(['dood 0', 'dood 1', 'liefde 0'], ['liefde 1', 'tijd 0', 'tijd 1']) == [
        'dood 0', 'liefde 1', 'dood 1', 'tijd 0', 'liefde 0', 'tijd 1'
    ]

def test_faro_shuffle_opgavevoorbeeld_2():
    assert faro_shuffle(['blad 1', 'blad 2', 'blad 3', 'steen 1'], ['steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3']) == [
        'blad 1', 'steen 2', 'blad 2', 'steen 3', 'blad 3', 'schaar 1', 'steen 1', 'schaar 2', 'schaar 3'
    ]

def test_faro_shuffle_opgavevoorbeeld_3():
    assert faro_shuffle([], ['James 7']) == ['James 7']

def test_faro_shuffle_standaard_kaartspel():
    assert faro_shuffle(
        ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HB', 'HD', 'HH', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'RB', 'RD', 'RH'],
        ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'KB', 'KD', 'KH', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SB', 'SD', 'SH']
    ) == [
        'H1', 'K1', 'H2', 'K2', 'H3', 'K3', 'H4', 'K4', 'H5', 'K5', 'H6', 'K6', 'H7', 'K7', 'H8', 'K8', 'H9', 'K9', 'H10', 'K10', 'HB', 'KB', 'HD', 'KD', 'HH', 'KH',
        'R1', 'S1', 'R2', 'S2', 'R3', 'S3', 'R4', 'S4', 'R5', 'S5', 'R6', 'S6', 'R7', 'S7', 'R8', 'S8', 'R9', 'S9', 'R10', 'S10', 'RB', 'SB', 'RD', 'SD', 'RH', 'SH'
    ]

def test_faro_shuffle_4_kleuren_8_waarden():
    assert faro_shuffle(
        ['H1', 'H7', 'H8', 'H9', 'H10', 'HB', 'HD', 'HH', 'R1', 'R7', 'R8', 'R9', 'R10', 'RB', 'RD', 'RH'],
        ['K1', 'K7', 'K8', 'K9', 'K10', 'KB', 'KD', 'KH', 'S1', 'S7', 'S8', 'S9', 'S10', 'SB', 'SD', 'SH']
    ) == [
        'H1', 'K1', 'H7', 'K7', 'H8', 'K8', 'H9', 'K9', 'H10', 'K10', 'HB', 'KB', 'HD', 'KD', 'HH', 'KH',
        'R1', 'S1', 'R7', 'S7', 'R8', 'S8', 'R9', 'S9', 'R10', 'S10', 'RB', 'SB', 'RD', 'SD', 'RH', 'SH'
    ]

def test_faro_shuffle_6_kleuren_9_waarden():
    assert faro_shuffle(
        ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'],
        ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9']
    ) == [
        'Y1', 'G1', 'Y2', 'G2', 'Y3', 'G3', 'Y4', 'G4', 'Y5', 'G5', 'Y6', 'G6', 'Y7', 'G7', 'Y8', 'G8', 'Y9', 'G9',
        'R1', 'O1', 'R2', 'O2', 'R3', 'O3', 'R4', 'O4', 'R5', 'O5', 'R6', 'O6', 'R7', 'O7', 'R8', 'O8', 'R9', 'O9',
        'B1', 'P1', 'B2', 'P2', 'B3', 'P3', 'B4', 'P4', 'B5', 'P5', 'B6', 'P6', 'B7', 'P7', 'B8', 'P8', 'B9', 'P9'
    ]
