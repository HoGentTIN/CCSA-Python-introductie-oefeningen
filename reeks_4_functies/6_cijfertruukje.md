# Cijfertruukje

Schrijf een natuurlijk getal op een blaadje papier:

> 886328712442992

Tel het aantal even en oneven cijfers, en ook het totaal aantal cijfers:

> 10 5 15

Vorm een nieuw getal door de cijfers van de voorgaande drie getallen samen te voegen:

> 10515

Voer dezelfde procedure nogmaals uit op het bekomen getal:

> 1 4 5 ⟶ 145

En blijf dit herhalen:

> 1 2 3 ⟶ 123

Je zal finaal altijd bij het getal 123 uitkomen.

#### Opmerking

Bij het toepassen van de procedure om het volgende getal te bepalen, dien je de voorloopnullen te laten vallen als er geen even cijfers in het getal staan. Als we bijvoorbeeld vertrekken van het getal 111, dan bepalen we het volgende getal als

> 0 3 3 ⟶ 33 (en niet 033)

Dat maakt een verschil omdat 33 geen even cijfers heeft (en bij een volgende toepassing van de procedure 22 oplevert) en 033 wel een even cijfer heeft (en bij een volgende toepassing van de procedure 123 zou opleveren).

### Opgave

-   Schrijf een functie `even_oneven` waaraan een natuurlijk getal (int) moet doorgegeven worden. De functie moet een tuple met twee natuurlijke getallen (int) teruggeven, die respectievelijk aangeven hoeveel even en oneven cijfers er in het gegeven getal voorkomen.
    
-   Schrijf een functie `volgende` waaraan een natuurlijk getal (int) moet doorgegeven worden. De functie moet het getal (int) teruggeven dat men bekomt door de procedure uit de inleiding eenmaal toe te passen op het gegeven getal.
    
-   Schrijf een functie `stappen` waaraan een natuurlijk getal (int) moet doorgegeven worden. De functie moet teruggeven hoeveel keer (int) we de procedure uit de inleiding moeten toepassen vooraleer we het getal 123 bekomen, als we beginnen bij het gegeven getal.
    

### Voorbeeld

```
>>> even_oneven(886328712442992)
(10, 5)
>>> even_oneven(10515)
(1, 4)
>>> even_oneven(145)
(1, 2)

>>> volgende(886328712442992)
10515
>>> volgende(10515)
145
>>> volgende(145)
123

>>> stappen(886328712442992)
3
>>> stappen(1217637626188463187643618416764317864)
4
>>> stappen(0)
2
>>> stappen(1)
5

```