def geef_invoer_aan_pudding_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan pudding.py en de uitvoer op te halen.
    """
    import sys
    sys.modules.pop("reeks_1_expressies.pudding", None) # zorg ervoor dat de module bij elke test opnieuw geladen wordt
    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))
    import reeks_1_expressies.pudding as pudding
    captured = capsys.readouterr()
    return captured.out.strip() # retourneert de output als string

def test_pudding_voorbeeld_1(capsys, monkeypatch):
    invoer = ["200", "0.70", "12", "550"]
    verwacht = "Phillips spendeerde $140.0 voor 8800 frequent flyer mijlen."
    resultaat = geef_invoer_aan_pudding_return_uitvoer(capsys, monkeypatch, invoer)
    assert resultaat == verwacht


def test_pudding_voorbeeld_2(capsys, monkeypatch):
    invoer = ["12000", "0.25", "10", "1000"]
    verwacht = "Phillips spendeerde $3000.0 voor 1200000 frequent flyer mijlen."
    resultaat = geef_invoer_aan_pudding_return_uitvoer(capsys, monkeypatch, invoer)
    assert resultaat == verwacht


def test_pudding_randgeval(capsys, monkeypatch):
    # Randgeval: aantal gekocht net niet voldoende voor extra coupon
    inputs = ["11", "1.50", "6", "500"]
    uitvoer = geef_invoer_aan_pudding_return_uitvoer(capsys, monkeypatch, inputs)
    assert uitvoer == "Phillips spendeerde $16.5 voor 500 frequent flyer mijlen."

def test_pudding_grote_getallen(capsys, monkeypatch):
    # Grote getallen als invoer
    inputs = ["100000", "0.99", "4", "100"]
    uitvoer = geef_invoer_aan_pudding_return_uitvoer(capsys, monkeypatch, inputs)
    assert uitvoer == "Phillips spendeerde $99000.0 voor 2500000 frequent flyer mijlen."

def test_pudding_niets_gekocht(capsys, monkeypatch):
    # Geen pudding gekocht: geen kosten, geen mijlen
    inputs = ["0", "1.50", "6", "500"]
    uitvoer = geef_invoer_aan_pudding_return_uitvoer(capsys, monkeypatch, inputs)
    assert uitvoer == "Phillips spendeerde $0.0 voor 0 frequent flyer mijlen."

def test_pudding_nog_geen_coupon(capsys, monkeypatch):
    # Minder gekocht dan nodig voor 1 coupon: geen mijlen
    inputs = ["4", "2.15", "5", "50"]
    uitvoer = geef_invoer_aan_pudding_return_uitvoer(capsys, monkeypatch, inputs)
    assert uitvoer == "Phillips spendeerde $8.6 voor 0 frequent flyer mijlen."

def test_pudding_precies_een_coupon(capsys, monkeypatch):
    # Exact genoeg gekocht voor 1 coupon
    inputs = ["5", "2.00", "5", "100"]
    uitvoer = geef_invoer_aan_pudding_return_uitvoer(capsys, monkeypatch, inputs)
    assert uitvoer == "Phillips spendeerde $10.0 voor 100 frequent flyer mijlen."

def test_pudding_gratis(capsys, monkeypatch):
    # Gratis pudding, toch mijlen sparen
    inputs = ["10", "0", "5", "100"]
    uitvoer = geef_invoer_aan_pudding_return_uitvoer(capsys, monkeypatch, inputs)
    assert uitvoer == "Phillips spendeerde $0.0 voor 200 frequent flyer mijlen."

def test_pudding_onder_coupon_1_pudding(capsys, monkeypatch):
    # Slechts 1 pudding, terwijl je er meer nodig hebt voor een coupon
    inputs = ["1", "3.00", "5", "90"]
    uitvoer = geef_invoer_aan_pudding_return_uitvoer(capsys, monkeypatch, inputs)
    assert uitvoer == "Phillips spendeerde $3.0 voor 0 frequent flyer mijlen."
