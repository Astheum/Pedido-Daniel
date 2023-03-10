from tkinter import *
import os
import webbrowser

def link():
    os.startfile('https://astheum.github.io/Pedido-Daniel/')

def abrir_janela():
    janela02 = Tk()
    janela02.title('Alerta!!!')

    blankSpace = Label(janela02, text='     ')
    blankSpace.grid(column=0, row=0)

    mensagemHack02 = Label(janela02, text='Seu computador foi invadido, deseja reiniciar o computador?')
    mensagemHack02.grid(column=1, row=1)

    blankSpace = Label(janela02, text='     ')
    blankSpace.grid(column=2, row=2)

    blankSpace = Label(janela02, text='     ')
    blankSpace.grid(column=3, row=3)

    bt = Button(janela02, text='   Sim   ', command= abrir_janela)
    bt.grid(column= 2, row=3)

    blankSpace = Label(janela02, text='     ')
    blankSpace.grid(column=3, row=3)

    bt2 = Button(janela02, text='   Não   ', command= abrir_janela02)
    bt2.grid(column=4, row=3)
    
    blankSpace = Label(janela02, text='     ')
    blankSpace.grid(column=5, row=4)


def abrir_janela02():
    janela03 = Tk()
    janela03.title('Alerta!!!')

    blankSpace = Label(janela03, text='     ')
    blankSpace.grid(column=0, row=0)

    mensagemHack03 = Label(janela03, text='Precisamos de uma confirmação de email para prosseguirmos!')
    mensagemHack03.grid(column=1, row=1)

    blankSpace = Label(janela03, text='     ')
    blankSpace.grid(column=2, row=2)

    bt = Button(janela03, text='   Clique aqui   ', command= link)
    bt.grid(column= 2, row=3)
    
    blankSpace = Label(janela03, text='     ')
    blankSpace.grid(column=5, row=4)


janela01 = Tk()
janela01.title('Alerta!!!')

blankSpace = Label(janela01, text='     ',)
blankSpace.grid(column=0, row=0)

mensagemHack = Label(janela01, text='Suas informações correm perigo!')
mensagemHack.grid(column=1, row=1)

blankSpace = Label(janela01, text='     ',)
blankSpace.grid(column=2, row=2)

btLink = Button(janela01, text='Continuar', command= abrir_janela)
btLink.grid(column= 1, row=3)

blankSpace = Label(janela01, text='     ',)
blankSpace.grid(column=0, row=4)

janela01.mainloop()