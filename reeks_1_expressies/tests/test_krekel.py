import pytest

def geef_invoer_aan_krekel_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan krekel.py en de uitvoer op te halen.
    """
    import sys
    sys.modules.pop("reeks_1_expressies.krekel", None)  # telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_1_expressies.krekel as krekel

    captured = capsys.readouterr()
    return captured.out.strip().split('\n')

def test_krekel_voorbeeld_opgave(capsys, monkeypatch):
    # Voorbeeld uit de opgave: 18 tsjirpen per 15 seconden
    invoer = ["18"]
    uitvoer = geef_invoer_aan_krekel_return_uitvoer(capsys, monkeypatch, invoer)
    # Controle op beide delen van de outputregel
    assert uitvoer[0].startswith("temperatuur (Fahrenheit): ")
    assert float(uitvoer[0].split(": ")[1]) == pytest.approx(44.5, abs=1e-6)
    assert uitvoer[1].startswith("temperatuur (Celsius): ")
    assert float(uitvoer[1].split(": ")[1]) == pytest.approx(6.857142857142858, abs=1e-6)

def test_krekel_grens_nul_tsjirpen(capsys, monkeypatch):
    # Randgeval: 0 tsjirpen per 15 seconden
    invoer = ["0"]
    uitvoer = geef_invoer_aan_krekel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0].startswith("temperatuur (Fahrenheit): ")
    assert float(uitvoer[0].split(": ")[1]) == pytest.approx(40.0, abs=1e-6)
    assert uitvoer[1].startswith("temperatuur (Celsius): ")
    assert float(uitvoer[1].split(": ")[1]) == pytest.approx(4.285714285714286, abs=1e-6)

def test_krekel_minimaal_een_tsjirp(capsys, monkeypatch):
    # Minimale niet-nul invoer: 1 tsjirp per 15 sec
    invoer = ["1"]
    uitvoer = geef_invoer_aan_krekel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0].startswith("temperatuur (Fahrenheit): ")
    assert float(uitvoer[0].split(": ")[1]) == pytest.approx(40.25, abs=1e-6)
    assert uitvoer[1].startswith("temperatuur (Celsius): ")
    assert float(uitvoer[1].split(": ")[1]) == pytest.approx(4.428571428571429, abs=1e-6)

def test_krekel_typische_waarde(capsys, monkeypatch):
    # Typische waarde binnen bereik
    invoer = ["50"]
    uitvoer = geef_invoer_aan_krekel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0].startswith("temperatuur (Fahrenheit): ")
    assert float(uitvoer[0].split(": ")[1]) == pytest.approx(52.5, abs=1e-6)
    assert uitvoer[1].startswith("temperatuur (Celsius): ")
    assert float(uitvoer[1].split(": ")[1]) == pytest.approx(11.428571428571429, abs=1e-6)

def test_krekel_grote_waarde(capsys, monkeypatch):
    # Grote waarde: 200 tsjirpen per 15 sec
    invoer = ["200"]
    uitvoer = geef_invoer_aan_krekel_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer[0].startswith("temperatuur (Fahrenheit): ")
    assert float(uitvoer[0].split(": ")[1]) == pytest.approx(90.0, abs=1e-6)
    assert uitvoer[1].startswith("temperatuur (Celsius): ")
    assert float(uitvoer[1].split(": ")[1]) == pytest.approx(32.85714285714286, abs=1e-6)
