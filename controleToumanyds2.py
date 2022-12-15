from PySide6 import QtWidgets
from PySide6 import QtGui
from math import floor


class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(400, 100)
        self.setWindowTitle("Video_calculate")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()

        self.layoutVer = QtWidgets.QVBoxLayout()
        self.layoutHor = QtWidgets.QHBoxLayout()

        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()

        self.layoutSV4 = QtWidgets.QVBoxLayout()

        self.layoutH5 = QtWidgets.QHBoxLayout()

        self.layoutSV6 = QtWidgets.QVBoxLayout()

        self.layoutH7 = QtWidgets.QHBoxLayout()

        self.layoutV1 = QtWidgets.QVBoxLayout()
        self.layoutV2 = QtWidgets.QVBoxLayout()
        self.layoutV3 = QtWidgets.QVBoxLayout()
        self.layoutV4 = QtWidgets.QVBoxLayout()
        self.layoutV5 = QtWidgets.QVBoxLayout()
        
        # self.layoutH8 = QtWidgets.QHBoxLayout()



    def create_widgets(self):


        self.lbl_image = QtWidgets.QLabel("une image")

        image = QtGui.QPixmap(r"C:\Users\snir\Pictures\camera.png")
        self.lbl_image.setPixmap(image)

        self.lbl_espace1 = QtWidgets.QLabel()
        self.lbl_espace2 = QtWidgets.QLabel()
        self.lbl_espace3 = QtWidgets.QLabel()
        self.lbl_espace4 = QtWidgets.QLabel()

        self.radioBt_duree = QtWidgets.QRadioButton("Durée")
        self.radioBt_hdd = QtWidgets.QRadioButton("HDD")

        self.lbl_taille = QtWidgets.QLabel("taille")
        self.LEdit_taille = QtWidgets.QLineEdit()
        self.LEdit_taille.setPlaceholderText("Saisir la taille")

        self.lbl_ips = QtWidgets.QLabel("IPS")
        self.LEdit_ips = QtWidgets.QLineEdit()
        self.LEdit_ips.setPlaceholderText("Saisir l'Ips")

        self.lbl_Hdd = QtWidgets.QLabel("Hdd")
        self.LEdit_Hdd = QtWidgets.QLineEdit()
        self.LEdit_Hdd.setPlaceholderText("Saisir l'Hdd")

        self.lbl_Dure = QtWidgets.QLabel("Durée")
        self.lbl_Jour = QtWidgets.QLabel("Jour")
        self.LEdit_Jour = QtWidgets.QLineEdit()
        
        self.lbl_Heures = QtWidgets.QLabel("Heures")
        self.LEdit_Heures = QtWidgets.QLineEdit()

        self.lbl_minute = QtWidgets.QLabel("minute")
        self.LEdit_minute = QtWidgets.QLineEdit()

        self.lbl_seconde = QtWidgets.QLabel("seconde")
        self.LEdit_seconde = QtWidgets.QLineEdit()

        # self.lbl_resultat = QtWidgets.QLabel("résultat")
        # self.LEdit_resultat = QtWidgets.QLineEdit()

        self.btn_calculer = QtWidgets.QPushButton("calculer")
        self.btn_exit = QtWidgets.QPushButton("exit")
        self.radioBt_hdd.setChecked(True)
        self.LEdit_Hdd.setDisabled(True)

    def addWigets_to_layouts(self):
        self.layoutVer.addLayout(self.layoutH0)
        self.layoutVer.addLayout(self.layoutH1)
        self.layoutVer.addLayout(self.layoutH2)
        self.layoutVer.addLayout(self.layoutH3)

        self.layoutHor.addLayout(self.layoutVer)
        self.layoutHor.addWidget(self.lbl_image)



        self.layoutH0.addWidget(self.radioBt_duree)
        self.layoutH0.addWidget(self.radioBt_hdd)

        self.layoutH1.addWidget(self.lbl_taille)
        self.layoutH1.addWidget(self.LEdit_taille)

        self.layoutH2.addWidget(self.lbl_ips)
        self.layoutH2.addWidget(self.LEdit_ips)
    
        self.layoutH3.addWidget(self.lbl_Hdd)
        self.layoutH3.addWidget(self.LEdit_Hdd)

        self.layoutSV4.addWidget(self.lbl_espace1)
        self.layoutSV4.addWidget(self.lbl_espace3)

        self.layoutV1.addWidget(self.lbl_Dure)

        self.layoutV2.addWidget(self.lbl_Jour)
        self.layoutV2.addWidget(self.LEdit_Jour)

        self.layoutV3.addWidget(self.lbl_Heures)
        self.layoutV3.addWidget(self.LEdit_Heures)

        self.layoutV4.addWidget(self.lbl_minute)
        self.layoutV4.addWidget(self.LEdit_minute)

        self.layoutV5.addWidget(self.lbl_seconde)
        self.layoutV5.addWidget(self.LEdit_seconde)

        self.layoutH5.addLayout(self.layoutV1)
        self.layoutH5.addLayout(self.layoutV2)
        self.layoutH5.addLayout(self.layoutV3)
        self.layoutH5.addLayout(self.layoutV4)
        self.layoutH5.addLayout(self.layoutV5)

        self.layoutSV6.addWidget(self.lbl_espace2)
        self.layoutSV6.addWidget(self.lbl_espace4)

        self.layoutH7.addWidget(self.btn_calculer)
        self.layoutH7.addWidget(self.btn_exit)

        self.layoutV.addLayout(self.layoutHor)
        # self.layoutV.addLayout(self.layoutH0)
        # self.layoutV.addLayout(self.layoutH1)
        # self.layoutV.addLayout(self.layoutH2)
        # self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutSV4)
        self.layoutV.addLayout(self.layoutH5)
        self.layoutV.addLayout(self.layoutSV6)
        self.layoutV.addLayout(self.layoutH7)
        # self.layoutV.addLayout(self.layoutH8)
       
        self.setLayout(self.layoutV)

    #;def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)

    def setup_connections(self):
        self.btn_exit.clicked.connect(quit)
        self.radioBt_duree.clicked.connect(self.duree)
        self.radioBt_hdd.clicked.connect(self.hdd)
        self.btn_calculer.clicked.connect(self.calculer)

    def duree(self):
        if self.radioBt_duree.isChecked():
            self.nettoyer()
            print("Activer")

            self.LEdit_Jour.setDisabled(True)
            self.LEdit_Heures.setDisabled(True)
            self.LEdit_minute.setDisabled(True)
            self.LEdit_seconde.setDisabled(True)
            self.LEdit_taille.setDisabled(False)
            self.LEdit_Hdd.setDisabled(False)



    def hdd(self):
        if self.radioBt_hdd.isChecked():
            self.nettoyer()
            print("Désactiver")

            self.LEdit_Jour.setDisabled(False)
            self.LEdit_Heures.setDisabled(False)
            self.LEdit_minute.setDisabled(False)
            self.LEdit_seconde.setDisabled(False)

            self.LEdit_Hdd.setDisabled(True)
            self.LEdit_taille.setDisabled(False)
    
    def calculer(self):
        if self.radioBt_duree.isChecked():
            print("duree")
            try:
                taille_float = float(self.LEdit_taille.text())
                ips_float = float(self.LEdit_ips.text())
                hdd_float = float(self.LEdit_Hdd.text())
                # resultat=(taille_float*ips_float*hdd_float)/(1024*1024)
                print("JE CALCULE")
            except:
                print("erreur de conversion")
                self.nettoyer()
            else:   
                duree_cal=(1024*1024*hdd_float)/(taille_float*ips_float)
                #ûprint("JE CALCULE")
                if duree_cal>=86400:
                    jour_float = str(floor(duree_cal/86400))
                    self

                #print("Résultat",duree_cal)

        elif self.radioBt_hdd.isChecked():
            print("hdd")
            try:
                taille_float = float(self.LEdit_taille.text())
                ips_float = float(self.LEdit_ips.text())
                jour_float = float(self.LEdit_Jour.text())
                heure_float = float(self.LEdit_Heures.text())
                minute_float = float(self.LEdit_minute.text())
                seconde_float = float(self.LEdit_seconde.text()) 
                # duree_en_sec = (jour_float*86400) + (heure_float *3600) +(minute_float *60) + seconde_float
                # print("la duree en sec",duree_en_sec)
                # resultat=(taille_float*ips_float*hdd_float)/(1024*1024)
                # print("JE CALCULE")
            except:
                print("erreur de conversion")
                self.nettoyer()
            else:   
                print("JE CALCULE")
                duree_en_sec = (jour_float*86400) + (heure_float *3600) +(minute_float *60) + seconde_float
                hdd_cal=(taille_float*ips_float* duree_en_sec)/(1024*1024)
                print("Résultat",hdd_cal)
                self.LEdit_Hdd.setText(str(hdd_cal))

        #     calculestockage=(resultat*1024*1024)/(self.LEdit_taille.text())


    # def calculer(self):
    #    if self.radioBt_duree.isChecked():
    #         try:
    #             taille_float = float(self.LEdit_taille.text())
    #             ips_float = float(self.LEdit_ips.text())
    #             hdd_float = float(self.LEdit_Hdd.text())
    #             # resultat=(taille_float*ips_float*hdd_float)/(1024*1024)
    #             print("JE CALCULE")
    #         except:
    #             print("erreur de conversion")
    #             self.nettoyer()
    #         else:   
    #             print("JE CALCULE")
    #             duree_cal=(1024*1024*hdd_float)/(taille_float*ips_float)
    #             print("Résultat",duree_cal)
        

    #     # if self.radioBt_hdd.isChecked():
    #     #     try:
    #     #         taille_float = float(self.LEdit_taille.text())
    #     #         ips_float = float(self.LEdit_ips.text())
    #     #         hdd_float = float(self.LEdit_Hdd.text())
    #     #         # resultat=(taille_float*ips_float*hdd_float)/(1024*1024)
    #     #         print("JE CALCULE")
    #     #     except:
    #     #         print("erreur de conversion")
    #     #         self.nettoyer()
    #     #     else:   
    #     #         print("JE CALCULE")
    #     #         duree_cal=(1024*1024*hdd_float)/(taille_float*ips_float)
    #     #         print("Résultat",duree_cal)

    #     # #     calculestockage=(resultat*1024*1024)/(self.LEdit_taille.text())
    #     #     print(resultat)



    def nettoyer(self):
        self.LEdit_Hdd.setText(" ")
        self.LEdit_ips.setText(" ")
        self.LEdit_taille.setText(" ")
        self.LEdit_Jour.setText(" ")
        self.LEdit_Heures.setText(" ")
        self.LEdit_minute.setText(" ")
        self.LEdit_seconde.setText(" ")


app = QtWidgets.QApplication([])
form = MaFenetre()
form.show()
app.exec()