import random
secret=random.randint(1,10)
essai=[]
nombre=int(input("Devinez le secret :"))
while nombre!= secret :
      essai.append(nombre)
      if nombre<secret:
          print("nombre plus grand que",nombre)
      else:
          print("nombre plus petit que", nombre)
      nombre=int(input("Devinez le secret :"))

print("Bravo vous avez trouvez !")
print("la liste de vos essai",essai)