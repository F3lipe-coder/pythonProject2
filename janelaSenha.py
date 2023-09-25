#-*- coding: utf-8 -*-
import PySimpleGUI as sg
from Variavel import *

def janelaRecuperarSenha():
    layout = [
        [
            sg.Push(background_color="#2F6073"),

            sg.Image("img/mudarSenha.png",
                     background_color="#2F6073"),

            sg.Push(background_color="#2F6073")
        ],
# ------------------------------------------------------------
        [
            sg.Text("Entre com o seu CPF",
                    size=18,
                    text_color="#FFFFFF",
                    font=("Helvetica",12),
                    background_color="#2F6073"),

            sg.Input(key="-CPF-",
                     size=20,
                     background_color="#FFFFFF",
                     font="Helvetica 15")
        ],
# ------------------------------------------------------------
        [
            sg.Button("Recuperar Senha",
                      size=15,
                      font="arial 15",
                      pad=8,
                      mouseover_colors=("#FFFFFF","#FFE054"),
                      button_color="#5AADBF"),

            sg.Text("",
                    visible=False,
                    background_color="#2F6073",
                    text_color="#5AADBF")
        ]
# ------------------------------------------------------------
    ]
    return sg.Window("Recuperar Senha",
                     layout,
                     background_color="#2F6073")
janela_senha = janelaRecuperarSenha()