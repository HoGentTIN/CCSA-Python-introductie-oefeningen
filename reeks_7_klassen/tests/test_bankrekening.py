from reeks_7_klassen.bankrekening import BankRekening

# --- Tests voor __init__, storten, afhalen, __str__, __repr__ met voorbeelden uit de opgave ---

def test_bankrekening_init_str_afhalen_storten_voorbeeld1_uit_opgave():
    b1 = BankRekening('Jan Jansen', '001457894501', 10000)
    b2 = BankRekening('Peter Peeters', '842457894511', 10000)
    b1.storten(250)
    b1.afhalen(1000)
    b2.afhalen(300)
    assert str(b1) == 'Jan Jansen, 001457894501, bedrag: 9250'
    assert str(b2) == 'Peter Peeters, 842457894511, bedrag: 9700'
    assert repr(b2) == "BankRekening('Peter Peeters', '842457894511', 9700)"

def test_bankrekening_repr_voorbeeld2_uit_opgave():
    b3 = BankRekening('David Davidse', '002457896312')
    b3.storten(112)
    assert str(b3) == 'David Davidse, 002457896312, bedrag: 112'
    assert repr(b3) == "BankRekening('David Davidse', '002457896312', 112)"

# --- Uitgebreid testscenario: storten, afhalen, negatief saldo ---

def test_bankrekening_meerdere_bewerkingen():
    b1 = BankRekening('Kasper Kaspers', '11111111', 10000)
    b1.storten(741)
    assert str(b1) == 'Kasper Kaspers, 11111111, bedrag: 10741'
    b1.afhalen(10741)
    assert str(b1) == 'Kasper Kaspers, 11111111, bedrag: 0'
    b1.afhalen(200)
    assert str(b1) == 'Kasper Kaspers, 11111111, bedrag: -200'
    b1.storten(500)
    assert str(b1) == 'Kasper Kaspers, 11111111, bedrag: 300'
    assert repr(b1) == "BankRekening('Kasper Kaspers', '11111111', 300)"

# --- Randgeval: standaard initieel bedrag (0) ---

def test_bankrekening_init_standaardwaarde():
    b4 = BankRekening('Eva Even', '987654321')
    assert str(b4) == 'Eva Even, 987654321, bedrag: 0'
    b4.storten(1)
    assert str(b4) == 'Eva Even, 987654321, bedrag: 1'
    assert repr(b4) == "BankRekening('Eva Even', '987654321', 1)"
