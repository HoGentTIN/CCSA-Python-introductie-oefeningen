# Dubbels

Welke getallen komen meerdere keren voor in een gegeven lijst?

### Opgave

1.  Schrijf een functie `dubbel` die een lijst van getallen als argument neemt, en het element van de lijst teruggeeft dat tweemaal voorkomt. De functie moet de waarde None teruggeven als er geen enkel getal meer dan één keer voorkomt in de lijst. Er is hoogstens één getal dat tweemaal voorkomt.
    
2.  Schrijf een functie `dubbels` die een lijst van getallen als argument neemt, en twee verzamelingen teruggeeft. De eerste verzameling bevat alle elementen die slechts eenmaal voorkomen in de lijst en de tweede verzameling bevat alle elementen die meer dan eenmaal voorkomen in de lijst.
    

### Voorbeeld

```
>>> dubbel([1, 2, 3, 4, 2])
2
>>> dubbel([1, 2, 3, 4])
>>> dubbel([1, 2, 3, 4, 5, 6, 100, -234, 15, 0, -20000, 15])
15

>>> dubbels([1, 2, 3, 4, 2])
({1, 3, 4}, {2})
>>> dubbels([2, 8, 8, 6, 10, -20, -4, -2, -4])
({2, 6, 10, -20, -2}, {8, -4})
>>> dubbels([1, 3, 5, 7, 2, 4, 6])
({1, 2, 3, 4, 5, 6, 7}, set())
```