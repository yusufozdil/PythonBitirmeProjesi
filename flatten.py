liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flattenListe = []

def flatten(liste):
    for i in liste:
        if type(i)==list:
            flatten(i)
        else:
            flattenListe.append(i)

flatten(liste)
print(flattenListe)