import pytest

def geef_invoer_aan_autoverhuurbedrijf_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan autoverhuurbedrijf.py en de uitvoer op te halen.
    """
    import sys
    sys.modules.pop("reeks_1_expressies.autoverhuurbedrijf", None)
    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))
    import reeks_1_expressies.autoverhuurbedrijf as autoverhuurbedrijf
    captured = capsys.readouterr()
    return captured.out.strip()

def test_autoverhuurbedrijf_voorbeeld_opgave(capsys, monkeypatch):
    # Voorbeeld uit opgave
    invoer = ["123.789", "666.666", "62.5"]
    verwacht = 11.51273677094443
    uitvoer = geef_invoer_aan_autoverhuurbedrijf_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(float(verwacht), abs=1e-6)

def test_autoverhuurbedrijf_gehele_waarden(capsys, monkeypatch):
    # Gehele km-standen, geheel aantal liter
    invoer = ["100", "300", "20"]
    verwacht = "10.0"
    uitvoer = geef_invoer_aan_autoverhuurbedrijf_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(float(verwacht), abs=1e-6)

def test_autoverhuurbedrijf_kleine_afstand(capsys, monkeypatch):
    # Kleine afstand, kleine hoeveelheid benzine
    invoer = ["0", "10", "1"]
    verwacht = "10.0"
    uitvoer = geef_invoer_aan_autoverhuurbedrijf_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(float(verwacht), abs=1e-6)

def test_autoverhuurbedrijf_decimale_liter(capsys, monkeypatch):
    # Decimaal aantal liters, gehele afstand
    invoer = ["0", "100", "5.5"]
    verwacht = "5.5"
    uitvoer = geef_invoer_aan_autoverhuurbedrijf_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(float(verwacht), abs=1e-6)

def test_autoverhuurbedrijf_klein_verbruik(capsys, monkeypatch):
    # Weinig verbruik op (relatief) grote afstand
    invoer = ["0", "1000", "20"]
    verwacht = "2.0"
    uitvoer = geef_invoer_aan_autoverhuurbedrijf_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(float(verwacht), abs=1e-6)

def test_autoverhuurbedrijf_allemaal_kommagetallen(capsys, monkeypatch):
    # Weinig verbruik op (relatief) grote afstand
    invoer = ["100.590562", "177.459337", "36.380107"]
    verwacht = "47.327549"
    uitvoer = geef_invoer_aan_autoverhuurbedrijf_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(float(verwacht), abs=1e-6)