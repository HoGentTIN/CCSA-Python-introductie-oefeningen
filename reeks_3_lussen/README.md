Hier ga je aan de slag met lussen in Python.

Denk steeds na of een `for` dan wel een `while` lus het meest geschikt is.

Een typisch gebruik van `for` is samen met de `range` functie. De som van de getallen 
1 t.e.m. 10 wordt als volgt berekend:
```python
som = 0
for i in range(1,11): # eindpunt niet inbegrepen!
    som += i
print(som)
```

Voor sommige oefeningen kan je handig gebruikmaken van de [math](https://docs.python.org/3.7/library/math.html) module.
```python
import math

print(math.pi)
print(math.floor(math.pi))
``` 
drukt het volgende af
```
3.141592653589793
3
```

**Te lezen:**
- [First steps towards programming](https://docs.python.org/3.7/tutorial/introduction.html#first-steps-towards-programming)
- [For statements](https://docs.python.org/3.7/tutorial/controlflow.html#for-statements)
- [Range function](https://docs.python.org/3.7/tutorial/controlflow.html#the-range-function)