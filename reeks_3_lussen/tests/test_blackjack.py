def geef_invoer_aan_blackjack_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan blackjack.py en de uitvoer als string op te halen.
    """
    import sys
    sys.modules.pop("reeks_3_lussen.blackjack", None)  # steeds verse import

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_3_lussen.blackjack as blackjack

    captured = capsys.readouterr()
    return captured.out.strip()

def test_blackjack_gewonnen_exact_21(capsys, monkeypatch):
    # Speler haalt exact 21 in drie beurten
    invoer = ["8", "7", "6"]
    uitvoer = geef_invoer_aan_blackjack_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == "Gewonnen!"

def test_blackjack_verbrand_net_over_21(capsys, monkeypatch):
    # Speler haalt boven 21 (22)
    invoer = ["10", "10", "2"]
    uitvoer = geef_invoer_aan_blackjack_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == "Verbrand (22)"

def test_blackjack_voorzichtig_minder_dan_21(capsys, monkeypatch):
    # Speler stopt onder 21 (19), met kaart 0
    invoer = ["9", "6", "3", "1", "0"]
    uitvoer = geef_invoer_aan_blackjack_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == "Voorzichtig gespeeld (19)"

def test_blackjack_direct_stop_na_eerste_kaart(capsys, monkeypatch):
    # Eén kaart en dan meteen stoppen
    invoer = ["7", "0"]
    uitvoer = geef_invoer_aan_blackjack_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == "Voorzichtig gespeeld (7)"

def test_blackjack_verbrand_na_lange_reeks(capsys, monkeypatch):
    # Serie van kleine kaarten eindigt met verbrand
    invoer = ["2", "2", "2", "2", "2", "2", "2", "2", "6"]
    uitvoer = geef_invoer_aan_blackjack_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == "Verbrand (22)"

def test_blackjack_max_kaart_en_stop_onder_21(capsys, monkeypatch):
    # Eén hoge kaart, daarna stoppen met 0
    invoer = ["11", "0"]
    uitvoer = geef_invoer_aan_blackjack_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == "Voorzichtig gespeeld (11)"
