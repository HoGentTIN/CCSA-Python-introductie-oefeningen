def geef_invoer_aan_omkeren_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan omkeren.py en de uitvoer als string op te halen.
    """
    import sys
    sys.modules.pop("reeks_1_expressies.omkeren", None)  # zorg dat de module per test opnieuw geladen wordt
    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_1_expressies.omkeren as omkeren

    captured = capsys.readouterr()
    return captured.out.strip()  # retourneert de hele outputregel

def test_omkeren_voorbeeld_opgave(capsys, monkeypatch):
    # Voorbeeld uit de opgave
    invoer = ["1234", "666", "789"]
    verwacht = "789 666 1234"
    uitvoer = geef_invoer_aan_omkeren_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_omkeren_geordend_oplopend(capsys, monkeypatch):
    # Oplopende getallen
    invoer = ["1", "2", "3"]
    verwacht = "3 2 1"
    uitvoer = geef_invoer_aan_omkeren_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_omkeren_allemaal_gelijk(capsys, monkeypatch):
    # Drie gelijke getallen
    invoer = ["7", "7", "7"]
    verwacht = "7 7 7"
    uitvoer = geef_invoer_aan_omkeren_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_omkeren_nul_waarden(capsys, monkeypatch):
    # Eén of meerdere nullen
    invoer = ["0", "12", "0"]
    verwacht = "0 12 0"
    uitvoer = geef_invoer_aan_omkeren_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_omkeren_negatieve_getallen(capsys, monkeypatch):
    # Ook bij negatieve invoer (mits voorbeeldoplossing dit correct verwerkt)
    invoer = ["-5", "42", "3"]
    verwacht = "3 42 -5"
    uitvoer = geef_invoer_aan_omkeren_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_omkeren_grote_getallen(capsys, monkeypatch):
    # Grote getallen
    invoer = ["1000000", "999", "123456789"]
    verwacht = "123456789 999 1000000"
    uitvoer = geef_invoer_aan_omkeren_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht
