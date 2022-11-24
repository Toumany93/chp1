from PySide6 import QtWidgets
from math import sqrt
import sys

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("calculer un discriminant")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()


    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()
        self.layoutH6 = QtWidgets.QHBoxLayout()
        self.layoutH7 = QtWidgets.QHBoxLayout()
        self.layoutH8 = QtWidgets.QHBoxLayout()
        self.layoutH9 = QtWidgets.QHBoxLayout()



    def create_widgets(self):
        self.lbl_coef_a= QtWidgets.QLabel("a")
        self.LEdit_coef_a = QtWidgets.QLineEdit()
        self.LEdit_coef_a.setPlaceholderText("a")


        self.lbl_coef_b = QtWidgets.QLabel("b")
        self.LEdit_coef_b = QtWidgets.QLineEdit()
        self.LEdit_coef_b.setPlaceholderText("b")


        self.lbl_lbl_coef_c = QtWidgets.QLabel("c")
        self.LEdit_coef_c = QtWidgets.QLineEdit()
        self.LEdit_coef_c.setPlaceholderText("c")


        self.btn_Effacer = QtWidgets.QPushButton("Effacer")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

        self.lbl_delta = QtWidgets.QLabel("Le resultat du discriminant est = ")
        self.lbl_valeur_delta = QtWidgets.QLabel(".......")

        self.lbl_x1 = QtWidgets.QLabel("La racine x1 est : ")
        self.lbl_x1_valeur = QtWidgets.QLabel(".......")

        self.lbl_x2 = QtWidgets.QLabel("La racines x2 est : ")
        self.lbl_x2_valeur = QtWidgets.QLabel(".......")
        
        self.lbl_message1= QtWidgets.QLabel(" ")
        self.lbl_message2 = QtWidgets.QLabel(".......")
        
        
        self.btn_Calculer = QtWidgets.QPushButton("Calculer")

        self.message = QtWidgets.QMessageBox()
        self.message.setText("Erreur de saisie")

        self.message1 = QtWidgets.QMessageBox()
        self.message1.setText("     le calcule proposer n'est pas possible,recommencer  *_* ")


    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_coef_a)
        self.layoutH1.addWidget(self.LEdit_coef_a)


        self.layoutH2.addWidget(self.lbl_coef_b)
        self.layoutH2.addWidget(self.LEdit_coef_b)


        self.layoutH3.addWidget(self.lbl_lbl_coef_c)
        self.layoutH3.addWidget(self.LEdit_coef_c)



        self.layoutH4.addWidget(self.btn_Calculer)
        self.layoutH4.addWidget(self.btn_Effacer)

        self.layoutH5.addWidget(self.lbl_delta)
        self.layoutH5.addWidget(self.lbl_valeur_delta)

        self.layoutH6.addWidget(self.lbl_x1)
        self.layoutH6.addWidget(self.lbl_x1_valeur)

        self.layoutH7.addWidget(self.lbl_x2)
        self.layoutH7.addWidget(self.lbl_x2_valeur)

        # self.layoutH8.addWidget(self.lbl_message1)
        # self.layoutH8.addWidget(self.lbl_message2)




        self.layoutH9.addWidget(self.btn_Quitter)
        

        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)
        self.layoutV.addLayout(self.layoutH6)
        self.layoutV.addLayout(self.layoutH7)

        # self.layoutV.addLayout(self.layoutH8)
        self.layoutV.addWidget(self.lbl_message2)

        self.layoutV.addLayout(self.layoutH9)

        self.setLayout(self.layoutV)

    def main_widget(self):
        self.widget = QtWidgets.QWidget(self)  
        self.widget.setLayout(self.layoutV)
        self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Effacer.clicked.connect(self.clear_Ledit)
        self.btn_Calculer.clicked.connect(self.calculer)


    def clear_Ledit(self):
        self.LEdit_coef_a.setText("")
        self.LEdit_coef_b.setText("")
        self.LEdit_coef_c.setText("")
        self.lbl_valeur_delta.setText(".....")
        self.lbl_x1_valeur.setText(".....")
        self.lbl_x2_valeur.setText(".....")


        
    def calculer (self):
        try :
        
            a = float(self.LEdit_coef_a.text())
            b = float(self.LEdit_coef_b.text())
            c = float(self.LEdit_coef_c.text())    
        except:
            self.clear_Ledit()
            self.message.show()
        
        else:

            if a == 0:
                self.clear_Ledit()
                self.message1.show()
                
        
            
            if b == 0:
                self.clear_Ledit()
                self.message1.show()
                
                discriminant = (b*b) -(4*a*c)
            self.lbl_valeur_delta.setText(str(discriminant))
            print(discriminant)

            if discriminant>0:
                racine1 = (-b -sqrt(discriminant))/(2*a)
                racine2 =(-b + sqrt(discriminant))/(2*a)
                self.lbl_x1_valeur.setText(str(racine1)) 
                self.lbl_x2_valeur.setText(str(racine2)) 
                self.lbl_message2.setText("               il y'a deux solutions reelles -_-")
                print(racine1)
                print(racine2)
                # print("il y'a deux solutions reelles -_-")

            elif discriminant == 0: 
                self.lbl_x1.setText("Une seule racine x0 = ")
                racine1 = (-b)/(2*a)
                self.lbl_x1_valeur.setText(str(racine1)) 
                self.lbl_message2.setText("                 il y'a qu'une solution :/")
                print(racine1)
                #print("il y'a qu'une solution :/")
                self.lbl_x2.hide()
                self.lbl_x2_valeur.hide()

            elif discriminant> 0 :
                racine1 = (-b - sqrt(discriminant)) / (2*a)
                racine2 = (-b + sqrt(discriminant)) / (2*a)
                self.lbl_x1_valeur.setText(str(racine1)) 
                self.lbl_x2_valeur.setText(str(racine2))
                self.lbl_message2.setText("                 il y'a deux solutions imaginaires :)")
                print(racine1)
                print(racine2)
            # print("il y'a deux solutions imaginaires :)")

                        


        
        # self.lbl_somme2.setText(str())
       
        # if resultat :



    
if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()
