#for å kunne hente og redigere på bilde og importere de ulike fuksjonene
from PIL import Image
import sys 
sys.path.append('c:\\Users\\danil\\OneDrive\\Informasjonsteknologi\\programmering 3\\Bildebehandling app')

#informasjon om filteret
print('Velkommen til andre filter meny')

#har må brukeren skrive ja for å se filteren
gå_videre = input('For å se vår black and white filter skriv ja.')

#har vil en while løkke kjøre så lenge gå_videre ikke er lik ja
while gå_videre !='ja':
        gå_videre = input('For å vår black and white filter skriv ja.')


#har er det det som skjer vis gå_videre er lik ja, der brukeren får velge hvilken bilde skal behandles og filteret jeg brukte
if gå_videre == 'ja':
    from PIL import Image
    valg = input('skriv navnet til bilde du vil bruke og pass på at det er i samme mappe. Husk å skriv først Hvor filen befinner seg. f.eks. Bilder/.')
    image = Image.open(valg)
    redigert_bilde = image.getchannel('R')
    redigert_bilde.show() 

    #har blir brukeren spurt om de vil lagre bilde eller ikke
    like_eller_ikke = input('likte du dette filtere skriv ja eller nei. vis svaret ditt er ja må du oppgi hvor du vil lagre bilde og oppgi hva vil du lagre det som:')

#vis like_eller_ikke er lik ja vil brukeren få muligheten til å lagre bilde og deretter vil tredjeOppgave bli importert
if like_eller_ikke == 'ja':
    lagre = input('hvor vil du lagre bilde?')
    redigert_bilde.save(lagre)
    import tredjeOppgave

 #vis brukeren ikke vil lagre bilde vil tredjeOppgave bli importert   
elif like_eller_ikke == 'nei':
   import tredjeOppgave

