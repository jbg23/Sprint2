from PIL import Image

class Veljalit:
    def __init__(self):
        print('smidur veljalit')

    def spurningar_litur(self, bord):
        self.bord = bord
        self.veljalitinn()

    def veljalitinn(self):
        #Bjóða upp á að velja leikmann -> sýna myndir -> velja leikmann ->næsta borð
        Bla = Image.open('BlaMina.png')
        Bla.show()
        Bleik = Image.open('BleikMina.png')
        Bleik.show()
        Raud = Image.open('RaudMina.png')
        Raud.show()

def main():
    pass

if __name__== '__main__':
    main()
else:
    print('þú ert innportuð í veljalit')
