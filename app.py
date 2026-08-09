import webview
from tkinter import *

# --- Seu Código Original Aqui ---
root = Tk()
root.title("Calculadora")
root.resizable(False,False)
root.geometry("400x400")
expressao = ""
operacao = StringVar()

def press(num):
    global expressao
    expressao = expressao + str(num)
    operacao.set(expressao)

def limpar():
    global expressao
    expressao = ""
    operacao.set("")

def teclaigual():
    try:
        global expressao
        total = str(eval(expressao))
        operacao.set(total)
        expressao = ""
    except:
        operacao.set(" error ")
        expressao = ""

entrada = Entry( textvariable=operacao,font=("Verdana", 15, ), bd = 12)
entrada.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.15)

butao7 = Button( text=' 7 ', fg='black', bg='gainsboro',  bd=3, command=lambda: press(7))
butao7.place(relx=0.1,rely=0.2,relheight=0.15,relwidth=0.15)
butao8 = Button( text=' 8 ', fg='black', bg='gainsboro',  bd=3, command=lambda: press(8))
butao8.place(relx=0.3,rely=0.2,relheight=0.15,relwidth=0.15)
butao9 = Button( text=' 9 ', fg='black', bg='gainsboro',  bd=3, command=lambda: press(9))
butao9.place(relx=0.5,rely=0.2,relheight=0.15,relwidth=0.15)

butao4 = Button( text=' 4 ', fg='black', bg='gainsboro',  bd=3, command=lambda: press(4))
butao4.place(relx=0.1,rely=0.4,relheight=0.15,relwidth=0.15)
butao5 = Button( text=' 5 ', fg='black', bg='gainsboro',  bd=3, command=lambda: press(5))
butao5.place(relx=0.3,rely=0.4,relheight=0.15,relwidth=0.15)
butao6 = Button( text=' 6 ', fg='black', bg='gainsboro',  bd=3, command=lambda: press(6))
butao6.place(relx=0.5,rely=0.4,relheight=0.15,relwidth=0.15)

butao1 = Button( text=' 1 ', fg='black', bg='gainsboro',  bd=3, command=lambda: press(1))
butao1.place(relx=0.1,rely=0.6,relheight=0.15,relwidth=0.15)
butao2 = Button( text=' 2 ', fg='black', bg='gainsboro',  bd=3, command=lambda: press(2))
butao2.place(relx=0.3,rely=0.6,relheight=0.15,relwidth=0.15)
butao3 = Button( text=' 3 ', fg='black', bg='gainsboro',  bd=3, command=lambda: press(3))
butao3.place(relx=0.5,rely=0.6,relheight=0.15,relwidth=0.15)

butao0 = Button( text=' 0 ', fg='black', bg='gainsboro',  bd=3, command=lambda: press(0))
butao0.place(relx=0.1,rely=0.8,relheight=0.15,relwidth=0.15)

decimal = Button( text='.', fg='black', bg='orange', command=lambda: press('.'),bd=3)
decimal.place(relx=0.3,rely=0.8,relheight=0.15,relwidth=0.15)

limpara = Button( text=' C ', fg='black', bg='red',  bd=3, command=limpar)
limpara.place(relx=0.5,rely=0.8,relheight=0.15,relwidth=0.15)

mais = Button( text=' + ', fg='black', bg='green', command=lambda: press("+"),bd=3)
mais.place(relx=0.7,rely=0.2,relheight=0.15,relwidth=0.15)

menos = Button( text='-', fg='black', bg='green', command=lambda: press("-"),bd=3)
menos.place(relx=0.7,rely=0.4,relheight=0.15,relwidth=0.15)

dividir = Button( text='/', fg='black', bg='green', command=lambda: press("/"),bd=3)
dividir.place(relx=0.7,rely=0.6,relheight=0.15,relwidth=0.15)

multiplicar = Button( text='*', fg='black', bg='green', command=lambda: press("*"),bd=3)
multiplicar.place(relx=0.7,rely=0.8,relheight=0.15,relwidth=0.15)

igual = Button(text=' = ', fg='black', bg='#FFD700',command=teclaigual)
igual.place(relx=0.86,rely=0.2,relheight=0.75,relwidth=0.1)

# --- Alteração para fazer funcionar como APP Web ---
# Em vez de root.mainloop(), iniciamos a janela do webview com o Tkinter dentro
def start_gui():
    root.mainloop()

# Criar a janela do navegador que exibirá o código Tkinter
window = webview.create_window("Calculadora Retrô", start_gui, width=430, height=450, resizable=False)
webview.start()
