# snake-ai


Bude had, který se bude rozhodovat na základě neuronové sítě. Nejjednodušší varianta je neuronová síť s 1 hidden layerem, nějakým počtem vstupních neuronů a 4 výstupními, které budou určovat, na kterou stranu má zabočit.

Struktura neuronové sítě může být trochu komplikovanější - může mít paměť (např. být rekurentní, nebo LSTM).

Genetický algoritmus bude inicializovaný tak, že na začátku uděláme 100 variant hada, které se budou lišit váhami v síti, budou vygenerované náhodně. Ty budou soutěžit v nějakém pokusném prostředí. Každá varianta hada bude mít 100 pokusů a vybereme 5 nejlepších. Z každé vznikne 20 dalších variant.

Takto to budeme opakovat po několik generací, než začne vývoj stagnovat.

Bylo by zajímavé pozorovat:

1. které parametry genetického algoritmu vedou k rychlému vývoji
2. která architektura neuronových sítí dosáhne nejlepších výsledků
