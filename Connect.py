import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import sys,requests
import sqlite3,os
import pyautogui
import socket,subprocess


working_dir = os.getcwd()
# working_dir = working_dir.replace(r"/Connect","")


resolution = pyautogui.size()
SCREEN_WIDTH = resolution.width
SCREEN_HEIGHT = resolution.height

SCREEN_WIDTH_Frame_One = int(SCREEN_WIDTH*0.3)
SCREEN_HEIGHT_Frame_One = int(SCREEN_HEIGHT*0.5)

SCREEN_WIDTH_Frame_Two = int(SCREEN_WIDTH*0.3)
SCREEN_HEIGHT_Frame_Two = int(SCREEN_HEIGHT*0.5)

SCREEN_WIDTH_Frame_Three = int(SCREEN_WIDTH*0.7)
SCREEN_HEIGHT_Frame_Three = int(SCREEN_HEIGHT*0.7)

MY_HOST_NAME = socket.gethostname()



rec_json = {}

rec_json["fold_path"] = ""
rec_json["fold_struct"] = {}

show_flatlist_flag = "0"

try :
    os.remove(os.path.join(working_dir,'Log','Connect.db'))
except :
    pass

try :
    os.remove(os.path.join(working_dir,'Log','Connection.db'))
except :
    pass

try :
    subprocess.Popen(os.path.join(working_dir,r"Connection.exe"), creationflags=subprocess.CREATE_NEW_CONSOLE)
except Exception as s :
    print("Start Connection.exe - Exception : ",s)



import time
time.sleep(1)

############3
try :
    conn = sqlite3.connect(os.path.join(working_dir,'Log','Connect.db'))
    conn.execute("CREATE TABLE IF NOT EXISTS CONNECT(C1 TEXT PRIMARY KEY,C2 TEXT)")

    try :
        conn.execute("INSERT INTO CONNECT(C1,C2) VALUES('R1','')")
    except Exception as e :
        print("Connect.db (R1) Exception : ",e)

    try :
        conn.execute("INSERT INTO CONNECT(C1,C2) VALUES('R2','')")
    except Exception as e :
        print("Connect.db (R2) Exception : ",e)

    try :
        conn.execute("INSERT INTO CONNECT(C1,C2) VALUES('R3','')")
    except Exception as e :
        print("Connect.db (R3) Exception : ",e)

    conn.commit()
    conn.close()
except Exception as e :
    print("Connect.db Exception : ",e)


try :
    conn = sqlite3.connect(os.path.join(working_dir,'Log','Connection.db'))
    conn.execute("CREATE TABLE IF NOT EXISTS CONNECT(C1 TEXT PRIMARY KEY,C2 TEXT)")

    try :
        conn.execute("INSERT INTO CONNECT(C1,C2) VALUES('R1','')")
    except Exception as e :
        print("Connect.db (R1) Exception : ",e)

    try :
        conn.execute("INSERT INTO CONNECT(C1,C2) VALUES('R2','')")
    except Exception as e :
        print("Connect.db (R2) Exception : ",e)

    try :
        conn.execute("INSERT INTO CONNECT(C1,C2) VALUES('R3','')")
    except Exception as e :
        print("Connect.db (R3) Exception : ",e)

    conn.commit()
    conn.close()
except Exception as e :
    print("Connection.db Exception : ",e)
#########################################################################
#########################################################################
# Frame_One

