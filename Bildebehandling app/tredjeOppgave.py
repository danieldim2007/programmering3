#for å kunne hente og redigere på bilde og importere de ulike fuksjonene
from PIL import Image
import sys 
sys.path.append('c:\\Users\\danil\\OneDrive\\Informasjonsteknologi\\programmering 3\\Bildebehandling app')
#informasjon om filteret
print('velkommen til tredje filter meny! Har for du rotere bilde')
print('Du kan velge mellom 90 grader med klokka, 90 grader mot klokka eller 180 grader')

#har må brukeren skrive hvor mange grader de vil rotere bildet sitt
antall_grader = (input('Hvor mange grader vil du rotere bildet. Skriv 90 grader med klokka, 90 grader mot klokka eller 180 grader.'))

#vis de vil rotere 90 grader med klokka for de muligheten til å velge bilde de vil rotere og rotere det 90 grader med lokka
if antall_grader == '90 grader med klokka':
    valg = input('skriv navnet til bilde du vil bruke og pass på at det er i samme mappe. Husk å skriv først Hvor filen befinner seg. f.eks. Bilder/.')
    img = Image.open(valg)
    imgage = img.rotate(angle=90)
    imgage.show()

    #har blir brukeren spurt om de vil lagre bilde eller ikke
    like_eller_ikke = input('likte du dette filtere skriv ja eller nei. vis svaret ditt er  ja må du oppgi hvor du vil lagre bilde og oppgi hva vil du lagre det som:')

#vis de vil rotere 90 grader mot klokka for de muligheten til å velge bilde de vil rotere og rotere det 90 grader med lokka
elif antall_grader == '90 grader mot klokka':
     from PIL import Image
     valg = input('skriv navnet til bilde du vil bruke og pass på at det er i samme mappe. Husk å skriv først Hvor filen befinner seg. f.eks. Bilder/.')
     img = Image.open(valg)
     imgage = img.rotate(angle=-90)
     imgage.show()

     #har blir brukeren spurt om de vil lagre bilde eller ikke
     like_eller_ikke = input('likte du dette filtere skriv ja eller nei. vis svaret ditt er  ja må du oppgi hvor du vil lagre bilde og oppgi hva vil du lagre det som:')

#vis de vil rotere 180 grader for de muligheten til å velge bilde de vil rotere og rotere det 90 grader med lokka   
elif antall_grader == '180 grader':
     from PIL import Image
     valg = input('skriv navnet til bilde du vil bruke og pass på at det er i samme mappe. Husk å skriv først Hvor filen befinner seg. f.eks. Bilder/.')
     img = Image.open(valg)
     imgage = img.rotate(angle=180)
     imgage.show()

     #har blir brukeren spurt om de vil lagre bilde eller ikke
     like_eller_ikke = input('likte du dette filtere skriv ja eller nei. vis svaret ditt er  ja må du oppgi hvor du vil lagre bilde og oppgi hva vil du lagre det som:')    

#vis like_eller_ikke er lik ja vil brukeren få muligheten til å lagre bilde og deretter vil fjerdeOppgave bli importert
if like_eller_ikke == 'ja':
    lagre = input('hvor vil du lagre bilde?')
    imgage.save(lagre)
    import fjerdeOppgave

#vis brukeren ikke vil lagre bilde vil fjerdeOppgave bli importert  
elif like_eller_ikke == 'nei':
    import fjerdeOppgave




    

