import sys

# import para criar a tela principal
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

i=3

def stop():
    sit = 1
    return sit

def iniciar():
    i = stop()
    while(2 < i):
        print("Ativo")
        



# Acessar os sistema operacional
app = QApplication(sys.argv)

# Criação da janela
janela = QWidget()
janela.resize(500, 300)
janela.setWindowTitle("Aula PyQt6")

btn = QPushButton("Iniciar", janela)
btn.setGeometry(100, 100, 120,50)
btn.clicked.connect(iniciar)

le = QLineEdit("", janela)


janela.show()

app.exec()