import pytest

def geef_invoer_aan_vierkantsvergelijking_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan vierkantsvergelijking.py en de uitvoer als lijst van regels op te halen.
    """
    import sys
    sys.modules.pop("reeks_2_selectiestructuren.vierkantsvergelijking", None)

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))
    import reeks_2_selectiestructuren.vierkantsvergelijking as vierkantsvergelijking

    captured = capsys.readouterr()
    return captured.out.strip().split('\n')

def test_vierkantsvergelijking_twee_wortels(capsys, monkeypatch):
    invoer = ["1.0", "-5.0", "6.0"]
    uitvoer = geef_invoer_aan_vierkantsvergelijking_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0] == "twee wortels"
    assert float(uitvoer[1]) == pytest.approx(2.0, abs=1e-6)
    assert float(uitvoer[2]) == pytest.approx(3.0, abs=1e-6)

def test_vierkantsvergelijking_geen_wortels(capsys, monkeypatch):
    invoer = ["1.0", "0.0", "2.0"]
    uitvoer = geef_invoer_aan_vierkantsvergelijking_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["geen wortels"]

def test_vierkantsvergelijking_een_wortel(capsys, monkeypatch):
    invoer = ["1.0", "-1.0", "0.25"]
    uitvoer = geef_invoer_aan_vierkantsvergelijking_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0] == "een wortel"
    assert float(uitvoer[1]) == pytest.approx(0.5, abs=1e-6)

def test_vierkantsvergelijking_decimalen(capsys, monkeypatch):
    invoer = ["1.0", "-5.5", "7.36"]
    uitvoer = geef_invoer_aan_vierkantsvergelijking_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0] == "twee wortels"
    assert float(uitvoer[1]) == pytest.approx(2.3, abs=1e-6)
    assert float(uitvoer[2]) == pytest.approx(3.2, abs=1e-6)

def test_vierkantsvergelijking_symmetrisch(capsys, monkeypatch):
    invoer = ["1.0", "-2.0", "1.0"]
    uitvoer = geef_invoer_aan_vierkantsvergelijking_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0] == "een wortel"
    assert float(uitvoer[1]) == pytest.approx(1.0, abs=1e-6)

def test_vierkantsvergelijking_negatieve_waarden(capsys, monkeypatch):
    invoer = ["-1.0", "6.0", "-8.0"]
    uitvoer = geef_invoer_aan_vierkantsvergelijking_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0] == "twee wortels"
    assert float(uitvoer[1]) == pytest.approx(2.0, abs=1e-6)
    assert float(uitvoer[2]) == pytest.approx(4.0, abs=1e-6)

def test_vierkantsvergelijking_decimalen_negatief(capsys, monkeypatch):
    invoer = ["-2.580799", "-44.047435", "18.039197"]
    uitvoer = geef_invoer_aan_vierkantsvergelijking_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0] == "twee wortels"
    assert float(uitvoer[1]) == pytest.approx(-17.467522, abs=1e-6)
    assert float(uitvoer[2]) == pytest.approx(0.400158, abs=1e-6)

def test_vierkantsvergelijking_decimalen_groot(capsys, monkeypatch):
    # Extra test: grote negatieve getallen en positieve c
    invoer = ["-70.341786", "-95.824142", "95.647505"]
    uitvoer = geef_invoer_aan_vierkantsvergelijking_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0] == "twee wortels"
    assert float(uitvoer[1]) == pytest.approx(-2.031575, abs=1e-6)
    assert float(uitvoer[2]) == pytest.approx(0.669310, abs=1e-6)
