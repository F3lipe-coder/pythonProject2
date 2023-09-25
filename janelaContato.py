#-*- coding: utf-8 -*-
import PySimpleGUI as sg
from Variavel import *

def janelaContato():
    layout=[
        [
            sg.Image("img/logoAPP.png",
                     background_color="#2F6073"),

            sg.Push(background_color="#2F6073"),

            sg.Text("Contato",
                    background_color="#2F6073",
                    font=fonteTitulo),

            sg.Push(background_color="#2F6073")
        ],

        [
            sg.HSep()
        ],

        [
            sg.Text("Email",
                    background_color="#2F6073",
                    font=fontTexto,
                    size=10),

            sg.Input(size=(45, 50),
                     background_color="#FFFFFF",
                     font=fontTexto),

            sg.Text("Telefone",
                    background_color="#2F6073",
                    font=fontTexto,
                    size=10),

            sg.Input(size=20,
                     background_color="#FFFFFF",
                     font=fontTexto)
        ],

        [
            sg.HSep()
        ],

#Rua | Numero | CEP
        [
            sg.Text("Rua",
                    background_color="#2F6073",
                    font=fontTexto,
                    size=10),

            sg.Input(size=(45, 50),
                     background_color="#FFFFFF",
                     font=fontTexto),

            sg.Text("Numero",
                    background_color="#2F6073",
                    font=fontTexto,
                    size=10),

            sg.Input(size=10,
                     background_color="#FFFFFF",
                     font=fontTexto),

            sg.Text("CEP",
                    background_color="#2F6073",
                    font=fontTexto,
                    size=5),

            sg.Input(size=16,
                     background_color="#FFFFFF",
                     font=fontTexto),

            sg.Button("Buscar",
                      font=fontTexto)
         ],
# Bairro | Cidade | SP
        [
            sg.Text("Bairro",
                    background_color="#2F6073",
                    font=fontTexto,
                    size=10),

            sg.Input(size=(45, 50),
                     background_color="#FFFFFF",
                     font=fontTexto),

            sg.Text("Cidade",
                    background_color="#2F6073",
                    font=fontTexto,
                    size=10),

            sg.Input(size=25,
                     background_color="#FFFFFF",
                     font=fontTexto),

            sg.Text("Estado",
                    background_color="#2F6073",
                    font=fontTexto,
                    size=10),

            sg.Input(size=10,
                     background_color="#FFFFFF",
                     font=fontTexto)
        ],
    #Button Cadastrar e o Buscar
        [
            sg.Push(background_color=cor_fundo),

            sg.Button("Voltar",
                      font=fontTexto,
                      size=18),

            sg.Button("Cadastrar",
                      font=fontTexto,
                      size=18),

            sg.Push(background_color=cor_fundo)
        ]
    ]
    return sg.Window("Contato",
                     layout,
                     background_color="#2F6073")
