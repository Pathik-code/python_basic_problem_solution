



# Take the input of the square matrix 
x, y = map(int, input('Enter matrix dimensions (x✗y): ').split(','))
print('No of rows:', x)
print('No of columns:', y)

i = 0
mat_str = ''
for i in range(x):
    if i == 0:
        mat_str += ' -' + ' '*(2*y - 1) + '-\n'
    mat_str += '|'
    for j in range(y):
        num = input(f'{mat_str} ')
        mat_str += f' {num}'
    mat_str += ' |\n'
    
mat_str += ' -' + ' '*(2*y - 1) + '-\n'
print(mat_str)



