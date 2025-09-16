def geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan botsing.py en de uitvoer als string op te halen.
    """
    import sys
    sys.modules.pop("reeks_2_selectiestructuren.botsing", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_2_selectiestructuren.botsing as botsing

    captured = capsys.readouterr()
    return captured.out.strip()

def test_botsing_geen_botsing_voorbeeld1(capsys, monkeypatch):
    # Voorbeeld 1 uit de opgave: geen botsing
    invoer = ["0", "0", "1", "2", "4", "1", "5", "5"]
    verwacht = "geen botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_botsing_botsing_voorbeeld2(capsys, monkeypatch):
    # Voorbeeld 2 uit de opgave: botsing
    invoer = ["0", "0", "2", "3", "1", "2", "5", "5"]
    verwacht = "botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_botsing_raken_maar_niet_overlappen_hoek(capsys, monkeypatch):
    # Rechthoeken raken elkaar net in een hoek, geen overlap
    invoer = ["0", "0", "2", "2", "2", "2", "4", "4"]
    verwacht = "geen botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht


def test_botsing_raken_maar_niet_overlappen_horizontaal(capsys, monkeypatch):
    # Rechthoeken raken elkaar net aan de zijkant, geen overlap
    invoer = ["0", "0", "2", "2", "2", "0", "4", "2"]
    verwacht = "geen botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_botsing_raken_maar_niet_overlappen_verticaal(capsys, monkeypatch):
    # Rechthoeken raken elkaar net aan de onderkant, geen overlap
    invoer = ["0", "0", "2", "2", "0", "2", "2", "4"]
    verwacht = "geen botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_botsing_volledige_overlap(capsys, monkeypatch):
    # De ene rechthoek volledig binnen de andere
    invoer = ["0", "0", "5", "5", "1", "1", "3", "3"]
    verwacht = "botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_botsing_deels_overlappen_hoek(capsys, monkeypatch):
    # Rechthoeken overlappen enkel in een hoek
    invoer = ["0", "0", "3", "3", "2", "2", "5", "5"]
    verwacht = "botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_botsing_omgewisselde_volgorde(capsys, monkeypatch):
    # Coördinaten van rechthoeken in verschillende volgorde, nog steeds overlappen
    invoer = ["5", "5", "0", "0", "3", "3", "2", "2"]
    verwacht = "botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_botsing_ver_geen_botsing(capsys, monkeypatch):
    # Rechthoeken liggen ver uit elkaar
    invoer = ["0", "0", "1", "1", "10", "10", "11", "11"]
    verwacht = "geen botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_botsing_deels_in_elkaar(capsys, monkeypatch):
    # Rechthoeken overlappen gedeeltelijk
    invoer = ["27", "19", "39", "33", "20", "27", "34", "33"]
    verwacht = "botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_botsing_overlappende_rect_met_herhaalde_punten(capsys, monkeypatch):
    # Tweemaal hetzelfde paar punten in verschillende volgorde (=zelfde rechthoek)
    invoer = ["39", "19", "27", "33", "27", "19", "39", "33"]
    verwacht = "botsing"
    uitvoer = geef_invoer_aan_botsing_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht
