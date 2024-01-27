from abc import ABC,abstractmethod
class  modalcar(ABC):
    @abstractmethod
    def Break():
        pass
    @abstractmethod
    def speed_up():
        pass
    @abstractmethod
    def speed_down(): 
        pass
class  BMW(modalcar):
    def __init__(self,speed=25,stop=True):
        self.speed = speed
        self.stop  =  stop

    def speed_up(self):
        self.speed+=25
        self.stop = False

    def Break(self):
        self.speed = 25
        self.stop = True   

    def speed_down(self):
        if not self.stop:
            self.speed -=25
            if self.speed ==25:
                self.stop = True
