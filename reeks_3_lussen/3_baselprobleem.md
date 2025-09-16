# Het probleem van Basel

Omstreeks 1735 loste de Zwitserse wiskundige Leonard Euler het beroemde <a href="http://nl.wikipedia.org/wiki/Bazel-probleem" target="_blank">probleem van Basel</a><sup class="footnote-url visible-print-inline">1</sup> op. Hij vond namelijk een exacte uitdrukking voor de oneindige som $$\sum_{i=1}^{\infty} \frac{1}{i^2} = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \dots$$ Euler bewees dat deze som exact gelijk is aan $\frac{\pi^2}{6}$. We noteren de <em>partieelsommen</em> van deze reeks als $f_n$. Met andere woorden $$f_n = \sum_{i=1}^n \frac{1}{i^2}$$ Voor deze partieelsommen bewees Euler dus dat $$\lim_{n\to\infty} f_n = \frac{\pi^2}{6}$$

### Invoer

Geen invoer

### Uitvoer

Twee regels:

-   eerste regel: de waarde van $f_{100}$ als een decimaal getal,
    
-   tweede regel: de kleinste waarde $n \in \N$ waarvoor $\left| f_n - \frac{\pi^2}{6} \right| \leq \frac{1}{100}$
.