import datetime as dt #Importei a biblioteca datetime para fazer uso da data atual

def visitante(nome_input, cpf_input, email_input, tel_input, data_cad_input, data_nasc_input):# Inportante entender que todos
    # os esses parametros estão se tornando uma lista


    nome = nome_input
    cpf = cpf_input
    email = email_input
    telefone = tel_input
    data_cadastro = data_cad_input
    data_nascimento = data_nasc_input
    return [nome, cpf, email, telefone, data_cadastro, data_nascimento]


def porteiro (nome_input, senha_input, cpf_input):

    if nome_input.isalpha() and len(nome_input)>=2:
        nome = nome_input
        senha = senha_input
        cpf = cpf_input
        return [nome, senha, cpf]


def visita (rg_usuario, data, hora_entrada, hora_saida, motivo, seguranca):

    rg_user = rg_usuario
    data_visita = data
    h_entrada = hora_entrada
    h_saida = hora_saida
    motivo_visita = motivo
    responsavel = seguranca
    return [rg_user, data_visita,h_entrada, h_saida, motivo_visita,responsavel]


visitante = list()
while True:
    print("MENU".center(40,"#"))
    print("""
    Opção 1-> Cadastrar Visitante
    Opção 2-> Deletar visitante
    Opção 3-> Cadastrar visita
    Opção 4-> Cadastrar segurança
    Opção 5-> Listar visitas
    Opção 6-> Listar visitantes
    Opção 7-> sair do sistema
    """)

    opcao = input("Digite a opção desejada:")
    if opcao.strip() in ["1", "2", "3", "4", "5", "6"]:

        if opcao == "1":

            print("Cadastro de visitantes".center(30,"#"))


            lista = visitante(input("Nome:"), input("CPF:")),input("Email:"), input("Telefone:"),
            dt.datetime.today(),input("Data de nascimento:")


            visitantes.append(lista)

        elif opcao == "2":
            print("Deletar visitante".center(40,"#"))
            cpf_ddeletar = input("Digite o CPF de usuario que deseja deletar:")

            for id, visitante in enumerate(visitatntes):


                if visitante [1] == cpf_ddeletar:
                    visitantes.pop(id)


        elif opcao == "6":
            print(visitantes)

        if opcao == "7":
            break

     else:
         print("Não existe essa opção")



