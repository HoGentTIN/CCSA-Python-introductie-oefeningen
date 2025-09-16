# Varkenslatijn

Varkenslatijn (of _Pig Latin_ in het Engels, of _Igpay Atinlay_ in het Varkenslatijn) is een Engels taalspelletje dat vooral populair is bij kinderen. Die gebruiken het als geheimtaal of louter voor de grap. Met Latijn heeft dit taalspelletje niets te maken. De verwijzing naar deze taal is zuiver gebaseerd op de associatie met een vreemde, onbegrijpbare taal.

Het principe van varkenslatijn is eenvoudig. Engelse woorden worden vervormd met behulp van drie eenvoudige regels:

-   Voeg het achtervoegsel -way toe aan woorden die beginnen met een klinker.
    
-   Bij woorden die beginnen met één of meer medeklinkers, worden deze naar het einde van het woord verplaatst. Hieraan wordt het achtervoegsel -ay toegevoegd. Wanneer de letter u voorafgegaan wordt door de letter q, dan wordt die ook als een medeklinker beschouwd.
    
-   Als de eerste letter van het woord een hoofdletter was, dan wordt de eerste letter van het vervormde woord ook omgezet naar een hoofdletter. Als de eerste letter van het woord een medeklinker is en de eerste klinker van het woord is een kleine letter, dan wordt de eerste letter van het woord met een kleine letter geschreven in het vervormde woord. Voor de andere letters blijft het gebruik van hoofdletters en kleine letters behouden.
    

### Opgave

-   Schrijf een functie `varkenswoord` waaraan een (Engels) woord (str) moet doorgegeven worden. Dat woord mag enkel uit letters bestaan. De functie moet de verlatijnste versie van het woord (str) teruggeven volgens de regels van het varkenslatijn. Hou hierbij ook rekening met de regels voor hoofdletters en kleine letters zoals die hierboven beschreven werden.
    
-   Schrijf een functie `varkenslatijn` die een gegeven zin (str) omzet naar zijn verlatijnste versie (str). Hierbij moeten alle individuele woorden verlatijnst worden volgens de regels van het varkenslatijn. Woorden worden daarbij gedefinieerd als de langste mogelijke reeks van letters. Alle karakters van de zin die geen letter zijn (leestekens, cijfers, spaties, …) moeten ongewijzigd overgenomen worden in de verlatijnste versie van de zin.
    

### Voorbeeld

```
>>> varkenswoord('egg')
'eggway'
>>> varkenswoord('Pig')
'Igpay'
>>> varkenswoord('Latin')
'Atinlay'
>>> varkenswoord('trash')
'ashtray'
>>> varkenswoord('quit')
'itquay'
>>> varkenswoord('BaNaNa')
'ANaNabay'
>>> varkenswoord('DNa')
'AdNay'
>>> varkenswoord('plover')
'overplay'
>>> varkenswoord('plunder')
'underplay'

>>> varkenslatijn('And now for something completely different!')
'Andway ownay orfay omethingsay ompletelycay ifferentday!'
>>> varkenslatijn('Stwike him, centuwion, stwike him vewy wuffly')
'Ikestway imhay, entuwioncay, ikestway imhay ewyvay ufflyway'
```