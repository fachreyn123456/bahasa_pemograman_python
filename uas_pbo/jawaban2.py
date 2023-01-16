class Garden :
    def __init__(self) :
        self.anggrek = "Anggrek"
        self.mawar = "Mawar"
        self.melati = "Melati"

class Bunga :
    def __init__(self) :
        Garden.__init__(self)
        print(self.__Mawar)
        print("call class Mawar")
    
#call garden
obj = Garden()
print(obj.anggrek)