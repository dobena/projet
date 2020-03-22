
from threading import Thread


print("station de base!")




class StationBase(Thread):
    def __init__(self, id, position, tampon, puissanceMax, nbUEConnectés):
        Thread.__init__(self)
        self.id = id  # integer
        self.position = position # array
        self.tampon = tampon # Queue
        self.puissanceMax = puissanceMax# Double
        self.nbUEConnectés = nbUEConnectés   # integer
        print("La station de base est crée")
    # # methodes or functions
    def Reception_Message_1(self):
      print("Reception_Message_1")

    def Envoi_Message_2(self):
      print("Envoi_Message_2")

    def Reception_Message_3(self):
      print("Reception_Message_3")

    def Envoi_Message_4(self):
      print("Envoi_Message_4")

    def ecouterCanal(self):
      print("ecouterCanal")


