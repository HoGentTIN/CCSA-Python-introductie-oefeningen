import pytest
from reeks_4_functies.lawaaidoofheid import maximale_blootstelling


@pytest.mark.parametrize(
    "db", [
        40,    # Gevallen onder 80 dB: onbeperkte blootstellingsduur (=-1)
        60,
        75,
        79.8
    ]
)
def test_lawaaidoofheid_lager_dan_80db_geen_risico(db):
    assert maximale_blootstelling(db) == -1.0

def test_lawaaidoofheid_80db_max_8_uur():
    # Geluidsniveau van exact 80 dB → 8 uur = 28800 seconden
    assert maximale_blootstelling(80) == 28800.0

def test_lawaaidoofheid_82_9db_nog_8_uur():
    # Geluidsniveau van 82.9 dB → nog steeds binnen 80–83 dB → 8 uur
    assert maximale_blootstelling(82.9) == 28800.0

def test_lawaaidoofheid_83_0db_max_4_uur():
    # Geluidsniveau van precies 83.0 dB → 4 uur (halveertijd van 8 uur)
    assert maximale_blootstelling(83.0) == 14400.0

def test_lawaaidoofheid_86db_max_2_uur():
    # Geluidsniveau van 86 dB → 2 uur = 7200 seconden
    assert maximale_blootstelling(86) == 7200.0

def test_lawaaidoofheid_90db_max_1_uur():
    # Geluidsniveau van 90 dB → 1 uur = 3600 seconden
    assert maximale_blootstelling(90) == 3600.0

@pytest.mark.parametrize(
    "db", [
        95,    # Geluidsniveau van 95 dB → 15 minuten = 900 seconden
        97,    # Geluidsniveau van 97 dB → valt in zelfde interval als 95 dB → 15 minuten
    ]
)
def test_lawaaidoofheid_95db_en_97db_max_15_min(db):
    assert maximale_blootstelling(db) == 900.0

def test_lawaaidoofheid_118db_max_7_seconden():
    # Geluidsniveau van 118 dB → 7.03125 seconden
    assert pytest.approx(maximale_blootstelling(118), rel=1e-6) == 7.03125