class Frame_One(object):

    def Connect_Button_Clicked(self) :
        username_entered = self.Username_Label_Text.text()
        password_entered = self.Password_Label_Text.text()


        if((username_entered=="") or (password_entered=="")) :
            Dia_Box = QMessageBox()
            Dia_Box.setIcon(QMessageBox.Warning)
            Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
            Dia_Box.setText("Please, Enter valid input !")
            Dia_Box.setWindowTitle("Invalid Input")
            Dia_Box.setStandardButtons(QMessageBox.Ok)
            if (Dia_Box.exec() == QMessageBox.Ok) :
                self.Username_Label_Text.setText("")
                self.Password_Label_Text.setText("")

        else :

            con_flag = "0"

            try :
                conn = sqlite3.connect(os.path.join(working_dir,'Log','Connect.db'))

                # Hostname :
                try :
                    conn.execute("UPDATE CONNECT SET C2 = '{}' WHERE C1='R1'".format(MY_HOST_NAME))
                except :
                    pass
                    con_flag = "1"
                    

                # Username :
                try :
                    conn.execute("UPDATE CONNECT SET C2 = '{}' WHERE C1='R2'".format(username_entered))
                except :
                    pass
                    con_flag = "1"


                # Password :
                try :
                    conn.execute("UPDATE CONNECT SET C2 = '{}' WHERE C1='R3'".format(password_entered))
                except :
                    pass
                    con_flag = "1"


                conn.commit()
                conn.close()
            except Exception as e :
                print("Connect.db Exception : ",e)
                con_flag = "1"


            if(con_flag == "0") :
                Dia_Box = QMessageBox()
                Dia_Box.setIcon(QMessageBox.Information)
                Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                Dia_Box.setText("Connection is successfully established !")
                Dia_Box.setWindowTitle("Connected")
                Dia_Box.setStandardButtons(QMessageBox.Ok)
                if (Dia_Box.exec() == QMessageBox.Ok) :
                    self.Username_Label_Text.setText("")
                    self.Password_Label_Text.setText("")

                    Frame_Two_Screen.show()
                    Frame_One_Screen.close()


            else :
                Dia_Box = QMessageBox()
                Dia_Box.setIcon(QMessageBox.Warning)
                Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                Dia_Box.setText("Oops ! Error In Connection.")
                Dia_Box.setWindowTitle("Invalid Input")
                Dia_Box.setStandardButtons(QMessageBox.Ok)
                if (Dia_Box.exec() == QMessageBox.Ok) :
                    self.Username_Label_Text.setText("")
                    self.Password_Label_Text.setText("")
        


    def setupUi(self, Frame_One):
        Frame_One.setObjectName("Frame_One")
        Frame_One.resize(SCREEN_WIDTH_Frame_One, SCREEN_HEIGHT_Frame_One)
        Frame_One.setMinimumSize(SCREEN_WIDTH_Frame_One, SCREEN_HEIGHT_Frame_One)
        Frame_One.setMaximumSize(SCREEN_WIDTH_Frame_One, SCREEN_HEIGHT_Frame_One)
        Frame_One.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))



        # Fonts :
        heading_font = QFont()
        heading_font.setFamily("Lucida Bright")
        heading_font.setStyleHint(QFont.Monospace)
        heading_font.setFixedPitch(True)
        heading_font.setPointSize(25)
        heading_font.setBold(True)
        heading_font.setWeight(100)


        label_font = QFont()
        label_font.setFamily("Times New Roman")
        label_font.setStyleHint(QFont.Monospace)
        label_font.setFixedPitch(True)
        label_font.setPointSize(10)
        label_font.setBold(True)
        label_font.setWeight(100)

        # Heading (Label) :
        self.Heading_Label = QtWidgets.QLabel(Frame_One)
        self.Heading_Label.setGeometry(10, int(SCREEN_HEIGHT_Frame_One*0.05), int(SCREEN_WIDTH_Frame_One-20), int(SCREEN_HEIGHT_Frame_One*0.20))
        self.Heading_Label.setObjectName('Heading_Label')
        self.Heading_Label.setStyleSheet("background-color:none;")
        self.Heading_Label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.Heading_Label.setText("Connect")
        self.Heading_Label.setFont(heading_font)

        # Username (Label) :
        self.Username_Label = QtWidgets.QLabel(Frame_One)
        self.Username_Label.setGeometry(20, int(SCREEN_HEIGHT_Frame_One*0.35), int(SCREEN_WIDTH_Frame_One-40), int(SCREEN_HEIGHT_Frame_One*0.10))
        self.Username_Label.setObjectName('Username_Label')
        self.Username_Label.setStyleSheet("background-color:none;")
        self.Username_Label.setText("Enter Your Username :")
        self.Username_Label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.Username_Label.setFont(label_font)

        # Username (Value) :
        self.Username_Label_Text = QtWidgets.QLineEdit(Frame_One)
        self.Username_Label_Text.setGeometry(20, int(SCREEN_HEIGHT_Frame_One*0.45), int(SCREEN_WIDTH_Frame_One-40), int(SCREEN_HEIGHT_Frame_One*0.10))
        self.Username_Label_Text.setObjectName('Username_Label_Text')
        self.Username_Label_Text.setStyleSheet("background-color:none; border-radius:5px")
        self.Username_Label_Text.setText("")

        # Password (Label) :
        self.Password_Label = QtWidgets.QLabel(Frame_One)
        self.Password_Label.setGeometry(20, int(SCREEN_HEIGHT_Frame_One*0.60), int(SCREEN_WIDTH_Frame_One-40), int(SCREEN_HEIGHT_Frame_One*0.10))
        self.Password_Label.setObjectName('Password_Label')
        self.Password_Label.setStyleSheet("background-color:none;")
        self.Password_Label.setText("Enter Your Password :")
        self.Password_Label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.Password_Label.setFont(label_font)

        # Username (Value) :
        self.Password_Label_Text = QtWidgets.QLineEdit(Frame_One)
        self.Password_Label_Text.setGeometry(20, int(SCREEN_HEIGHT_Frame_One*0.70), int(SCREEN_WIDTH_Frame_One-40), int(SCREEN_HEIGHT_Frame_One*0.10))
        self.Password_Label_Text.setObjectName('Password_Label_Text')
        self.Password_Label_Text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_Label_Text.setStyleSheet("background-color:none; border-radius:5px")
        self.Password_Label_Text.setText("")

        # Connect Button :
        self.Connect_Button = QtWidgets.QPushButton(Frame_One)
        self.Connect_Button.setGeometry(int(SCREEN_WIDTH_Frame_One*0.5)-50, int(SCREEN_HEIGHT_Frame_One*0.85), 100, int(SCREEN_HEIGHT_Frame_One*0.10))
        self.Connect_Button.setObjectName('Connect_Button')
        self.Connect_Button.setStyleSheet("QPushButton{background-color : rgb(247, 134, 110); font-size : 15px; font-weight: bold; border-radius:6px;}QPushButton::pressed{background-color : rgb(255, 66, 0); border-radius:6px;}QPushButton::hover{border: 2px solid rgba(0,0,255,0.7); border-radius:6px;}")
        self.Connect_Button.setText("Connect")
        self.Connect_Button.clicked.connect(self.Connect_Button_Clicked)


        self.retranslateUi(Frame_One)
        QtCore.QMetaObject.connectSlotsByName(Frame_One)
  

    def retranslateUi(self, Frame_One):
        _translate = QtCore.QCoreApplication.translate
        Frame_One.setWindowTitle(_translate("Frame_One", "Connection"))



