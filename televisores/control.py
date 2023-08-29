class Control:
    def __init__(self):
        self.tv = None

    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()

    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def turnOff(self):
        self.tv.turnOff()

    def turnOn(self):
        self.tv.turnOn()

    def getTv(self):
        return self.tv

    def setTv(self, tv):
        self.tv = tv

    def setCanal(self, canal):
        self.tv.setCanal(canal)

    def setVolumen(self, volumen):
        self.tv.setVolumen(volumen)