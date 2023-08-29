class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.control = None
        self.marca = marca
        self.estado = estado
        self.precio = 500
        self.volumen = 1
        self.canal = 1
        TV.numTV += 1

    def getCanal(self):
        return self.canal

    def setCanal(self, canal):
        if 120 >= canal >= 1 and self.estado:
            self.canal = canal

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        if 7 >= volumen >= 0 and self.estado:
            self.volumen = volumen

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getEstado(self):
        return self.estado

    def setPrecio(self, precio):
        self.precio = precio

    def getPrecio(self):
        return self.precio

    def turnOff(self):
        self.estado = False

    def turnOn(self):
        self.estado = True

    def canalUp(self):
        if (self.canal < 120 and self.estado):
            self.canal += 1

    def canalDown(self):
        if (self.canal > 1 and self.estado):
            self.canal -= 1

    def volumenUp(self):
        if self.volumen < 7 and self.estado:
            self.volumen += 1

    def volumenDown(self):
        if self.volumen > 0 and self.estado:
            self.volumen -= 1

    @staticmethod
    def setNumTV(num):
        TV.numTV = num

    @staticmethod
    def getNumTV():
        return TV.numTV