#########################################################################
#########################################################################
# Frame_Two

class Frame_Two(object):

    def Connect_Button_Clicked(self) :
        hostname_entered = self.Hostname_Label_Text.text()
        username_entered = self.Username_Label_Text.text()
        password_entered = self.Password_Label_Text.text()


        if((hostname_entered=="") or (username_entered=="") or (password_entered=="")) :
            Dia_Box = QMessageBox()
            Dia_Box.setIcon(QMessageBox.Warning)
            Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
            Dia_Box.setText("Please, Enter valid input !")
            Dia_Box.setWindowTitle("Invalid Input")
            Dia_Box.setStandardButtons(QMessageBox.Ok)
            if (Dia_Box.exec() == QMessageBox.Ok) :
                self.Hostname_Label_Text.setText("")
                self.Username_Label_Text.setText("")
                self.Password_Label_Text.setText("")

        else :

            con_flag = "0"
            try :
                host_ip = socket.gethostbyname(hostname_entered)
                con_flag = "1"
            except :
                con_flag = "0"
            


            if(con_flag == "1") :

                try :
                    url = "http://{}:50111/host_check/{}/{}/{}".format(host_ip,hostname_entered,username_entered,password_entered)
                    r = requests.get(url, allow_redirects=True)
                    res_text = r.text
                except :
                    res_text = ""


                if(res_text=="Connected") :
                    try :
                        conn = sqlite3.connect(os.path.join(working_dir,'Log','Connection.db'))

                        conn.execute("UPDATE CONNECT SET C2 = '{}' WHERE C1='R1'".format(hostname_entered))
                        conn.execute("UPDATE CONNECT SET C2 = '{}' WHERE C1='R2'".format(username_entered))
                        conn.execute("UPDATE CONNECT SET C2 = '{}' WHERE C1='R3'".format(password_entered))

                        conn.commit()
                        conn.close()
                    except Exception as e :
                        print("Connection.db Exception : ",e)


                    Dia_Box = QMessageBox()
                    Dia_Box.setIcon(QMessageBox.Information)
                    Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                    Dia_Box.setText("You are successfully connected to Host !")
                    Dia_Box.setWindowTitle("Connected")
                    Dia_Box.setStandardButtons(QMessageBox.Ok)
                    if (Dia_Box.exec() == QMessageBox.Ok) :
                        self.Hostname_Label_Text.setText("")
                        self.Username_Label_Text.setText("")
                        self.Password_Label_Text.setText("")


                        Frame_Three_Screen.show()
                        Frame_Two_Screen.close()

                        global rec_json
                        try :
                            url = "http://{}:50111/file_structure_start".format(host_ip)
                            r = requests.get(url, allow_redirects=True)
                            rec_json = r.json()
                        except :
                            rec_json = {}


                        global show_flatlist_flag
                        show_flatlist_flag = "1"



                else :
                    Dia_Box = QMessageBox()
                    Dia_Box.setIcon(QMessageBox.Warning)
                    Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                    Dia_Box.setText("Please, Enter Valid Host's Credentials.")
                    Dia_Box.setWindowTitle("Wrong Input")
                    Dia_Box.setStandardButtons(QMessageBox.Ok)
                    if (Dia_Box.exec() == QMessageBox.Ok) :
                        self.Hostname_Label_Text.setText("")
                        self.Username_Label_Text.setText("")
                        self.Password_Label_Text.setText("")

            else :
                Dia_Box = QMessageBox()
                Dia_Box.setIcon(QMessageBox.Warning)
                Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                Dia_Box.setText("Given Host is NOT in Connection.")
                Dia_Box.setWindowTitle("Invalid Host")
                Dia_Box.setStandardButtons(QMessageBox.Ok)
                if (Dia_Box.exec() == QMessageBox.Ok) :
                    self.Hostname_Label_Text.setText("")
                    self.Username_Label_Text.setText("")
                    self.Password_Label_Text.setText("")





    def setupUi(self, Frame_Two):
        Frame_Two.setObjectName("Frame_Two")
        Frame_Two.resize(SCREEN_WIDTH_Frame_Two, SCREEN_HEIGHT_Frame_Two)
        Frame_Two.setMinimumSize(SCREEN_WIDTH_Frame_Two, SCREEN_HEIGHT_Frame_Two)
        Frame_Two.setMaximumSize(SCREEN_WIDTH_Frame_Two, SCREEN_HEIGHT_Frame_Two)
        Frame_Two.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))



        # Fonts :
        heading_font = QFont()
        heading_font.setFamily("Arial")
        heading_font.setStyleHint(QFont.Monospace)
        heading_font.setFixedPitch(True)
        heading_font.setPointSize(15)
        heading_font.setBold(True)
        heading_font.setWeight(100)


        label_font = QFont()
        label_font.setFamily("Times New Roman")
        label_font.setStyleHint(QFont.Monospace)
        label_font.setFixedPitch(True)
        label_font.setPointSize(10)
        label_font.setBold(True)
        label_font.setWeight(100)





        # Heading (Label) :
        self.Heading_Label = QtWidgets.QLabel(Frame_Two)
        self.Heading_Label.setGeometry(10, int(SCREEN_HEIGHT_Frame_Two*0.0), int(SCREEN_WIDTH_Frame_Two-20), int(SCREEN_HEIGHT_Frame_Two*0.10))
        self.Heading_Label.setObjectName('Heading_Label')
        self.Heading_Label.setStyleSheet("background-color:none;")
        self.Heading_Label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.Heading_Label.setText("Host Credential")
        self.Heading_Label.setFont(heading_font)


        # Hostname (Label) :
        self.Hostname_Label = QtWidgets.QLabel(Frame_Two)
        self.Hostname_Label.setGeometry(20, int(SCREEN_HEIGHT_Frame_Two*0.15), int(SCREEN_WIDTH_Frame_Two-40), int(SCREEN_HEIGHT_Frame_Two*0.10))
        self.Hostname_Label.setObjectName('Hostname_Label')
        self.Hostname_Label.setStyleSheet("background-color:none;")
        self.Hostname_Label.setText("Enter Host's Desktop Name :")
        self.Hostname_Label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.Hostname_Label.setFont(label_font)

        # Hostname (Value) :
        self.Hostname_Label_Text = QtWidgets.QLineEdit(Frame_Two)
        self.Hostname_Label_Text.setGeometry(20, int(SCREEN_HEIGHT_Frame_Two*0.25), int(SCREEN_WIDTH_Frame_Two-40), int(SCREEN_HEIGHT_Frame_Two*0.10))
        self.Hostname_Label_Text.setObjectName('Hostname_Label_Text')
        self.Hostname_Label_Text.setStyleSheet("background-color:none; border-radius:5px")
        self.Hostname_Label_Text.setText("")


        # Username (Label) :
        self.Username_Label = QtWidgets.QLabel(Frame_Two)
        self.Username_Label.setGeometry(20, int(SCREEN_HEIGHT_Frame_Two*0.40), int(SCREEN_WIDTH_Frame_Two-40), int(SCREEN_HEIGHT_Frame_Two*0.10))
        self.Username_Label.setObjectName('Username_Label')
        self.Username_Label.setStyleSheet("background-color:none;")
        self.Username_Label.setText("Enter Host's Username :")
        self.Username_Label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.Username_Label.setFont(label_font)

        # Username (Value) :
        self.Username_Label_Text = QtWidgets.QLineEdit(Frame_Two)
        self.Username_Label_Text.setGeometry(20, int(SCREEN_HEIGHT_Frame_Two*0.50), int(SCREEN_WIDTH_Frame_Two-40), int(SCREEN_HEIGHT_Frame_Two*0.10))
        self.Username_Label_Text.setObjectName('Username_Label_Text')
        self.Username_Label_Text.setStyleSheet("background-color:none; border-radius:5px")
        self.Username_Label_Text.setText("")

        # Password (Label) :
        self.Password_Label = QtWidgets.QLabel(Frame_Two)
        self.Password_Label.setGeometry(20, int(SCREEN_HEIGHT_Frame_Two*0.65), int(SCREEN_WIDTH_Frame_Two-40), int(SCREEN_HEIGHT_Frame_Two*0.10))
        self.Password_Label.setObjectName('Password_Label')
        self.Password_Label.setStyleSheet("background-color:none;")
        self.Password_Label.setText("Enter Host's Password :")
        self.Password_Label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.Password_Label.setFont(label_font)

        # Username (Value) :
        self.Password_Label_Text = QtWidgets.QLineEdit(Frame_Two)
        self.Password_Label_Text.setGeometry(20, int(SCREEN_HEIGHT_Frame_Two*0.75), int(SCREEN_WIDTH_Frame_Two-40), int(SCREEN_HEIGHT_Frame_Two*0.10))
        self.Password_Label_Text.setObjectName('Password_Label_Text')
        self.Password_Label_Text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_Label_Text.setStyleSheet("background-color:none; border-radius:5px")
        self.Password_Label_Text.setText("")

        # Connect Button :
        self.Connect_Button = QtWidgets.QPushButton(Frame_Two)
        self.Connect_Button.setGeometry(int(SCREEN_WIDTH_Frame_Two*0.5)-50, int(SCREEN_HEIGHT_Frame_Two*0.88), 100, int(SCREEN_HEIGHT_Frame_Two*0.08))
        self.Connect_Button.setObjectName('Connect_Button')
        self.Connect_Button.setStyleSheet("QPushButton{background-color : rgb(247, 134, 110); font-size : 15px; font-weight: bold; border-radius:6px;}QPushButton::pressed{background-color : rgb(255, 66, 0); border-radius:6px;}QPushButton::hover{border: 2px solid rgba(0,0,255,0.7); border-radius:6px;}")
        self.Connect_Button.setText("Connect")
        self.Connect_Button.clicked.connect(self.Connect_Button_Clicked)


        self.retranslateUi(Frame_Two)
        QtCore.QMetaObject.connectSlotsByName(Frame_Two)
  

    def retranslateUi(self, Frame_Two):
        _translate = QtCore.QCoreApplication.translate
        Frame_Two.setWindowTitle(_translate("Frame_Two", "Connection"))




