prof=["Login", "Senha"]

print('====== <<< ''\033[1;96m''Sistema''\033[0;0m'' ======')
while True:
    prof[0]=input("Login: ")
    prof[1]=input("Senha: ")

    if prof[0] == "José" and prof[1] == "1234":
        print("     Bem-vindo ao sistema")
        break
    else:
        print("Usuário ou senha incorreto, tente novamente.")


print('====== <<< ''\033[1;96m''Alunos''\033[0;0m'' >>> ======')


aluno1=["Nome","nota 1","nota 2","nota 3"]

aluno1[0]="João"
aluno1[1]=float(input("Nota 1:"))
aluno1[2]=float(input("Nota 2:"))
aluno1[3]=float(input("Nota 3:"))

media=(aluno1[1]+aluno1[2]+aluno1[3])/3
print(media)

print(f"Nome:{aluno1[0]}")
print(f"Média:{media}")

if media>=7:
    print("Aprovado!")
else:
    print("Reprovado")
