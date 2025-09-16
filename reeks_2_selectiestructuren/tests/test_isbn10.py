def geef_invoer_aan_isbn_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan isbn.py en de uitvoer als string op te halen.
    """
    import sys
    sys.modules.pop("reeks_2_selectiestructuren.isbn10", None)  # Module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_2_selectiestructuren.isbn10 as isbn10

    captured = capsys.readouterr()
    return captured.out.strip()

def test_isbn_voorbeeld_ok(capsys, monkeypatch):
    # Opgavevoorbeeld met OK-uitvoer
    invoer = ["9", "9", "7", "1", "5", "0", "2", "1", "0", "0"]
    verwacht = "OK"
    uitvoer = geef_invoer_aan_isbn_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_isbn_voorbeeld_fout(capsys, monkeypatch):
    # Opgavevoorbeeld met FOUT-uitvoer
    invoer = ["9", "9", "7", "1", "5", "0", "2", "1", "0", "8"]
    verwacht = "FOUT"
    uitvoer = geef_invoer_aan_isbn_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_isbn_allemaal_nullen_ok(capsys, monkeypatch):
    # Randgeval: alles nul (moet OK zijn)
    invoer = ["0"] * 10
    verwacht = "OK"
    uitvoer = geef_invoer_aan_isbn_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_isbn_grens_ok(capsys, monkeypatch):
    # We nemen een geldig tiencijferig ISBN met controlecijfer 1
    invoer = ["5", "7", "6", "6", "4", "5", "2", "8", "6", "1"]
    verwacht = "OK"
    uitvoer = geef_invoer_aan_isbn_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_isbn_tussen_geval_OK(capsys, monkeypatch):
    # Willekeurig tussenliggend geldig ISBN
    invoer = ["9", "2", "8", "3", "7", "8", "1", "1", "5", "5"]
    verwacht = "OK"
    uitvoer = geef_invoer_aan_isbn_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_isbn_tussen_geval_fout(capsys, monkeypatch):
    # Willekeurig ongeldig ISBN, laatste cijfer wijkt af
    invoer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    verwacht = "FOUT"
    uitvoer = geef_invoer_aan_isbn_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht
