from PySide6 import QtWidgets
import socket
import uuid
import platform
import os
from requests import get


import requests






class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300, 100)
        self.setWindowTitle("BTS SNIR2 - QDialog")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        

    def create_layouts(self):
        self.monFormulaire = QtWidgets.QFormLayout()
        self.setLayout(self.monFormulaire)

    def create_widgets(self): 
        self.lbl_titre = QtWidgets.QLabel("Computer informations")
        
        self.LEdit_hostname = QtWidgets.QLineEdit()
        self.LEdit_hostname.setText(socket.gethostname())
        self.LEdit_hostname.setDisabled(True)

        self.LEdit_LanIpAddress = QtWidgets.QLineEdit()
        lan= socket.gethostbyname(socket.gethostname())
        self.LEdit_LanIpAddress.setText(lan)
        self.LEdit_LanIpAddress.setDisabled(True)
        
        self.LEdit_MAC_adresse = QtWidgets.QLineEdit()
        mac = (('-'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
        for ele in range(0,8*6,8)][::-1])))
        self.LEdit_MAC_adresse.setText(mac)
        self.LEdit_MAC_adresse.setDisabled(True)
       
        self.LEdit_WAN_ipADRESS = QtWidgets.QLineEdit()
        ip = requests.get('https://checkip.amazonaws.com').text.strip()
        # ip = get('https://api.ipify.org').content.decode('utf8')
        self.LEdit_WAN_ipADRESS.setText(' {}'.format(ip))
        self.LEdit_WAN_ipADRESS.setDisabled(True)

        self.LEdit_Systeme = QtWidgets.QLineEdit()
        self.LEdit_Systeme.setText(platform.system())
        self.LEdit_Systeme.setDisabled(True)

        self.btn_Exit = QtWidgets.QPushButton("Exit")
    
    
    def addWigets_to_layouts(self):
        self.monFormulaire.addRow(self.lbl_titre)
        self.monFormulaire.addRow("Hostname",self.LEdit_hostname)
        self.monFormulaire.addRow("Lan IP Address",self.LEdit_LanIpAddress)
        self.monFormulaire.addRow("MAC Address",self.LEdit_MAC_adresse)
        self.monFormulaire.addRow("WAN IP Address",self.LEdit_WAN_ipADRESS)
        self.monFormulaire.addRow("System",self.LEdit_Systeme)
        self.monFormulaire.addRow(self.btn_Exit)


    def setup_connections(self):
        self.btn_Exit.clicked.connect(quit)
   
app = QtWidgets.QApplication([])
form = MaFenetre()
form.show()
app.exec()