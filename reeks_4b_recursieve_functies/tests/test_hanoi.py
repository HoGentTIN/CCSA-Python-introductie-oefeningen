import pytest
from reeks_4b_recursieve_functies.hanoi import hanoi

def run_hanoi_geef_stdout_terug(n, capsys):
    """
    Roept hanoi.hanoi(n) aan en geeft de standaarduitvoer terug als string.
    """
    hanoi(n)
    captured = capsys.readouterr()
    return captured.out.strip().split('\n') # plaats de output in een lijst van regels

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_hanoi_1(capsys):
    resultaat = run_hanoi_geef_stdout_terug(1, capsys)
    assert resultaat == [
        "Schijf 1 van A naar C", 
        "1 stappen gedaan"
        ]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_hanoi_2(capsys):
    resultaat = run_hanoi_geef_stdout_terug(2, capsys)
    assert resultaat == [
        "Schijf 1 van A naar B", 
        "Schijf 2 van A naar C", 
        "Schijf 1 van B naar C", 
        "3 stappen gedaan"
    ]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_hanoi_3(capsys):
    resultaat = run_hanoi_geef_stdout_terug(3, capsys)
    assert resultaat == [
        "Schijf 1 van A naar C",
        "Schijf 2 van A naar B",
        "Schijf 1 van C naar B",
        "Schijf 3 van A naar C",
        "Schijf 1 van B naar A",
        "Schijf 2 van B naar C",
        "Schijf 1 van A naar C",
        "7 stappen gedaan"
    ]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_hanoi_4(capsys):
    resultaat = run_hanoi_geef_stdout_terug(4, capsys)
    assert resultaat == [
        "Schijf 1 van A naar B",
        "Schijf 2 van A naar C",
        "Schijf 1 van B naar C",
        "Schijf 3 van A naar B",
        "Schijf 1 van C naar A",
        "Schijf 2 van C naar B",
        "Schijf 1 van A naar B",
        "Schijf 4 van A naar C",
        "Schijf 1 van B naar C",
        "Schijf 2 van B naar A",
        "Schijf 1 van C naar A",
        "Schijf 3 van B naar C",
        "Schijf 1 van A naar B",
        "Schijf 2 van A naar C",
        "Schijf 1 van B naar C",
        "15 stappen gedaan"
    ]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_hanoi_5(capsys):
    resultaat = run_hanoi_geef_stdout_terug(5, capsys)
    assert resultaat == [
        "Schijf 1 van A naar C",
        "Schijf 2 van A naar B",
        "Schijf 1 van C naar B",
        "Schijf 3 van A naar C",
        "Schijf 1 van B naar A",
        "Schijf 2 van B naar C",
        "Schijf 1 van A naar C",
        "Schijf 4 van A naar B",
        "Schijf 1 van C naar B",
        "Schijf 2 van C naar A",
        "Schijf 1 van B naar A",
        "Schijf 3 van C naar B",
        "Schijf 1 van A naar C",
        "Schijf 2 van A naar B",
        "Schijf 1 van C naar B",
        "Schijf 5 van A naar C",
        "Schijf 1 van B naar A",
        "Schijf 2 van B naar C",
        "Schijf 1 van A naar C",
        "Schijf 3 van B naar A",
        "Schijf 1 van C naar B",
        "Schijf 2 van C naar A",
        "Schijf 1 van B naar A",
        "Schijf 4 van B naar C",
        "Schijf 1 van A naar C",
        "Schijf 2 van A naar B",
        "Schijf 1 van C naar B",
        "Schijf 3 van A naar C",
        "Schijf 1 van B naar A",
        "Schijf 2 van B naar C",
        "Schijf 1 van A naar C",
        "31 stappen gedaan"
    ]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_hanoi_6(capsys):
    resultaat = run_hanoi_geef_stdout_terug(6, capsys)
    assert resultaat == [
        "Schijf 1 van A naar B",
        "Schijf 2 van A naar C",
        "Schijf 1 van B naar C",
        "Schijf 3 van A naar B",
        "Schijf 1 van C naar A",
        "Schijf 2 van C naar B",
        "Schijf 1 van A naar B",
        "Schijf 4 van A naar C",
        "Schijf 1 van B naar C",
        "Schijf 2 van B naar A",
        "Schijf 1 van C naar A",
        "Schijf 3 van B naar C",
        "Schijf 1 van A naar B",
        "Schijf 2 van A naar C",
        "Schijf 1 van B naar C",
        "Schijf 5 van A naar B",
        "Schijf 1 van C naar A",
        "Schijf 2 van C naar B",
        "Schijf 1 van A naar B",
        "Schijf 3 van C naar A",
        "Schijf 1 van B naar C",
        "Schijf 2 van B naar A",
        "Schijf 1 van C naar A",
        "Schijf 4 van C naar B",
        "Schijf 1 van A naar B",
        "Schijf 2 van A naar C",
        "Schijf 1 van B naar C",
        "Schijf 3 van A naar B",
        "Schijf 1 van C naar A",
        "Schijf 2 van C naar B",
        "Schijf 1 van A naar B",
        "Schijf 6 van A naar C",
        "Schijf 1 van B naar C",
        "Schijf 2 van B naar A",
        "Schijf 1 van C naar A",
        "Schijf 3 van B naar C",
        "Schijf 1 van A naar B",
        "Schijf 2 van A naar C",
        "Schijf 1 van B naar C",
        "Schijf 4 van B naar A",
        "Schijf 1 van C naar A",
        "Schijf 2 van C naar B",
        "Schijf 1 van A naar B",
        "Schijf 3 van C naar A",
        "Schijf 1 van B naar C",
        "Schijf 2 van B naar A",
        "Schijf 1 van C naar A",
        "Schijf 5 van B naar C",
        "Schijf 1 van A naar B",
        "Schijf 2 van A naar C",
        "Schijf 1 van B naar C",
        "Schijf 3 van A naar B",
        "Schijf 1 van C naar A",
        "Schijf 2 van C naar B",
        "Schijf 1 van A naar B",
        "Schijf 4 van A naar C",
        "Schijf 1 van B naar C",
        "Schijf 2 van B naar A",
        "Schijf 1 van C naar A",
        "Schijf 3 van B naar C",
        "Schijf 1 van A naar B",
        "Schijf 2 van A naar C",
        "Schijf 1 van B naar C",
        "63 stappen gedaan"
    ]
