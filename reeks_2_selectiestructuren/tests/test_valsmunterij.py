def geef_invoer_aan_valsmunterij_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan valsmunterij.py en de uitvoer als string op te halen.
    """
    import sys
    sys.modules.pop("reeks_2_selectiestructuren.valsmunterij", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))
    import reeks_2_selectiestructuren.valsmunterij as valsmunterij

    captured = capsys.readouterr()
    return captured.out.strip()

def test_valsmunterij_evenwicht_evenwicht(capsys, monkeypatch):
    # Eerste en tweede weging in evenwicht: muntstuk 9 is vals
    invoer = ["evenwicht", "evenwicht"]
    verwacht = "muntstuk #9 is vervalst"
    uitvoer = geef_invoer_aan_valsmunterij_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_valsmunterij_evenwicht_links(capsys, monkeypatch):
    # Eerst evenwicht, dan links: muntstuk 8 is vals
    invoer = ["evenwicht", "links"]
    verwacht = "muntstuk #8 is vervalst"
    uitvoer = geef_invoer_aan_valsmunterij_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_valsmunterij_evenwicht_rechts(capsys, monkeypatch):
    # Eerst evenwicht, dan rechts: muntstuk 7 is vals
    invoer = ["evenwicht", "rechts"]
    verwacht = "muntstuk #7 is vervalst"
    uitvoer = geef_invoer_aan_valsmunterij_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_valsmunterij_links_evenwicht(capsys, monkeypatch):
    # Eerst links, dan evenwicht: muntstuk 6 is vals
    invoer = ["links", "evenwicht"]
    verwacht = "muntstuk #6 is vervalst"
    uitvoer = geef_invoer_aan_valsmunterij_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_valsmunterij_links_links(capsys, monkeypatch):
    # Eerst links, dan links: muntstuk 5 is vals
    invoer = ["links", "links"]
    verwacht = "muntstuk #5 is vervalst"
    uitvoer = geef_invoer_aan_valsmunterij_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_valsmunterij_links_rechts(capsys, monkeypatch):
    # Eerst links, dan rechts: muntstuk 4 is vals
    invoer = ["links", "rechts"]
    verwacht = "muntstuk #4 is vervalst"
    uitvoer = geef_invoer_aan_valsmunterij_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_valsmunterij_rechts_evenwicht(capsys, monkeypatch):
    # Eerst rechts, dan evenwicht: muntstuk 3 is vals
    invoer = ["rechts", "evenwicht"]
    verwacht = "muntstuk #3 is vervalst"
    uitvoer = geef_invoer_aan_valsmunterij_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_valsmunterij_rechts_links(capsys, monkeypatch):
    # Eerst rechts, dan links: muntstuk 2 is vals
    invoer = ["rechts", "links"]
    verwacht = "muntstuk #2 is vervalst"
    uitvoer = geef_invoer_aan_valsmunterij_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_valsmunterij_rechts_rechts(capsys, monkeypatch):
    # Eerst rechts, dan rechts: muntstuk 1 is vals
    invoer = ["rechts", "rechts"]
    verwacht = "muntstuk #1 is vervalst"
    uitvoer = geef_invoer_aan_valsmunterij_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht
