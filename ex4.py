
# bai 4 ve variables and names
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
car_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = carpool_capacity/cars_driven # tra ve gia tri kieu float vi space_in_a_car la kieu float
# phep chia cho kieu float gia tri la kieu float

print()

print("there are ", cars,"cars available.")
print("there are olny", drivers, "drivers available.")
print("there will be ", car_not_driven, "empty cars today.")
print("we can transport ", carpool_capacity, "people today.")
print("we have ", passengers,"to carpool today.")
print("we need to put about ", average_passenger_per_car, "in each car.")
