# C-som

De _c-som_ van een getal wordt bepaald door de som van de cijfers van dit getal te berekenen, en deze procedure te blijven herhalen totdat het bekomen getal bestaat uit één enkel cijfer. Zo hebben we bijvoorbeeld dat:

> ```
> c-som(8) = 8
> c-som(377096267) = c-som(47) = c-som(11) = 2
> ```

### Opgave

Schrijf een functie `csom` waaraan een natuurlijk getal (int) moet doorgegeven worden. De functie moet de c-som van dit getal als (int) teruggeven.

### Voorbeeld

```
>>> csom(8)
8
>>> csom(377096267)
2
```