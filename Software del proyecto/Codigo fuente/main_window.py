from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox
from PySide2.QtGui import QBrush, QColor, QPen
from PySide2.QtCore import Slot
from tablero import Ui_MainWindow
from random import randint
from automata import AFD

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.ui.pushButton.clicked.connect(self.tirar_dado)
        self.boton = self.ui.pushButton
        self.random = self.ui.dado
        self.automata = AFD(qn=0)
        self.setWindowTitle('Serpientes y escaleras')
        self.i = 0

        self.pen = QPen()
        self.pen.setWidth(2)

        self.pen2 = QPen()
        self.pen2.setWidth(2)

        self.pen3 = QPen()
        self.pen3.setWidth(2)

        self.greenpen = QPen()
        self.greenpen.setWidth(2)

        self.green = QColor(0,250,154)
        self.greenpen.setColor(self.green)

        self.color = QColor(139, 0, 0)
        self.pen.setColor(self.color)

        self.color2 = QColor(0, 173, 181)
        self.pen2.setColor(self.color2)

        self.color3 = QColor(255, 255, 255)
        self.pen3.setColor(self.color3)

        for i in range(10, 361, 70):
            self.scene.addEllipse(600, i, 0, 0, self.pen, QBrush(self.color))
            self.scene.addEllipse(0, i, 0, 0, self.pen, QBrush(self.color))
            self.scene.addLine(600, i, 0, i, self.pen)
      
        for j in range(0, 601, 120):
            self.scene.addEllipse(j, 10, 0, 0, self.pen, QBrush(self.color))
            self.scene.addEllipse(j, 360, 0, 0, self.pen, QBrush(self.color))
            self.scene.addLine(j, 10, j, 360, self.pen)
        
        self.scene.addEllipse(35, 300, 50, 50, self.pen2, QBrush(self.color2))
        self.scene.addSimpleText('\n\n\n\t\t\t\t\t\t               FINAL')
           
    @Slot()
    def tirar_dado(self):
        #obtener numero aleatorio      
        random = randint(1,6)

        for j in range(random):
            self.automata.agregarSimboloEntrada(1) # agregar símbolos de entrada

        self.random.setText(f'Obtuviste: {random}')

        #mientras haya simbolos de entrada
        while self.i < len(self.automata.getSimbolosEntrada()):
            estado = self.automata.matriz[(self.automata.getEstadoActual(), self.automata.getSimboloEntrada(self.i))]

            self.dibujar_ficha()
            self.automata.setEstadoActual(estado)
            
            print(f'Estado actual q{self.automata.getEstadoActual()}')
            self.i+=1

        self.mostrar_alertas()

          
    def dibujar_ficha(self):
        if self.automata.getEstadoActual() == 0:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(35, 300, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(155, 300, 50, 50, self.pen2, QBrush(self.color2))
            
        elif self.automata.getEstadoActual() == 1:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(155, 300, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(275, 300, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 2:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(275, 300, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(395, 300, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 3:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(395, 300, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(515, 300, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 4:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(515, 300, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(515, 230, 50, 50, self.pen2, QBrush(self.color2))

            #si el símbolo de entrada es == 0, es una escalera
            elif self.automata.getSimboloEntrada(self.i) == 0:
                self.scene.addEllipse(515, 300, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(35, 160, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 5:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(515, 230, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(395, 230, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 6:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(395, 230, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(275, 230, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 7:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(275, 230, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(155, 230, 50, 50, self.pen2, QBrush(self.color2))

            #si el símbolo de entrada es == 0, es una escalera
            elif self.automata.getSimboloEntrada(self.i) == 0:
                self.scene.addEllipse(275, 230, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(275, 160, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 8:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(155, 230, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(35, 230, 50, 50, self.pen2, QBrush(self.color2))
            
            #si el símbolo de entrada es == 0, es una escalera
            elif self.automata.getSimboloEntrada(self.i) == 0:
                self.scene.addEllipse(155, 230, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(275, 90, 50, 50, self.pen2, QBrush(self.color2))
                    
        elif self.automata.getEstadoActual() == 9:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(35, 230, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(35, 160, 50, 50, self.pen2, QBrush(self.color2))

            #si el símbolo de entrada es == 0, es una serpiente
            elif self.automata.getSimboloEntrada(self.i) == 2:
                self.scene.addEllipse(35, 230, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(275, 300, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 10:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(35, 160, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(155, 160, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 11:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(155, 160, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(275, 160, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 12:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(275, 160, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(395, 160, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 13:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(395, 160, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(515, 160, 50, 50, self.pen2, QBrush(self.color2))

            #si el símbolo de entrada es == 2, es una serpiente
            elif self.automata.getSimboloEntrada(self.i) == 2:
                self.scene.addEllipse(395, 160, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(515, 230, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 14:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(515, 160, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(515, 90, 50, 50, self.pen2, QBrush(self.color2))
                
        
        elif self.automata.getEstadoActual() == 15:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(515, 90, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(395, 90, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 16:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(395, 90, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(275, 90, 50, 50, self.pen2, QBrush(self.color2))
            
            #si el símbolo de entrada es == 2, es una serpiente
            elif self.automata.getSimboloEntrada(self.i) == 2:
                self.scene.addEllipse(395, 90, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(395, 160, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 17:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(275, 90, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(155, 90, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 18:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(155, 90, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(35, 90, 50, 50, self.pen2, QBrush(self.color2))
            
            #si el símbolo de entrada es == 2, es una serpiente
            elif self.automata.getSimboloEntrada(self.i) == 2:
                self.scene.addEllipse(155, 90, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(35, 230, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 19:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(35, 90, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(35, 20, 50, 50, self.pen2, QBrush(self.color2))
            
            #si el símbolo de entrada es == 0, es una escalera
            elif self.automata.getSimboloEntrada(self.i) == 0:
                self.scene.addEllipse(35, 90, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(275, 20, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 20:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(35, 20, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(155, 20, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 21:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(155, 20, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(275, 20, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 22:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(275, 20, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(395, 20, 50, 50, self.pen2, QBrush(self.color2))
        
        elif self.automata.getEstadoActual() == 23:
            #si el símbolo de entrada es == 1
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(395, 20, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(515, 20, 50, 50, self.pen2, QBrush(self.color2))
            
            #si el símbolo de entrada es == 2, es una serpiente
            elif self.automata.getSimboloEntrada(self.i) == 2:
                self.scene.addEllipse(395, 20, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(515, 90, 50, 50, self.pen2, QBrush(self.color2))
                
        
        elif self.automata.getEstadoActual() == 24:
            #fin
            if self.automata.getSimboloEntrada(self.i) == 1:
                self.scene.addEllipse(515, 20, 50, 50, self.pen3, QBrush(self.color3))
                self.scene.addEllipse(515, 20, 50, 50, self.pen2, QBrush(self.color2))
                #self.scene.addEllipse(515, 20, 50, 50, self.pen2, QBrush(self.color2))
                #break
                            
        else:
            pass
    
    def mostrar_alertas(self):
        #es escalera
        if self.automata.getEstadoActual() == 4:
            self.automata.agregarSimboloEntrada(0)
            QMessageBox.information(
                self,
                'Escalera',
                f'Subiste a q10'
            )
            self.scene.addEllipse(515, 300, 50, 50, self.pen3, QBrush(self.color3))
            self.scene.addEllipse(35, 160, 50, 50, self.pen2, QBrush(self.color2))
            self.random.setText(f'')

        
        #es escalera
        elif self.automata.getEstadoActual() == 7:
            self.automata.agregarSimboloEntrada(0)
            QMessageBox.information(
                self,
                'Escalera',
                f'Subiste a q12'
            )
            self.scene.addEllipse(275, 230, 50, 50, self.pen3, QBrush(self.color3))
            self.scene.addEllipse(275, 160, 50, 50, self.pen2, QBrush(self.color2))
            self.random.setText(f'')

        
        #es escalera
        elif self.automata.getEstadoActual() == 8:
            self.automata.agregarSimboloEntrada(0)
            QMessageBox.information(
                self,
                'Escalera',
                f'Subiste a q17'
            )
            self.scene.addEllipse(155, 230, 50, 50, self.pen3, QBrush(self.color3))
            self.scene.addEllipse(275, 90, 50, 50, self.pen2, QBrush(self.color2))
            self.random.setText(f'')

        
        #es serpiente
        elif self.automata.getEstadoActual() == 9:
            self.automata.agregarSimboloEntrada(2)
            QMessageBox.warning(
                self,
                'Serpiente',
                f'Caiste a q1'
            )
            self.scene.addEllipse(35, 230, 50, 50, self.pen3, QBrush(self.color3))
            self.scene.addEllipse(155, 300, 50, 50, self.pen2, QBrush(self.color2))
            self.random.setText(f'')

        
        #es serpiente
        elif self.automata.getEstadoActual() == 13:
            self.automata.agregarSimboloEntrada(2)
            QMessageBox.warning(
                self,
                'Serpiente',
                f'Caiste a q5'
            )
            self.scene.addEllipse(395, 160, 50, 50, self.pen3, QBrush(self.color3))
            self.scene.addEllipse(515, 230, 50, 50, self.pen2, QBrush(self.color2))
            self.random.setText(f'')

        
        #es serpiente
        elif self.automata.getEstadoActual() == 16:
            self.automata.agregarSimboloEntrada(2)
            QMessageBox.warning(
                self,
                'Serpiente',
                f'Caiste a q13'
            )
            self.scene.addEllipse(395, 90, 50, 50, self.pen3, QBrush(self.color3))
            self.scene.addEllipse(395, 160, 50, 50, self.pen2, QBrush(self.color2))
            self.random.setText(f'')

        
        #es serpiente
        elif self.automata.getEstadoActual() == 18:
            self.automata.agregarSimboloEntrada(2)
            QMessageBox.warning(
                self,
                'Serpiente',
                f'Caiste a q9'
            )
            self.scene.addEllipse(155, 90, 50, 50, self.pen3, QBrush(self.color3))
            self.scene.addEllipse(35, 230, 50, 50, self.pen2, QBrush(self.color2))
            self.random.setText(f'')

        
        #es escalera
        elif self.automata.getEstadoActual() == 19:
            self.automata.agregarSimboloEntrada(0)
            QMessageBox.information(
                self,
                'Escalera',
                f'Subiste a q22'
            )
            self.scene.addEllipse(35, 90, 50, 50, self.pen3, QBrush(self.color3))
            self.scene.addEllipse(275, 20, 50, 50, self.pen2, QBrush(self.color2))
            self.random.setText(f'')

        
        #es serpiente
        elif self.automata.getEstadoActual() == 23:
            self.automata.agregarSimboloEntrada(2)
            QMessageBox.warning(
                self,
                'Serpiente',
                f'Caiste a q15'
            )
            self.scene.addEllipse(395, 20, 50, 50, self.pen3, QBrush(self.color3))
            self.scene.addEllipse(515, 90, 50, 50, self.pen2, QBrush(self.color2))
            self.random.setText(f'')
        
        elif self.automata.getEstadoActual() == 24:
            QMessageBox.information(
                        self,
                        'Felicidades',
                        f'Haz ganado!'
                    )
            
            self.close()
            print(f'Conjunto de símbolos de entrada: {self.automata.getSimbolosEntrada()}')
            input('Haz ganado!')
            




        