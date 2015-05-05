# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:56:25 2015

@author: davson
"""
import os

class Aluno:
    next = ""
    def __init__(self, name="", adress="", email=""):
        self.name = name
        self.adress = adress
        self.email = email
    def __str__(self):
        return "\nAluno: " + self.name + "\nEndereço:" + self.adress + "\nE-mail: " + self.email
   

primeiro = Aluno()
atual = primeiro
ultimo = primeiro

while True:
    os.system("clear")
    print "Escolha uma opção abaixo: "
    print "(1) Cadastrar um aluno "
    print "(2) Verificar os alunos "
    print "(3) Pesquisar por nome "
    print "(4) Sair do programa "
    option = raw_input("Digite sua escolha e dê enter ")
    
    if option == "1":
        os.system("clear")
        name = raw_input("Digite o nome do aluno: ")
        adress = raw_input("Digite o endereco do aluno: ")
        email = raw_input("Digite o e-mail do aluno: ")
        obj = Aluno(name, adress, email)
        if primeiro.name == "":
            primeiro = obj
            ultimo = primeiro
        else:
            ultimo.next = obj
            ultimo = ultimo.next
            
    elif option == "2":
        atual = primeiro
        while True:
            print atual
            if atual.next=="":
                break
            else:        
                atual = atual.next
        raw_input("Tecle para continuar")
        
    elif option == "3":
        atual = primeiro
        nome = raw_input("Digite o nome a ser pesquisado")
        while True:
            if nome == atual.name: print atual
            if atual.next == "":
                break;
            else:
                atual = atual.next
        raw_input("Tecle para continuar")                           
    elif option == "4":
        break;
