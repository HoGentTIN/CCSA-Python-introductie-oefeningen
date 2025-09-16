# Botsende rechthoeken

Wat is de onderlinge positie van twee gegeven objecten? Het is een belangrijke vraag, die niet altijd even makkelijk te beantwoorden is door een computerprogramma. Als twee objecten in het vlak overlappen, dan noemen we dit een botsing. Een botsing kan bijvoorbeeld gebruikt worden om te bepalen of twee onderdelen op een kaart in elkaar liggen, of om delen van foto's te analyseren.

Bij deze opgave gaan we een vereenvoudigde versie van het probleem bekijken. We stellen een object voor door zijn [_axis-aligned bounding box_](http://en.wikipedia.org/wiki/Minimum_bounding_box#Axis-aligned_minimum_bounding_box). Dit is de rechthoek die net het object omsluit en waarvan de zijden evenwijdig zijn met de $X$- en $Y$-as. We zeggen dan dat twee objecten botsen als hun _bounding boxes_ overlappen.

### Invoer

De invoer bestaat uit acht gehele getallen (één per regel) die tweemaal twee diametrale punten van twee rechthoeken voorstellen. Het eerste getal is telkens de $X$-coördinaat en het tweede getal de $Y$-coördinaat. De rechthoeken zijn echte rechthoeken (en dus niet ontaard als lijnstuk of punt).

### Uitvoer

De uitvoer bestaat uit één regel. Deze regel bevat de tekst _botsing_ als de twee rechthoeken overlappen en de tekst _geen botsing_ als de twee rechthoeken niet overlappen. Opgelet: raken is niet hetzelfde als overlappen!

### Voorbeeld 1

**Invoer:**

```
0
0
1
2
4
1
5
5
```

**Uitvoer:**

```
geen botsing
```

### Voorbeeld 2

**Invoer:**

```
0
0
2
3
1
2
5
5
```

**Uitvoer:**

```
botsing
```