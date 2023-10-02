#-*- coding: utf-8 -*-
import PySimpleGUI as sg
from Variavel import *

def janelaLogin():
    layout = [
        [
            sg.Push(background_color="#2F6073"),

            sg.Image("img/fundoApp.png",
                     background_color="#2F6073"),

            sg.Push(background_color="#2F6073")
        ],
# ------------------------------------------------------------
#   Área login
#------------------------------------------------------------
        [
            sg.Image("img/dentro.png",
                     background_color="#2F6073"),

            sg.Text("Login",
                    size=7,
                    background_color="#2F6073",
                    text_color="#FFFFFF",
                    font=fontTexto),

            sg.Input(size=20,
                     background_color="#FFFFFF",
                     font=" roboto 15",
                     key="-LOGIN-")
        ],
# ------------------------------------------------------------
# Área senha
# ------------------------------------------------------------
        [
            sg.Image("img/seguro.png",
                     background_color="#2F6073"),

            sg.Text("Senha",
                    size=7,
                    background_color="#2F6073",
                    text_color="#FFFFFF",
                    font=" roboto 20"),

            sg.Input(size=20,
                     background_color="#FFFFFF",
                     font=" roboto 15",
                     password_char="*",
                     key="-SENHA-")
        ],
# ------------------------------------------------------------

# ------------------------------------------------------------
        [
            sg.Push(background_color="#2F6073"),

            sg.Button("Entrar",
                      size=10,
                      font="arial 15",
                      pad=25,
                      mouseover_colors=("#FFFFFF","#FFE054"),
                      button_color="#5AADBF",
                      key="-BOTAO-"),

            sg.Push(background_color="#2F6073")
        ],
# ------------------------------------------------------------

# ------------------------------------------------------------
        [
            sg.Push(background_color="#2F6073"),

            sg.Text("Recuperar Senha!",
                    background_color="#2F6073",
                    text_color="#5AADBF",
                    font=("Helvetica",12),
                    enable_events=True,
                    key="-CREATE_USER-"),

            sg.Push(background_color="#2F6073")
        ]
# ------------------------------------------------------------
    ]
    return sg.Window("Login",
                     layout,
                     background_color="#2F6073")

janela_login = janelaLogin()
janela_login.read()