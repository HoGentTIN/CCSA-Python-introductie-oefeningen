# Bovensteboven

We zeggen dat een getal bovensteboven is, als we ditzelfde getal opnieuw lezen wanneer we het 180° ronddraaien. De getallen 689 en 1961 zijn voorbeelden van getallen die bovensteboven zijn.

### Opgave

-   Schrijf een functie `bovensteboven` waaraan een getal $n \in \N$ als argument moet doorgegeven worden. De functie moet een Booleaanse waarde als resultaat teruggeven, die aangeeft of het gegeven getal bovensteboven is of niet.
    
-   Gebruik de functie `bovensteboven` om een functie `volgende` te schrijven waaraan een getal $n \in \N$ als argument moet doorgegeven worden. De functie moet het eerstvolgende bovensteboven getal teruggeven dat groter is dan $n$.
    

### Voorbeeld

```
>>> bovensteboven(689)
True
>>> bovensteboven(1961)
True
>>> bovensteboven(2965)
False
>>> bovensteboven(68089)
True
>>> bovensteboven(90306)
False

>>> volgende(689)
808
>>> volgende(1961)
6009
>>> volgende(98765)
98886
```