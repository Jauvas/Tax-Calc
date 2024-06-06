from datetime import date


cost = int(input('please enter the Cost of the car in $:\n'))
insurance = int(input('please enter the insurance in $:\n'))
freight = int(input('please enter the freight cost in $\n:'))
YOM = int(input('Year of manufacture:\n'))

currentYear = date.today().year

#age of vehicle
age = currentYear - YOM

#CIF is the customs Value
CIF = cost + insurance + freight

dollarRate = int(input('what is the current dollar rate?\n'))
CIFConversion = CIF * dollarRate


'''as per 2024, 
    Importduty=25%,
    VAT=18%,WithholdingTax=6%,
    Environmentallevy=50%(since the car is above 9 years since it was manufactured),
    Infrastructure levy = 1.5%     
'''

#import duty
importDuty = (25/100) * CIFConversion

#VAT
vat = (18/100) * (CIFConversion + importDuty)

#withholding tax
wht = (6/100) * CIFConversion

#infrastructural levy
iL = (1.5/100) * CIFConversion

#environmental levy
eL = (50/100) * CIFConversion

if(age < 9):
    totalTax = importDuty + vat + iL + wht
    print('Below 9 years')
else:
    totalTax = importDuty + vat + iL + wht + eL
    print('older than 9 years')


finalCost = CIFConversion + totalTax

print('CIF $',CIF, '\nCIF Conversion UGX', CIFConversion,
      '\nTotal Tax UGX:',totalTax,
      '\nFinal Cost UGX:',finalCost)