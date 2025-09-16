# ISBN-13

Binnen het ISBN-13 (_International Standard Book Numbering_) systeem krijgt elk boek een unieke code toegewezen die bestaat uit 13 cijfers. De eerste 12 daarvan geven informatie over het boek zelf, terwijl het laatste louter een controlecijfer is dat dient om foutieve ISBN-13 codes te detecteren.

<img src=../img/isbn13dual.gif alt="ISBN-13" width="400">\
<sub>Voorbeeld van een ISBN-13 nummer en equivalente streepjescode. Bron afbeelding: [ActiveBarcode](https://www.activebarcode.com/codes/isbn13dual).</sub>


Als $x_1, \ldots, x_{12}$ de eerste 12 cijfers van een ISBN-13 code voorstellen, dan wordt het controlecijfer $x_{13}$ als volgt berekend: 

$$\begin{align} o = x_1 + x_3 + x_5 + x_7 + x_9 + x_{11} \\
      e = x_2 + x_4 + x_6 + x_8 + x_{10} + x_{12} \\ x_{13} = (10 - (o
      + 3e)\!\!\!\!\mod{10})\!\!\!\!\!\mod{10}\end{align}$$

Een ISBN-13 code is tegelijkertijd ook een EAN-13 code. De **Europese artikelnummering** (EAN) is een streepjescode die wereldwijd wordt toegepast als artikelcodering in winkels ten behoeve van kassa-afhandeling en voorraadadministratie. Enkel de EAN-13 codes die starten met 978 en 979 zijn gereserveerd voor ISBN-13 codes. Dit betekent dus dat een ISBN-13 code enkel geldig is als ze begint met 978 en 979. Het vierde cijfer identificeert het land waar het boek gepubliceerd is. Landen met dezelfde taal worden hierin gegroepeerd. Hieronder vind je een overzicht van deze groepen.

| groepsidentifier | registratiegroep |
| --- | --- |
| 0, 1 | Engelstalige landen |
| 2 | Franstalige landen |
| 3 | Duitstalige landen |
| 4 | Japan |
| 5 | Russischtalige landen |
| 7 | China |
| 6, 8, 9 | Overige landen |

### Opgave

Schrijf een functie `overzicht` waaraan een lijst (list) van strings (str) moet doorgegeven worden. Deze strings stellen ISBN-13 codes voor. De functie moet een overzicht **uitschrijven** dat de verdeling weergeeft van de lijst van ISBN-13 codes over de verschillende registratiegroepen. Ongeldige ISBN-13 codes moeten in het overzicht opgenomen worden onder de categorie Fouten. Gebruik de namen van de registratiegroepen en handhaaf hun volgorde zoals ze in onderstaand voorbeeld weergegeven worden. Registratiegroepen waarvoor geen ISBN-13 codes in de lijst voorkomen, moeten ook in het overzicht opgenomen worden (met 0 voorkomens).

### Voorbeeld

```
>>> codes = [
...    '9789743159664', '9785301556616', '9797668174969', '9781787559554',
...    '9780817481461', '9785130738708', '9798810365062', '9795345206033', 
...    '9792361848797', '9785197570819', '9786922535370', '9791978044523', 
...    '9796357284378', '9792982208529', '9793509549576', '9787954527409', 
...    '9797566046955', '9785239955499', '9787769276051', '9789910855708', 
...    '9783807934891', '9788337967876', '9786509441823', '9795400240705', 
...    '9787509152157', '9791478081103', '9780488170969', '9795755809220', 
...    '9793546666847', '9792322242176', '9782582638543', '9795919445653', 
...    '9796783939729', '9782384928398', '9787590220100', '9797422143460', 
...    '9798853923096', '9784177414990', '9799562126426', '9794732912038', 
...    '9787184435972', '9794455619207', '9794270312172', '9783811648340', 
...    '9799376073039', '9798552650309', '9798485624965', '9780734764010', 
...    '9783635963865', '9783246924279', '9797449285853', '9781631746260', 
...    '9791853742292', '9781796458336', '9791260591924', '9789367398012' 
... ]
>>> overzicht(codes)
Engelstalige landen: 8
Franstalige landen: 4
Duitstalige landen: 6
Japan: 3
Russischtalige landen: 7
China: 8
Overige landen: 11
Fouten: 9
```