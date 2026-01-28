notes=[]
somme=0
nombre=int(input("entrez une note:"))
while nombre !=(-1):
     
      somme=somme+nombre
      notes.append(nombre)
      nombre=int(input("entrez une note:")) 

    
print("la moyenne est",somme/len(notes))
maxnote=notes[0]
minnote=notes[0]
nbre=0
for nombre in notes:
      if nombre>maxnote:
            maxnote=nombre
      if nombre<minnote:
            minnote=nombre
      if nombre>10:
            nbre+=1
print("la meilleur note est :",maxnote)    
print("la mauvaise  note est :",minnote)
print("le nombre de note superieur à 10 est:",nbre)          
