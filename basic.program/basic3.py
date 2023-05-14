t=int(input("enter temperature in degree celcius"))
v=int(input("enter wind speed km"))
s=13.12 + 0.6215*t - 11.37*v**0.16 + 0.3965*t*v**0.16
print(round(s))
