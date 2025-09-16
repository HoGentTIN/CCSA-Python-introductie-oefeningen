# Blackjack

Het casino-spelletje Blackjack (of 21-en) is heel eenvoudig. Je krijgt twee kaarten met waarden van 1 tot en met 11. Vervolgens mag je onbeperkt kaarten bijvragen of stoppen. De speler die het dichtst bij 21 eindigt, is de winnaar. Heb je meer dan 21 dan ben je verbrand en sowieso verloren.

![Blackjack](../img/blackjack.avif)
<sub>Bron afbeelding: Duncan Nicholls, getty images.</sub>

### Opgave

Vraag aan de gebruiker één voor één kaarten met een waarde van 1 tot en met 11. Het programma stopt met het vragen van kaarten in de volgende drie gevallen:

-   Het totaal van de kaarten is 21. Toon de boodschap `Gewonnen!`.
-   Het totaal van de kaarten is meer dan 21, bijvoorbeeld 24. Toon dan `Verbrand (24)`.
-   Het totaal van de kaarten is minder dan 21, bijvoorbeeld 19 en de gebruiker geeft een kaart met waarde 0. Toon `Voorzichtig gespeeld (19)`.

### Voorbeeld

**Invoer:**
```
9
6
3
1
0
```

**Uitvoer:**

```
Voorzichtig gespeeld (19)

```