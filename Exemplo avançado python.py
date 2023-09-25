users = list()
login = set()

def lin():
    print("-"*36)
while True:
    print('====== <<< ''\033[1;96m''Atividade-Menu''\033[0;0m'' >>> ======')
    print('|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Cliente           |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Dados do Cliente            |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Entrar Cliente              |')
    print('|  [''\033[1;36m''4''\033[0;0m''] -------                     |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Sair                        |')
    lin()
    choice = input('\033[1;36m''Insira uma opção: ''\033[0;0m')
    lin()
    if choice == "1":
        register: str = input("Cadastre um usuário:")
        password: str = input("Cadastre uma senha:")
        user = [register, password]
        if len(user) != 0:
            for i in user:
                login.add(i[0])
            size = len(login)
            login.add(register)
            if len(login) == size:
                print("Login já cadastrado no sistema.")
            else:
                users.append(user)
        else:
            users.append(user)
    if choice == "2":
        print(users)
    if choice == "0":
        break
    if choice == "4":
        enter_login: str = input("Digite o login novamente:")
        enter_password: str = input("Digite a senha novamente:")
        for i in users:
            users.pop(i[0])