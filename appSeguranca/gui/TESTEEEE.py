# -*- coding: utf-8 -*-
import PySimpleGUI as sg
from Variavel import *
from appPonto_prof.telaLogin_prof import janelaMenu, janelaBaterPonto
from appSeguranca.gui.janelaContato import janelaContato
from appSeguranca.gui.janelaFuncionario import janelaCadastrarFuncionario
from appSeguranca.gui.janelaListarFunci import janelaListarFuncionario
from appSeguranca.gui.janelaLogin import janelaLogin

telaLogin, telaCadastrar, telaContato, telaListarUsuarios, telaPonto, telaMenu = janelaLogin(), None, None, None, None, None

while True:
    window, events, values = sg.read_all_windows()
    if window == telaLogin and events == sg.WIN_CLOSED:
        break
    if window == telaLogin and events == "-ENTRAR-":
        nome = values["-LOGIN-"]
        senha = values["-SENHA-"]

#Vou varrer o txt

        if nome in ["carlos", "maria", "pedro"] and senha == "123":
            sg.Popup("Seja bem vindo! ", nome)
            telaMenu = janelaMenu()
            telaLogin.hide()
    if window == telaMenu and events == sg.WIN_CLOSED:
        break
    if window == telaMenu and events == "-CADASTRAR-":
        telaCadastrar = janelaCadastrarFuncionario()
        telaMenu.hide()

    if window == telaCadastrar and events == sg.WIN_CLOSED:
        nome = values["-NOME-"]
        cpf = values["-CPF-"]
        data_nascimento = values["-NASCIMENTO-"]
        cargo = values["-CARGOS-"]
        id = values["-ID_CONTATO-"]
        senha = values["radio1"]== True


#       telaCadastrar.hide()
#      telaMenu.un_hide()
    if window == telaCadastrar and events == "-VOLTAR-":
        telaMenu.un_hide()
        telaCadastrar.hide()
    if window == telaCadastrar and events == "-CONTATO-":
        telaContato = janelaContato()
    if window == telaContato and events == sg.WIN_CLOSED:
        telaContato.hide()
    if window == telaContato and events == "-VOLTAR-":
        telaContato.hide()

    if window == telaMenu and events == "-LISTAR-":
        telaListarUsuarios = janelaListarFuncionario()
        telaMenu.hide()
    if window == telaListarUsuarios and events == sg.WIN_CLOSED:
        telaListarUsuarios.hide()
        telaMenu.un_hide()
    if window == telaListarUsuarios and events == "-VOLTAR-":
        telaListarUsuarios.hide()
        telaMenu.un_hide()
    if window == telaMenu and events == "-BATER_PONTO-":
        telaPonto = janelaBaterPonto()
        telaMenu.hide()
    if window == telaPonto and events == sg.WIN_CLOSED:
        telaPonto.hide()
        telaMenu.un_hide()
    if window == telaPonto and events == "-VOLTAR-":
        telaPonto.hide()
        telaMenu.un_hide()
# destruido o arquivo tk usado para pegar as fontes
# root.destroy()
