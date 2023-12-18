#for å kunne imporete de ulike funksjoenene 
import sys 
sys.path.append('c:/Users/danil/OneDrive/Informasjonsteknologi/programmering 3/Bildebehandling app')
#informasjon
print('velkommen til beldebehandlingsapp') 
print('her får du muligheten til å velge mellom seks forskjellige filtre og får muligheten til å manipulere bildene dine')
print('basert på hvilken filter du sender blir du sendt videre til neste filter. Vis du f.eks. velger blir du sendt til en, derettter til to, til tre, osv.')
print('Når du har gått gjennom alle filterne stopper programmet.')

# har får brukeren muligheten til å ta et valg
valg = int(input('hvilket filter vil du bruke?'))

# det er en statenment som hva er det som kommer til å skje vis vlag er lik 1
if valg == 1: 

     import førsteOppgave
 
   # det er en statenment som hva er det som kommer til å skje vis vlag er lik 2 
elif valg == 2: 

     import andreOppgave
 
# det er en statenment som hva er det som kommer til å skje vis vlag er lik 3
elif valg == 3: 

     import tredjeOppgave
    
 # det er en statenment som hva er det som kommer til å skje vis vlag er lik 4
elif valg == 4:
     import fjerdeOppgave

   
# det er en statenment som hva er det som kommer til å skje vis vlag er lik 5
elif valg == 5:
   
     import femteOppgave
    
    
# det er en statenment som hva er det som kommer til å skje vis vlag er lik 6
elif valg == 6:

     import skjeteOppgave

   

