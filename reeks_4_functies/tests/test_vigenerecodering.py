import pytest
from reeks_4_functies.vigenerecodering import codeer, decodeer

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "t, s, verwacht", [
        ('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS', 'PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!'),
        ('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR', 'OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!'),
    ]
)
def test_codeer_opgavevoorbeelden(t, s, verwacht):
    assert codeer(t, s) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "t, s, verwacht", [
        ("STOP! DON'T SAY THE BABY'S NAME!", 'INQUISITION', "AGEJ! LHV'G FQS LPX PNJL'M FIFM!"),
        ("FOUR HOURS TO BURY THE CAT?   YES, IT WOULDN'T KEEP STILL.", 'SUPPOSED', "XIJG ZSXJM IC FXJS IVW FSN?   CHK, XH ARMFSC'L NWYE GLMOD."),
    ]
)
def test_codeer_andere_voorbeelden(t, s, verwacht):
    assert codeer(t, s) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "origineel, sleutel", [
        # codeer gevolgd door decodeer (met zelfde sleutel) geeft altijd de oorspronkelijke input terug
        ("HELLO WORLD! THIS IS A TEST WITH KEY.", "SECRET"),
        ("SOME TEXT WITH CAPITALS AND SYMBOLS?!", "ABC"),
    ]
)
def test_codeer_decodeer_inverse(origineel, sleutel):
    gecodeerd = codeer(origineel, sleutel)
    assert decodeer(gecodeerd, sleutel) == origineel

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "t, s, verwacht", [
        ("PYTHON123!", "KEY", "ZCRRSL123!"),
        ("ABC XYZ", "D", "DEF ABC"),
    ]
)
def test_codeer_korte_voorbeelden(t, s, verwacht):
    assert codeer(t, s) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "t, s, verwacht", [
        ('PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!', 'CIRCUS', 'NOBODY EXPECTS THE SPANISH INQUISITION!'),
        ('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR', 'OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!'),
    ]
)
def test_decodeer_opgavevoorbeelden(t, s, verwacht):
    assert decodeer(t, s) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "t, s, verwacht", [
        ("AGEJ! LHV'G FQS LPX PNJL'M FIFM!", 'INQUISITION', "STOP! DON'T SAY THE BABY'S NAME!"),
        ("XIJG ZSXJM IC FXJS IVW FSN?   CHK, XH ARMFSC'L NWYE GLMOD.", 'SUPPOSED', "FOUR HOURS TO BURY THE CAT?   YES, IT WOULDN'T KEEP STILL."),
    ]
)
def test_decodeer_andere_voorbeelden(t, s, verwacht):
    assert decodeer(t, s) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "t, s, verwacht", [
        ("ZCRRSL123!", "KEY", "PYTHON123!"),
        ("DEF ABC", "D", "ABC XYZ"),
    ]
)
def test_decodeer_kortere_sleutels(t, s, verwacht):
    assert decodeer(t, s) == verwacht

@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "t, s, verwacht", [
        ("UMIG DIVPNXG... UUM FAUIGY MHTB'Y E SHHOGMEOVQ, FHT IA DRVGJTM?", 'DEVASTATING',
         "RING KICHARD... BUT SURELY THAT'S A SPOONERISM, NOT AN ANAGRAM?"),
        ("COMMVKJCR... MEIVPUC, WURX WF VVQ FIKBOYU...", 'COMMERCIAL',
         'AAAARTHUR... AARTHUR, KING OF THE BRITONS...'),
    ]
)
def test_decodeer_langere_sleutels(t, s, verwacht):
    assert decodeer(t, s) == verwacht