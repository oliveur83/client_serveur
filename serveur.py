import pickle
import socket
import threading, time

HEADER = 10
Format = 'Utf8'
host, port = ('', 15556)
# Création d’une socket (IPv4, TCP)
mySocket = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
mySocket.bind((host, port))
mySocket.listen()
# Identification IPv4 (IP, Port)
#mySocket.bind((host, port))
# nombre de rejet acceptés
# mySocket.listen(5)
mySocket.listen()
print('Le serveur est actif')
#numClient = 1

dic = {'A': '10001', 'B': '10010', 'C': '100000',
       'D': '10001', 'E': '10010', 'F': '100000',
       'G': '10001', 'H': '10010', 'I': '100000',
       'J': '10001', 'K': '10010', 'L': '100000',
       'M': '10001', 'N': '10010', 'O': '100000',
       'P': '10001', 'Q': '10010', 'R': '100000'}

while True:
    conn, adress = mySocket.accept()
    msg = pickle.dumps(dic)
    entente = bytes(f'{len(msg) : < {HEADER}}', 'Utf8')
    conn.send(entente+msg)

class ClientThread(threading.Thread) :
    def __int__(self, conn, adress):
        threading.Thread.__init__(self)
        self.conn = conn
        self.adress = adress
    def run (self) :
        file_name = self.conn.recv(2048).decode(Format)
        fp = open(file_name, 'rb')
        self.conn.send(fp.read())
        print("le fichier est envoyé")

"""
def clientTreatment(conn, adress, numClient) :
    print(f' {adress} est connceté')

    for i in range(10):
        time.sleep(1)
        msg = f'Etape {i}'
        conn.send(msg.encode(Format))
    time.sleep(1)
    msg = "FIN"
    conn.send(msg.encode(Format))
    print("Fin de la communication")
    conn.close()
"""
"""
numClient = 1

while True:
    print("Je suis en attente du client")
    conn, address = mySocket.accept()
    threadClient = ClientThread(conn, address)
    threadClient.start()
    #tClient = threading.Thread(target=clientTreatment(conn,address, numClient), args=(conn,address,numClient))
    print("Le client numéro {} s’est connecté".format(
        numClient))

    #thread pour lenvoie
    #tClient.start()

    #thread pour la reception

    numClient += 1
    # fermeture de la connexion
# fermeture du serveur
mySocket.close()
"""

"""
#a pas oublier
print("je suis en attente d'un client")
conn, adress = mySocket.accept()
threadClient = ClientThread(conn, adress)
threadClient.start()
threadClient.join()
conn.close()
"""