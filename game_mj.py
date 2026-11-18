import radio as R


############################################################################################################################################
############################################################################################################################################

R.selection_signal(6)


# ce dictionnaire tradution vous permet de traduire les messages reçus. Il est vide pour l'instant, mais vous pouvez le remplir avec les traductions que vous trouvez.

traduction={"-2":" ","-3":"+","-5":"="}

############################################################################################################################################
############################################################################################################################################










def play():
    while True:


############################################################################################################################################
############################################################################################################################################


        # notez que les messages arrivent sous forme de liste : [signal a, signal b, signal c, ...] contenant des nombres entiers.


        

                    
     

        def decode(message):
            return [i - 1420405752 for i in message]

        def code(message):
           return message + 1420405752




        reçu=R.reception()

        reçu=decode(reçu)

        reçu=R.traduire(reçu,traduction) #remplace les symboles du mesages par ce de votre dictionnaire de traduction

        R.afficher(reçu)      #affiche le message reçu et traduit


 #       reponse=(int(input()))  
        reponse=code(int(input()))


        R.envoyer([reponse])    #utilise la radio pour envoyer notre message aux aliens (entrez la fréquence du signal à envoyer)


#############################################################################################################################################
#############################################################################################################################################







    return

R.start()
play()