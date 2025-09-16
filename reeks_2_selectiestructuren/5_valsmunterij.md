# Valsmunterij

Je beschikt over negen muntstukken en een weegschaal. Je weet dat één van de muntstukken vervalst is, in die zin dat het lichter gemaakt is dan de andere muntstukken. Is het mogelijk om het vervalste muntstuk te identificeren door maar twee keer te wegen?

Dat kan inderdaad door de volgende strategie toe te passen. Nummer de muntstukken van 1 tot en met 9. Verdeel de muntstukken in drie groepen: een groep met de muntstukken 1-2-3, een groep met de muntstukken 4-5-6 en een groep met de muntstukken 7-8-9. Plaats de groep 1-2-3 aan de linkerkant van de weegschaal en weeg die af tegen de groep 4-5-6 die je aan de rechterkant van de weegschaal plaatst. Als de weegschaal in evenwicht is, dan zit het vervalste muntstuk in de groep die niet werd afgewogen. Anders zit het vervalste muntstuk in de lichtste groep.

Nu de zoekruimte vernauwd is tot een groep van drie verdachte muntstukken, kunnen we bij een tweede weging hetzelfde principe toepassen. Plaats het eerste muntstuk van de verdachte groep aan de linkerkant van de weegschaal, en weeg het af tegen het tweede muntstuk van de verdachte groep. Als de weegschaal niet in evenwicht is, dan is het vervalste muntstuk het lichtste van de twee gewogen muntstukken. Anders is het derde muntstuk van de verdachte groep vervalst.

### Invoer

Twee regels die de stand van de weegschaal aangeven bij respectievelijk een eerste en een tweede weging als je de strategie toepast zoals hierboven beschreven. Als de weegschaal in evenwicht is, dan wordt de stand beschreven door de tekst evenwicht. Anders wordt de stand van de weegschaal beschreven door de kant van de weegschaal die het laagst staat: links of rechts.

### Uitvoer

De tekst

> muntstuk #_n_ is vervalst

waarbij _n_ ingevuld wordt met het nummer van het vervalste muntstuk.

### Voorbeeld

**Invoer:**

```
links
evenwicht
```

**Uitvoer:**

```
muntstuk #6 is vervalst
```

