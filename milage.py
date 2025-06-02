odometter=int(input("enter the odometer reading"))
fuel=int(input("the fuel in litres :"))            
reading=int(input("entre the reading"))
run=reading-odometter
mileage=run/fuel
print(mileage,"km per litre")