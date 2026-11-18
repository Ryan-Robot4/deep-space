import numpy as np

class niveau:
    def __init__(self,level,message,reponse):
        self.id=level
        self.msg=message
        self.reponse=reponse

lvl = 0


lvl_0=niveau(0,[0],[0])
lvl_1=niveau(1,[1],[1])
lvl_2=niveau(2,[0,1,2,3],[4])
lvl_3=niveau(3,[0,-2,1,-2,2,-2,3,-2,4,-2],[5])
lvl_4=niveau(4,[0,-2,1,-2,2,-2,3,-2,4,-2,5,-2,6,-2,7,-2,10,-2,11,-2,12,-2],[13])
lvl_5=niveau(5,[1,-2,1,-3,-2,-5,-2,2,-2,-2,3,-2,1,-3,-2,-5,-2,4,-2,-2,1,-2,3,-3,-2,-5,-2],[4])
lvl_6=niveau(6,[4,-2,4,-3,-2,-5,-2],[10])
lvl_7=niveau(7,[5,-2,5,-4,-2,-5,-2,0,-2,-2,3,-2,1,-4,-2,-5,-2,2,-2,-2,1,-2,1,-4,-2],[0])

niveau=[lvl_0,lvl_1,lvl_2,lvl_3,lvl_4,lvl_5,lvl_6,lvl_7]

def selection_signal(niveau=0):
    global lvl
    lvl=niveau

def start():
    print("NOUS VENONS D'INTERCEPTER UN SIGNAL PROVENANT DE L'ESPACE PROFOND. CE MESSAGE REPETE EN BOUCLE LA MEME FREQUENCE : CELLE DE L'ATOME D'HYDROGENE. UTILISEZ LA RADIO ET ENVOYEZ DES SIGNAUX POUR TENTER DE RENTRER EN COMMUNICATION AVEC.")

def traduire(message,traduction):
            message_traduit=message.copy()
            for i in range(len(message_traduit)):
                if str(message_traduit[i]) in traduction:
                    message_traduit[i]=traduction[str(message_traduit[i])]
            return message_traduit

def afficher(message):
    for i in range(len(message)):
        print(message[i])

        
def code(message):
    return [i + 1420405752 for i in message]


def reception():

    return code(niveau[lvl].msg)

def envoyer(reponse):
    global lvl
    if lvl == 4:
        print("ON POURRAIT PEUT ETRE TRANSFORMER TOUS CES CHIFFRES AVANT DE CONTINUER POUR QUE CE SOIT PLUS LISIBLE ?")
        print("FAITES UNE FONCTION QUI VA RAMENER LES CHIFFRES A UNE ECHELLE PLUS LISIBLE (PAR EXEMPLE 0,1,2...) POUR QUE CE SOIT PLUS FACILE A LIRE ET A COMPRENDRE")
        print("POUR REVENIR AU NIVEAU SOUHAITE ENTRE LE NUMERO DU SIGNAL DANS LA FONCTION SELECTION_SIGNAL()")
    if lvl == 5:
        print("VOUS AVEZ PENSE A REMPLIR LE DICTIONNAIRE DE TRADUCTION ?")
    if lvl == 6:
            print("PEUT ETRE SERAIT-IL PLUS PRATIQUE DE PASSER A UNE BASE 10 ?")
        

    if reponse==code(niveau[lvl].reponse):
        lvl+=1
        print("#########################\nnouveau signal\n#########################")
        print(f"#########################\nsignal n°{lvl}\n#########################")
    else:
        print("pas de changement de signal")







