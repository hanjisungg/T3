#T3

#ex 185

#creation du meme bon de commande que dans l exercice pour avoir un exemple
table = [
{"ref": "18635", "designation": "lot crayons HB", "prix": 2.30, "qte": 1},
{"ref": "15223", "designation": "stylo rouge", "prix": 1.50, "qte": 0},
{"ref": "20112", "designation": "cahier petits carreaux", "prix": 3.50, "qte": 2}
]


#####################################################################################
#validation des données --> non utile: sur Python deja valide 
def valide(x):
    ref = x["ref"]
    designation = x["designation"]
    prix = float(x["prix"])
    qte = int(x["qte"])
    return {"ref": ref, "designation": designation, "prix": prix, "qte": qte}

table_valide = [valide(x) for x in table]

#######################################################################################

#petit 1
def verifie_quantites(table):
    for e in table:
        if e["qte"] <= 0:
            return False
    return True


#petit 2
def nombre_produit(table):
    somme = 0
    for t in table:
        somme += t["qte"]
    return somme


#ex 186

#petit 1
def purge_commande(b):
    nouvelle_table = [{"ref": e["ref"],"designation": e["designation"], "prix": e["prix"], "qte": e["qte"]} for e in b if e["qte"] > 0]
    return nouvelle_table

#petit 2
def prix(b):
    nouvelle_table = purge_commande(b)
    somme = 0
    for e in nouvelle_table:
        somme += e["prix"]*e["qte"]
    return somme