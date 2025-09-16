import pytest

def geef_invoer_aan_dedriewijzen_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan dedriewijzen.py en de uitvoer als string op te halen.
    """
    import sys
    sys.modules.pop("reeks_3_lussen.dedriewijzen", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_3_lussen.dedriewijzen as dedriewijzen

    captured = capsys.readouterr()
    return captured.out.strip()

@pytest.mark.timeout(1)
def test_dedriewijzen_opgavevoorbeeld(capsys, monkeypatch):
    invoer = ["65.52"]
    verwacht = "€0.52 + €2.00 + €63.00 = €0.52 x €2.00 x €63.00 = €65.52"
    uitvoer = geef_invoer_aan_dedriewijzen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1)
def test_dedriewijzen_10_8(capsys, monkeypatch):
    invoer = ["10.8"]
    verwacht = "€0.40 + €5.00 + €5.40 = €0.40 x €5.00 x €5.40 = €10.80"
    uitvoer = geef_invoer_aan_dedriewijzen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1)
def test_dedriewijzen_46_2(capsys, monkeypatch):
    invoer = ["46.2"]
    verwacht = "€0.70 + €1.50 + €44.00 = €0.70 x €1.50 x €44.00 = €46.20"
    uitvoer = geef_invoer_aan_dedriewijzen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1)
def test_dedriewijzen_69_96(capsys, monkeypatch):
    invoer = ["69.96"]
    verwacht = "€0.06 + €27.50 + €42.40 = €0.06 x €27.50 x €42.40 = €69.96"
    uitvoer = geef_invoer_aan_dedriewijzen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1)
def test_dedriewijzen_5_49(capsys, monkeypatch):
    invoer = ["5.49"]
    verwacht = "€1.25 + €1.80 + €2.44 = €1.25 x €1.80 x €2.44 = €5.49"
    uitvoer = geef_invoer_aan_dedriewijzen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1)
def test_dedriewijzen_30_36(capsys, monkeypatch):
    invoer = ["30.36"]
    verwacht = "€0.46 + €2.40 + €27.50 = €0.46 x €2.40 x €27.50 = €30.36"
    uitvoer = geef_invoer_aan_dedriewijzen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1)
def test_dedriewijzen_98_07(capsys, monkeypatch):
    invoer = ["98.07"]
    verwacht = "€0.05 + €28.02 + €70.00 = €0.05 x €28.02 x €70.00 = €98.07"
    uitvoer = geef_invoer_aan_dedriewijzen_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht
