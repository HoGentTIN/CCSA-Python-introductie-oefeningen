def geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan vierkaartenprobleem.py en de uitvoer als string op te halen.
    """
    import sys
    sys.modules.pop("reeks_2_selectiestructuren.vierkaartenprobleem", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_2_selectiestructuren.vierkaartenprobleem as vierkaartenprobleem

    captured = capsys.readouterr()
    return captured.out.strip()

def test_vierkaartenprobleem_waarde_oneven_ja_fout(capsys, monkeypatch):
    # waarde, 3, speler zegt ja (fout)
    invoer = ["waarde", "3", "ja"]
    verwacht = "Fout: kaarten met waarde 3 moeten niet gedraaid worden."
    uitvoer = geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_vierkaartenprobleem_waarde_oneven_nee_juist(capsys, monkeypatch):
    # waarde, 3, speler zegt nee (juist)
    invoer = ["waarde", "3", "nee"]
    verwacht = "Juist: kaarten met waarde 3 moeten niet gedraaid worden."
    uitvoer = geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_vierkaartenprobleem_waarde_even_ja_juist(capsys, monkeypatch):
    # waarde, 8, speler zegt ja (juist)
    invoer = ["waarde", "8", "ja"]
    verwacht = "Juist: kaarten met waarde 8 moeten gedraaid worden."
    uitvoer = geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_vierkaartenprobleem_waarde_even_nee_fout(capsys, monkeypatch):
    # waarde, 2, speler zegt nee (fout)
    invoer = ["waarde", "2", "nee"]
    verwacht = "Fout: kaarten met waarde 2 moeten gedraaid worden."
    uitvoer = geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_vierkaartenprobleem_waarde_groot_even_juist(capsys, monkeypatch):
    # waarde, 1000, speler zegt ja (juist)
    invoer = ["waarde", "1000", "ja"]
    verwacht = "Juist: kaarten met waarde 1000 moeten gedraaid worden."
    uitvoer = geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_vierkaartenprobleem_kleur_rood_nee_juist(capsys, monkeypatch):
    # kleur, rood, speler zegt nee (juist)
    invoer = ["kleur", "rood", "nee"]
    verwacht = "Juist: kaarten met kleur rood moeten niet gedraaid worden."
    uitvoer = geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_vierkaartenprobleem_kleur_rood_ja_fout(capsys, monkeypatch):
    # kleur, rood, speler zegt ja (fout)
    invoer = ["kleur", "rood", "ja"]
    verwacht = "Fout: kaarten met kleur rood moeten niet gedraaid worden."
    uitvoer = geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_vierkaartenprobleem_kleur_bruin_nee_fout(capsys, monkeypatch):
    # kleur, bruin, speler zegt nee (fout)
    invoer = ["kleur", "bruin", "nee"]
    verwacht = "Fout: kaarten met kleur bruin moeten gedraaid worden."
    uitvoer = geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_vierkaartenprobleem_kleur_groen_ja_juist(capsys, monkeypatch):
    # kleur, groen, speler zegt ja (juist)
    invoer = ["kleur", "groen", "ja"]
    verwacht = "Juist: kaarten met kleur groen moeten gedraaid worden."
    uitvoer = geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

def test_vierkaartenprobleem_kleur_roze_nee_fout(capsys, monkeypatch):
    # kleur, roze, speler zegt nee (fout)
    invoer = ["kleur", "roze", "nee"]
    verwacht = "Fout: kaarten met kleur roze moeten gedraaid worden."
    uitvoer = geef_invoer_aan_vierkaartenprobleem_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht