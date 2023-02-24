#6923621
#ADOMAKO-MENSAH YAW OWUSU
#COMPUTER APPLICATION ASSIGNMENT 3
#https://github.com/pxpxyaw/




Car =["Toyota Corolla","Toyota Yaris","Toyota Camry","Toyota Rav4","Toyota Highlander","Toyota Fortuner","Toyota Sienna","Toyota Land Cruiser Prado",
      "Toyota Hilux","Toyota Tundra","Toyota Tacoma","Toyota Sequoia","Toyota Matrix","Nissan Pathfinder",
      "Nissan Sentra","Nissan Maxima","Nissan Versa","Nissan Patrol","Nissan Titan","Nissan Frotier",
      "Hyundai Accent","Hyundai Elantra","Hyundai Tucson","Hyundai Sonata","Hyundai Santa Fe","Honda Civic","Honda Accord","Honda Pilot","Honda Odyssey",
      "Mercedes-Benz C-Class"]
Models=["2001","2005","2010","2015","2020"]
Price=[20000,40000,100000,150000,200000]
CarModelPrice=[]
print("Welcome to PY Car Dealership")
order=input("Which car would you like to buy?")
if order in Car:
   model=input("Please enter the model of the car you would like to buy.")
   if model in Models:
     if model=="2001":
      print("The price of the vehicle chosen is GHS",Price[0])
     elif model=="2005":
      print("The price of the vehicle chosen is GHS",Price[1])
     elif model=="2010":
      print("The price of the vehicle chosen is GHS",Price[2])
     elif model=="2015":
      print("The price of the vehicle chosen is GHS",Price[3])
     elif model=="2020":
      print("The price of the vehicle chosen is GHS",Price[4])
   else:
     print("This model is not available")
else:
 print("This vehicle is not available")
 
      
    