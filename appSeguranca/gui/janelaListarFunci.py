#-*- coding: utf-8 -*-
import PySimpleGUI as sg
from Variavel import *

def janelaListarFuncionario():
    lista = [
        "Gerente",
        "Supervisor",
        "Suporte",
        "Segurança"
    ]

    top_tabela = [
        "Nome",
        "Nascimento",
        "CPF",
        "Cargo",
        "Telefone",
        "Nivel"
    ]

    valores = [[]]

    layout = [
        [
            sg.Image("img/logoAPP.png",
                     background_color="#2F6073"),

            sg.Push(background_color="#2F6073"),

            sg.Text("LISTAR FUNCIONARIO",
                    background_color="#2F6073",
                    font=fonteTitulo),

            sg.Push(background_color="#2F6073")
        ],

        [
            sg.HSep()
        ],

        [
            sg.Text("Nome",
                    background_color="#2F6073",
                    font=fontTexto,
                    size=10),

            sg.Input(size=(70,50),
                     background_color="#FFFFFF",
                     font=fontTexto),

            sg.Text("Nascimento",
                    background_color="#2F6073",
                    font=fontTexto),

            sg.Input(size=20,
                     background_color="#FFFFFF",
                     font=fontTexto),

            sg.Image("img/calendar.png",
                     background_color="#2F6073")
        ],

        [
            sg.Text("CPF",
                    background_color="#2F6073",
                    font=fontTexto,
                    size=10),

            sg.Input(size=20,
                     background_color="#FFFFFF",
                     font=fontTexto),

            sg.Text("Cargo",
                    background_color=cor_fundo,
                    font=fontTexto,
                    size=10),

            sg.Combo(lista,size=30,
                     default_value="Escolha o Cargos",
                     font=fontTexto,
                     button_arrow_color="#FFFFFF",
                     button_background_color="#2F6073"),

            sg.Text("Cadastrar Contato",
                    size=15,
                    font=fontTexto,
                    background_color=cor_fundo),

            sg.Image("img/contato.png",
                     background_color="#2F6073")
        ],

        [
            sg.HSep()
        ],

        [
            sg.Text("Senha",
                    size=10,
                    background_color=cor_fundo,
                    font=fontTexto),

            sg.Input(font=fontTexto,
                     size=15,
                     password_char='*'),

            sg.Text("Nivel",
                    font=fontTexto,
                    background_color=cor_fundo),

            sg.Radio("ADM",
                     "radio1",
                     font=fontTexto,
                     background_color=cor_fundo),

            sg.Radio("COMUM",
                     "radio1",
                     default=True,
                     font=fontTexto,
                     background_color=cor_fundo),

            sg.Push(background_color=cor_fundo),

            sg.Button("Cadastrar",
                      font=fontTexto,
                      size=20),

            sg.Push(background_color=cor_fundo)
        ],

        [
            sg.HSep()
        ],
       #Vai entrar uma tabela mostrando os usuarioas
        [
            sg.Table(headings=top_tabela,
                     values=valores)
        ],

        [
            sg.HSep()
        ],

        [
            sg.Push(background_color=cor_fundo),
            sg.Text("By: Rogério Sobral Ribeiro",
                    background_color=cor_fundo),
            sg.Push(background_color=cor_fundo)
        ]
    ]
    return sg.Window("Listar",
                     layout,
                     resizable=True,
                     background_color="#2F6073")



    return sg.Window("Menu", layout, resizable=False, background_color="#2F6073", finalize=True)

    telaLogin, telaCadastrar,telaContato,telaListarUsuarios, telaPonto,telaMenu = janelaLogin(),None,None,None, None, None

    while True:
       window,events, values = sg.read_all_windows()
       if window==telaLogin and events==sg.WIN_CLOSED:
           break
       if window==telaLogin and events=="-ENTRAR-":
           nome = values["-LOGIN-"]
           senha= values["-SENHA-"]
           if nome in ["carlos", "maria","pedro"] and senha == "123":
               sg.Popup("Seja bem vindo! ",nome)
               telaMenu=janelaMenu()
               telaLogin.hide()
       if window == telaMenu and events == sg.WIN_CLOSED:
           break
       if window == telaMenu and events == "-CADASTRAR-":
           telaCadastrar = janelaCadastrarFuncionario()
           telaMenu.hide()
       if window==telaCadastrar and events==sg.WIN_CLOSED:
           telaCadastrar.hide()
           telaMenu.un_hide()
       if window == telaCadastrar and events == "-VOLTAR-":
           telaMenu.un_hide()
           telaCadastrar.hide()
       if window == telaCadastrar and events == "-CONTATO-":
           telaContato=janelaContato()
       if window == telaContato and events==sg.WIN_CLOSED:
           telaContato.hide()
       if window == telaContato and events == "-VOLTAR-":
           telaContato.hide()

       if window==telaMenu and events=="-LISTAR-":
           telaListarUsuarios=janelaListarFuncionario()
           telaMenu.hide()
       if window== telaListarUsuarios and events==sg.WIN_CLOSED:
           telaListarUsuarios.hide()
           telaMenu.un_hide()
       if window == telaListarUsuarios and events=="-VOLTAR-":
           telaListarUsuarios.hide()
           telaMenu.un_hide()
       if window == telaMenu and events =="-BATER_PONTO-":
           telaPonto=janelaBaterPonto()
           telaMenu.hide()
       if window==telaPonto and events== sg.WIN_CLOSED:
           telaPonto.hide()
           telaMenu.un_hide()
       if window== telaPonto and events =="-VOLTAR-":
           telaPonto.hide()
           telaMenu.un_hide()
    # destruido o arquivo tk usado para pegar as fontes
    #root.destroy()