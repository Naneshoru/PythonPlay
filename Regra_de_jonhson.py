
Matrix1=[ [17,7],[42,10],[10,25],[12,32],[22,42],[20,24] ]
n=len(Matrix1)
tarefa=dict((i+1, Matrix1[i]) for i in range(0,n))
coluna1=[]
coluna2=[]
print("\n\t\tRegra de Jonhson.")

for j in range(1,n+1):
    if tarefa[j][0] < tarefa[j][1]:
        coluna1.append(j)
    else:
        coluna2.append(j)

for k in range(0, len(coluna1)):
    for j in range(0,len(coluna1)-1):
        if tarefa[coluna1[j]][0] >= tarefa[coluna1[j+1]][0]:
            aux=coluna1[j]
            coluna1[j]=coluna1[j+1]
            coluna1[j+1]=aux

for k in range(0,len(coluna2)):
    for j in range(0,len(coluna2)-1):
        if tarefa[coluna2[j]][1] <= tarefa[coluna2[j+1]][1]:
            aux=coluna2[j]
            coluna2[j]=coluna2[j+1]
            coluna2[j+1]=aux
            
print("\nResultado:",coluna1+coluna2)
