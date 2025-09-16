# De drie wijzen

Caspar, Melchior en Balthasar gingen in de buurtwinkel op zoek naar cadeautjes voor de geboorte van de zoon van een gemeenschappelijke vriend, en vonden er goud, wierook en mirre. Bij de kassa vermenigvuldigde de kassierster de prijzen van de drie geschenken met elkaar om zo een totaalbedrag van €65.52 te bekomen. De drie vrienden wezen de kassierster fijntjes op het feit dat ze de prijzen niet had moeten vermenigvuldigen, maar had moeten optellen. Met het schaamrood op de wangen berekende de kassierster het totaalbedrag opnieuw, maar nu door op te tellen in plaats van te vermenigvuldigen. Tot ieders verbazing kwam ze op exact hetzelfde bedrag uit als bij haar eerste berekening. Wat was de prijs van de afzonderlijke geschenken?

### Invoer

Een getal $t \in \mathbb{R}$, uitgedrukt met twee cijfers na de komma, waarvoor geldt dat $t > 0$.

### Uitvoer

Bepaal drie getallen $a, b, c \in \mathbb{R^+}$ met maximaal twee
      cijfers na de komma waarvoor geldt dat: $$\begin{cases} a + b + c = t \\ a
      \cdot b \cdot c = t \\ 0 \leq a \leq b \leq c \end{cases}$$ We
      garanderen ook dat er altijd juist één combinatie is waarvoor
      deze voorwaarden gelden. Schrijf het gevonden resultaat uit aan de hand
      van volgende template:

> €a + €b + €c = €a x €b x €c = €t

Hierbij moeten alle getallen uitgeschreven worden met twee cijfers na de komma.

### Voorbeeld

**Invoer:**

```
65.52
```

**Uitvoer:**

```
€0.52 + €2.00 + €63.00 = €0.52 x €2.00 x €63.00 = €65.52
```