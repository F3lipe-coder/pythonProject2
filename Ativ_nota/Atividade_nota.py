# -*- coding: utf-8 -*-
# Atividade. Criar uma tela que contenha:
#  --> Quatro(4) variáveis;
#   --> A interface do usuário deve possuir
# uma tabela que receba os dados das variáveis;
#     --> Salvar em txt.

# -----------------------------------------------
# --> Começar o código - Import
# -----------------------------------------------
from PySimpleGUI import (
    Text, Input, Push,
    Table, CalendarButton, Window,
    Frame, Button, theme,
    WINDOW_CLOSED, popup, WIN_CLOSED
)

# -----------------------------------------------
# --> Variável
# -----------------------------------------------
tema = 'BrownBlue'


def lerTxt():
    with open("dados.txt", "r+") as file:
        lista = list()
        for linha in file:
            linha.replace("\n","")
            arquivo = linha.split(" ")
            lista.append(arquivo)
        return lista

# -----------------------------------------------
# --> Função para janela
# -----------------------------------------------
def janela_atividade():
    theme(tema)

    listar = [
        'Nome',
        'Email',
        'Tel.',
        'Data A.'
    ]

    layout_cima = [
        [
            Push(),
            Text('Cadastrar Funcionário',
                 size=(52, 1),
                 justification='c'),
            Push()
        ],
    ]

    layout_esquerda = [
        [
            Text('Nome:',
                 size=(12, 1)),
            Input(key='-nome-')
        ],

        [
            Text('Email:',
                 size=(12, 1)),
            Input(key='-email-')
        ],

        [
            Text('Tel.:',
                 size=(12, 1)),
            Input(key='-tel-')
        ],

        [
            Text('Data Admissão:',
                 size=(12, 1)),
            Input(key='-data-',
                  size=(33, 1),
                  readonly=True),
            CalendarButton('Calendario',
                           default_date_m_d_y=(1, 1, 2023),
                           format='%d_%m_%Y',
                           close_when_date_chosen=False,
                           target='-data-'
                           )
        ]
    ]

    layout_direita = [
        [
            Table(headings=listar,
                  values=[],
                  key='-tabela-',
                  justification='center',
                  def_col_width=12,
                  auto_size_columns=False
                  )
        ]
    ]

    layout_baixo = [
        [
            Button('FECHAR',
                   key='-fechar-'),
            Push(),
            Button('ATUALIZAR',
                   key='-atualizar-'),
            Push(),
            Button('CADASTRAR',
                   key='-cadastrar-')
        ]
    ]

    layout = [
        [
            Frame('',
                  layout_cima)
        ],

        [
            Frame('CONTATO',
                  layout_esquerda)
        ],

        [
            Frame('TABELA',
                  layout_direita,
                  size=(442, 200))
        ],

        [
            Frame('',
                  layout_baixo,
                  size=(442, 35))
        ]
    ]

    return Window('ATIVIDADE',
                  layout)


# -----------------------------------------------
# --> Lógica da janela
# -----------------------------------------------

janela = janela_atividade()

while True:
    eventos, valores = janela.read()
    match eventos:
        case '-cadastrar-':
            nome = valores['-nome-']
            email = valores['-email-']
            tel = valores['-tel-']
            data = valores['-data-']
            with open('dados.txt', 'a+') as arquivo:
                arquivo.write(f'{nome} {email} {tel} {data}\n')
                popup('REGISTRO REALIZADO!')
            janela['-tabela-'].update(values=lerTxt())
        case '-atualizar':
            janela['-tabela-'].update(values=lerTxt())
        case '-fechar-':
            break
janela.close()

