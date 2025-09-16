# Vigenèrecodering

De **Vigenèrecodering** is in de cryptografie één van de klassieke methoden om tekst te versleutelen. De methode werd oorspronkelijk beschreven door Giovanni Batista Bellaso in zijn boek _La cifra del Sig_ uit 1553, maar raakte pas in de 19<sup>e</sup> eeuw algemeen bekend door Blaise de Vigenère, waardoor het zijn naam kreeg.

Om een tekst te versleutelen kiest men eerst een geheim sleutelwoord, bijvoorbeeld ZODIAK. Het sleutelwoord mag enkel bestaan uit hoofdletters (geen spaties), en wordt herhaald totdat een string verkregen wordt met dezelfde lengte als de oorspronkelijke tekst die moet gecodeerd worden (de herhaling wordt hiertoe achteraan afgebroken). Dit herhaalde sleutelwoord schrijft men dan onder de oorspronkelijke tekst.

```
     originele tekst : DIT IS EXTREEM GEHEIM!
                       ++++++++++++++++++++++
        sleutelwoord : ZODIAKZODIAKZODIAKZODI
                       ======================
  versleutelde tekst : CWW IC SABRODA OERDWP!
```

Vervolgens telt men de corresponderende letters uit de originele tekst en
      het sleutelwoord bij elkaar op. Bij deze optelling worden de letters `A`
      tot `Z` beschouwd als de getallen 0 tot 25. De optelling wordt
      uitgevoerd modulo 26 (het aantal letters in het alfabet). De
      Vigenèrecodering kan dus worden geschreven als $$V_i = (O_i + S_i)\
      \mathrm{mod}\ 26\,,$$ waarbij $V_i$ de $i$-de letter uit de
      versleutelde tekst voorstelt, $O_i$ de $i$-de letter uit de originele
      tekst en $S_i$ de $i$-de letter uit het sleutelwoord. Voor de eerste
      letter uit het bovenstaande voorbeeld krijgen we dus $$\mathrm{D} +
      \mathrm{Z} = (3 + 25)\ \mathrm{mod}\ 26 = 2 = \mathrm{C}\,.$$

Om te ontcijferen gebruikt men een gelijkaardige procedure, waarbij een
      letter van het sleutelwoord van de corresponderende letter uit het
      gecodeerde bericht wordt afgetrokken. De Vigenèrecodering kan dus
      worden geschreven als $$O_i = (V_i - S_i)\ \mathrm{mod}\ 26\,.$$

### Opgave

-   Schrijf een functie `codeer` die een gegeven tekst $t$
          (str) versleutelt volgens de Vigenèrecodering op
          basis van een gegeven sleutel $s$ (str) die enkel uit
          hoofdletters bestaat. De originele tekst $t$ en de sleutel $s$
          moeten als argument aan de functie doorgegeven worden. De functie moet
          de versleutelde tekst (str) als resultaat teruggeven.
          Hierbij moeten enkel de hoofdletters uit de originele tekst
          versleuteld worden. Alle overige karakters (kleine letters, spaties,
          cijfers, leestekens, …) blijven ongewijzigd in de gecodeerde
          tekst.
    
-   Schrijf een functie `decodeer` als duale functie van de
          functie `codeer`. Deze functie moet dus een gegeven tekst
          $t$ (str) ontcijferen volgens de
          Vigenèredecodering op basis van een gegeven sleutel $s$ (str)
          die enkel uit hoofdletters bestaat. De versleutelde tekst $t$ en de
          sleutel $s$ moeten als argument aan de functie doorgegeven worden.
          De functie moet de ontcijferde tekst (str) als resultaat
          teruggeven. Hierbij moeten enkel de hoofdletters uit de versleutelde
          tekst ontcijferd worden. Alle overige karakters (kleine letters,
          spaties, cijfers, leestekens, …) blijven ongewijzigd in de
          ontcijferde tekst.
    

### Voorbeeld

```
>>> codeer('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS')
'PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!'

>>> decodeer('PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!', 'CIRCUS')
'NOBODY EXPECTS THE SPANISH INQUISITION!'

>>> codeer('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR')
'OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!'

>>> decodeer('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR')
'OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!'
```