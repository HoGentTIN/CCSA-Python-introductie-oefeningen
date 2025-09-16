Hier ga je aan de slag met de zeer krachtige `dict` datastructuur. Je gebruikt ook `set` bewerkingen.

Het gebruik van een `dict` is zeer eenvoudig. Zie de voorbeelden hieronder. 

We maken een nieuwe dictionary.
```python
d = {'cat': 'cute', 'dog': 'furry'} 
print(d['cat'])
```
drukt af
```
cute
```
We kunnen een nieuw element toevoegen:
```python
d['fish'] = 'wet'
```
Laat ons nu eens alle elementen van de dictionary overlopen en afdrukken
```python
for k, v in d.items():
    print(f"{k} is {v}")
```
drukt af:
```
cat is cute
dog is furry
fish is wet
```
Vragen of een sleutel tot de dictionary behoort:
```python
if 'fish' in d:
    print("Er is een vis.")
else:
    print("Er is geen vis.")
```
Drukt af
```
Er is een vis.
```
Tot slot kan je ook eenvoudig sleutelwaarden wijzigen:
```python
d['fish'] = 'very wet'
```
en verwijderen
```python
del d['fish'] # 'fish' is nu niet langer in een sleutelwaarde
```

**Te lezen:**

- [Sets](https://docs.python.org/3.7/tutorial/datastructures.html#sets)
- [Dictionaries](https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries)