from PySide6 import QtWidgets
import socket
import uuid
import platform
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
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutV1 = QtWidgets.QVBoxLayout()
        self.layoutV2 = QtWidgets.QVBoxLayout()
        self.layoutH = QtWidgets.QHBoxLayout()
        

    def create_widgets(self):
      
        self.lbl_titre = QtWidgets.QLabel("Computer informations")

        self.lbl_hostname = QtWidgets.QLabel("Hostname")
        self.LEdit_hostname = QtWidgets.QLineEdit()
        

        self.lbl_LanIpAddress = QtWidgets.QLabel("Lan Ip Address")
        self.LEdit_LanIpAddress = QtWidgets.QLineEdit()
       

        self.lbl_MAC_adresse = QtWidgets.QLabel("MAC_adresse")
        self.LEdit_MAC_adresse = QtWidgets.QLineEdit()
       

        self.lbl_WAN_ipADRESS = QtWidgets.QLabel("WAN_ipADRESS")
        self.LEdit_WAN_ipADRESS = QtWidgets.QLineEdit()
        

        self.lbl_Systeme = QtWidgets.QLabel("Systeme")
        self.LEdit_Systeme = QtWidgets.QLineEdit()
       

    
        self.btn_Exit = QtWidgets.QPushButton("Exit")

        self.LEdit_hostname.setText(socket.gethostname())
        self.LEdit_hostname.setDisabled(True)
        lan= socket.gethostbyname(socket.gethostname())
        self.LEdit_LanIpAddress.setText(lan)
        self.LEdit_LanIpAddress.setDisabled(True)
        mac = (('-'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
        for ele in range(0,8*6,8)][::-1])))
        self.LEdit_MAC_adresse.setText(mac)
        self.LEdit_MAC_adresse.setDisabled(True)
        ip = requests.get('https://checkip.amazonaws.com').text.strip()
        # ip = get('https://api.ipify.org').content.decode('utf8')
        self.LEdit_WAN_ipADRESS.setText(' {}'.format(ip))
        self.LEdit_WAN_ipADRESS.setDisabled(True)
        self.LEdit_Systeme.setText(platform.system())
        self.LEdit_Systeme.setDisabled(True)
    
       

    def addWigets_to_layouts(self):

      
        self.layoutV.addWidget(self.lbl_titre)
        self.layoutV1.addWidget(self.lbl_hostname)
        self.layoutV1.addWidget(self.lbl_LanIpAddress)
        self.layoutV1.addWidget(self.lbl_MAC_adresse)
        self.layoutV1.addWidget(self.lbl_WAN_ipADRESS)
        self.layoutV1.addWidget(self.lbl_Systeme)

        self.layoutV2.addWidget(self.LEdit_hostname)
        self.layoutV2.addWidget(self.LEdit_LanIpAddress)
        self.layoutV2.addWidget(self.LEdit_MAC_adresse)
        self.layoutV2.addWidget(self.LEdit_WAN_ipADRESS)
        self.layoutV2.addWidget(self.LEdit_Systeme)
       
        self.layoutH.addLayout(self.layoutV1)
        self.layoutH.addLayout(self.layoutV2)

   
        self.layoutV.addLayout(self.layoutH)
        
        self.layoutV.addWidget(self.btn_Exit)

        self.setLayout(self.layoutV)


    def setup_connections(self):
        self.btn_Exit.clicked.connect(quit)
   

  


app = QtWidgets.QApplication([])
form = MaFenetre()
form.show()
app.exec()