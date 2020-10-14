# Hallgatói segédlet

## Osztály

Szintaktika:
```
class osztalynev:
	def __init__(self,parameter1,parameter2):
		pass
	def metodusnev1(self,parameter1,parameter2):
		pass
```

Az init az osztály konstruktora, ez állítja be a osztály adattagjait és kezdőértékűket
A pass üres részt jelent.

Default kezdőértékadás paramétereknek:

```
def metodusnev1(self,parameter1=0):
	pass
```

Abban az esetben, ha üresen hagyjuk a metódushívásnál a paramétert, akkor az egyenlőségjel után levő értéket veszi fel.

Példányosítás:
```
class osztalynev:
	def __init__(self,parameter1,parameter2):
		pass
	def metodusnev1(self,parameter1,parameter2):
		pass

objektum = osztalynev() # ez a sor a példányosítás
```

## Láthatóság

Három esetet különböztetünk meg:
1. Public (bárhonnan elérhető)

```
class A:
	def __init__(self,n):
		self.valtozo = n
```

2. Private (csak az osztály éri el, dupla alulvonás jelüli)
```
class B:
	def __init__(self,n):
		self.__valtozo = n
```

3. Protected(csak az ősosztály, és a ráépülő osztályok érik el, egyszeres alulvonás jelöli)
```
class C:
	def __init__(self,n):
		self._valtozo = n
```


## Lekérdező, beállító metódusok

Szintaktika:

```
def getValtozo(self):
	return self.valtozo

def setValtozo(self,other):
	self.valtozo = other.valtozo
```

A get kezdetű lesz a lekérdező metódus és mindig visszatér eredménnyel.
A set kezdetű lesz a beállító, és változók értékét állítja be.

## Operátor túlterhelés
Lehetőség van az egyszerűbb műveletek (+ - * == >= <= != ) implementálására a saját osztályaink esetében. 
Eredményként így használható később a kódban: D = D1 + D2. Nem kell külön elérni az egyes osztályváltozókat.

Szintaktika:
```
class E:
	def __op__(self,param):
	pass
```

Példa összeadásra (public eset, sima értékvisszatérés):
```
class F:
	def __init__(self,n):
		self.valtozo = n
	
	def __add__(self,other):
		return self.valtozo + other.valtozo
```

Példa összeadásra (public eset, osztály értékvisszatérés):
```
class F:
	def __init__(self,n):
		self.valtozo = n
	
	def __add__(self,other):
		return F(self.valtozo + other.valtozo)
```

Példa összeadásra(public eset, sima értékvisszatérés típusvizsgálattal):
```
class G:
	def __init__(self,n):
		self.valtozo = n
	
	def __add__(self,other):
		if(type(other) == 'int'):
			return self.valtozo + other
```

Példa összeadásra(public eset, sima értékvisszatérés osztálytípusának vizsgálatával):
```
class G:
	def __init__(self,n):
		self.valtozo = n
	
	def __add__(self,other):
		if(isistance(other,G)):
			return self.valtozo + other
```
AZ isistance használható az előző példa esetében is:
```
class G:
	def __init__(self,n):
		self.valtozo = n
	
	def __add__(self,other):
		if(isistance(other,int)):
			return self.valtozo + other
```

Példa összeadásra (private eset, sima értékvisszatérés):
```
class F:
	def __init__(self,n):
		self.__valtozo = n
	
	def getValtozo(self):
		return self.__valtozo
	def __add__(self,other):
		return self.__valtozo + other.getValtozo()
```
## Metódusok túlterhelése

```
class F2:
	def Print(self):
		pass
	def Print(self,valtozo):
		print(valtozo)
```

Annyi a lényeg, hogy ugyanazon névvel vannak ellátva a metódusok, csak a paraméterlistájuk különbözik.
## Öröklődés,beágyazott osztály

Szintaktika:
```
class A:
	def __init__(self):
		pass

class B(A):
	def __init__(self):
		super().__init__()
```

Az A-t ősosztálynak,a B-t pedig származtatott osztálynak nevezzük. 
Zárójelben felsoroljuk az ősosztályok nevét.
A super automatikusan tudja, mi a neve az ősosztálynak, nekünk nem szükséges tudni.

Szintaktika paraméterekkel és default kezdőértékekkel:
```
class A:
	def __init__(self,n=0):
		self.__valtozo = n

class B(A):
	def __init__(self,a=0):
		super().__init__(a)
```

Szintaktika beágyazott osztályra:

```
class A:
	def __init__(self):
		self.__valtozo = self.B(5)

	class B:
		def __init__(self,a=0):
			super().__init__(a)
```

Itt annyi a lényeg, hogy az osztály leírását egy másik osztályon belülre helyezzük el.
