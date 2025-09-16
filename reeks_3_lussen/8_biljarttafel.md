# Biljarttafel
<sub>Bron oefening en afbeelding: [Dodona - Biljarttafel](https://dodona.be/nl/activities/364433585/).</sub>

Leg een bal in de linkeronderhoek van een rechthoekige biljarttafel met pockets (gaten) in elk van de vier hoeken. Stoot daarna de bal in een hoek van 45° weg van de pocket. Ga ervan uit dat er geen wrijving is waardoor de bal niet afremt, en neem ook aan dat de bal perfect botst aan de randen (in een hoek van 90°). Waar raakt de bal de banden alvorens in één van de pockets te verdwijnen?

|<img src=../img/biljarttafel.png alt="biljarttafel" width="600">|
|:--:|
|Een biljarttafel met hoogte 6 en breedte 8, met de benamingen van de verschillende banden en pockets.|

Om de positie van de bal te kunnen beschrijven, gaan we ervan uit dat de
      biljarttafel gehele afmetingen heeft: de hoogte $h$ en de breedte $b$
      van de tafel zijn natuurlijke getallen (de eenheden zijn voor deze opgave
      niet belangrijk). Zoals aangegeven op bovenstaande figuur, leggen we een
      denkbeeldig assenstelsel bovenop de biljarttafel, met de X-as langs de
      onderband en de Y-as langs de linkerband. Op die manier kunnen we de
      posities waar de bal de banden raakt, omschrijven aan de hand van $(x,
      y)$-coördinaten, waarbij $x, y \in \mathbb{N}$ en $0 \leq x \leq
      b, 0 \leq y \leq h$. De oorsprong $(0, 0)$ van het assenstelsel ligt in
      de linkeronderhoek van de biljarttafel.

### Invoer

Twee regels die respectievelijk de hoogte $h \in \mathbb{N}_0$ en de
      breedte $b \in \mathbb{N}_0$ van een biljarttafel aangeven.

### Uitvoer

Voor elke opeenvolgende band waartegen de bal botst, moet een regel uitgeschreven worden met de benaming van de band, gevolgd door een spatie en de $(x, y)$-coördinaten waar de bal die band raakt. De banden worden benoemd zoals aangegeven op bovenstaande figuur.

De laatste regel die moet uitgeschreven worden, bevat de benaming van de pocket waarin de bal verdwijnt, gevolgd door een spatie en de $(x, y)$-coördinaten van die pocket. De pockets worden benoemd zoals aangegeven op bovenstaande figuur.

### Voorbeeld

**Invoer:**

```
6
8
```

**Uitvoer:**

```
bovenband (6, 6)
rechterband (8, 4)
onderband (4, 0)
linkerband (0, 4)
bovenband (2, 6)
rechteronderpocket (8, 0)
```