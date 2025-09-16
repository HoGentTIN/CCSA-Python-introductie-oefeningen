# Grootste gemene deler

De grootste gemene deler is het grootste gehele getal dat twee andere getallen kan delen zonder dat er een rest overblijft. Bijvoorbeeld, de grootste gemene deler van 14 en 21 is 7, omdat 7 het grootste getal is waardoor je 14 en 21 beide kunt delen.

Euclides' algoritme om de grootste gemene deler te bepalen zegt dat als je de grootste kunt delen door de kleinste (zonder rest), dan is het de kleinste. Anders is het de uitkomst van het bepalen van de grootste gemene deler van de kleinste en de rest die overblijft als je de grootste deelt door de kleinste. Dit is een recursieve definitie.

### Opgave

Schrijf een recursieve functie `ggd` waaraan twee natuurlijke getallen $a$ en $b$ moeten doorgegeven worden. De functie moet de grootste gemene deler van de getallen teruggeven op basis van een implementatie volgens Euclides’ algoritme.

> #### Tip
> 
> Testen of twee getallen door elkaar gedeeld kunnen worden, en het berekenen van een rest, kunnen beide gedaan worden met de modulo operator. Deze code kan _heel_ erg kort zijn.

### Voorbeeld

```
>>> ggd(14, 21)
7
```