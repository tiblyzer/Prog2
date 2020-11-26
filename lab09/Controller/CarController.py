class CarController:
    def readCarParameters(self,c):
        return c.getType() + "," + c.getRendszam() + "," + c.getEvjarat()

        pass

    def storeCarParameters(self,c,p_type,p_rendszam,p_evjarat):
        c.setType(p_type)
        c.setRendszam(p_rendszam)
        c.setEvjarat(p_evjarat)
        pass