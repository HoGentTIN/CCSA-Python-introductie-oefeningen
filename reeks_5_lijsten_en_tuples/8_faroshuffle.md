# Faro shuffle

Een Faro shuffle is een shuffle waarbij de kaarten precies in twee gelijke helften worden verdeeld en perfect worden afgewisseld (Engels: "interleaved").

![Faro shuffle](../img/faroshuffle.avif)
<sub>Bron afbeelding: [magicianmasterclass.com](https://www.magicianmasterclass.com/term/faro-shuffle)</sub>

### Opgave

In deze oefening simuleren we een 'perfecte' faro shuffle. Implementeer hiervoor volgende functies:

-   `nieuw_kaartspel`: De eerste parameter is een lijst van kleuren, de tweede parameter een lijst van waarden. De functie geeft een nieuwe lijst terug waarbij aan elk kleur achtereenvolgend alle waarden werden toegevoegd in samengestelde strings.
  
-   `splits_kaartspel`: De gegeven kaartenlijst met minstens één kaart wordt in twee gelijke delen gesplitst. De functie geeft een tuple terug bestaande uit de twee gelijke delen van de gegeven kaartenlijst. Bij een kaartendeck van oneven lengte, bevat het tweede deel exact één kaart meer dan het eerste deel.
  
-   `faro_shuffle`: voegt de twee meegegeven kaartenlijsten samen volgens het principe van de faro shuffle. Je mag ervan uitgaan dat het kaartendeck gesplitst werd volgens de functie `splits_kaartspel`.

### Voorbeeld

```
>>> nieuw_kaartspel(['dood ', 'liefde ', 'tijd '],['0', '1'])
['dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1']
>>> nieuw_kaartspel(['blad ', 'steen ', 'schaar '],['1', '2', '3'])
['blad 1', 'blad 2', 'blad 3', 'steen 1', 'steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3']
>>> nieuw_kaartspel(['James '],['7'])
['James 7']

>>> splits_kaartspel(['dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1'])
(['dood 0', 'dood 1', 'liefde 0'], ['liefde 1', 'tijd 0', 'tijd 1'])
>>> splits_kaartspel(['blad 1', 'blad 2', 'blad 3', 'steen 1', 'steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3'])
(['blad 1', 'blad 2', 'blad 3', 'steen 1'], ['steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3'])
>>> splits_kaartspel(['James 7'])
([], ['James 7'])

>>> faro_shuffle(['dood 0', 'dood 1', 'liefde 0'],['liefde 1', 'tijd 0', 'tijd 1'])
['dood 0', 'liefde 1', 'dood 1', 'tijd 0', 'liefde 0', 'tijd 1']
>>> faro_shuffle(['blad 1', 'blad 2', 'blad 3', 'steen 1'],['steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3'])
['blad 1', 'steen 2', 'blad 2', 'steen 3', 'blad 3', 'schaar 1', 'steen 1', 'schaar 2', 'schaar 3']
>>> faro_shuffle([],['James 7'])
['James 7']

```