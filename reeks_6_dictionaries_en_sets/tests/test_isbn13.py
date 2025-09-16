import pytest
from reeks_6_dictionaries_en_sets.isbn13 import overzicht

# --- Hulpfunctie ---
def run_overzicht_geef_stdout_terug(codes, capsys):
    """
    Roept overzicht aan en geeft de standaarduitvoer terug als lijst van regels.
    """
    overzicht(codes)
    captured = capsys.readouterr()
    return captured.out.strip().split('\n')

# --- Testcases ---
@pytest.mark.timeout(1)
def test_overzicht_voorbeeld_uit_opgave(capsys):
    codes = [
        '9789743159664', '9785301556616', '9797668174969', '9781787559554',
        '9780817481461', '9785130738708', '9798810365062', '9795345206033',
        '9792361848797', '9785197570819', '9786922535370', '9791978044523',
        '9796357284378', '9792982208529', '9793509549576', '9787954527409',
        '9797566046955', '9785239955499', '9787769276051', '9789910855708',
        '9783807934891', '9788337967876', '9786509441823', '9795400240705',
        '9787509152157', '9791478081103', '9780488170969', '9795755809220',
        '9793546666847', '9792322242176', '9782582638543', '9795919445653',
        '9796783939729', '9782384928398', '9787590220100', '9797422143460',
        '9798853923096', '9784177414990', '9799562126426', '9794732912038',
        '9787184435972', '9794455619207', '9794270312172', '9783811648340',
        '9799376073039', '9798552650309', '9798485624965', '9780734764010',
        '9783635963865', '9783246924279', '9797449285853', '9781631746260',
        '9791853742292', '9781796458336', '9791260591924', '9789367398012'
    ]
    result = run_overzicht_geef_stdout_terug(codes, capsys)
    expected = [
        "Engelstalige landen: 8",
        "Franstalige landen: 4",
        "Duitstalige landen: 6",
        "Japan: 3",
        "Russischtalige landen: 7",
        "China: 8",
        "Overige landen: 11",
        "Fouten: 9",
    ]
    assert result == expected

@pytest.mark.timeout(1)
def test_overzicht_allemaal_foute_lengte(capsys):
    codes = ['97812345678', '978123456789012', '978123456789']
    result = run_overzicht_geef_stdout_terug(codes, capsys)
    assert result == [
        "Engelstalige landen: 0",
        "Franstalige landen: 0",
        "Duitstalige landen: 0",
        "Japan: 0",
        "Russischtalige landen: 0",
        "China: 0",
        "Overige landen: 0",
        "Fouten: 3"
    ]

@pytest.mark.timeout(1)
def test_overzicht_foutieve_checksum(capsys):
    codes = ['9780306406158']
    result = run_overzicht_geef_stdout_terug(codes, capsys)
    assert result == [
        "Engelstalige landen: 0",
        "Franstalige landen: 0",
        "Duitstalige landen: 0",
        "Japan: 0",
        "Russischtalige landen: 0",
        "China: 0",
        "Overige landen: 0",
        "Fouten: 1"
    ]

@pytest.mark.timeout(1)
def test_overzicht_allemaal_ongeldige_prefix(capsys):
    codes = ['9811234567897', '1234567890123', '0009876543210']
    result = run_overzicht_geef_stdout_terug(codes, capsys)
    assert result == [
        "Engelstalige landen: 0",
        "Franstalige landen: 0",
        "Duitstalige landen: 0",
        "Japan: 0",
        "Russischtalige landen: 0",
        "China: 0",
        "Overige landen: 0",
        "Fouten: 3"
    ]

@pytest.mark.timeout(1)
def test_overzicht_leeg(capsys):
    result = run_overzicht_geef_stdout_terug([], capsys)
    assert result == [
        "Engelstalige landen: 0",
        "Franstalige landen: 0",
        "Duitstalige landen: 0",
        "Japan: 0",
        "Russischtalige landen: 0",
        "China: 0",
        "Overige landen: 0",
        "Fouten: 0"
    ]

