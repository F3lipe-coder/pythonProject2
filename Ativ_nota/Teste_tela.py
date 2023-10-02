#-*- coding: utf-8 -*-
import PySimpleGUI as sg
sg.theme("DarkGrey3")

# Criar uma tela de cadastro, nesta tela vai ter uma tabela
# Deve pegar os dados da tela salvar em um txt
# Depois ler esse txt e mostrar os valores na tabela

# Cadastro de despesas:

# descrição da despesa; =>
# valor da despesa; =>
# data da despesa; =>


# Criando TxT
def lerTxt():
    with open("dados.txt", "r+") as file:
        lista = list()
        for linha in file:
            linha.replace("\n","")
            arquivo = linha.split(" ")
            lista.append(arquivo)
        return lista

def tela():
    cabecalho = [
        "Descrição Desp.",
        "Valor Desp.",
        "Data Desp."
    ]

    layout=[
        [
            sg.Text("Descrição Desp:",
                    size=(12,1)),

            sg.Input(key="-DESC.DESP-")
        ],

        [
            sg.Text("Valor Desp:",
                    size=(12,1)),

            sg.Input(key="-VAL.DESP-")
        ],

        [
            sg.Text("Data Desp:",
                    size=(12,1)),

            sg.Input(key="-DT.DESP-",
                     readonly=True,
                     size=(20, 1)
                     ),

            sg.CalendarButton("Calendario",
                              default_date_m_d_y=(1, 1, 2023),
                              format="%d_%m_%Y",
                              close_when_date_chosen=False,
                              target="-DT.DESP-"
                              ),

            sg.Push(),

            sg.VerticalSeparator(),

            sg.Push(),

            sg.Button("Cadastrar",
                      key="-CADASTRAR-")
        ],

        [
            sg.HSep()
        ],

        [
            sg.Table(headings=cabecalho,
                     values=[],
                     key="-TABELA-")
        ]

    ]

    return  sg.Window("Tela", layout,finalize=True, element_justification="l")

janela=tela()

while True:
    events, values = janela.read()

    match events:
        case "-CADASTRAR-":
            descricao = values["-DESC.DESP-"]
            valor = values["-VAL.DESP-"]
            data = values["-DT.DESP-"]
            with open("dados.txt", "a+") as arquivo:
                arquivo.write(f"{descricao} {valor} {data}\n")

            janela["-TABELA-"].update(values=lerTxt())

        case sg.WIN_CLOSED:
            break
janela.close()

match open('dados.txt'):
    case _ if [_]:
        print(1)