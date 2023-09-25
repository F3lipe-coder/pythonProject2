#-*- coding: latin-1 -*-

import PySimpleGUI as sg

layout=[
    [sg.Push(background_color="#FFFFFF"),sg.Text("LOGIN", font=("Helvetica ",20,"bold"),text_color="#E8BF58",background_color="#FFFFFF"),sg.Push(background_color="#FFFFFF")],
    [sg.Push(background_color="#FFFFFF"),sg.Image("fundo_tratado_novo.png"),sg.Push(background_color="#FFFFFF")],
    [sg.Image("dentro.png",background_color="#FFFFFF"),sg.Text("Login",size=7,background_color="#FFFFFF",text_color="#E8BF58",font=" roboto 20" ),sg.Input(size=20,background_color="#FFFFFF",font=" roboto 15", key="-LOGIN-")],
    [sg.Image("seguro.png",background_color="#FFFFFF"),sg.Text("Senha",size=7,background_color="#FFFFFF",text_color="#E8BF58", font=" roboto 20"),sg.Input(size=20,background_color="#FFFFFF",font=" roboto 15",password_char="*",key="-SENHA-" )],
    [sg.Push(background_color="#FFFFFF"),sg.Button("Entrar",size=10,font="arial 15",pad=25,mouseover_colors=("#FFFFFF","#FFE054"),button_color="#E8BF58",key="-BOTAO-"),sg.Push(background_color="#FFFFFF")]

]

window = sg.Window("Tela Login",layout,background_color="#FFFFFF",finalize=True)

while True:
    events,values = window.read()