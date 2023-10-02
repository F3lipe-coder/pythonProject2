# -*- coding: utf-8 -*-
# Atividade. Criar uma tela que contenha:
#  --> Quatro(4) variáveis;
#   --> A interface do usuário deve possuir
# uma tabela que receba os dados das variáveis;
#     --> Salvar em txt.
import PySimpleGUI as sg

# ----------------------------------------
# Função para criação de uma tela de login
# ----------------------------------------
def tela_login():
    """
    Tela destina à cadastro de usuário ao
    pegar o login e senha

    :return: O nome da tela e o layout
    """
    sg.theme('DarkBlue')
    layout = [
        [
            sg.Text('Usuário')
        ],

        [
            sg.Input(key='usuario')
        ],

        [
            sg.Text('Senha')
        ],

        [
            sg.Input(key='senha',
                     password_char='*')
        ],

        [
            sg.Button('Login')
        ],

        [
            sg.Text('',
                    key='mensagem')
        ]
    ]
    return sg.Window('Login',
                     layout=layout)
# ----------------------------------------

window = tela_login()

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Login':
        senha_user = '1234'
        user = 'joao'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_user and usuario == user:
            window['mensagem'].update('Login realizado com sucesso!')
        else:
            window['mensagem'].update('senha ou usuario incorreto!')

