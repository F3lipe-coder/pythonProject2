#-*- coding: utf-8 -*-
import PySimpleGUI as sg
from Variavel import *

def janelaCadastrarFuncionario():
    lista=["Gerente", "Supervisor", "Suporte", "Segurança"]
    layout = [

        [
            sg.Image("img/logoAPP.png",
                     background_color="#2F6073"),

            sg.Push(background_color="#2F6073"),

            sg.Text("CADASTRAR FUNCIONARIO",
                    background_color="#2F6073",
                    font=fonteTitulo),

            sg.Push(background_color="#2F6073")
        ],
# ------------------------------------------------------------

        [
            sg.HSep()
        ],
# ------------------------------------------------------------
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
# ------------------------------------------------------------
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

            sg.Combo(lista,
                     size=30,
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
# ------------------------------------------------------------
        [
            sg.HSep()
        ],
# ------------------------------------------------------------
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

            sg.Radio("ADM","radio1",
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

        [
            [
                sg.Text("Observações de uso: "
                        "\nCadastrar o nascimento use o calendario :"
                        "\nA senha deve ter 6 caracteres:"
                        "\nPara cadastrar o contato clique no icone:",
                        font=fontTexto,
                        background_color=cor_fundo)
            ],

            sg.Push(background_color=cor_fundo),

            sg.Image("img/fundoCadastro.png",
                     background_color=cor_fundo),

            sg.Push(background_color=cor_fundo)
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
    return sg.Window("Cadastro",
                     layout,
                     resizable=True,
                     background_color="#2F6073")