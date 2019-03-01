from PIL import Image

class Veljalit:
    def __init__(self):
        print('smidur veljalit')

    def veljalit_litur(self, bord):
        self.veljalitinn()

    def veljalitinn(self):
        #Bjóða upp á að velja leikmann -> sýna myndir -> velja leikmann ->næsta borð
        print('Veldu þann lit á Mínu sem þú vilt vera')
        Bla = Image.open('BlaMina.png')
        Bla.show()
        Bleik = Image.open('BleikMina.png')
        Bleik.show()
        Raud = Image.open('RaudMina.png')
        Raud.show()

        litur = input('Sláðu inn 1 fyrir bláa Mínu, 2 fyrir bleika Mínu og 3 fyrir rauða Mínu\n')
        if litur == '1':
            print('Þú ert blá Mína')
        if litur == '2':
            print('Þú ert bleik Mína')
        if litur == '3':
            print('Þú ert rauð Mína')

def main():
    pass

if __name__== '__main__':
    main()
else:
    print('þú ert innportuð í veljalit')
