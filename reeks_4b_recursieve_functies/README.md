In deze reeks van oefeningen ga je aan de slag in Python met recursieve functies.

Typisch voor recursie is het feit dat in de body van de functie, de functie zichzelf opnieuw aanroept. Typisch is het voorkomen van een basisgeval, waarna de recursie stopt. Check zeker dat je in elk geval ook in deze basisstap geraakt, anders creëer je een oneindige lus en stopt uw algoritme niet.

Een kort voorbeeld: de som van de eerste n natuurlijke getallen.
```python
def somEersteNGetallenRecursief(n):
    som = 0
    if n==0:
        return 0        
    else :
        return n + somEersteNGetallenRecursief(n-1)

n = int(input("Geef een natuurlijk getal:"))

print (somEersteNGetallenRecursief(n))
```
geeft bijvoorbeeld bij invoer:
```
3
```

de volgende uitvoer:
```
6
```