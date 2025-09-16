import pytest

def test_boeken_printed_output(capsys):
    from reeks_1_expressies import boeken

    captured = capsys.readouterr().out # laat toe om de uitvoer van de console (tot nu toe) te capteren
    output = captured.strip()  # verwijder eventuele extra spaties of nieuwe regels

    assert float(output) == pytest.approx(945.45, abs=1e-6)
