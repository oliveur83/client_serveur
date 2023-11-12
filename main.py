class element:
    def __init__(self,occ):
        self.occurence=occ
class feuille(element):
    def __init__(self,car,occ):
        element.__init__(self,occ)
        self.caractere =car
    def __repr__(self):
        return (f'caractere {self.caractere}: occurence ={self.occurence}')
class noeud(element):
    def __init__(self,gauche,droite):
        element.__init__(self,gauche.occurence+droite.occurence)
        self.gauche=gauche
        self.droite=droite
        
    def __repr__(self) -> str:
        return (f'occurence noeud{self.occurence}')

def create_list():
    liste_arbre=[]
    file=open('data.txt','rb')
    datafile=file.read().decode("utf8")
    while len(datafile)>0:
        car=datafile[0]
        occ=datafile.count(car)
        datafile=datafile.replace(car,'')
        liste_arbre.append(feuille(car,occ))
   
    return sorted(liste_arbre,key=lambda elements: elements.occurence,reverse=True)

def creation_arbre(arbre):
    while len(arbre) > 1:
        gauche = arbre.pop()
        droite = arbre.pop()
        arbre.append(noeud(gauche, droite))
        arbre = sorted(arbre, key=lambda x: x.occurence, reverse=True)
    return arbre[0]
 
def create_code(arbre, code,dico):
    if isinstance(arbre, feuille):
        dico[arbre.caractere] = code
    else:
        type(arbre)
        create_code(arbre.gauche , code + "0",dico)
        create_code(arbre.droite, code + "1",dico)
        
liste=create_list()
listet=creation_arbre(liste)
dico=dict()
create_code(listet,'',dico)
print("dd",dico)
