import pytest
from reeks_4_functies.bigmacindex import waardering, wisselkoersanalyse

def test_waardering_voorbeeld_opgave():
    # Voorbeeld uit de opgave: Europa (zie 3_bigmacindex.md)
    assert waardering(3.44, 0.70) == "overgewaardeerd"

@pytest.mark.parametrize(
    "prijs, koers, verwacht", [
        # Sterk ondergewaardeerd (v <= -25)
        (2.39, 1.63, "sterk ondergewaardeerd"),                     # Sterk ondergewaardeerd
        (75.0, 28.8, "sterk ondergewaardeerd"),                     # NT dollar, Taiwan
        # Ondergewaardeerd (-25 < v <= -5)
        (8.63, 2.80, "ondergewaardeerd"),                           # zloty, Polen
        (10.0, 2.74, "ondergewaardeerd"),                           # sol, Peru
        # Ongeveer gelijk (-5 < v <= 5)
        (1850, 463, "ongeveer gelijk"),                             # peso, Chili
        (760, 188, "ongeveer gelijk"),                              # forint, Hongarije
        # Overgewaardeerd (5 < v <= 25)
        (3.44, 0.70, "overgewaardeerd"),                            # eurozone
        (4.73, 0.95, "overgewaardeerd"),                            # canadian dollar, Canada
        # Sterk overgewaardeerd (v > 25)
        (9.50, 1.54, "sterk overgewaardeerd"),                      # real, Brazilië
        (28.5, 5.20, "sterk overgewaardeerd"),                      # danish crown, Denemarken
    ]
)
def test_waardering_alle_mogelijke_resultaten(prijs, koers, verwacht):
    assert waardering(prijs, koers) == verwacht

@pytest.mark.parametrize(
    "prijs, koers, verwacht", [
        (3.04843, 1, "sterk ondergewaardeerd"),    # v = -25,1  → sterk ondergewaardeerd
        (6.11314, 2, "ondergewaardeerd"),          # v = -24,9  → ondergewaardeerd
        (11.58729, 3, "ondergewaardeerd"),         # v = -5,1   → ondergewaardeerd
        (15.48228, 4, "ongeveer gelijk"),          # v = -4,9   → ongeveer gelijk
        (21.38785, 5, "overgewaardeerd"),          # v = 5,1    → overgewaardeerd
        (40.73256, 8, "sterk overgewaardeerd"),    # v = 25,1   → sterk overgewaardeerd
    ]
)
def test_waardering_grenswaarden_afrondingsveilig(prijs, koers, verwacht):
    assert waardering(prijs, koers) == verwacht

def test_wisselkoersanalyse_euro_voorbeeld_opgave():
    # Voorbeeld uit de opgave (zie 3_bigmacindex.md)
    assert wisselkoersanalyse('3.44 euro', 0.70) == "De euro is overgewaardeerd ten opzichte van de dollar."

import pytest

@pytest.mark.parametrize(
    "prijs_en_eenheid, koers, verwacht", [
        ('2.39 pond sterling', 1.63, "De pond sterling is sterk ondergewaardeerd ten opzichte van de dollar."),
        ('84.0 rupee', 44.4, "De rupee is sterk ondergewaardeerd ten opzichte van de dollar."),
        ('75.0 NT dollar', 28.8, "De NT dollar is sterk ondergewaardeerd ten opzichte van de dollar."),
        ('10.0 sol', 2.74, "De sol is ondergewaardeerd ten opzichte van de dollar."),
        ('1850 peso', 463, "De peso is ongeveer gelijk ten opzichte van de dollar."),
        ('760 forint', 188, "De forint is ongeveer gelijk ten opzichte van de dollar."),
        ('4.73 canadian dollar', 0.95, "De canadian dollar is overgewaardeerd ten opzichte van de dollar."),
        ('15.9 shekel', 3.40, "De shekel is overgewaardeerd ten opzichte van de dollar."),
        ('5.10 NZ dollar', 1.16, "De NZ dollar is overgewaardeerd ten opzichte van de dollar."),
        ('9.50 real', 1.54, "De real is sterk overgewaardeerd ten opzichte van de dollar."),
        ('28.5 danish crown', 5.20, "De danish crown is sterk overgewaardeerd ten opzichte van de dollar."),
        ('6.50 swiss franc', 0.81, "De swiss franc is sterk overgewaardeerd ten opzichte van de dollar."),
    ]
)
def test_wisselkoersanalyse_alle_mogelijke_resultaten(prijs_en_eenheid, koers, verwacht):
    assert wisselkoersanalyse(prijs_en_eenheid, koers) == verwacht
