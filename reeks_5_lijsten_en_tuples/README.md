Oefeningen waarin je Python `list` en `tuple` gebruikt. Lists zijn één van de werkpaarden in Python.

Tracht waar mogelijk handig gebruik te maken van list comprehensions. 
Stel dat je een `list` wil maken met daarin de getallen van 1 t.e.m. 10, dan kan je dit zonder list comprehension als volgt doen:
```python
mijn_lijst = [] # start met lege lijst
for i in range(1, 11):
    mijn_lijst.append(i) # Voeg achteraan toe aan de lijst
print(mijn_lijst)
```
Met een list comprehension kan dit veel handiger:
```python
mijn_lijst = [i for i in range(1, 11)]
print(mijn_lijst)
```
Je kan er ook een filter op zetten. Stel dat we enkel kwadraten van de even getallen willen overhouden.
```python
kwadraten_even_getallen = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(kwadraten_even_getallen)
```
Dit laatste drukt (zoals verwacht) `[4, 16, 36, 64, 100]` af.

Een lijst doorlopen gaat typisch als volgt:
```python
fruit = ['appel', 'peer', 'kiwi']
for item in fruit:
   print(item)
```
geeft als uitvoer
```
appel
peer
kiwi
```
Als we echter ook de index willen gebruiken dan kunnen we `enumerate` gebruiken:
```python
fruit = ['appel', 'peer', 'kiwi']
for index, item in enumerate(fruit):
   print(item * (index + 1))
```
Dit geeft als uitvoer:
```
appel
peerpeer
kiwikiwikiwi
```

**Te lezen**:
- [Lists](https://docs.python.org/3.7/tutorial/introduction.html#lists)
- [More on Lists](https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists)