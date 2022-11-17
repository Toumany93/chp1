from PySide6 import QtWidgets
# import sys

class MaFenetre1(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("Se connecter")
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

    def create_widgets(self):
        self.lbl_Login = QtWidgets.QLabel("Login")
        self.LEdit_Login = QtWidgets.QLineEdit("user")
        self.LEdit_Login.setPlaceholderText("Saisir votre Login")

        self.lbl_Password = QtWidgets.QLabel("Password")
        self.LEdit_Password = QtWidgets.QLineEdit("pass")
        self.LEdit_Password.setPlaceholderText("Saisir votre Password")

        self.btn_connect = QtWidgets.QPushButton("Se connecter")
        # self.btn_Quitter = QtWidgets.QPushButton("Quitter")
        self.lbl_disconnect = QtWidgets.QLabel("Déconnecté")

    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_Login)
        self.layoutH1.addWidget(self.LEdit_Login)

        self.layoutH2.addWidget(self.lbl_Password)
        self.layoutH2.addWidget(self.LEdit_Password)

        self.layoutH3.addWidget(self.btn_connect)
        # self.layoutH3.addWidget(self.btn_Quitter)
        self.layoutH4.addWidget(self.lbl_disconnect)

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
        # self.btn_Quitter.clicked.connect(quit)
        self.btn_connect.clicked.connect(self.se_connecter)
         
    def se_connecter(self):
        # self.LEdit_Nom.setText("")
        # print("essai méthode connect")
        if self.LEdit_Login.text() == "user" and self.LEdit_Password.text() == "pass":
            form1.hide()
            form2.show()
         
        else:
            print("Erreur de connexion")
            # self.lbl_disconnect.setText("Déconnecté")
            self.LEdit_Login.setText("")
            self.LEdit_Password.setText("")


class MaFenetre2(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("Disconnect")
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

    def create_widgets(self):
        # self.lbl_Login = QtWidgets.QLabel("Login")
        # self.LEdit_Login = QtWidgets.QLineEdit("user")
        # self.LEdit_Login.setPlaceholderText("Saisir votre Login")

        # self.lbl_Password = QtWidgets.QLabel("Password")
        # self.LEdit_Password = QtWidgets.QLineEdit("pass")
        # self.LEdit_Password.setPlaceholderText("Saisir votre Password")

        self.btn_disconnect = QtWidgets.QPushButton("Se déconnecter")
        # self.btn_Quitter = QtWidgets.QPushButton("Quitter")
        self.lbl_connect = QtWidgets.QLabel("Connecté")

    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.btn_disconnect)
       

       

      
        self.layoutH4.addWidget(self.lbl_connect)

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
        # self.btn_Quitter.clicked.connect(quit)
        self.btn_disconnect.clicked.connect(self.se_deconnecter)
         
    def se_deconnecter(self):
        form1.show()
        form2.hide()
        # self.LEdit_Nom.setText("")
        # print("essai méthode connect")
        # if self.LEdit_Login.text() == "user" and self.LEdit_Password.text() == "pass":
        #     self.lbl_disconnect.setText("deconnecté")
        #     self.btn_connect.setText("Se déconnecter")
        #     self.lbl_Login.hide()
        #     self.lbl_Password.hide()
        #     self.LEdit_Login.hide()
        #     self.LEdit_Password.hide()
        # else:
        #     print("Erreur de connexion")
        #     self.lbl_disconnect.setText("Déconnecté")
        #     self.LEdit_Login.setText("")
        #     self.LEdit_Password.setText("")



app = QtWidgets.QApplication([])

form1 = MaFenetre1()
form2 = MaFenetre2()
form1.show()
form2.hide()
app.exec()

    

# if __name__ == '__main__':
#     # Create the Qt Application
#     app = QtWidgets.QApplication([])
#     # Create and show the form
#     form1 = MaFenetre1()
#     form2 = MaFenetre2()
#     form1.show()
#     form2.hide()
#     # Run the main Qt loop
#     # sys.exit(app.exec())
#     app.exec()
