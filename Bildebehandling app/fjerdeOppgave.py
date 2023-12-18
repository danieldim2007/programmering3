#for å kunne hente og redigere på bilde og importere de ulike fuksjonene
from PIL import Image
import sys 
sys.path.append('c:\\Users\\danil\\OneDrive\\Informasjonsteknologi\\programmering 3\\Bildebehandling app')

#informasjon om filteret og et huske regle for brukeren

print('Velkommen til fjerde filter')
print('Har for du muliheten til å endre størrelsen på bilde')
print('Husk at størrelsen på et instagram bilde er 1080 gange 1080.')

#har må brukeren skrve 1080 gange 1080 for å endrestørrelse 
Endre_størrelse_på_bilde = input('Skriv 1080 gange 1080 for å endre størrelsen på bilde.')

#har vil en while løkke kjøre så lenge Endre_størrelse_på_bilde ikke er lik og brukeren vil bli bet om å skrive 1080 gange 1080
while Endre_størrelse_på_bilde != '1080 gange 1080':
  Endre_størrelse_på_bilde = input('Skriv 1080 gange 1080 for å endre størrelsen på bilde.')

#vis brukeren skrev 1080 gange 1080 vil de først få muligheten til å velge bilde de vil endre størrelse på
if Endre_størrelse_på_bilde == '1080 gange 1080':
  valg = input('skriv navnet til bilde du vil bruke og pass på at det er i samme mappe. Husk å skriv først Hvor filen befinner seg. f.eks. Bilder/.')
  img = Image.open(valg)
  ny_størrelse = img.resize((1080,1080))
  ny_størrelse.show()

  #har blir brukeren spurt om de vil lagre bilde eller ikke
  like_eller_ikke = input('likte du dette filtere skriv ja eller nei. vis svaret ditt er ja må du oppgi hvor du vil lagre bilde og oppgi hva vil du lagre det som:')

#vis like_eller_ikke er lik ja vil brukeren få muligheten til å lagre bilde og deretter vil femteOppgave bli importert
if like_eller_ikke == 'ja':
    lagre = input('hvor vil du lagre bilde?')
    ny_størrelse.save(lagre)
    import femteOppgave


 #vis brukeren ikke vil lagre bilde vil femteOppgave bli importert   
elif like_eller_ikke == 'nei':
    import femteOppgave

