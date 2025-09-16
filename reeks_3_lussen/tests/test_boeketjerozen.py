import pytest

def geef_invoer_aan_boeketjerozen_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan boeketjerozen.py en de uitvoer als lijst van regels op te halen.
    """
    import sys
    sys.modules.pop("reeks_3_lussen.boeketjerozen", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_3_lussen.boeketjerozen as boeketjerozen

    captured = capsys.readouterr()
    return captured.out.strip().split('\n')

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_boeketjerozen_opgavevoorbeeld(capsys, monkeypatch):
    # Voorbeeld uit de opgave: 100, 53, <
    invoer = ["100", "53", "<"]
    uitvoer = geef_invoer_aan_boeketjerozen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["2", "51", "49"]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_boeketjerozen_grote_aantallen_kleiner_dan(capsys, monkeypatch):
    invoer = ["222", "114", "<"]
    uitvoer = geef_invoer_aan_boeketjerozen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["2", "112", "110"]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_boeketjerozen_kleine_aantallen_groter_dan(capsys, monkeypatch):
    invoer = ["34", "4", ">"]
    uitvoer = geef_invoer_aan_boeketjerozen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["2", "2", "32"]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_boeketjerozen_veel_blauw_groter_dan(capsys, monkeypatch):
    invoer = ["6", "50", ">"]
    uitvoer = geef_invoer_aan_boeketjerozen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["48", "2", "4"]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_boeketjerozen_minimaal_toegestaan_wit_en_blauw_groter_dan(capsys, monkeypatch):
    # w+b net boven minimale grens
    invoer = ["138", "4", ">"]
    uitvoer = geef_invoer_aan_boeketjerozen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["2", "2", "136"]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_boeketjerozen_minimaal_toegestaan_rood_kleiner_dan(capsys, monkeypatch):
    invoer = ["5", "230", "<"]
    uitvoer = geef_invoer_aan_boeketjerozen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["227", "3", "2"]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_boeketjerozen_minimaal_toegestaan_wit_groter_dan(capsys, monkeypatch):
    invoer = ["5", "244", ">"]
    uitvoer = geef_invoer_aan_boeketjerozen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["242", "2", "3"]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_boeketjerozen_kleine_waarden_kleiner_dan(capsys, monkeypatch):
    invoer = ["7", "6", "<"]
    uitvoer = geef_invoer_aan_boeketjerozen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["2", "4", "3"]

