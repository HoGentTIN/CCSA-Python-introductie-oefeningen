# Bankrekening

Het concept van een bankrekening in een programma vormt een goede kandidaat voor een klasse. Een bankrekening heeft typisch de volgende eigenschappen (attributen): de naam van de rekeninghouder, het rekeningnummer en het huidige bedrag op de rekening. We kunnen drie acties uitvoeren op een bankrekening: geld afhalen, geld storten en de gegevens van de bankrekening weergeven.

### Opgave

Je opdracht bestaat erin een klasse `BankRekening` aan te maken met volgende methoden:

1.  De initialisatiemethode `__init__` krijgt als parameters de naam van de rekeninghouder, een rekeningnummer en een initieel bedrag mee. Het meegeven van een initieel bedrag als parameter is optioneel, en krijgt als standaardwaarde de waarde 0.
    
2.  De methode `__str__` geeft een stringrepresentatie van een bankrekening terug. Baseer je voor de vorm waarin de gegevens worden uitgeschreven op het voorbeeld hieronder.
    
3.  De methode `__repr__` geeft eveneens een uitprintbare stringrepresentatie van een bankrekening terug. Waar de methode `__str__` wordt gebruikt om een representatie van een object te bekomen die gemakkelijk leesbaar is voor een menselijke gebruiker, geeft de `__repr__` een representatie terug die gelezen kan worden door de python interpreter. De methode `__repr__` geeft een syntactisch correcte Python expressie, die — wanneer deze geëvalueerd zou worden — een object creëert dat gelijk is aan het object dat origineel werd doorgegeven aan `__repr__`.
    
4.  Twee methoden `storten(self, n)` en `afhalen(self, n)`. De parameter n van deze methoden is het bedrag dat bijgestort of afgehaald wordt.
    

### Voorbeeld

```
>>> b1 = BankRekening('Jan Jansen', '001457894501', 10000)
>>> b2 = BankRekening('Peter Peeters', '842457894511', 10000)
>>> b1.storten(250)
>>> b1.afhalen(1000)
>>> b2.afhalen(300)
>>> str(b1)
'Jan Jansen, 001457894501, bedrag: 9250'
>>> print(b2)
Peter Peeters, 842457894511, bedrag: 9700
>>> repr(b2)
"BankRekening('Peter Peeters', '842457894511', 9700)"
>>> b3 = BankRekening('David Davidse', '002457896312')
>>> b3.storten(112)
>>> print(b3)
David Davidse, 002457896312, bedrag: 112
>>> b3
BankRekening('David Davidse', '002457896312', 112)
```