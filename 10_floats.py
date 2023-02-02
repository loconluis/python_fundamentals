x = 3.3
y = 1.1 + 2.2
print(x)
print(y)

print(x == y)

# formas de strings
y_string = format(y, ".2g")
print('str ==>', y_string)
print(y_string == str(x))

# Forma matematica
print('*******')
print(y, x)

tolerance = 0.00001
print(abs(x-y) < tolerance)