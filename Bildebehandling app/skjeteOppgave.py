#for å kunne hente og redigere på bilde og importere de ulike fuksjonene
from PIL import Image, ImageOps
import sys 
sys.path.append('c:\\Users\\danil\\OneDrive\\Informasjonsteknologi\\programmering 3\\Bildebehandling app')

#informasjon om filteret
print('Velkommen til siste filter')
print('Har for du muliheten til å ta et polar bilde')

#har må brukeren skrive gå videre for å gå videre
gå_videre = input('for å gå videre skriv gå videre.')

#har vil en while løkke kjøres så lenge gå_videre ikke er lik gå_videre, der brukeren blir bet om å skrive gå videre
while gå_videre != 'gå videre':
 gå_videre = input('for å gå videre skriv gå videre.')

#vis brukeren skriver gå videre vil de få muligheten til å velge hvilken bilde de vil redigere som kommer til å behandles av funksjonen jeg valte
if gå_videre == 'gå videre':
 valg = input('skriv navnet til bilde du vil bruke og pass på at det er i samme mappe. Husk å skriv først Hvor filen befinner seg. f.eks. Bilder/.')
 img = Image.open(valg)
 image_andre = ImageOps.fit(img,(760,760))
ramme = Image.open('Bilder/polaroid-frame-PNG-6.png')
polar = ramme.convert("RGB")
polar.paste(image_andre,(64,64))
polar.show()

#har blir brukeren spurt om de vil lagre bilde eller ikke
like_eller_ikke = input('likte du dette filtere skriv ja eller nei. vis svaret ditt er  ja må du oppgi hvor du vil lagre bilde og oppgi hva vil du lagre det som.')

#vis like_eller_ikke er lik ja vil brukeren få muligheten til å lagre bilde og deretter vil førsteOppgave bli importert
if  like_eller_ikke == 'ja':
 lagre = input('hvor vil du lagre bilde?')
 polar.save(lagre)
 import førsteOppgave

#vis brukeren ikke vil lagre bilde vil førsteOppgave bli importert
if like_eller_ikke == 'nei':
  import førsteOppgave



 

  
