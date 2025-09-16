def geef_invoer_aan_getalladder_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan getalladder.py en de uitvoer als lijst van regels op te halen.
    """
    import sys
    sys.modules.pop("reeks_3_lussen.getalladder", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_3_lussen.getalladder as getalladder

    captured = capsys.readouterr()
    return captured.out.strip().split('\n') # geef elke regel als apart item in de lijst terug

def test_getalladder_minimaal(capsys, monkeypatch):
    # Minimale toegestane invoer (n = 1)
    invoer = ["1"]
    uitvoer = geef_invoer_aan_getalladder_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["1"]

def test_getalladder_opgave_vb1(capsys, monkeypatch):
    # Voorbeeld uit de opgave (n = 3)
    invoer = ["3"]
    uitvoer = geef_invoer_aan_getalladder_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["1", "12", "123"]

def test_getalladder_opgave_vb2(capsys, monkeypatch):
    # Ander voorbeeld uit de opgave (n = 5)
    invoer = ["5"]
    uitvoer = geef_invoer_aan_getalladder_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["1", "12", "123", "1234", "12345"]

def test_getalladder_maximaal(capsys, monkeypatch):
    # Maximale toegestane invoer (n = 9)
    invoer = ["9"]
    uitvoer = geef_invoer_aan_getalladder_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "1",
        "12",
        "123",
        "1234",
        "12345",
        "123456",
        "1234567",
        "12345678",
        "123456789"
    ]