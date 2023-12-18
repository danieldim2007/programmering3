#for å kunne hente og redigere på bilde og importere de ulike fuksjonene
from PIL import Image, ImageEnhance
import sys 
sys.path.append('c:\\Users\\danil\\OneDrive\\Informasjonsteknologi\\programmering 3\\Bildebehandling app')

#informasjon om filteret
print('Velkonmmen til første filter meny! Har får du muligheten til å prøve et passende filter')

#har må brukeren skrive ja for å se filteren
gå_videre = input('For å filteren må skriv ja.')

#har vil en while løkke kjøre så lenge gå_videre ikke er lik ja
while gå_videre !='ja':
        gå_videre = input('For å se filteren skriv ja.')

#har er det det som skjer vis gå_videre er lik ja, der brukeren får velge hvilken bilde skal behandles og filteret jeg brukte
if gå_videre == 'ja':
    valg = input('skriv navnet til bilde du vil bruke og pass på at det er i samme mappe. Husk å skriv først Hvor filen befinner seg. f.eks. Bilder/.')
    image = Image.open(valg)
    første_filter = ImageEnhance.Color(image)
    redigert_bilde = første_filter.enhance(2)
    redigert_bilde.show()

#har blir brukeren spurt om de vil lagre bilde eller ikke
like_eller_ikke = input("likte du dette filtere skriv ja eller nei. vis svaret ditt er  ja må du oppgi hvor du vil lagre bilde og oppgi hva vil du lagre det som.")

#vis like_eller_ikke er lik ja vil brukeren få muligheten til å lagre bilde og deretter vil andreOppgave bli importert
if like_eller_ikke == 'ja':
    lagre = input('hvor vil du lagre bilde?')
    redigert_bilde.save(lagre)
    import andreOppgave

#vis brukeren ikke vil lagre bilde vil andreOppgave bli importert
elif like_eller_ikke == 'nei':
    import andreOppgave



    

