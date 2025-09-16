def geef_invoer_aan_bladsteenschaar_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan bladsteenschaar.py en de uitvoer op te halen.
    """
    import sys
    sys.modules.pop("reeks_2_selectiestructuren.bladsteenschaar", None)  # Module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_2_selectiestructuren.bladsteenschaar as bladsteenschaar

    captured = capsys.readouterr()
    return captured.out.strip()

def test_bladsteenschaar_voorbeeld_opgave(capsys, monkeypatch):
    # Voorbeeld uit de opgave
    invoer = ["Spock", "blad"]
    verwacht = "speler2 wint"
    uitvoer = geef_invoer_aan_bladsteenschaar_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_bladsteenschaar_gelijkspel(capsys, monkeypatch):
    # Gelijkspel
    invoer = ["steen", "steen"]
    verwacht = "gelijkspel"
    uitvoer = geef_invoer_aan_bladsteenschaar_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_bladsteenschaar_speler1_wint(capsys, monkeypatch):
    # Speler1 wint met schaar tegen blad
    invoer = ["schaar", "blad"]
    verwacht = "speler1 wint"
    uitvoer = geef_invoer_aan_bladsteenschaar_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_bladsteenschaar_speler2_wint(capsys, monkeypatch):
    # Speler2 wint met Spock tegen schaar
    invoer = ["schaar", "Spock"]
    verwacht = "speler2 wint"
    uitvoer = geef_invoer_aan_bladsteenschaar_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_bladsteenschaar_hagedis_eet_blad(capsys, monkeypatch):
    # Hagedis eet blad (speler1 wint)
    invoer = ["hagedis", "blad"]
    verwacht = "speler1 wint"
    uitvoer = geef_invoer_aan_bladsteenschaar_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_bladsteenschaar_blad_weerlegt_spock(capsys, monkeypatch):
    # Blad wint van Spock (speler2 wint)
    invoer = ["Spock", "blad"]
    verwacht = "speler2 wint"
    uitvoer = geef_invoer_aan_bladsteenschaar_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_bladsteenschaar_tussen_geval(capsys, monkeypatch):
    # Steen plet hagedis (speler1 wint)
    invoer = ["steen", "hagedis"]
    verwacht = "speler1 wint"
    uitvoer = geef_invoer_aan_bladsteenschaar_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_bladsteenschaar_tussen_geval_2(capsys, monkeypatch):
    # Hagedis vergiftigt Spock (speler1 wint)
    invoer = ["hagedis", "Spock"]
    verwacht = "speler1 wint"
    uitvoer = geef_invoer_aan_bladsteenschaar_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht
