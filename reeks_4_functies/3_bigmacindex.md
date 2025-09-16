# Big Mac index

De _Big Mac index_ is een methode waarmee wisselkoersen op een licht verteerbare manier kunnen geanalyseerd worden. Deze index werd in 1986 door Pam Woodall ontwikkeld voor de Amerikaanse krant _The Economist_. Sindsdien publiceert die krant elk jaar een geactualiseerde versie van de index. Deze index gaf ook aanleiding tot de term _burgernomics_.

Het principe werkt heel eenvoudig. De Big Mac wisselkoers tussen twee landen kan berekend worden door de prijs van een Big Mac in één land (in de lokale munteenheid van dat land) te delen door de prijs van een Big Mac in een ander land (opnieuw in de lokale munteenheid van dat land). Deze berekende wisselkoers wordt dan vergeleken met de reële wisselkoers op dat ogenblik. Indien deze lager uitvalt, dan is de eerste munt ondergewaardeerd ten opzichte van de tweede, anders is de eerste munt overgewaardeerd ten opzichte van de tweede. Dit wordt geïllustreerd aan de hand van volgend voorbeeld:

-   in Europa betaalt men €3.44 voor een Big Mac
    
-   in de Verenigde Staten betaalt men $4.07 voor een Big Mac
    
-   de wisselkoers kan dus berekend worden als €3.44 / $4.07 = €0.845 per dollar
    
-   de reële wisselkoers bedraagt echter €0.70 per dollar
    
-   de euro is dus met 20.7% overgewaardeerd ten opzichte van de dollar $\left(\frac{0.845-0.70}{0.70}\times 100 = 20.7\% \right)$
    

De cijfers die gebruikt werden in bovenstaand voorbeeld zijn gebaseerd op de [versie van de Big Mac index](http://www.economist.com/blogs/dailychart/2011/07/big-mac-index) zoals die op 28 juli 2011 werd gepubliceerd door _The Economist_.

### Opgave

1.  Schrijf een functie `waardering` die op basis van de Big Mac index een analyse maakt van de wisselkoers van een bepaald land ten opzichte van de dollar. Aan deze functie moeten twee argumenten meegegeven worden die als _floating point_ getallen moeten beschouwd worden: 
    - de prijs van een Big Mac, en 
    - de reële wisselkoers ten opzichte van de dollar. 

    Bij de berekening van de Big Mac wisselkoers mag de functie uitgaan van een kostprijs van $4.07 voor een Big Mac in de Verenigde Staten. Op basis van de procentuele verhouding van de berekende dollarkoers ten opzichte van de reële dollarkoers, moet de functie een string teruggeven overeenkomstig onderstaande tabel.
        
    | VERHOUDING (%) | WAARDERING |
    | --- | --- |
    | v ≤ −25 | sterk ondergewaardeerd |
    | −25 < v ≤ −5 | ondergewaardeerd |
    | −5 < v ≤5 | ongeveer gelijk |
    | 5 < v ≤ 25 | overgewaardeerd |
    | v > 25 | sterk overgewaardeerd |
        
    Zo moet de functie voor een kostprijs van €3.44 voor een Big Mac in Europa en een reële dollarkoers van €0.70 per dollar, de string overgewaardeerd als resultaat teruggeven.
    
2.  Gebruik de functie `waardering` om een functie `wisselkoersanalyse` te schrijven. Aan deze functie moeten twee argumenten doorgegeven worden: de kostprijs van een Big Mac en de wisselkoers van de dollar (in lokale munteenheid per dollar). De kostprijs moet doorgegeven worden als een string die zowel het bedrag als de lokale munteenheid vermeldt, van elkaar gescheiden door een komma: bijvoorbeeld "3.44 euro" of "2.39 pond sterling". Merk dus op dat de munteenheid zelf uit meerdere woorden kan bestaan. De functie wisselkoersanalyse moet een string teruggeven die de waardering van de lokale munt ten opzichte van de dollar omschrijft. Als formaat voor de beschrijving gebruik je de volgende template
    
    > De _euro_ is _overgewaardeerd_ ten opzichte van de dollar.
    
    De cursieve fragmenten van deze template zijn variabel, en moeten door de functie `wisselkoersanalyse` worden ingevuld op basis van de opgegeven naam van de munteenheid en de berekende waardering.
    

### Voorbeeld

```
>>> waardering(3.44, 0.70)
'overgewaardeerd'
>>> wisselkoersanalyse('3.44 euro', 0.70)
'De euro is overgewaardeerd ten opzichte van de dollar.'
```