# bounce.py
#
# Exercise 1.5

bounces = 0
height = 100.0

while bounces < 10:
    bounces += 1
    height *= 0.6
    print(bounces, end=" ")
    print(round(height, 4))
