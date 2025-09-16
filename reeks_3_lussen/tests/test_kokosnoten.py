import pytest

def geef_invoer_aan_kokosnoten_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan kokosnoten.py en de uitvoer als lijst van regels op te halen.
    """
    import sys
    sys.modules.pop("reeks_3_lussen.kokosnoten", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_3_lussen.kokosnoten as kokosnoten

    captured = capsys.readouterr()
    return captured.out.strip().split('\n')


@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_kokosnoten_opgavevoorbeeld_5_piraten(capsys, monkeypatch):
    # Voorbeeld uit de opgave: 5 piraten, 3121 kokosnoten
    invoer = ["5", "3121"]
    uitvoer = geef_invoer_aan_kokosnoten_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "3121 noten = 624 noten voor piraat#1 en 1 noot voor de aap",
        "2496 noten = 499 noten voor piraat#2 en 1 noot voor de aap",
        "1996 noten = 399 noten voor piraat#3 en 1 noot voor de aap",
        "1596 noten = 319 noten voor piraat#4 en 1 noot voor de aap",
        "1276 noten = 255 noten voor piraat#5 en 1 noot voor de aap",
        "elke piraat krijgt 204 noten en geen noten voor de aap",
    ]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_kokosnoten_opgavevoorbeeld_4_piraten(capsys, monkeypatch):
    # Tweede voorbeeld uit de opgave: 4 piraten, 1234 kokosnoten
    invoer = ["4", "1234"]
    uitvoer = geef_invoer_aan_kokosnoten_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "1234 noten = 308 noten voor piraat#1 en 2 noten voor de aap",
        "924 noten = 231 noten voor piraat#2 en geen noten voor de aap",
        "693 noten = 173 noten voor piraat#3 en 1 noot voor de aap",
        "519 noten = 129 noten voor piraat#4 en 3 noten voor de aap",
        "elke piraat krijgt 96 noten en 3 noten voor de aap",
    ]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_kokosnoten_veel_kokosnoten_5_piraten_geen_over(capsys, monkeypatch):
    # Test met 5 piraten en veel kokosnoten (80968827)
    invoer = ["5", "80968827"]
    uitvoer = geef_invoer_aan_kokosnoten_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "80968827 noten = 16193765 noten voor piraat#1 en 2 noten voor de aap",
        "64775060 noten = 12955012 noten voor piraat#2 en geen noten voor de aap",
        "51820048 noten = 10364009 noten voor piraat#3 en 3 noten voor de aap",
        "41456036 noten = 8291207 noten voor piraat#4 en 1 noot voor de aap",
        "33164828 noten = 6632965 noten voor piraat#5 en 3 noten voor de aap",
        "elke piraat krijgt 5306372 noten en geen noten voor de aap"
    ]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_kokosnoten_veel_kokosnoten_6_piraten_4_over(capsys, monkeypatch):
    # Test met 6 piraten en veel kokosnoten (214622281)
    invoer = ["6", "214622281"]
    uitvoer = geef_invoer_aan_kokosnoten_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "214622281 noten = 35770380 noten voor piraat#1 en 1 noot voor de aap",
        "178851900 noten = 29808650 noten voor piraat#2 en geen noten voor de aap",
        "149043250 noten = 24840541 noten voor piraat#3 en 4 noten voor de aap",
        "124202705 noten = 20700450 noten voor piraat#4 en 5 noten voor de aap",
        "103502250 noten = 17250375 noten voor piraat#5 en geen noten voor de aap",
        "86251875 noten = 14375312 noten voor piraat#6 en 3 noten voor de aap",
        "elke piraat krijgt 11979426 noten en 4 noten voor de aap"
    ]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_kokosnoten_veel_kokosnoten_7_piraten_geen_over(capsys, monkeypatch):
    # Test met 7 piraten en veel kokosnoten (823537)
    invoer = ["7", "823537"]
    uitvoer = geef_invoer_aan_kokosnoten_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "823537 noten = 117648 noten voor piraat#1 en 1 noot voor de aap",
        "705888 noten = 100841 noten voor piraat#2 en 1 noot voor de aap",
        "605046 noten = 86435 noten voor piraat#3 en 1 noot voor de aap",
        "518610 noten = 74087 noten voor piraat#4 en 1 noot voor de aap",
        "444522 noten = 63503 noten voor piraat#5 en 1 noot voor de aap",
        "381018 noten = 54431 noten voor piraat#6 en 1 noot voor de aap",
        "326586 noten = 46655 noten voor piraat#7 en 1 noot voor de aap",
        "elke piraat krijgt 39990 noten en geen noten voor de aap"
    ]

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_kokosnoten_veel_kokosnoten_5_piraten_1_over(capsys, monkeypatch):
    # Test met 5 piraten en veel kokosnoten (16545472)
    invoer = ["5", "16545472"]
    uitvoer = geef_invoer_aan_kokosnoten_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == [
        "16545472 noten = 3309094 noten voor piraat#1 en 2 noten voor de aap",
        "13236376 noten = 2647275 noten voor piraat#2 en 1 noot voor de aap",
        "10589100 noten = 2117820 noten voor piraat#3 en geen noten voor de aap",
        "8471280 noten = 1694256 noten voor piraat#4 en geen noten voor de aap",
        "6777024 noten = 1355404 noten voor piraat#5 en 4 noten voor de aap",
        "elke piraat krijgt 1084323 noten en 1 noot voor de aap"
    ]