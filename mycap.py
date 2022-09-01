#task-1
rad=float(input('input the radius of the circle:'))
area=3.14*(rad**2)
print('the area of the circle with radius',rad,'is:',area)

#task-2
filename=input('input the filename:')
m=filename.split('.')
if m[-1]=='py':
    print('the extension of the file is:','python')
if m[-1]=='txt':
    print('the extension of the file is:','text')
if m[-1]=='dat':
     print('the extension of the file is:','binary')

