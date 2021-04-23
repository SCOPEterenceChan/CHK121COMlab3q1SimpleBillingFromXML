def loanTable(loanAmount,annualInterestRate,monthlyPayment):

        month = 1
        startingBalance = loanAmount
        payment = monthlyPayment
        middleBalance = loanAmount - payment
        interest = middleBalance * annualInterestRate/12/100
        endingBalance = middleBalance + interest
        
        print("\n")
        print("%25s%30s%30s"%
              ("Starting","Middle","Ending"))
        print("%10s%15s%15s%15s%15s%15s"%
              ("Month","Balance","Payment","Balance","Interest","Balance"))
        print("-"*85)
              
        while startingBalance > 0:
            print("%10d%15.2f%15.2f%15.2f%15.2f%15.2f"%
              (month,startingBalance,payment,middleBalance,interest,endingBalance))
            month+=1
            startingBalance = endingBalance
            
            if endingBalance > monthlyPayment:
                payment = monthlyPayment
            else: payment = endingBalance
            
            middleBalance =  startingBalance - payment
            interest = middleBalance * annualInterestRate/12/100
            endingBalance = middleBalance + interest
            
def loanTableHTML(loanAmount,annualInterestRate,monthlyPayment):

        fileOut = open('loanTable.html','w')

        month = 1
        startingBalance = loanAmount
        payment = monthlyPayment
        middleBalance = loanAmount - payment
        interest = middleBalance * annualInterestRate/12/100
        endingBalance = middleBalance + interest

        fileOut.write('''
<table border=1>
<tr><th>Month</th><th>Starting <br />Balance</th><th>Payment</th><th>Middle <br />Balance</th>
<th>Interest</th><th>Ending<br /> Balance</th></tr>
''')
              
        while startingBalance > 0:
            fileOut.write("<tr align=right><td>%10d</td><td>%15.2f</td><td>%15.2f</td><td>%15.2f</td><td>%15.2f</td><td>%15.2f</td>"%
                          (month,startingBalance,payment,middleBalance,interest,endingBalance))
            month+=1
            startingBalance = endingBalance
            
            if endingBalance > monthlyPayment:
                payment = monthlyPayment
            else: payment = endingBalance
            
            middleBalance =  startingBalance - payment
            interest = middleBalance * annualInterestRate/12/100
            endingBalance = middleBalance + interest
            
        fileOut.write("</table>")
        fileOut.close()
