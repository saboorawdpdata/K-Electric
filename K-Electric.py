# scenario 2

# name=input("Enter your Name:")
# 
# 150-300 60rs per unit for commercial
# 150-300 40rs per unit for Domestic
# 
# 300-450 85rs per unit for commercial
# 300-450 60rs per unit for Domestic
# 
# 450-600 100rs per unit for commercial
# 450-600 80rs per unit for Domestic

name=input("Enter your name:")

cust_t=int(input(f"Dear {name} Which Customer type are you? \nPress 1. for Commercial \nPress 2. for Domestic: \n"))

if cust_t==1: #commercial
    print(f"Customer Type: Commercial \nInvoice Name: {name}")
    units=int(input("Number of units you consumed?:"))
    if units>=450 and units<800:
        print(f"Dear {name}  \nAs per your {units}  \nYou will be charged as Rs100/Unit for commercial \nYour Bill of Electricity for Current Month is \nRs{units*100}")
    elif units>=300 and units<450:
        print(f"Dear {name}  \nAs per your {units}  \nYou will be charged as Rs85/Unit for commercial \nYour Bill of Electricity for Current Month is \nRs{units*85}")
    
    elif units<300:
        print(f"Dear {name}  \nAs per your {units}  \nYou will be charged as Rs65/Unit for commercial \nYour Bill of Electricity for Current Month is \nRs{units*65}")
    else:
        print(f"Dear {name}  \nAs per your {units}  \nYou will be charged as Rs150/Unit for commercial \nYour Bill of Electricity for Current Month is \nRs{units*150}"

elif cust_t==2:   #domestic
    print(f"Customer Type: Domestic \nInvoice Name: {name}")
    units=int(input("Number of units you consumed?:"))
    if units>=450 and units<800:
        print(f"Dear {name}  \nAs per your {units}  \nYou will be charged as Rs80/Unit for commercial \nYour Bill of Electricity for Current Month is \nRs{units*80}")
    elif units>=300 and units<450:
        print(f"Dear {name}  \nAs per your {units}  \nYou will be charged as Rs60/Unit for commercial \nYour Bill of Electricity for Current Month is \nRs{units*60}")
    
    elif units<300:
        print(f"Dear {name}  \nAs per your {units}  \nYou will be charged as Rs40/Unit for commercial \nYour Bill of Electricity for Current Month is \nRs{units*40}")
    else:
        print(f"Dear {name}  \nAs per your {units}  \nYou will be charged as Rs100/Unit for commercial \nYour Bill of Electricity for Current Month is \nRs{units*100}"
              
              
             