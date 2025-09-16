def geef_invoer_aan_appels_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan appels.py en de uitvoer als lijst van regels op te halen.
    """
    import sys
    sys.modules.pop("reeks_1_expressies.appels", None)  # module telkens opnieuw laden
    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))
    import reeks_1_expressies.appels as appels
    captured = capsys.readouterr()
    return captured.out.strip().split('\n')

def test_appels_voorbeeld_opgave(capsys, monkeypatch):
    # Voorbeeld uit de opgave: 743 appels
    invoer = ["743"]
    uitvoer = geef_invoer_aan_appels_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["1", "2", "3"]

def test_appels_exact_een_kist(capsys, monkeypatch):
    # Exact 20 appels: één volle kist, geen palletten, geen rest
    invoer = ["20"]
    uitvoer = geef_invoer_aan_appels_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["0", "1", "0"]

def test_appels_minder_dan_een_kist(capsys, monkeypatch):
    # Minder dan kistgrootte
    invoer = ["7"]
    uitvoer = geef_invoer_aan_appels_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["0", "0", "7"]

def test_appels_exact_een_pallet(capsys, monkeypatch):
    # Precies 35 kisten = 700 appels
    invoer = ["700"]
    uitvoer = geef_invoer_aan_appels_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["1", "0", "0"]

def test_appels_grote_hoeveelheid(capsys, monkeypatch):
    # Grote hoeveelheid appels
    invoer = ["15000"]
    uitvoer = geef_invoer_aan_appels_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["21", "15", "0"]

def test_appels_allemaal_op(capsys, monkeypatch):
    # Precies verdeelbaar, niks rest
    invoer = ["29400"]
    uitvoer = geef_invoer_aan_appels_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["42", "0", "0"]

def test_appels_nul_appels(capsys, monkeypatch):
    # Geen appels
    invoer = ["0"]
    uitvoer = geef_invoer_aan_appels_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["0", "0", "0"]

def test_appels_meerdere_palletten_en_kisten_en_over(capsys, monkeypatch):
    # Meer dan 1 pallet en 1 kist, met rest
    invoer = ["7355"]
    uitvoer = geef_invoer_aan_appels_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["10", "17", "15"]