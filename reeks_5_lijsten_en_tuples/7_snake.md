# Snake

Snake is een eenvoudig computerspelletje dat eind jaren '90 in opdracht van Nokia werd ontwikkeld. Het werd in 1998 gemaakt door Taneli Armanto en was één van de drie spellen die als standaard beschikbaar waren op de Nokia 6110 mobiele telefoon.

![Snake](../img/snake.avif)

In het spel bestuurt de speler een slang op een speelveld. De speler kan het hoofd van de slang naar boven, beneden, links of rechts sturen, de rest van de slang volgt vanzelf. Het doel is om bolletjes (voedsel) te verzamelen die punten opleveren en waardoor de slang steeds langer wordt. Tegelijk moet de speler vermijden om tegen de muren of tegen het eigen lichaam van de slang te botsen.

Om de slang van richting te doen veranderen gebruik je de pijltjestoetsen. Opdat de slang zichzelf niet zou opeten, mag je nooit de toetsen ↑ en ↓ (of omgekeerd) na elkaar indrukken. Ook de combinatie ← en → is een dodelijke combinatie.

In deze oefening gaan jullie in een lijst van pijltjestoetsen op zoek naar zo een dodelijke combinatie. Als toetsen gebruiken we <, >, v en ^. Een voorbeeld van een lijst van commando's is:

['<', 'v', '<', '>', '<', '^']

Je merkt dat het 4e commando het tegengestelde is van het 3e commando: we hebben dus een reeks van **3 opeenvolgende niet-dodelijke** commando's verwerkt.

Nemen we bovendien aan dat de slang op het scherm op coördinaten (0, 0) start en dat bij elke pijltjestoets de slang juist één pixel verplaatst wordt, dan is **de laatste levende positie van de slang** (-2, -1). Tip: verifieer dit met een schets van een assenstelsel waarop je de stappen aangeeft.

Merk op: we gaan uit van een vereenvoudigde versie van het spel, waarin de slang exact 1 pixel groot blijft.

### Opgave

Programmeer volgende functies:

-   Aan de functie `beweeg` geef je de coördinaten mee van de slang en een pijltjestoets. De functie verplaatst de slang 1 pixel in de richting van het pijltje en geeft de nieuwe coördinaten terug.
  
-   De functie `teruggekeerd` vraagt twee pijltjestoetsen in een lijst. De functie geeft True terug indien de twee pijltjes tegengestelde richtingen zijn, bijvoorbeeld '>' en '<'. In het andere geval wordt False teruggegeven.
  
-   `laatst_levende_positie` vraagt een niet-lege lijst van pijltjestoetsen en geeft een tuple terug met het aantal geldige zetten en de x- en y-coördinaat van de laatste levende positie.

### Voorbeeld

```
>>beweeg((-6, -6), '<')
(-7, -6)
>>beweeg((7, 3), '^')
(7, 4)

>>teruggekeerd(['^', 'v'])
True
>>teruggekeerd(['>', 'v'])
False

>>laatste_levende_positie(['>', '<', '^'])
(1, 1, 0)
>>laatste_levende_positie(['v', '>', 'v', '<', '^', '^'])
(6, 0, 0)

```

