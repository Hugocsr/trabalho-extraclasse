entrada = int(input())
lista28 =['FEV']
lista30 = ['ABR','JUN','SET','NOV']
lista31 = ['JAN','MAR','MAI','JUL','AGO','OUT','DEZ']

for i in range(entrada):
    entrada2 = input()
    k = entrada2.split(' ')
    k[1]=k[1][:3]
    if k[0] in lista31:
        if k[1] == 'SEG' or k[1] =='TER' or k[1]=='QUA':
            print(8)
        elif k[1] =='DOM' or k[1]=='QUI':
            print(9)
        else:
            print(10)
    elif k[0] in lista30:
        if k[1] =='SEG' or k[1]=='TER' or k[1]=='QUA' or k[1]=='QUI':
            print(8)
        elif k[1]=='SEX' or k[1]=='DOM':
            print(9)
        else:
            print(10)
    else:
        print(8)