@pytest.mark.timeout(1)
def test_overzicht_korte_gemengde_lijst(capsys):
    codes = ['9780306406157', '9782744142559', '9787509152157', '1234567890123']
    result = run_overzicht_geef_stdout_terug(codes, capsys)
    assert result == [
        "Engelstalige landen: 1",
        "Franstalige landen: 0",
        "Duitstalige landen: 0",
        "Japan: 0",
        "Russischtalige landen: 0",
        "China: 1",
        "Overige landen: 0",
        "Fouten: 2"
    ]


@pytest.mark.timeout(1)
def test_overzicht_lange_gemengde_lijst_met_weinig_fouten(capsys):
    codes = [
        '9780366889006', '9780672570865', '9798450230504', '9788075650795',
        '9793896993884', '3120159848302', '9796967664041', '9792310068122',
        '9794583471838', '9799335865217', '9794737769668', '9786535105687',
        '9789440013092', '9796269320898', '2286905006431', '9789409030917',
        '9782565667140', '9794504920599', '9795649925333', '9783831288793',
        '9796334109588', '9791623214691', '9782420104773', '9796342580362',
        '9797707602378', '9793821837016', '9784655126230', '9789392882227',
        '9782784239289', '9782648759014', '9784158992585', '9782845274525',
        '9793065919387', '9788858011409', '9798340741677', '9785708690579',
        '9786486680554', '9789851980563', '9781709021428', '9799262686121',
        '9796673408328', '9782741666844', '9785292594840', '9781793894649',
        '9795639666390', '9788977839502', '9789143167153', '9795511242346',
        '9786034303874', '9792946617466', '9787948612519', '9794456389673',
        '9798069696692', '9787338702592', '9799792509235', '9786315047435',
        '9796207294663', '9799707819046', '9799018596179', '9788436792285',
        '9791761791962'
        ]
    result = run_overzicht_geef_stdout_terug(codes, capsys)
    assert result == [
        "Engelstalige landen: 6",
        "Franstalige landen: 8",
        "Duitstalige landen: 4",
        "Japan: 6",
        "Russischtalige landen: 5",
        "China: 3",
        "Overige landen: 26",
        "Fouten: 3"
    ]

@pytest.mark.timeout(1)
def test_overzicht_lange_gemengde_lijst_met_veel_fouten(capsys):
    codes = [
        '6007564129479', '9796511909345', '9792436588245', '9791237518765',
        '9790751215891', '9782000814726', '9799357263766', '9789009873976',
        '9796236456117', '9795374766874', '9798979270524', '9790392340204',
        '9798824633672', '9794830820297', '9794185238396', '9785615418181',
        '9784681485165', '9797679993061', '1124350246624', '9795954296630',
        '9784686346751', '9784102965405', '9790194571868', '9787575987146',
        '9791366030105', '9793141197838', '3609420838520', '9795928309144',
        '9796312236020', '9786180980479', '9782722157415', '9796520383822',
        '9780761545224', '6197922531423', '9792284559176', '9796013566510',
        '9092224904021', '9797596332493', '9799041872585', '9784486957140',
        '9792432741160', '9784716619312', '9797965887227', '9788485498642',
        '9783333120674', '9783036533414', '9790727766990', '9788239964287',
        '9792229314228', '9780228470717', '9785030490718', '9783632599663',
        '9794145427952', '9793211136781', '9794649073969', '9784535099911',
        '9795886781622', '9787109787230', '9797649762840', '9797880237954',
        '5073889584287', '9781476451688', '9789109387661', '9797219350538',
        '9794682455680', '9791748980839', '9791529189406', '9791203213083',
        '9782642201113', '9780860227366', '9796068432853', '9784720748756',
        '5938033842425', '9783041153423', '9792603770527', '9785830278232',
        '9787389736799', '9792451440122', '9788629356821'
    ]
    result = run_overzicht_geef_stdout_terug(codes, capsys)
    assert result == [
        "Engelstalige landen: 12",
        "Franstalige landen: 8",
        "Duitstalige landen: 4",
        "Japan: 10",
        "Russischtalige landen: 5",
        "China: 8",
        "Overige landen: 13",
        "Fouten: 19"
    ]
