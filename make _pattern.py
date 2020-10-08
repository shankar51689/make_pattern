n=int(input('Enter odd number'))
for i in range(n):
    for j in range(n):
        if(i==0):
            if(j>=0 and j<(n+1)//2):
                print('* ',end='')
            elif(j>=(((n+1)//2)-2) and j<(n-1)):
                print('  ',end='')
            else:
                print('*',end='')
        elif(i>=1 and i<(n//2)):
            if(j<(n//2)):
                print('  ',end='')
            elif(j>(n//2) and j<(n-1)):
                print('  ',end='')
            else:
                print('* ',end='')
        elif(i==(n//2)):
            print('* ',end='')
            
        elif(i>(n//2) and i<(n-1)):
            if(j==0 or j==(n//2)):
                print('* ',end='')
            else:
                print('  ',end='')
        else:
            if(j==0):
                print('* ',end='')
            elif(j>0 and j<(n//2)):
                print('  ',end='')
            else:
                print('* ',end='')
    print()
