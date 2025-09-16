import pytest

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_basel_output(capsys):
    from reeks_3_lussen import baselprobleem

    captured = capsys.readouterr() # laat toe om de uitvoer van de console (tot nu toe) te capteren
    regels = captured.out.strip().split('\n') # plaats de output in een lijst van regels

    assert float(regels[0]) == pytest.approx(1.63498390018, abs=1e-6)
    assert regels[1] == "100" 