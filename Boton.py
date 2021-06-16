# Importar los GUI widgets que se van a usar
from guizero import App, TextBox, PushButton, Text, info
import socket

prendo = 'p'
apago = 'a'

# La direccion IP esta hardcodeada

DIR = ("192.168.2.120", 10000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(DIR)


app = App(width=500, height=500, layout="grid")

# Definiciones de funcion para los eventos
def btn_prender_clicked():
    lbl_name.value = "Prendido"
    s.send(prendo.encode("ascii"))
    

def btn_apagar_clicked():
    lbl_name.value = "Apagado"
    s.send(apago.encode("ascii"))

# GUI widgets

lbl_name = Text(app, text="Apagado", grid=[0,0])
btn_prender = PushButton(app, command=btn_prender_clicked, text="Prender", grid=[1,0])
btn_apagar = PushButton(app, command=btn_apagar_clicked, text="Apagar", grid=[1,1])

# Mostrar GUI en la pantalla

app.display()




