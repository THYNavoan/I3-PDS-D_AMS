#parameter is the value that the funtion needed to make it work
#local is in
#global is out

def celsuis_to_fahrenheit(celcuis, round_to=1):
    far = celcuis * 9 / 5 + 32
    return far
celsuis_to_fahrenheit(0)
print(celsuis_to_fahrenheit(98),"*F")

def fahrenheit_to_celsuis(fahrenheit, round_to=1):
    cel = (fahrenheit-32) * 5 / 9
    return cel
fahrenheit_to_celsuis(0)
print(fahrenheit_to_celsuis(98.6), "*C")



def celsius_to_fahrenheit(c, round_to=1):
    """Convert degrees Celsius to degrees Fahrenheit."""
    return round(c * 9 / 5 + 32, round_to)


def fahrenheit_to_celsius(f, round_to=1):
    """Convert degrees Fahrenheit to degrees Celsius."""
    return round((f - 32) * 5 / 9, round_to)


print("\n  °C  |   °F")
print("------+-------")
for c in range(0, 101, 20):
#(X,Y,Z) X start, Y finish, Z is step

    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")

print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))

print(fahrenheit_to_celsuis(200, round_to=0))

