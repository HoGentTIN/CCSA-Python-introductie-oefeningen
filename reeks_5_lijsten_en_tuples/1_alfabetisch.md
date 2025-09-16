# Alfabetisch

Zet de woorden van een zin in alfabetische volgorde.

### Opgave

Schrijf een functie `alfabetisch` waaraan een string als argument moet doorgegeven worden. De string bevat een zin waarvan de woorden enkel bestaan uit kleine letters, en van elkaar worden gescheiden door één enkele spatie. Er komen geen leestekens voor in de zin. De functie moet een string teruggeven waarin de woorden uit de gegeven zin in alfabetische volgorde geplaatst werden, en ook telkens van elkaar gescheiden worden door één enkele spatie.

### Voorbeeld

```
>>> alfabetisch('zeven zatte zaventemse zotten zullen zeven zomerse zondagen zwemmen zonder zwembroek')
'zatte zaventemse zeven zeven zomerse zondagen zonder zotten zullen zwembroek zwemmen'

>>> alfabetisch('een pet met een platte klep is een plattekleppet')
'een een een is klep met pet platte plattekleppet'

>>> alfabetisch('je ziet een boel vliegen vliegen maar er is geen een bij bij')
'bij bij boel een een er geen is je maar vliegen vliegen ziet'
```