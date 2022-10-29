G = 6.674e-11


m1 = float(input('Enter weight of first body (Kg): '))
m2 = float(input('Enter weight of second body (Kg): '))
r = float(input('Enter distance (m): '))


F = G * m1 * m2 / r**2


print('Gravitational Force = %f Newton' %(F))