# example:

def increment(nr: float) -> float:
  return nr1 + 1

def decrement(nr: float) -> float:
  return nr1 - 1

def add(nr1:float , nr2: float) -> float:
  return nr1 + nr2
  

def substract(nr1:float , nr2 :float):
  return nr1 - nr2
  

def multiply(nr1:float , nr2 : float):
  return nr1 * nr2
  

def divide(nr1:float, nr2:float):
  if nr2 != 0:
    return nr1 / nr2
  else:
    return "je kunt niet delen door 0 "
  


nr1 = 10
nr2 = 5
  
resultaat = increment(nr1)
print(resultaat)

resultaat = decrement(nr1)
print(resultaat)

resultaat = add(nr1,nr2)
print(resultaat)

resultaat = substract(nr1,nr2)
print(resultaat)

resultaat = multiply(nr1,nr2)
print(resultaat)

resultaat = divide(nr1,nr2)
print(resultaat)

