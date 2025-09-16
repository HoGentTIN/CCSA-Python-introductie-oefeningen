import pytest

def geef_invoer_aan_bevriende_getallen_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan bevriendegetallen.py en de uitvoer als string op te halen.
    """
    import sys
    sys.modules.pop("reeks_3_lussen.bevriendegetallen", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_3_lussen.bevriendegetallen as bevriendegetallen

    captured = capsys.readouterr()
    return captured.out.strip()

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_bevriende_getallen_uit_opgavetekst(capsys, monkeypatch):
    invoer = ["220", "284"]
    verwacht = "220 en 284 zijn bevriende getallen"
    uitvoer = geef_invoer_aan_bevriende_getallen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_bevriende_getallen_opgave_voorbeeld_1(capsys, monkeypatch):
    invoer = ["2620", "2924"]
    verwacht = "2620 en 2924 zijn bevriende getallen"
    uitvoer = geef_invoer_aan_bevriende_getallen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_bevriende_getallen_opgave_voorbeeld_2(capsys, monkeypatch):
    invoer = ["27856", "29355"]
    verwacht = "27856 en 29355 zijn geen bevriende getallen"
    uitvoer = geef_invoer_aan_bevriende_getallen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_bevriende_getallen_klein_niet_bevriend(capsys, monkeypatch):
    invoer = ["76", "92"]
    verwacht = "76 en 92 zijn geen bevriende getallen"
    uitvoer = geef_invoer_aan_bevriende_getallen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_bevriende_getallen_groter_bevriend(capsys, monkeypatch):
    invoer = ["1184", "1210"]
    verwacht = "1184 en 1210 zijn bevriende getallen"
    uitvoer = geef_invoer_aan_bevriende_getallen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_bevriende_getallen_groter_niet_bevriend(capsys, monkeypatch):
    invoer = ["27856", "29355"]
    verwacht = "27856 en 29355 zijn geen bevriende getallen"
    uitvoer = geef_invoer_aan_bevriende_getallen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_bevriende_getallen_heel_groot_niet_bevriend(capsys, monkeypatch):
    invoer = ["93007", "97833"]
    verwacht = "93007 en 97833 zijn geen bevriende getallen"
    uitvoer = geef_invoer_aan_bevriende_getallen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_bevriende_getallen_heel_groot_bevriend(capsys, monkeypatch):
    invoer = ["63020", "76084"]
    verwacht = "63020 en 76084 zijn bevriende getallen"
    uitvoer = geef_invoer_aan_bevriende_getallen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht