from veljalit import Veljalit
from Spurningaleikur import spurningaleikur

#Segja velkominn, viltu spila
#Velja lit á karakter
#Spila borðin

class inngangur:
    pass

    def tilbaka_inngangur(self):
        pass

#Runnar veljalit - virkar ekki
def main():
    byrja = input('Viltu spila leikinn? Sláðu inn 1 fyrir já eða 0 fyrir nei\n')
    #byrja = 1
    #Viltu velja lit?
    if byrja=='1':
        litur= Veljalit()
        litur.veljalit_litur(litur)

        #Viltu hefja leik? Já eða nei
        bord1= spurningaleikur()
        bord1.spurningar_bord1(bord1)


if __name__=='__main__':
    main()
