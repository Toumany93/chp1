from PySide6 import QtWidgets

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300, 100)
        self.setWindowTitle("              Toumany    ")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.mesdsgeBox = QtWidgets.QMessageBox()
        self.radioBt_IMC = QtWidgets.QRadioButton("IMC")
        self.radioBt_calculatrice = QtWidgets.QRadioButton("calculatrice")

        self.lbl_Taille = QtWidgets.QLabel("Taille")
        self.LEdit_Taille = QtWidgets.QLineEdit()
        self.LEdit_Taille.setPlaceholderText("Saisir votre Taille en cm........")
        
        self.lbl_poids = QtWidgets.QLabel("Poids")
        self.LEdit_poids = QtWidgets.QLineEdit()
        self.LEdit_poids.setPlaceholderText("Saisir votre Poids en kg........")

        self.lbl_message = QtWidgets.QLabel("L'IMC :")
        self.lbl_resultat = QtWidgets.QLabel("...")
       



        self.btn_calculer = QtWidgets.QPushButton("Calculer")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")
        self.radioBt_IMC.setChecked(True)
       

    def addWigets_to_layouts(self):

        self.layoutH0.addWidget(self.radioBt_IMC)
        self.layoutH0.addWidget(self.radioBt_calculatrice)

        self.layoutH1.addWidget(self.lbl_Taille)
        self.layoutH1.addWidget(self.LEdit_Taille)
        
        self.layoutH2.addWidget(self.lbl_poids)
        self.layoutH2.addWidget(self.LEdit_poids)

        self.layoutH3.addWidget(self.lbl_message)
        self.layoutH3.addWidget(self.lbl_resultat)

       
        self.layoutH4.addWidget(self.btn_calculer)
        self.layoutH4.addWidget(self.btn_Quitter)

        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)

    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.radioBt_IMC.clicked.connect(self.imc)
        self.radioBt_calculatrice.clicked.connect(self.calculatrice)
        self.btn_calculer.clicked.connect(self.calculer)

    def effacer(self):
        self.LEdit_poids.setText("")
        self.LEdit_Taille.setText("")
        self.lbl_resultat.setText("....")

    def calculer(self):
        if self.radioBt_IMC.isChecked():        
            try:
                poids = float(self.LEdit_poids.text())
                taille = float(self.LEdit_Taille.text())/100
            except:
                self.mesdsgeBox.setText("Erreur de conversion de la taille et le poids")
                self.effacer()
                self.mesdsgeBox.show()
            else:
                imc = poids/(taille**2)
                self.lbl_resultat.setText("{:.2f}".format(imc))
            if imc<18:
               self.mesdsgeBox.setText("Vous êtes trop maigre! ")
               self.mesdsgeBox.show()

            elif imc>=18 and imc < 25:
               self.mesdsgeBox.setText("Vous êtes Normal.")
               self.mesdsgeBox.show()

            elif imc>=25 and imc < 30:
               self.mesdsgeBox.setText("Vous êtes en surpoids.")
               self.mesdsgeBox.show()

            elif imc>=30 and imc < 35:
               self.mesdsgeBox.setText("Vous êtes comme Mario.")
               self.mesdsgeBox.show()

            elif imc>=35 :
               self.mesdsgeBox.setText("Vous êtes très obèse.")
               self.mesdsgeBox.show()    

        elif self.radioBt_calculatrice.isChecked():  
            try:
                nb1 = float(self.LEdit_poids.text())
                nb2 = float(self.LEdit_Taille.text())
            except:
                self.mesdsgeBox.setText("Erreur de conversion des deux nombres")
                self.effacer()
                self.mesdsgeBox.show()
            else:
                 self.lbl_resultat.setText("{:.2f}".format(nb1+nb2))


    def imc(self):
        if self.radioBt_IMC.isChecked():
            self.effacer()

        
            
            self.lbl_Taille.setText("Taille en cm")
            self.lbl_poids.setText("Poids en Kg : ")
            self.lbl_message.setText("L'IMC")
            self.LEdit_poids.setPlaceholderText("Saisir la poids en cm")
            self.LEdit_Taille.setPlaceholderText("Saisir le taille en kg")
            


    def calculatrice(self):
        if self.radioBt_calculatrice.isChecked():
            self.effacer()
            
            self.lbl_Taille.setText("Nombre 1 :")
            self.lbl_poids.setText("Nombre 2 :")
            self.lbl_message.setText("La somme :")
            self.LEdit_poids.setPlaceholderText("Saisir un nombre ")
            self.LEdit_Taille.setPlaceholderText("Saisir un nombre ")
           


app = QtWidgets.QApplication([])
form = MaFenetre()
form.show()
app.exec()