N = int( input( 'Введи размерность массива данных'))
bd = []
for i in range( N ):
    bd.append( int( input() ))

for i in range( len( bd )-1):
    j = i+1
    if bd[j] < bd[i]:
        k = bd[i]
        bd[i], bd[j] = bd[j], k

print( bd )
