# Buitenaards woordenboek

Na een aanval van een vijandig buitenaards ras ben je op een andere planeet beland waar men een volledig andere taal spreekt. Dankzij geavanceerde nanotechnologie krijg je een intern gehoorapparaat, maar een vertaalprogramma van de buitenaardse taal naar het Nederlands ontbreekt nog. De woordenlijst is al beschikbaar, alleen de vertaalfunctie moet nog geïmplementeerd worden.

### Opgave

- Schrijf een functie `vertaling_toevoegen` die 3 argumenten heeft: het eerste argument is een string (het woord dat je wil vertalen), het tweede is ook een string (de vertaling van het eerste argument) en het derde argument is de dictionary waarin je de vertaling wilt aan toevoegen (dit wil zeggen, voeg het te vertalen woord toe als een sleutel aan de dictionary met als overeenkomende waarde de vertaling van het woord).

- Schrijf een functie `vertaling` die 2 argumenten heeft: het eerste argument is een string (het woord dat je wil vertalen) en het tweede argument is het woordenboek dat is opgebouwd aan de hand van de functie `vertaling_toevoegen`. Als er een vertaling bestaat in het woordenboek geeft de functie de vertaling terug, anders geeft het de string "???" terug.

### Voorbeeld

```
>>> woordenboek = {}
>>> vertaling_toevoegen('plerzs', 'vrouw', woordenboek)
>>> vertaling_toevoegen('nirtu', 'bloem', woordenboek)
>>> vertaling_toevoegen('klinzoj', 'dorst', woordenboek)
>>> vertaling_toevoegen('tilza', 'hond', woordenboek)
>>> vertaling_toevoegen('zraidi', 'tijd', woordenboek)
>>> woordenboek
{'klinzoj': 'dorst', 'zraidi': 'tijd', 'tilza': 'hond', 'plerzs': 'vrouw', 'nirtu': 'bloem'}

>>> vertaling('tilza', woordenboek)
'hond'
>>> vertaling('guoles', woordenboek)
'???'
```