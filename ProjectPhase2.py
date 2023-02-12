#   Student Name: Radhika Jakka
#   CIS261
#   Project Phase 2
def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter from date (mm/dd/yyyy): ")
    todate = input("Enter to date (mm/dd/yyyy): ")
    return fromdate, todate
    
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay


def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00

    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        #write code to assign values to todate, empname, hours, hourlyrate, and taxrate from EmpLst
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        #print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        print()
        print("Name: ", empname)
        print("From Date: ",fromdate)
        print("To Date: ",todate)
        print("Hours Worked: ", f"{hours:,.2f}")
        print("Hurly Rate: ", f"{hourlyrate:,.2f}")
        print("Gross Pay: ", f"{grosspay:,.2f}")
        print("Tax Rate: ", f"{taxrate:,.2f}")
        print("Income Tax: ", f"{incometax:,.2f}")
        print("Net Pay: ", f"{netpay:,.2f}")
        print()
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        # the following line of code assigns TotEmployees totals to dictionary 
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGPay"] = TotGrossPay
        EmpTotals["TotTx"] = TotTax
        EmpTotals["TotNPay"] = TotNetPay


def PrintTotals(EmpTotals):    
    print()
    # use dictionary to print totals
    # the following line of code prints Total Employees from the dictionary
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    #print(f'Total Number Of Hours: {EmpTotals["TotEmp"]}')
    # write code to print TotalHrs, TotGrossPay, TotTax and TotNetPay from dictionary
    print(f'Total Number Of Hours: {EmpTotals["TotHrs"]}')
    print(f'Total GrossPay: {EmpTotals["TotGPay"]}')
    print(f'Total Tax: {EmpTotals["TotTx"]}')
    print(f'Total NetPay: {EmpTotals["TotNPay"]}')

if __name__ == "__main__":
    EmpDetailList = []
    EmpDetail_list = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        EmpDetailList.append(EmpDetail)

    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)
