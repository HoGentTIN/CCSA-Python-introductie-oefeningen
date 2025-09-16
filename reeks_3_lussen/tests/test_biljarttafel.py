import pytest

def geef_invoer_aan_biljarttafel_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan biljarttafel.py en de uitvoer als lijst van regels op te halen.
    """
    import sys
    sys.modules.pop("reeks_3_lussen.biljarttafel", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))
    import reeks_3_lussen.biljarttafel as biljarttafel

    captured = capsys.readouterr()
    return captured.out.strip().split('\n')

@pytest.mark.timeout(1)
def test_biljarttafel_opgavevoorbeeld(capsys, monkeypatch):
    # Voorbeeld uit de opgave: 6 x 8
    invoer = ["6", "8"]
    uitvoer = geef_invoer_aan_biljarttafel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "bovenband (6, 6)",
        "rechterband (8, 4)",
        "onderband (4, 0)",
        "linkerband (0, 4)",
        "bovenband (2, 6)",
        "rechteronderpocket (8, 0)"
    ]

@pytest.mark.timeout(1)
def test_biljarttafel_gelijkzijdige_tafel_direct_rechterbovenpocket(capsys, monkeypatch):
    invoer = ["10", "10"]
    uitvoer = geef_invoer_aan_biljarttafel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["rechterbovenpocket (10, 10)"]

@pytest.mark.timeout(1)
def test_biljarttafel_veel_botsen_tot_linkerbovenpocket(capsys, monkeypatch):
    invoer = ["2", "13"]
    uitvoer = geef_invoer_aan_biljarttafel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "bovenband (2, 2)",
        "onderband (4, 0)",
        "bovenband (6, 2)",
        "onderband (8, 0)",
        "bovenband (10, 2)",
        "onderband (12, 0)",
        "rechterband (13, 1)",
        "bovenband (12, 2)",
        "onderband (10, 0)",
        "bovenband (8, 2)",
        "onderband (6, 0)",
        "bovenband (4, 2)",
        "onderband (2, 0)",
        "linkerbovenpocket (0, 2)"
    ]

@pytest.mark.timeout(1)
def test_biljarttafel_direct_rechteronderpocket(capsys, monkeypatch):
    invoer = ["6", "12"]
    uitvoer = geef_invoer_aan_biljarttafel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "bovenband (6, 6)",
        "rechteronderpocket (12, 0)"
    ]

@pytest.mark.timeout(1)
def test_biljarttafel_heel_veel_botsingen_tot_linkerbovenpocket(capsys, monkeypatch):
    invoer = ["8", "15"]
    uitvoer = geef_invoer_aan_biljarttafel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "bovenband (8, 8)",
        "rechterband (15, 1)",
        "onderband (14, 0)",
        "bovenband (6, 8)",
        "linkerband (0, 2)",
        "onderband (2, 0)",
        "bovenband (10, 8)",
        "rechterband (15, 3)",
        "onderband (12, 0)",
        "bovenband (4, 8)",
        "linkerband (0, 4)",
        "onderband (4, 0)",
        "bovenband (12, 8)",
        "rechterband (15, 5)",
        "onderband (10, 0)",
        "bovenband (2, 8)",
        "linkerband (0, 6)",
        "onderband (6, 0)",
        "bovenband (14, 8)",
        "rechterband (15, 7)",
        "onderband (8, 0)",
        "linkerbovenpocket (0, 8)"
    ]

@pytest.mark.timeout(1)
def test_biljarttafel_meerdere_botsingen_tot_rechterbovenpocket(capsys, monkeypatch):
    invoer = ["9", "15"]
    uitvoer = geef_invoer_aan_biljarttafel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "bovenband (9, 9)",
        "rechterband (15, 3)",
        "onderband (12, 0)",
        "bovenband (3, 9)",
        "linkerband (0, 6)",
        "onderband (6, 0)",
        "rechterbovenpocket (15, 9)"
    ]

@pytest.mark.timeout(1)
def test_biljarttafel_kleinere_gelijkzijdige_tafel_direct_rechterbovenpocket(capsys, monkeypatch):
    invoer = ["4", "4"]
    uitvoer = geef_invoer_aan_biljarttafel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == ["rechterbovenpocket (4, 4)"]
