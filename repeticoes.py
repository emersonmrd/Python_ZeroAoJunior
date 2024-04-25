#Repetições

#for -> loop que percorre sequências, repetindo ações para cada elemento.
#while -> loop que executa ações enquanto a condição for verdadeira.

#for x in range(10):
    #print(x)

#while True:
    #print("Se eu rodar o script meu pc morre")

notas = []

#contador = 1
#while contador <=5:

for x in range(5):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    
    #alternativa: contadpr += 1
    #contador = contador +1

print("Qunatidade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota:", nota)