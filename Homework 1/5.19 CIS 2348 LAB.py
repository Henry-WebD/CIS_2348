print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,
    "-": 0
}
print("")
print("Select first service:")
service1 = input()
print("Select second service:")
service2 = input()
print("")
print("Davy's auto shop invoice")
print("")
if service1 == "-":
    print("Service 1: No service")
else:
    print("Service 1: " + str(service1) + ", $" + str(services[service1]))
if service2 == "-":
    print("Service 2: No service")
else:
    print("Service 2: " + str(service2) + ", $" + str(services[service2]))
print("")
total = services[service1] + services[service2]
print("Total: $" + str(total))
