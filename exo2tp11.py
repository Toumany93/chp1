from PySide6 import QtWidgets
import sys

class MaFenetre(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("Addition")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        self.main_widget()


    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.lbl_1nombre = QtWidgets.QLabel("1er nombre")
        self.LEdit_nombre1 = QtWidgets.QLineEdit()
        self.LEdit_nombre1.setPlaceholderText("Saisir votre nombre entier")


        self.lbl_2nombre = QtWidgets.QLabel("2ème nombre")
        self.LEdit_nombre2 = QtWidgets.QLineEdit()
        self.LEdit_nombre2.setPlaceholderText("Saisir votre nombre entier")

        self.btn_Effacer = QtWidgets.QPushButton("Effacer")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")
        self.lbl_message = QtWidgets.QLabel("La somme des deux nombre = ")
        self.lbl_somme = QtWidgets.QLabel(".......")
        self.btn_Calculer = QtWidgets.QPushButton("Calculer")

    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_1nombre)
        self.layoutH1.addWidget(self.LEdit_nombre1)


        self.layoutH2.addWidget(self.lbl_2nombre)
        self.layoutH2.addWidget(self.LEdit_nombre2)



        self.layoutH3.addWidget(self.btn_Calculer)
        self.layoutH3.addWidget(self.btn_Effacer)
        self.layoutH4.addWidget(self.lbl_message)
        self.layoutH4.addWidget(self.lbl_somme)
        self.layoutH5.addWidget(self.btn_Quitter)
        

        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)
        # self.setLayout(self.layoutV)

    def main_widget(self):
        self.widget = QtWidgets.QWidget(self)  
        self.widget.setLayout(self.layoutV)
        self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Effacer.clicked.connect(self.clear_Ledit)
        self.btn_Calculer.clicked.connect(self.calculer)
        
         
    def clear_Ledit(self):
        self.LEdit_nombre1.setText("")
        self.LEdit_nombre2.setText("")

    def calculer (self):
        resultat = int(self.LEdit_nombre1.text()) + int(self.LEdit_nombre2.text())
        self.lbl_somme.setText(str(resultat))
        print(resultat)





    

    

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()




    