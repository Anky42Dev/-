import temperature as t
a = t.celsius_to_fahrenheit(0)
print(f'fahrenheit: {a}')
b = t.fahrenheit_to_celsius(32)
print(f'celsius: {b}')
from temperature import celsius_to_fahrenheit as c_to_f, fahrenheit_to_celsius as f_to_c
c = c_to_f(69)
print(c)
d = f_to_c(67)
print(d)
