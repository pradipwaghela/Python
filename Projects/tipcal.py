print("Welcome to tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tio would you like to give? 10,20, or 15? "))
ppl=int(input("How many people to spilit the bill? "))
tip_per=tip/100
tip_amt=bill*tip_per
bilwtip= bill + tip_amt
bill_per=bilwtip/ppl
fnbil=round(bill_per,2)
print(f" Bill per person is ${fnbil}")
