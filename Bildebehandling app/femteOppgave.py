#for å kunne hente og redigere på bilde og importere de ulike fuksjonene
from PIL import Image, ImageFilter
import sys 
sys.path.append('c:\\Users\\danil\\OneDrive\\Informasjonsteknologi\\programmering 3\\Bildebehandling app')

#informasjon om filteret
print('Velkommen til femte filter')
print('Har for du muliheten til å få et blur bilde')

#har må brukeren skrive gå videre for å gå videre
gå_videre = input('for å gå videre skriv gå videre.')

#har vil en while løkke kjøres så lenge gå_videre ikke er lik gå_videre, der brukeren blir bet om å skrive gå videre
while gå_videre != 'gå videre':
 gå_videre = input('for å gå videre skriv gå videre.')

#vis gå_videre er lik gå videre, vi brukeren bli bet om hvilken bilde de vil bruke som vil redigeres av filteret jeg valgte
if gå_videre == 'gå videre':
 valg = input('skriv navnet til bilde du vil bruke og pass på at det er i samme mappe. Husk å skriv først Hvor filen befinner seg. f.eks. Bilder/.')
 image = Image.open(valg)
 blur_bilde = image.filter(ImageFilter.BLUR)
 blur_bilde.show()

 #har blir brukeren spurt om de vil lagre bilde eller ikke
 like_eller_ikke = input('likte du dette filtere skriv ja eller nei. vis svaret ditt er ja må du oppgi hvor du vil lagre bilde og oppgi hva vil du lagre det som.')

#vis like_eller_ikke er lik ja vil brukeren få muligheten til å lagre bilde og deretter vil skjeteOppgave bli importert
if like_eller_ikke == 'ja':
    lagre = input('hvor vil du lagre bilde?')
    blur_bilde.save(lagre)
    import skjeteOppgave

 #vis brukeren ikke vil lagre bilde vil skjeteOppgave bli importert   
elif like_eller_ikke == 'nei':
    import skjeteOppgave


