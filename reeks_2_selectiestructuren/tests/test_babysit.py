import pytest

def geef_invoer_aan_babysit_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan babysit.py en de uitvoer als string op te halen.
    """
    import sys
    sys.modules.pop("reeks_2_selectiestructuren.babysit", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))
    import reeks_2_selectiestructuren.babysit as babysit

    captured = capsys.readouterr()
    return captured.out.strip()

def test_babysit_voorbeeld_1_uit_opgave(capsys, monkeypatch):
    # Voorbeeld uit de opgave
    invoer = ["18", "45", "23", "15"]
    verwacht = 12.5
    uitvoer = geef_invoer_aan_babysit_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(verwacht, abs=1e-6)

def test_babysit_voorbeeld_2_uit_opgave(capsys, monkeypatch):
    # Eindtijd voor begintijd: ongeldige invoer
    invoer = ["18", "45", "0", "15"]
    verwacht = "ongeldige invoer"
    uitvoer = geef_invoer_aan_babysit_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_babysit_geldige_volle_uren(capsys, monkeypatch):
    # Begin om 18:00, einde om 21:00 (volledig aan €2/uur)
    invoer = ["18", "0", "21", "0"]
    verwacht = 6.0
    uitvoer = geef_invoer_aan_babysit_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(verwacht, abs=1e-6)

def test_babysit_rand_na_start(capsys, monkeypatch):
    # Kort babysitten net na aanvang (18:00 - 18:15)
    invoer = ["18", "0", "18", "15"]
    verwacht = 0.5
    uitvoer = geef_invoer_aan_babysit_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(verwacht, abs=1e-6)

def test_babysit_grens_naar_duurder_tarief(capsys, monkeypatch):
    # Wissel om exact 21:30
    invoer = ["21", "30", "23", "0"]
    # 21:30-23:00 = 1.5u aan €4/uur: 1.5×4 = 6.0
    verwacht = 6.0
    uitvoer = geef_invoer_aan_babysit_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(verwacht, abs=1e-6)

def test_babysit_gemengd_tarief(capsys, monkeypatch):
    # Start 20:00, eind 22:30 (1.5u aan €2, 1u aan €4)
    invoer = ["20", "0", "22", "30"]
    # 20:00-21:30 = 1.5u × 2 = 3.0; 21:30-22:30 = 1u × 4 = 4.0; totaal = 7.0
    verwacht = 7.0
    uitvoer = geef_invoer_aan_babysit_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(verwacht, abs=1e-6)

def test_babysit_bijna_middernacht(capsys, monkeypatch):
    # Bijna tot middernacht babysitten: 21:00 - 23:59
    invoer = ["21", "0", "23", "59"]
    verwacht = 10.933333333333334  # 1.0 (0.5u à 2 euro) + 9.933... (2.48333u à 4 euro)
    uitvoer = geef_invoer_aan_babysit_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(verwacht, abs=1e-3)

def test_babysit_korte_sessie_na_22u(capsys, monkeypatch):
    # Begin en einde kort na elkaar op dezelfde avond
    invoer = ["22", "42", "22", "46"]
    verwacht = 0.2666666666666657
    uitvoer = geef_invoer_aan_babysit_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(verwacht, abs=1e-6)

def test_babysit_alleen_duur_tarief(capsys, monkeypatch):
    # Sessie volledig binnen duur tarief (tussen 21:30 en middernacht)
    invoer = ["23", "17", "23", "38"]
    verwacht = 1.3999999999999915
    uitvoer = geef_invoer_aan_babysit_return_uitvoer(capsys, monkeypatch, invoer)
    assert float(uitvoer) == pytest.approx(verwacht, abs=1e-6)
