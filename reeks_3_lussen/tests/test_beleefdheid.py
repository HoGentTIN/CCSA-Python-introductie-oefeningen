import pytest

def geef_invoer_aan_beleefdheid_return_uitvoer(capsys, monkeypatch, inputs):
    """
    Hulpfunctie om invoer te geven aan beleefdheid.py en de uitvoer als string op te halen.
    """
    import sys
    sys.modules.pop("reeks_3_lussen.beleefdheid", None)  # module telkens opnieuw laden

    invoer_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda: next(invoer_iter))

    import reeks_3_lussen.beleefdheid as beleefdheid

    captured = capsys.readouterr()
    return captured.out.strip()

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_beleefdheid_voorbeeld_uit_opgavetekst(capsys, monkeypatch):
    # Voorbeeld uit de opgave
    invoer = ["15"]
    verwacht = "3"
    uitvoer = geef_invoer_aan_beleefdheid_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_beleefdheid_macht_van_twee_niet_beleefd(capsys, monkeypatch):
    # Onbeleefd, macht van twee: 16
    invoer = ["16"]
    verwacht = "0"
    uitvoer = geef_invoer_aan_beleefdheid_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_beleefdheid_grote_beleefdheid(capsys, monkeypatch):
    # Hoog beleefd getal: 3717 (11 manieren)
    invoer = ["3717"]
    verwacht = "11"
    uitvoer = geef_invoer_aan_beleefdheid_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_beleefdheid_klein_onbeleefd(capsys, monkeypatch):
    # Klein getal dat niet beleefd is: 2
    invoer = ["2"]
    verwacht = "0"
    uitvoer = geef_invoer_aan_beleefdheid_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_beleefdheid_grote_onbeleefde_macht_van_twee(capsys, monkeypatch):
    # Grote macht van twee: 512
    invoer = ["512"]
    verwacht = "0"
    uitvoer = geef_invoer_aan_beleefdheid_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_beleefdheid_enkelvoudige_beleefdheid(capsys, monkeypatch):
    # Slechts één som mogelijk: 5099 → 1
    invoer = ["5099"]
    verwacht = "1"
    uitvoer = geef_invoer_aan_beleefdheid_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_beleefdheid_groot_heel_beleefd(capsys, monkeypatch):
    # Zeer hoge beleefdheid: 8385 → 15
    invoer = ["8385"]
    verwacht = "15"
    uitvoer = geef_invoer_aan_beleefdheid_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht

@pytest.mark.timeout(1) # mag niet langer dan 1 seconde duren
def test_beleefdheid_klein_beleefd(capsys, monkeypatch):
    # Klein beleefd getal: 9
    invoer = ["9"]
    verwacht = "2"
    uitvoer = geef_invoer_aan_beleefdheid_return_uitvoer(capsys, monkeypatch, invoer)
    assert uitvoer == verwacht
