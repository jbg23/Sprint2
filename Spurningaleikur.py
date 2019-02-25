class Spurningaleikur:
    def __init__(self, gisk, svar):
          self.gisk = gisk
          self.svar = svar

spurningar_listi = [
     "Hvaða jólasveinn kemur fyrstur til byggða?\n(a) Stekkjastaur\n(b) Stúfur\n(c) Giljagaur\n(d) Kertasníkir\n",
     "Hvað heitir kærasti Mínu músar?\n(a) Mikki refur\n(b) Jenni\n(c) Mikki mús\n(d) Stuart litli\n",
     "Hvað heitir snjókarlinn í Frozen?\n(a) Guðmundur\n(b) Ingólfur\n(c) Ólafur\n(d) Snæfinnur\n",
     "Hvað heitir höfuðborg Danmerkur?\n(a) Árhús\n(b) Kaupmannahöfn\n(c) Stokkhólmur\n(d) Álaborg\n",
     "Hvaða dýr er merki hjá verslunarkeðjunni Bónus?\n(a) Köttur\n(b) Mús\n(c) Villisvín\n(d) Grís\n",
     "Í hvaða heimsálfu er Egyptaland?\n(a) Evrópa\n(b) Afríka\n(c) Asía\n(d) Eyjaálfa\n",
     "Hvað eru margar hliðar á trapissu?\n(a) Fimm\n(b) Fjórar\n(c) Þrjár\n(d) Núll\n",
     "Hvað heitir asninn í Shrek?\n(a) Asni\n(b) Eyrnaslapi\n(c) Fáviti\n(d) Fíóna\n",
     "Hvernig eru buxurnar hans bangsímon á litinn?\n(a) Rauðar\n(b) Bláar\n(c) Grænar\n(d) Hann er ekki í buxum\n",
     "Hvenær er þjóðhátíðardagur Íslendinga?\n(a) Fyrsta sunnudag í ágúst\n(b) 1.maí\n(c) 17.júní\n(d) 4.júlí\n",
]

spurningar = [
     Spurningaleikur(spurningar_listi[0], "a"),
     Spurningaleikur(spurningar_listi[1], "c"),
     Spurningaleikur(spurningar_listi[2], "c"),
     Spurningaleikur(spurningar_listi[3], "b"),
     Spurningaleikur(spurningar_listi[4], "d"),
     Spurningaleikur(spurningar_listi[5], "b"),
     Spurningaleikur(spurningar_listi[6], "b"),
     Spurningaleikur(spurningar_listi[7], "a"),
     Spurningaleikur(spurningar_listi[8], "d"),
     Spurningaleikur(spurningar_listi[9], "c"),
]

def spurningaleikur(spurningar):
     stig = 0
     fjspurninga = 0
     stig=0
     fjspurninga=0
     for spurning in spurningar:
         svar = input(spurning.gisk)
         if svar == spurning.svar:
             stig += 1
         fjspurninga += 1
         if stig == 4:
             print("Til hamingju! Þú náðir fjórum spurningum réttum og heldur því áfram í gegnum völundarhúsið.")
             break
     print("Þú náðir því miður ekki fjórum spurningum réttum og verður því að hefja leikinn aftur.")
spurningaleikur(spurningar)
#Hvernig gerum við þannig að við ef þú nærð ekki nógu mörgum stigum þá geturðu valið hvort þú viljir byrja aftur eða hætta?
