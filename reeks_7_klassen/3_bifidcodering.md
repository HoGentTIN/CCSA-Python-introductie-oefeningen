# Bifidcodering 

Bifidcodering is een klassieke handmatige coderingstechniek, ontwikkeld rond 1901 door Felix Delastelle. Ze combineert substitutie en fractionering via een vierkant rooster waarin alle mogelijke symbolen uit de tekst voorkomen.

Bijvoorbeeld, in onderstaand 9×9-rooster staat elk symbool op een unieke rij- en kolompositie (rijen en kolommen worden genummerd vanaf 0). Een spatie staat bv. op rij 6, kolom 8.

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| **0** | A | B | C | D | E | F | G | H | I |
| **1** | J | K | L | M | N | O | P | Q | R |
| **2** | S | T | U | V | W | X | Y | Z | 0 |
| **3** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| **4** | a | b | c | d | e | f | g | h | i |
| **5** | j | k | l | m | n | o | p | q | r |
| **6** | s | t | u | v | w | x | y | z |  |
| **7** | . | , | ; | : | ? | ! | " | ' | - |
| **8** | ( | ) | [ | ] | { | } | $ | = | % |

#### Coderen

Om een tekst te coderen met bifidcodering:

1. Bepaal voor elk symbool de rij- en kolompositie in het rooster.
2. Schrijf alle rijnummers en kolomnummers verticaal onder de corresponderende symbolen van de originele tekst. 

    Voorbeeld:
    ```
    originele tekst:  T h i s   i s   a   d e a d   p a r r o t !
                    -------------------------------------------
                rij:  2 4 4 6 6 4 6 6 4 6 4 4 4 4 6 5 4 5 5 5 6 7
              kolom:  1 7 8 0 8 8 0 8 0 8 3 4 0 3 8 6 0 8 8 5 1 5
    ```
3. Schrijf de cijfers achter elkaar: eerst alle rijnummers, dan alle kolomnummers.

    Voor het voorbeeld:
    ```
    2 4 4 6 6 4 6 6 ... 5 5 6 7 1 7 8 0 ... 8 6 0 8 8 5 1 5
    ```

4. Vorm paren van deze cijfers en vertaal elk paar terug naar een symbool in het rooster.

    Voor het voorbeeld:   
    ```
    2|4 4|6 6|4 6|6 ... 5|5 6|7 1|7 8|0 ... 8|6 0|8 8|5 1|5
    W   g   w   y       o   z   Q   (       $   I   }   O
    ```

Op die manier werd geïllustreerd hoe de originele tekst _This is a dead parrot!_ volgens de bifidcodering wordt omgezet in de gecodeerde tekst _WgwygeexfozQ(%II5D$I}O_. 

#### Decoderen

Voor decodering van een gecodeerd tekstbericht moet de omgekeerde bewerking uitgevoerd worden.

### Opgave

Implementeer een klasse `Bifid` met de volgende functionaliteit:

- **`__init__(self, n, symbolen)`**  
  Initialiseert een bifidcodering met een rooster van grootte `n × n` voor de symbolen in de string `symbolen`. Controleer dat `2 <= n <= 10` en dat het aantal symbolen exact `n²` is.  
  Geef een `AssertionError` met melding `er moet gelden dat 2 <= n <= 10`, respectievelijk `aantal symbolen komt niet overeen met grootte van het rooster` als dit niet het geval is.

- **`symbool(self, rij, kolom)`**  
  Geeft het symbool op de opgegeven positie in het rooster.  
  Geef een `AssertionError` met melding `ongeldige positie in rooster` bij een ongeldige positie.

- **`positie(self, symbool)`**  
  Geeft een tuple `(rij, kolom)` van het symbool in het rooster.  
  Geef een `AssertionError` met melding `symbool moet uit 1 karakter bestaan` als het symbool niet exact één karakter is of melding `onbekend symbool: '<symbool>'` als het symbool niet voorkomt in het rooster.

- **`codeer(self, tekst)`**  
  Geeft de bifid-gecodeerde versie van de opgegeven tekst terug.

- **`decodeer(self, code)`**  
  Geeft de oorspronkelijke versie van de gegeven gecodeerde tekst terug.

Gebruik het rooster dat werd opgegeven bij het aanmaken van het `Bifid`-object voor zowel coderen als decoderen.

### Voorbeeld

```
>>> codeerder = Bifid(9, ('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdef' 
                    'ghijklmnopqrstuvwxyz .,;:?!"\'-()[]{}$=%'))

>>> codeerder.symbool(2, 1)
'T'
>>> codeerder.symbool(7, 10)
Traceback (most recent call last):
AssertionError: ongeldige positie in rooster

>>> codeerder.positie('T')
(2, 1)
>>> codeerder.positie('FOUT')
Traceback (most recent call last):
AssertionError: symbool moet uit 1 karakter bestaan
>>> codeerder.positie('~')
Traceback (most recent call last):
AssertionError: onbekend symbool: '~'

>>> codeerder.codeer('This is a dead parrot!')
'WgwygeexfozQ(%II5D$I}O'
>>> codeerder.decodeer('WgwygeexfozQ(%II5D$I}O')
'This is a dead parrot!'

>>> codeerder = Bifid(20, '...')
Traceback (most recent call last):
AssertionError: er moet gelden dat 2 <= n <= 10
>>> codeerder = Bifid(3, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
Traceback (most recent call last):
AssertionError: aantal symbolen komt niet overeen met grootte van het rooster
```