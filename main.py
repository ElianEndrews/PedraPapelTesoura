import tkinter
import random
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

#------------cores-------------
co0 = "#FFFFFF"   #branca
co1 = "#333333"   #preta
co2 = "#fcc058"   #laranja
co3 = "#fff873"   #amarela
co4 = "#34eb3d"   #verde
co5 = "#e85151"   #vermelha
fundo = "#3b3b3b"

global jogador
global pc
global rodadas
global pontos_jogador
global pontos_pc

pontos_jogador = 0
pontos_pc = 0
rodadas = 5


# logica do jogo

def jogar(j):
    global rodadas
    global pontos_jogador
    global pontos_pc
    
    
    if rodadas > 0 :
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        jogador = j
        
        app_pc['text'] = pc
        app_pc['fg'] = co1
        
        if jogador == pc:
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3
            
        elif jogador == 'Pedra' and pc == 'Papel':
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            
            pontos_pc += 10
        
        elif jogador == 'Papel' and pc == 'Tesoura':
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            
            pontos_pc += 10
        
        elif jogador == 'Tesoura' and pc == 'Pedra':
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            
            pontos_pc += 10
        
        elif jogador == 'Pedra' and pc == 'Tesoura':
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co5
            app_linha['bg'] = co0 
            
            pontos_jogador += 10  
            
        elif jogador == 'Papel' and pc == 'Pedra':
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co5
            app_linha['bg'] = co0  
            
            pontos_jogador += 10
            
        elif jogador == 'Tesoura' and pc == 'Papel':
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co5
            app_linha['bg'] = co0  
            
            pontos_jogador += 10       
        
        app_1_pontos['text'] = pontos_jogador
        app_2_pontos['text'] = pontos_pc
        rodadas -= 1
        
        if rodadas == 0:
            fim_do_jogo()
        
        
    else:
        app_1_pontos['text'] = pontos_jogador
        app_2_pontos['text'] = pontos_pc
        fim_do_jogo()    

# iniciar jogo

def iniciar_jogo():
    global icon_1
    global b_icon_1
    global icon_2
    global b_icon_2
    global icon_3
    global b_icon_3
    
    
    b_jogar.destroy()
    
    
    icon_1 = Image.open('imagens/pedra.png')
    icon_1 = icon_1.resize((50, 50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda: jogar('Pedra'), width=50, image= icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT )
    b_icon_1.place(x=15, y=60)

    icon_2 = Image.open('imagens/papel.png')
    icon_2 = icon_2.resize((50, 50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('Papel'), width=50, image= icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT )
    b_icon_2.place(x=95, y=60)

    icon_3 = Image.open('imagens/tesoura.png')
    icon_3 = icon_3.resize((50, 50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=50, image= icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT )
    b_icon_3.place(x=170, y=60)


# terminar o jogo

def fim_do_jogo():
    global rodadas
    global pontos_jogador
    global pontos_pc
    
    pontos_jogador = 0
    pontos_pc = 0
    rodadas = 5
    
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()
    
    resultado_jogador = int(app_1_pontos['text'])
    resultado_pc = int(app_2_pontos['text'])
    
    if resultado_jogador > resultado_pc :
        app_vencedor = Label(frame_baixo, text='Parabens, você ganhou', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co4)
        app_vencedor.place(x=5, y=60)
    elif resultado_jogador < resultado_pc :
        app_vencedor = Label(frame_baixo, text='Infelizmente você perdeu', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co5)
        app_vencedor.place(x=5, y=60) 
    else :
        app_vencedor = Label(frame_baixo, text='Foi um empate', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
        app_vencedor.place(x=5, y=60)       
    
    b_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text='Jogar', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE )
    b_jogar.place(x=5, y=151)
    
    def jogar_denovo() :
        app_1_pontos['text'] = '0'
        app_2_pontos['text'] = '0'
        app_vencedor.destroy()
        b_jogar_denovo.destroy()
        
        iniciar_jogo()
        
    b_jogar_denovo = Button(frame_baixo, command=jogar_denovo, width=30, text='Jogar denovo', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE )
    b_jogar_denovo.place(x=5, y=151)




janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)


frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column= 0, sticky=NW )

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column= 0, sticky=NW )

estilo = ttk.Style(janela)
estilo.theme_use('clam')

app_1 = Label(frame_cima, text='Você', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70,)
app_1_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0,)
app_1_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=50, y=20,)

app_pontos = Label(frame_cima, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_pontos.place(x=125, y=20,)


app_2_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=170, y=20,)
app_2 = Label(frame_cima, text='PC', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=205, y=70,)
app_2_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0,)

app_pc = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_pc.place(x=190, y=10)

app_linha = Label(frame_cima, text='', width=255, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)



b_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text='Jogar', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE )
b_jogar.place(x=5, y=151)

janela.mainloop()