# Lawaaidoofheid

### Achtergrondinformatie

Lawaaidoofheid is een sluipend gevaar, waarbij slijtage van het gehoor optreedt in het slakkenhuis. Daar zitten immers haarcellen die door overbelasting beschadigd kunnen raken. Wanneer de beschadiging optreedt en hoe ernstig die uitvalt, is afhankelijk van de intensiteit en de duur van het lawaai. Een vuistregel die door audiologen gebruikt wordt, zegt dat men maximaal 8 uur per dag in een omgeving van 80 dB mag werken om risico op lawaaidoofheid te vermijden. Voor elke drie decibel die daarbij komt, moet je de blootstellingstijd halveren. Onlangs werd in sommige bioscopen een geluidsniveau tot 118 dB gemeten, waardoor je volgens bovenstaande regel in een dergelijke omgeving reeds na 7 seconden kans loopt om blijvende gehoorschade op te lopen. Langdurige blootstelling aan een omgeving van minder dan 80 dB levert normaal gezien geen risico op gehoorschade op.

### Opgave

Schrijf een functie `maximale_blootstelling` waaraan een reële waarde als argument moet doorgegeven worden. Deze waarde stelt een geluidsniveau in decibel voor. De functie moet de tijdsduur (een reëel getal dat een aantal seconden uitdrukt) teruggeven waarin men maximaal aan dit geluidsniveau mag blootgesteld worden, voordat men risico loopt op blijvende gehoorschade. Hiervoor moet de hierboven beschreven vuistregel gebruikt worden. Concreet moet de functie de waarde -1 teruggeven indien het gegeven geluidsniveau minder dan 80 dB bedraagt (deze waarde correspondeert met een onbeperkte tijdsduur). Voor een gegeven geluidsniveau binnen het interval [80, 83[ dB moet de functie een waarde teruggeven die correspondeert met een tijdsduur van 8 uur. Voor elk volgend geluidsinterval van 3 dB moet deze tijdsduur telkens gehalveerd worden ([83, 86[ -> 4 uur, [86, 89[ -> 2 uur, [89, 92[ -> 1 uur, …).

### Voorbeeld

```
>>> maximale_blootstelling(40)
-1.0
>>> maximale_blootstelling(60)
-1.0
>>> maximale_blootstelling(75)
-1.0
>>> maximale_blootstelling(80)
28800.0
>>> maximale_blootstelling(86)
7200.0
>>> maximale_blootstelling(90)
3600.0
>>> maximale_blootstelling(95)
900.0
>>> maximale_blootstelling(97)
900.0
>>> maximale_blootstelling(105)
112.5
>>> maximale_blootstelling(107)
56.25
>>> maximale_blootstelling(118)
7.03125
>>> maximale_blootstelling(115)
14.0625
>>> maximale_blootstelling(120)
3.515625
```