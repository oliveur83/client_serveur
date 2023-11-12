import pickle
import socket
import sys

HEADER = 10
Format = 'Utf8'
host, port =('localhost',15556)
#Création d’une socket (IPv4, TCP)
mySocket = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
mySocket.connect((host, port))

msg_total = b''
entete_msg = True

while True:
    msg = mySocket.recv(16)
    if(entete_msg):
        print(f'nouveau message length : {msg[:HEADER]}')
        len_msg = int(msg[:HEADER])
        entete_msg = False
    msg_total += msg

    if(len(msg_total) - HEADER) == len_msg:
        print(" J'ai reçu un nouvel objet")
        dic = pickle.loads(msg_total[HEADER:])
        print(dic)
        msg = b''
        entete_msg = True
        mySocket.close()
        socket.close()

"""
try :
    #Demande de connexion au serveur
    mySocket.connect((host, port))
    print("Je suis connecté ...")

except :
    print("Il y a eu un problème de connexion")
    sys.exit()

while True:
    print("Donnez le nom du fichier")
    file_name = input(" >> ")
    mySocket.send(file_name.encode(Format))
    file_name = f'./{file_name}'

    file = mySocket.recv(9999999)
    with open(file_name, 'wh') as name:
        name.write(file)
    #msgServer = mySocket.recv(1024).decode(Format)
    #print(f"S> {msgServer}")
    print("Le fichier a été sauvegardé")

    break
    if msgServer.upper() == 'FIN' : break
mySocket.close()"""