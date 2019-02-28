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
    #Viltu velja lit?
    val=1
    if val==1:
        print('hallo')
        bord1= Veljalit()
        bord1.spurningar_litur(bord1)

#Runnar spurningaleik
def main():
    #þú ert á byrjunarreit
    #Gerðu fval fyrir framhaldið
    val=1
    if val==1:
        print('hallo')
        bord1= spurningaleikur()
        bord1.spurningar_bord1(bord1)


if __name__=='__main__':
    main()
