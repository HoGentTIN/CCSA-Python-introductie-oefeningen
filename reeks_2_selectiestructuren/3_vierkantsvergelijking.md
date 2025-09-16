# Vierkantsvergelijkingen oplossen

Een vierkantsvergelijking $ax^2+bx+c=0$ met coëfficiënten $a,
b, c \in \mathbb{R}$ heeft

- geen reële wortels als $\Delta = b^2-4ac<0$,

- één reële wortel, namelijk $x=-\frac{b}{2a}$, als
  $\Delta=0$,

- twee reële wortels, namelijk
  $x=\frac{-b\pm\sqrt{\Delta}}{2a}$, als $\Delta>0$.

### Invoer

De coëfficiënten van de vierkantsvergelijking $a, b, c \in
\mathbb{R}$, in die volgorde en op drie afzonderlijke regels.

### Uitvoer

De tekst op de eerste regel van de uitvoer geeft aan hoeveel reële wortels de gegeven vierkantsvergelijking heeft: "geen wortels", "een wortel" of "twee wortels". Als er één reële wortel is, schrijf deze dan uit als tweede regel van de uitvoer. Als er twee reële wortels zijn, schrijf beide dan uit als tweede en derde regel van de uitvoer, waarbij de kleinste oplossing op regel twee staat.

### Voorbeeld 1

**Invoer:**

```
1.0
-5.0
6.0
```

**Uitvoer:**

```
twee wortels
2.0
3.0
```

### Voorbeeld 2

**Invoer:**

```
1.0
0.0
2.0
```

**Uitvoer:**

```
geen wortels
```

### Voorbeeld 3

**Invoer:**

```
1.0
-1.0
0.25
```

**Uitvoer:**

```
een wortel
0.5
```

### Voorbeeld 4

**Invoer:**

```
1.0
-5.5
7.36
```

**Uitvoer:**

```
twee wortels
2.3
3.2
```