#########################################################################
#########################################################################
# Frame_Three

class Frame_Three(object):


    def show_list_view_active(self) :
        global show_flatlist_flag
        if(show_flatlist_flag=="1") :
            self.show_list_view()
            show_flatlist_flag = "0"


    def show_list_view(self) :

        global rec_json

        fold_struct_path = rec_json["fold_path"]
        fold_struct_list = rec_json["fold_struct"]

        self.Path_Label.setText("Path : {}".format(fold_struct_path))

        self.model = QtGui.QStandardItemModel(self.File_List)
        self.File_List.setModel(self.model)
               

        for k,v in fold_struct_list.items() :
            if(v=="1") :
                item = QtGui.QStandardItem(QtGui.QIcon(os.path.join(working_dir,'Log','Folder.png')),k)
            else :
                item = QtGui.QStandardItem(QtGui.QIcon(os.path.join(working_dir,'Log','File.png')),k)

            self.model.appendRow(item)

            self.File_List.setSpacing(2)
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(12)
            font.setBold(False)
            self.File_List.setFont(font)



    def Browse_Button_Clicked(self) :
        try :
            browse_file_name = QFileDialog.getOpenFileName()[0]
        except Exception as r :
            print(r)
            browse_file_name = ""

        try :
            if(browse_file_name) :
                self.Browse_Button_Path_Label.setText(browse_file_name)
            else :
                self.Browse_Button_Path_Label.setText("")

        except Exception as r :
            print(r)
            self.Browse_Button_Path_Label.setText("")

        self.show_list_view()



    def Upload_Button_Clicked(self) :

        global rec_json

        fold_struct_path = rec_json["fold_path"]

        send_path = self.Browse_Button_Path_Label.text()

        if os.path.isfile(send_path) :  
            try :
                conn = sqlite3.connect(os.path.join(working_dir,'Log','Connection.db'))
                cur = conn.cursor()
                cur.execute("SELECT C2 FROM CONNECT WHERE C1=?", ("R1",))
                rows = cur.fetchall()[0][0]
   
                conn.commit()
                conn.close()
            except Exception as e :
                rows = ""
                print("Connection.db Exception : ",e)


            try :
                host_ip = socket.gethostbyname(rows)
            except :
                host_ip = ""


            try :
                url = "http://{}:50111/file_upload/{}".format(host_ip,fold_struct_path)
                binary_files = {'file': open(r'{}'.format(send_path), 'rb')}
                r = requests.post(url, files=binary_files)
                cred_status_code =  r.text

            except Exception as e:
                print("==> ", e)
                cred_status_code = ""

            try :
                if(cred_status_code=="200") :
                    Dia_Box = QMessageBox()
                    Dia_Box.setIcon(QMessageBox.Information)
                    Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                    Dia_Box.setText("File is uploaded successfully !")
                    Dia_Box.setWindowTitle("File Upload")
                    Dia_Box.setStandardButtons(QMessageBox.Ok)
                    if (Dia_Box.exec() == QMessageBox.Ok) :
                        self.Browse_Button_Path_Label.setText("")

                else :
                    Dia_Box = QMessageBox()
                    Dia_Box.setIcon(QMessageBox.Warning)
                    Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                    Dia_Box.setText("Oops ! Error In File Upload.")
                    Dia_Box.setWindowTitle("File Upload")
                    Dia_Box.setStandardButtons(QMessageBox.Ok)
                    if (Dia_Box.exec() == QMessageBox.Ok) :
                        self.Browse_Button_Path_Label.setText("")

            except :
                Dia_Box = QMessageBox()
                Dia_Box.setIcon(QMessageBox.Warning)
                Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                Dia_Box.setText("Oops ! Error In File Upload.")
                Dia_Box.setWindowTitle("File Upload")
                Dia_Box.setStandardButtons(QMessageBox.Ok)
                if (Dia_Box.exec() == QMessageBox.Ok) :
                    self.Browse_Button_Path_Label.setText("")


        else :
            Dia_Box = QMessageBox()
            Dia_Box.setIcon(QMessageBox.Warning)
            Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
            Dia_Box.setText("Please, Select valid file.")
            Dia_Box.setWindowTitle("File Upload")
            Dia_Box.setStandardButtons(QMessageBox.Ok)
            if (Dia_Box.exec() == QMessageBox.Ok) :
                self.Browse_Button_Path_Label.setText("")

        self.Refresh_Button_Clicked()


    def Refresh_Button_Clicked(self) :
        global rec_json
        fold_struct_path = rec_json["fold_path"]

        send_path = fold_struct_path

        if os.path.isdir(send_path) :  
            try :
                conn = sqlite3.connect(os.path.join(working_dir,'Log','Connection.db'))
                cur = conn.cursor()
                cur.execute("SELECT C2 FROM CONNECT WHERE C1=?", ("R1",))
                rows = cur.fetchall()[0][0]
                conn.commit()
                conn.close()
            except Exception as e :
                rows = ""
                print("Connection.db Exception : ",e)


            try :
                host_ip = socket.gethostbyname(rows)
            except :
                host_ip = ""


            try :
                url = "http://{}:50111/file_structure/{}".format(host_ip,send_path)
                r = requests.get(url, allow_redirects=True)
                rec_json = r.json()
            except :
                rec_json = {}

        else :
            print("File")

        self.show_list_view()


    def Back_Button_Clicked(self) :
        global rec_json

        fold_struct_path = rec_json["fold_path"]

        send_path = os.path.dirname(fold_struct_path)

        if os.path.isdir(send_path) :  
            try :
                conn = sqlite3.connect(os.path.join(working_dir,'Log','Connection.db'))
                cur = conn.cursor()
                cur.execute("SELECT C2 FROM CONNECT WHERE C1=?", ("R1",))
                rows = cur.fetchall()[0][0]
               
                conn.commit()
                conn.close()
            except Exception as e :
                rows = ""
                print("Connection.db Exception : ",e)


            try :
                host_ip = socket.gethostbyname(rows)
            except :
                host_ip = ""


            try :
                url = "http://{}:50111/file_structure/{}".format(host_ip,send_path)
                r = requests.get(url, allow_redirects=True)
                rec_json = r.json()
            except :
                rec_json = {}

        else :
            print("File")

        self.show_list_view()



    def on_Folder_Clicked(self, index):
        global rec_json
        fil_clicked = str(index.data())

        fold_struct_path = rec_json["fold_path"]

        send_path = os.path.join(fold_struct_path,fil_clicked)


        if os.path.isdir(send_path) :  
            try :
                conn = sqlite3.connect(os.path.join(working_dir,'Log','Connection.db'))
                cur = conn.cursor()
                cur.execute("SELECT C2 FROM CONNECT WHERE C1=?", ("R1",))
                rows = cur.fetchall()[0][0]
              
                conn.commit()
                conn.close()
            except Exception as e :
                rows = ""
                print("Connection.db Exception : ",e)


            try :
                host_ip = socket.gethostbyname(rows)
            except :
                host_ip = ""


            try :
                url = "http://{}:50111/file_structure/{}".format(host_ip,send_path)
                r = requests.get(url, allow_redirects=True)
                rec_json = r.json()
            except :
                rec_json = {}

        else :
            print("File")
        
        self.show_list_view()


    def flatlist_file_download(self,index):
        itms = self.File_List.selectedIndexes()

        file_selected = itms[0].data().strip()


        global rec_json

        fold_struct_path = rec_json["fold_path"]

        send_path = os.path.join(fold_struct_path,file_selected)

        try :
            conn = sqlite3.connect(os.path.join(working_dir,'Log','Connection.db'))
            cur = conn.cursor()
            cur.execute("SELECT C2 FROM CONNECT WHERE C1=?", ("R1",))
            rows = cur.fetchall()[0][0]
            
            conn.commit()
            conn.close()
        except Exception as e :
            rows = ""
            print("Connection.db Exception : ",e)


        try :
            host_ip = socket.gethostbyname(rows)
        except :
            host_ip = ""


        try :
            url = "http://{}:50111/file_download/{}".format(host_ip,send_path)
            r = requests.get(url, allow_redirects=True)
            cred_status_code =  r.status_code
            
            open(file_selected, 'wb').write(r.content)

        except :
            cred_status_code = 404


        try :
            if(cred_status_code==200) :
                Dia_Box = QMessageBox()
                Dia_Box.setIcon(QMessageBox.Information)
                Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                Dia_Box.setText("File is downloaded successfully !")
                Dia_Box.setWindowTitle("File Download")
                Dia_Box.setStandardButtons(QMessageBox.Ok)
                if (Dia_Box.exec() == QMessageBox.Ok) :
                    pass
            else :
                Dia_Box = QMessageBox()
                Dia_Box.setIcon(QMessageBox.Warning)
                Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                Dia_Box.setText("Oops ! Error In File Download.")
                Dia_Box.setWindowTitle("File Download")
                Dia_Box.setStandardButtons(QMessageBox.Ok)
                if (Dia_Box.exec() == QMessageBox.Ok) :
                    pass
        except :
            Dia_Box = QMessageBox()
            Dia_Box.setIcon(QMessageBox.Warning)
            Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
            Dia_Box.setText("Oops ! Error In File Download.")
            Dia_Box.setWindowTitle("File Download")
            Dia_Box.setStandardButtons(QMessageBox.Ok)
            if (Dia_Box.exec() == QMessageBox.Ok) :
                pass

        self.Refresh_Button_Clicked()




    def flatlist_file_delete(self,index):
        itms = self.File_List.selectedIndexes()

        file_selected = itms[0].data().strip()


        global rec_json

        fold_struct_path = rec_json["fold_path"]

        send_path = os.path.join(fold_struct_path,file_selected)

        try :
            conn = sqlite3.connect(os.path.join(working_dir,'Log','Connection.db'))
            cur = conn.cursor()
            cur.execute("SELECT C2 FROM CONNECT WHERE C1=?", ("R1",))
            rows = cur.fetchall()[0][0]
            conn.commit()
            conn.close()
        except Exception as e :
            rows = ""
            print("Connection.db Exception : ",e)


        try :
            host_ip = socket.gethostbyname(rows)
        except :
            host_ip = ""


        try :
            url = "http://{}:50111/file_delete/{}".format(host_ip,send_path)
            r = requests.get(url, allow_redirects=True)
            cred_status_code =  r.status_code
        except :
            cred_status_code = 404


        try :
            if(cred_status_code==200) :
                Dia_Box = QMessageBox()
                Dia_Box.setIcon(QMessageBox.Information)
                Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                Dia_Box.setText("File is deleted successfully !")
                Dia_Box.setWindowTitle("File Delete")
                Dia_Box.setStandardButtons(QMessageBox.Ok)
                if (Dia_Box.exec() == QMessageBox.Ok) :
                    pass
            else :
                Dia_Box = QMessageBox()
                Dia_Box.setIcon(QMessageBox.Warning)
                Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
                Dia_Box.setText("Oops ! Error In File Delete.")
                Dia_Box.setWindowTitle("File Delete")
                Dia_Box.setStandardButtons(QMessageBox.Ok)
                if (Dia_Box.exec() == QMessageBox.Ok) :
                    pass
        except :
            Dia_Box = QMessageBox()
            Dia_Box.setIcon(QMessageBox.Warning)
            Dia_Box.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))
            Dia_Box.setText("Oops ! Error In File Delete.")
            Dia_Box.setWindowTitle("File Delete")
            Dia_Box.setStandardButtons(QMessageBox.Ok)
            if (Dia_Box.exec() == QMessageBox.Ok) :
                pass

        self.Refresh_Button_Clicked()


           


    def rightMenuShow(self):
        global rec_json
        
        if(len(rec_json["fold_struct"])>0) :
    
            rightMenu = QMenu(self.File_List)

            download_Action = QAction ("Download", self.File_List, triggered = self.flatlist_file_download)
            rightMenu.addAction(download_Action)

            delete_Action = QAction ("Delete", self.File_List, triggered = self.flatlist_file_delete)
            rightMenu.addAction(delete_Action)

            refresh_Action = QAction ("Refresh", self.File_List, triggered = self.Refresh_Button_Clicked)
            rightMenu.addAction(refresh_Action)

            rightMenu.exec_(QtGui.QCursor.pos())


    def setupUi(self, Frame_Three):
        Frame_Three.setObjectName("Frame_Three")
        Frame_Three.resize(SCREEN_WIDTH_Frame_Three, SCREEN_HEIGHT_Frame_Three)
        Frame_Three.setMinimumSize(SCREEN_WIDTH_Frame_Three, SCREEN_HEIGHT_Frame_Three)
        Frame_Three.setMaximumSize(SCREEN_WIDTH_Frame_Three, SCREEN_HEIGHT_Frame_Three)
        Frame_Three.setWindowIcon(QtGui.QIcon(os.path.join(working_dir,'Log','Icon.png')))



        # Fonts :
        heading_font = QFont()
        heading_font.setFamily("Arial")
        heading_font.setStyleHint(QFont.Monospace)
        heading_font.setFixedPitch(True)
        heading_font.setPointSize(15)
        heading_font.setBold(True)
        heading_font.setWeight(100)


        label_font = QFont()
        label_font.setFamily("Times New Roman")
        label_font.setStyleHint(QFont.Monospace)
        label_font.setFixedPitch(True)
        label_font.setPointSize(10)
        label_font.setBold(True)
        label_font.setWeight(100)

        # Host (Icon) :
        self.Host_Label_Icon = QtWidgets.QLabel(Frame_Three)
        self.Host_Label_Icon.setGeometry(30, int(SCREEN_HEIGHT_Frame_Three*0.02), int(SCREEN_WIDTH_Frame_Three*0.08), int(SCREEN_HEIGHT_Frame_Three*0.06))
        self.Host_Label_Icon.setText("")
        self.Host_Label_Icon.setPixmap(QtGui.QPixmap(os.path.join(working_dir, r"Log\Host.png")))
        self.Host_Label_Icon.setScaledContents(True)
        self.Host_Label_Icon.setObjectName("Host_Label_Icon")


        # Host (Label) :
        self.Host_Label = QtWidgets.QLabel(Frame_Three)
        self.Host_Label.setGeometry(40+int(SCREEN_WIDTH_Frame_Three*0.1), int(SCREEN_HEIGHT_Frame_Three*0.0), int(SCREEN_WIDTH_Frame_Three*0.5), int(SCREEN_HEIGHT_Frame_Three*0.10))
        self.Host_Label.setObjectName('Host_Label')
        self.Host_Label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.Host_Label.setText(MY_HOST_NAME)
        self.Host_Label.setFont(heading_font)

        

        # Path (Label) :
        self.Path_Label = QtWidgets.QLabel(Frame_Three)
        self.Path_Label.setGeometry(20, int(SCREEN_HEIGHT_Frame_Three*0.1), int(SCREEN_WIDTH_Frame_Three-40), int(SCREEN_HEIGHT_Frame_Three*0.10))
        self.Path_Label.setObjectName('Path_Label')
        self.Path_Label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.Path_Label.setText("")
        self.Path_Label.setFont(label_font)



        self.File_List = QtWidgets.QListView(Frame_Three)
        self.File_List.setGeometry(10, int(SCREEN_HEIGHT_Frame_Three*0.2), int(SCREEN_WIDTH_Frame_Three-20), int(SCREEN_HEIGHT_Frame_Three*0.68))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.File_List.setFont(font)
        self.File_List.setStyleSheet("background-color: rgb(219, 213, 215);border:2px solid rgb(219, 213, 215);padding:10px;")
        self.File_List.setObjectName("File_List")
        self.File_List.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.File_List.doubleClicked.connect(self.on_Folder_Clicked)

        
        self.File_List.setContextMenuPolicy(Qt.CustomContextMenu)
        self.File_List.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)
        self.File_List.setEditTriggers(QAbstractItemView.NoEditTriggers)




        global rec_json

        fold_struct_path = rec_json["fold_path"]
        fold_struct_list = rec_json["fold_struct"]

        self.model = QtGui.QStandardItemModel(self.File_List)
        self.File_List.setModel(self.model)


        for k,v in fold_struct_list.items() :
            if(v=="1") :
                item = QtGui.QStandardItem(QtGui.QIcon(os.path.join(working_dir,'Log','Folder.png')),k)
            else :
                item = QtGui.QStandardItem(QtGui.QIcon(os.path.join(working_dir,'Log','File.png')),k)

            self.model.appendRow(item)

            self.File_List.setSpacing(2)
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(12)
            font.setBold(False)
            self.File_List.setFont(font)


        # Browse Button :
        self.Browse_Button = QtWidgets.QPushButton(Frame_Three)
        self.Browse_Button.setGeometry(10, int(SCREEN_HEIGHT_Frame_Three*0.9), int(SCREEN_WIDTH_Frame_Three*0.1)-10, int(SCREEN_HEIGHT_Frame_Three*0.08))
        self.Browse_Button.setObjectName('Browse_Button')
        self.Browse_Button.setStyleSheet("QPushButton{background-color : rgb(247, 134, 110); font-size : 15px; font-weight: bold; border-radius:6px;}QPushButton::pressed{background-color : rgb(255, 66, 0); border-radius:6px;}QPushButton::hover{border: 2px solid rgba(0,0,255,0.7); border-radius:6px;}")
        self.Browse_Button.setText("Browse")
        self.Browse_Button.clicked.connect(self.Browse_Button_Clicked)


        # Browse Button (Label) :
        self.Browse_Button_Path_Label = QtWidgets.QLabel(Frame_Three)
        self.Browse_Button_Path_Label.setGeometry(int(SCREEN_WIDTH_Frame_Three*0.1)+10, int(SCREEN_HEIGHT_Frame_Three*0.9), int(SCREEN_WIDTH_Frame_Three*0.7)-10, int(SCREEN_HEIGHT_Frame_Three*0.08))
        self.Browse_Button_Path_Label.setObjectName('Browse_Button_Path_Label')
        self.Browse_Button_Path_Label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.Browse_Button_Path_Label.setText("")
        self.Browse_Button_Path_Label.setFont(label_font)


        # Upload Button :
        self.Upload_Button = QtWidgets.QPushButton(Frame_Three)
        self.Upload_Button.setGeometry(int(SCREEN_WIDTH_Frame_Three*0.8)+10, int(SCREEN_HEIGHT_Frame_Three*0.9), int(SCREEN_WIDTH_Frame_Three*0.1)-10, int(SCREEN_HEIGHT_Frame_Three*0.08))
        self.Upload_Button.setObjectName('Upload_Button')
        self.Upload_Button.setStyleSheet("QPushButton{background-color : rgb(247, 134, 110); font-size : 15px; font-weight: bold; border-radius:6px;}QPushButton::pressed{background-color : rgb(255, 66, 0); border-radius:6px;}QPushButton::hover{border: 2px solid rgba(0,0,255,0.7); border-radius:6px;}")
        self.Upload_Button.setText("Upload")
        self.Upload_Button.clicked.connect(self.Upload_Button_Clicked)


        # Back Button :
        self.Back_Button = QtWidgets.QPushButton(Frame_Three)
        self.Back_Button.setGeometry(int(SCREEN_WIDTH_Frame_Three*0.9)+10, int(SCREEN_HEIGHT_Frame_Three*0.9), int(SCREEN_WIDTH_Frame_Three*0.1)-20, int(SCREEN_HEIGHT_Frame_Three*0.08))
        self.Back_Button.setObjectName('Back_Button')
        self.Back_Button.setStyleSheet("QPushButton{background-color : rgb(247, 134, 110); font-size : 15px; font-weight: bold; border-radius:6px;}QPushButton::pressed{background-color : rgb(255, 66, 0); border-radius:6px;}QPushButton::hover{border: 2px solid rgba(0,0,255,0.7); border-radius:6px;}")
        self.Back_Button.setText("<< Back")
        self.Back_Button.clicked.connect(self.Back_Button_Clicked)



        self.retranslateUi(Frame_Three)
        QtCore.QMetaObject.connectSlotsByName(Frame_Three)
  

        self.main_timer1 =QtCore.QTimer()
        self.main_timer1.timeout.connect(self.show_list_view_active)
        self.main_timer1.start(2000)

    def retranslateUi(self, Frame_Three):
        _translate = QtCore.QCoreApplication.translate
        Frame_Three.setWindowTitle(_translate("Frame_Three", "Connection"))

#########################################################################
#########################################################################
def GUI_Closed_Function() :
    try :
        os.system("taskkill /f /im Connection.exe")
    except Exception as t :
        print("Stop Connection.exe - Exception : ",t)

#########################################################################
#########################################################################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    app.lastWindowClosed.connect(GUI_Closed_Function)

    Frame_One_Screen = QtWidgets.QMainWindow()
    Frame_One_Ui = Frame_One()
    Frame_One_Ui.setupUi(Frame_One_Screen)
    Frame_One_Screen.show()

    Frame_Two_Screen = QtWidgets.QMainWindow()
    Frame_Two_Ui = Frame_Two()
    Frame_Two_Ui.setupUi(Frame_Two_Screen)

    Frame_Three_Screen = QtWidgets.QMainWindow()
    Frame_Three_Ui = Frame_Three()
    Frame_Three_Ui.setupUi(Frame_Three_Screen)

    sys.exit(app.exec_())