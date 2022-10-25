csv=open('test.csv', 'w+')
cont=0
with open('test.csv', 'a+') as file:
    while(cont<10000):
        file.write(str(cont)+","+'\n')
        print(cont)
        cont+=1
with open('test.csv') as myfile:
    total_lines = sum(1 for line in myfile)
    print("Il y a", total_lines, "ligne")