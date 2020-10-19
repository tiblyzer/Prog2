# Feladatleírás

1. Implementálja a Car nevű osztályt az UMl diagram alapján (konstruktor, és lekérdező/beállító metódusok)
A get kezdetű metódusok mindig a nevében szereplő adattagok értékével térnek vissza. A set kezdetű metódusok a paraméterként megkapott érték alapján mindig a nevükben szereplő adattagok értékét állítják be.
Plusz pontért lássa el a beállító metódusokat típusellenőrzéssel, hogy csak megfelelő értéket fogadjanak el!
2. Készítse el a Mercedes nevű osztályt a diagramban látható adattagok és metódusok alapján (konstruktor és lekérdező/beállító metódusok)!
3. Implementálja a Car és a Mercedes osztályok \_\_str\_\_ metódusát!
Az \_\_str\_\_ metódus mindig az adott osztály adattagjait adja vissza sztring-ként összekonkatenálva!
Írja felül a Mercedes osztályban a +, >= operátorokat úgy, hogy ár (originPrice) alapján az adott autó típus összehasonlíthatóvá, illetve összeadhatóvá váljon!
4. Implementálja a CarHandler osztályt az UML diagram alapján az alábbiak szerint!
    - A konstruktor inicializálja a carList változót üres listaként!
    - A readCarData beolvassa a carList listába a mercedes.txt-ben található adatokat. 
A szöveges állomány szóközzel tagolt, és egy sor az alábbi adatokat jelenti sorrendben:
	típus lóerő évjárat rendszám ár(millióban) végsebesség
    - A printContent metódus kiírja a lista elemeit.
    - A calculateReducePrice metódus meghívja és kiszámoltatja a csökkentett árat a Mercedes osztály reducePrice metódusával.
5. Implementálja a Mercedes osztály reducePrice metódusát, mely az adott típusnál 50% eséllyel csökkenti az adott autó árát véletlenszerűen választott százalékos értékkel!