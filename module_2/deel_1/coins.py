# name of student: 
# number of student:
# purpose of program: 
# structure of program: 

coinValues = [500,200,100,50,20,10,5,2,1] # Soorten munten in  centen.

toPay = int(float(input('Amount to pay: '))* 100) # Convert integer naar float en vermedigvuldigen met 100, vraagt de gebruiker het bedrag om te betalen.
paid = int(float(input('Paid amount: ')) * 100) #  Convert integer naar float en vermedigvuldigen met 100, vraagt de gebruiker het bedrag om te betalen.
change = paid - toPay # toPay aftrekken met paid.

while change > 0 and len(coinValues) > 0: # Blijf dit codeblok herhalen zolang change en coinvalues groter is dan 0.

  coinValue = coinValues.pop(0) # Loopt door alle coinvalues van groot naar klein.
  nrCoins = change // coinValue # Kijkt naar hoeveel coins er in de overgebleven change kunnen

  if nrCoins > 0: # Als er 1 of meer munten zijn.
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Laat zien hoeveel coins en centen er returned moeten worden
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Vraagt de user hoeveel coins van een bepaalde cent hij/zij returned heeft.
    change -= nrCoinsReturned * coinValue # trek de number of coins returned af van de change en vermedigvuldig met coinvalue.

if change > 0: # Als er overgebleven change is.
  print('Change not returned: ', str(change) + ' cents') # Laat zien hoeveel change er niet returned kon worden.
else:
  print('done')