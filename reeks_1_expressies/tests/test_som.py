def geef_invoer_aan_som_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan som.py en de uitvoer op te halen.
    """
    import sys
    sys.modules.pop("reeks_1_expressies.som", None)  # zorg ervoor dat de module bij elke test opnieuw geladen wordt
    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))
    import reeks_1_expressies.som as som
    captured = capsys.readouterr()
    return captured.out.strip() # retourneert de output als string

def test_som_voorbeeld(capsys, monkeypatch):
    # Voorbeeld uit de opgave
    invoer = ["1", "2"]
    verwacht = "3"
    uitvoer = geef_invoer_aan_som_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_som_nul_plus_nul(capsys, monkeypatch):
    # Randgeval: beide getallen zijn 0
    invoer = ["0", "0"]
    verwacht = "0"
    uitvoer = geef_invoer_aan_som_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_som_nul_plus_n(capsys, monkeypatch):
    # Randgeval: eerste getal is 0, tweede is positief
    invoer = ["0", "7"]
    verwacht = "7"
    uitvoer = geef_invoer_aan_som_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_som_grote_getallen(capsys, monkeypatch):
    # Twee grote getallen
    invoer = ["123456", "987654"]
    verwacht = "1111110"
    uitvoer = geef_invoer_aan_som_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_som_symmetrisch(capsys, monkeypatch):
    # Zelfde getal tweemaal
    invoer = ["42", "42"]
    verwacht = "84"
    uitvoer = geef_invoer_aan_som_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_som_een_plus_tien(capsys, monkeypatch):
    # Klein, veelgebruikt eenvoudig getal
    invoer = ["1", "10"]
    verwacht = "11"
    uitvoer = geef_invoer_aan_som_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht