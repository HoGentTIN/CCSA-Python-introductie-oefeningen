# Autogram

Autogrammen (Grieks: αὐτός = zelf, γράμμα = letter) zijn zinnen die zichzelf beschrijven, in die zin dat ze een inventaris maken van hun eigen letters. Essentieel bij het opstellen van autogrammen is het gebruik van voluit geschreven hoofdtelwoorden zoals "een", "twee", … bij het neerschrijven van de letterfrequenties. Hieronder een voorbeeld dat bedacht werd door Rudy Kousbroek:

> Dit pangram bevat vijf a's, twee b's, twee c's, drie d's, zesenveertig e's, vijf f's, vier g's, twee h's, vijftien i's, vier j's, een k, twee l's, twee m's, zeventien n's, een o, twee p's, een q, zeven r's, vierentwintig s's, zestien t's, een u, elf v's, acht w's, een x, een y, en zes z's.

Het is ontzettend moeilijk om een autogram te maken, omdat de zin die moet beschreven worden onbekend is totdat de omschrijving zelf voltooid is. 

### Opgave

-   Schrijf een functie `letterfrequenties` waaraan een string (str) moet doorgegeven worden. De functie moet een dictionary (dict) teruggeven die elke letter (str) die voorkomt in de gegeven zin afbeeldt op het aantal voorkomens (int) van die letter in de zin. Hierbij mag de functie bij het tellen van de letters geen onderscheid maken tussen hoofdletters en kleine letters, en moeten alle sleutels van de dictionary kleine letters zijn. Alle karakters uit de gegeven zin die geen letter zijn, moeten genegeerd worden bij het opstellen van de dictionary.
    
-   Schrijf een functie `letterposities` waaraan een string (str) moet doorgegeven worden. De functie moet een dictionary (dict) teruggeven die elke letter (str) die voorkomt in de gegeven zin afbeeldt op de verzameling (set) van alle posities (int) waar die letter voorkomt in de zin. Hierbij mag de functie geen onderscheid maken tussen hoofdletters en kleine letters, en moeten alle sleutels van de dictionary kleine letters zijn. Bij het bepalen van de posities van de letters moeten alle karakters van de zin in rekening gebracht worden. Hierbij staat het eerste karakter van de zin op positie 0, het tweede karakter op positie 1, enzoverder.
    

### Voorbeeld

```
>>> frequentie = letterfrequenties("fifteen e's, seven f's, four g's, six h's, eight i's, four n's, five o's, six r's, eighteen s's, eight t's, four u's, three v's, two w's, three x's")
>>> frequentie['e']
15
>>> frequentie['f']
7
>>> frequentie['g']
4

>>> frequentie = letterfrequenties("sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's")
>>> frequentie['e']
16
>>> frequentie['f']
5
>>> frequentie['g']
3

>>> posities = letterposities("fifteen e's, seven f's, four g's, six h's, eight i's, four n's, five o's, six r's, eighteen s's, eight t's, four u's, three v's, two w's, three x's")
>>> posities['e']
{4, 5, 8, 14, 16, 43, 67, 83, 88, 89, 97, 121, 122, 141, 142}
>>> posities['f']
{0, 2, 19, 24, 54, 64, 108}
>>> posities['g']
{29, 45, 85, 99}

>>> posities = letterposities("sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's")
>>> posities['e']
{4, 5, 8, 16, 26, 27, 46, 56, 82, 87, 88, 96, 110, 111, 121, 122}
>>> posities['f']
{13, 18, 53, 63, 138}
>>> posities['g']
{29, 84, 98}
```