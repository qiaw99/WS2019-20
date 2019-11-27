| Mensch  Wolf  Ziege Kohlkopf
|    0     0      0       0

Tatsächlich benötigen wir dringend nur diese 4 Zuständen, um alle Situationen zu simulieren. 0 bedeutet, dass der Teilnehmer noch nicht mit dem Boot über den Fluss fährt. 1 bedeutet aber, dass der Teilnehmer schon mit dem Boot über den Fluss gefahren hat.

Folgendes sind alle möglichen Situationen zu diesem Problem: 

1. 0, 0, 0, 0	--->  "Initialisierung"

2. 0, 1, 0, 0	--->  "mensch ziege kohlkopf | wolf"

3. 0, 0, 1, 0 	---> "mensch wolf kohlkopf | ziege"

4. 0, 0, 0, 1	--->  "mensch wolf ziege | kohlkopf"

5. 1, 0, 1, 0	--->  "wolf kohlkopf | mensch ziege"

6. 0, 1, 0, 1 	---> "mensch ziege | wolf kohlkopf"

7. 1, 0, 1, 1 	---> "wolf | mensch ziege kohlkopf"

8. 1, 1, 0, 1 	---> "ziege | mensch wolf kohlkopf"

9. 1, 1, 1, 0	--->  "kohlkopf | mensch wolf ziege"

10. 1, 1, 1, 1 	--->  "Fertig"

wobei die Sequenz von den Folgen genau wie die in der Tabelle ist.

Alle 10 möglichen Situationen entsprechen dann 10 Knoten in der Graph. Außerdem speichern wir die Graph mithilfe der Adjazenzmatrix. Um die Existenz von einer Kante zwischen zwei Knoten zu bestätigen, müssen wir folgende Bedingungen überprüfen:
Da nur der Mensch den Boot rudern kann, muss dann das Status vom Menschen verändert werden, also 0 -> 1 oder 1 -> 0. 
Maximal kann Status von einem Teilnehmer gleichzeitig geändert werden. Aber es kann auch sein, dass der Mensch alleine den Boot rudert. D.h. in diesem Fall verändert nur das Status vom Menschen.

Um alle Teilnehmer auf der anderen Seite vom Fluss übergehen zu können, sollen wir in der Tatsache einen Weg von “Initialisierung” nach “fertig” herausfinden, was gemeint ist, dass wir die ganze Graph durchgehen müssen, so dass wir am Ende Ergebnisse bekommen können.

