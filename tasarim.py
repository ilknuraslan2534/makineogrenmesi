# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasarim.ui'
#
# Created: Thu Jan 11 06:12:29 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(816, 565)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 561))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 781, 561))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.knn = QtGui.QPushButton(self.groupBox)
        self.knn.setGeometry(QtCore.QRect(140, 440, 131, 31))
        self.knn.setObjectName(_fromUtf8("knn"))
        self.dosyayukle_knn = QtGui.QPushButton(self.groupBox)
        self.dosyayukle_knn.setGeometry(QtCore.QRect(520, 440, 121, 31))
        self.dosyayukle_knn.setObjectName(_fromUtf8("dosyayukle_knn"))
        self.table_2 = QtGui.QTableWidget(self.groupBox)
        self.table_2.setGeometry(QtCore.QRect(440, 20, 321, 401))
        self.table_2.setObjectName(_fromUtf8("table_2"))
        self.table_2.setColumnCount(0)
        self.table_2.setRowCount(0)
        self.graphicsView = QtGui.QGraphicsView(self.groupBox)
        self.graphicsView.setGeometry(QtCore.QRect(0, 20, 401, 401))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 0, 831, 531))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.groupBox_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 20, 381, 391))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.groupBox_3)
        self.graphicsView_3.setGeometry(QtCore.QRect(400, 20, 381, 391))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.btn_kmeans = QtGui.QPushButton(self.groupBox_3)
        self.btn_kmeans.setGeometry(QtCore.QRect(570, 420, 121, 41))
        self.btn_kmeans.setObjectName(_fromUtf8("btn_kmeans"))
        self.btn_veriler = QtGui.QPushButton(self.groupBox_3)
        self.btn_veriler.setGeometry(QtCore.QRect(70, 420, 101, 41))
        self.btn_veriler.setObjectName(_fromUtf8("btn_veriler"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(270, 420, 231, 111))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 101, 61))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 20, 211, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 81, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 130, 351, 211))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.nb_label = QtGui.QLabel(self.groupBox_5)
        self.nb_label.setGeometry(QtCore.QRect(170, 35, 111, 31))
        self.nb_label.setObjectName(_fromUtf8("nb_label"))
        self.nb_bul = QtGui.QPushButton(self.groupBox_2)
        self.nb_bul.setGeometry(QtCore.QRect(1090, 150, 101, 31))
        self.nb_bul.setObjectName(_fromUtf8("nb_bul"))
        self.naviebayes = QtGui.QPushButton(self.groupBox_2)
        self.naviebayes.setGeometry(QtCore.QRect(270, 80, 121, 23))
        self.naviebayes.setObjectName(_fromUtf8("naviebayes"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.widget = QtGui.QWidget()
        self.widget.setObjectName(_fromUtf8("widget"))
        self.tabWidget.addTab(self.widget, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.groupBox_14 = QtGui.QGroupBox(self.tab_7)
        self.groupBox_14.setGeometry(QtCore.QRect(0, 0, 401, 531))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.graphicsView_4 = QtGui.QGraphicsView(self.groupBox_14)
        self.graphicsView_4.setGeometry(QtCore.QRect(0, 20, 391, 361))
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.groupBox_16 = QtGui.QGroupBox(self.groupBox_14)
        self.groupBox_16.setGeometry(QtCore.QRect(0, 390, 391, 131))
        self.groupBox_16.setObjectName(_fromUtf8("groupBox_16"))
        self.btnros = QtGui.QPushButton(self.groupBox_16)
        self.btnros.setGeometry(QtCore.QRect(90, 30, 161, 23))
        self.btnros.setObjectName(_fromUtf8("btnros"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_16)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 60, 161, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.btndengelenmemis = QtGui.QPushButton(self.groupBox_16)
        self.btndengelenmemis.setGeometry(QtCore.QRect(90, 90, 161, 23))
        self.btndengelenmemis.setObjectName(_fromUtf8("btndengelenmemis"))
        self.groupBox_15 = QtGui.QGroupBox(self.tab_7)
        self.groupBox_15.setGeometry(QtCore.QRect(400, 0, 401, 531))
        self.groupBox_15.setObjectName(_fromUtf8("groupBox_15"))
        self.rus = QtGui.QGraphicsView(self.groupBox_15)
        self.rus.setGeometry(QtCore.QRect(10, 40, 381, 241))
        self.rus.setObjectName(_fromUtf8("rus"))
        self.ros = QtGui.QGraphicsView(self.groupBox_15)
        self.ros.setGeometry(QtCore.QRect(10, 310, 391, 211))
        self.ros.setObjectName(_fromUtf8("ros"))
        self.label_10 = QtGui.QLabel(self.groupBox_15)
        self.label_10.setGeometry(QtCore.QRect(110, 290, 191, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_9 = QtGui.QLabel(self.groupBox_15)
        self.label_9.setGeometry(QtCore.QRect(110, 20, 141, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 0, 791, 531))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.tabloveriler = QtGui.QTableWidget(self.groupBox_6)
        self.tabloveriler.setGeometry(QtCore.QRect(0, 20, 431, 321))
        self.tabloveriler.setObjectName(_fromUtf8("tabloveriler"))
        self.tabloveriler.setColumnCount(0)
        self.tabloveriler.setRowCount(0)
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_7.setGeometry(QtCore.QRect(440, 10, 381, 241))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.trainveriler = QtGui.QTableWidget(self.groupBox_7)
        self.trainveriler.setGeometry(QtCore.QRect(10, 20, 331, 211))
        self.trainveriler.setObjectName(_fromUtf8("trainveriler"))
        self.trainveriler.setColumnCount(0)
        self.trainveriler.setRowCount(0)
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_8.setGeometry(QtCore.QRect(0, 350, 431, 171))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.dosyarandom = QtGui.QPushButton(self.groupBox_8)
        self.dosyarandom.setGeometry(QtCore.QRect(0, 30, 101, 31))
        self.dosyarandom.setObjectName(_fromUtf8("dosyarandom"))
        self.label_5 = QtGui.QLabel(self.groupBox_8)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 161, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_5.setPalette(palette)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_8)
        self.label_6.setGeometry(QtCore.QRect(220, 120, 191, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_6.setPalette(palette)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.btn_traintest = QtGui.QPushButton(self.groupBox_8)
        self.btn_traintest.setGeometry(QtCore.QRect(110, 30, 101, 31))
        self.btn_traintest.setObjectName(_fromUtf8("btn_traintest"))
        self.randomforest = QtGui.QPushButton(self.groupBox_8)
        self.randomforest.setGeometry(QtCore.QRect(220, 30, 91, 31))
        self.randomforest.setObjectName(_fromUtf8("randomforest"))
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_9.setGeometry(QtCore.QRect(440, 260, 381, 261))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.testveriler = QtGui.QTableWidget(self.groupBox_9)
        self.testveriler.setGeometry(QtCore.QRect(10, 20, 331, 241))
        self.testveriler.setObjectName(_fromUtf8("testveriler"))
        self.testveriler.setColumnCount(0)
        self.testveriler.setRowCount(0)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_10.setGeometry(QtCore.QRect(0, 0, 791, 341))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.tablonormalize = QtGui.QTableWidget(self.groupBox_10)
        self.tablonormalize.setGeometry(QtCore.QRect(0, 20, 791, 291))
        self.tablonormalize.setObjectName(_fromUtf8("tablonormalize"))
        self.tablonormalize.setColumnCount(0)
        self.tablonormalize.setRowCount(0)
        self.normalizetest = QtGui.QComboBox(self.tab_6)
        self.normalizetest.setGeometry(QtCore.QRect(290, 440, 171, 31))
        self.normalizetest.setObjectName(_fromUtf8("normalizetest"))
        self.normalizeyukle = QtGui.QPushButton(self.tab_6)
        self.normalizeyukle.setGeometry(QtCore.QRect(290, 370, 171, 41))
        self.normalizeyukle.setObjectName(_fromUtf8("normalizeyukle"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_8)
        self.groupBox_11.setGeometry(QtCore.QRect(370, 10, 421, 261))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.normaltrain = QtGui.QTableWidget(self.groupBox_11)
        self.normaltrain.setGeometry(QtCore.QRect(10, 20, 411, 221))
        self.normaltrain.setObjectName(_fromUtf8("normaltrain"))
        self.normaltrain.setColumnCount(0)
        self.normaltrain.setRowCount(0)
        self.groupBox_13 = QtGui.QGroupBox(self.tab_8)
        self.groupBox_13.setGeometry(QtCore.QRect(370, 280, 431, 251))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.normaltest = QtGui.QTableWidget(self.groupBox_13)
        self.normaltest.setGeometry(QtCore.QRect(10, 20, 411, 221))
        self.normaltest.setObjectName(_fromUtf8("normaltest"))
        self.normaltest.setColumnCount(0)
        self.normaltest.setRowCount(0)
        self.groupBox_17 = QtGui.QGroupBox(self.tab_8)
        self.groupBox_17.setGeometry(QtCore.QRect(0, 0, 371, 381))
        self.groupBox_17.setObjectName(_fromUtf8("groupBox_17"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox_17)
        self.tableWidget.setGeometry(QtCore.QRect(0, 20, 361, 351))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox_18 = QtGui.QGroupBox(self.tab_8)
        self.groupBox_18.setGeometry(QtCore.QRect(0, 400, 371, 131))
        self.groupBox_18.setObjectName(_fromUtf8("groupBox_18"))
        self.btnveridok = QtGui.QPushButton(self.groupBox_18)
        self.btnveridok.setGeometry(QtCore.QRect(20, 30, 111, 21))
        self.btnveridok.setObjectName(_fromUtf8("btnveridok"))
        self.traintest = QtGui.QPushButton(self.groupBox_18)
        self.traintest.setGeometry(QtCore.QRect(20, 60, 101, 31))
        self.traintest.setObjectName(_fromUtf8("traintest"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_18)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 40, 141, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.groupBox_12 = QtGui.QGroupBox(self.tab_9)
        self.groupBox_12.setGeometry(QtCore.QRect(0, 0, 321, 411))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.tableWidget_2 = QtGui.QTableWidget(self.groupBox_12)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 20, 311, 381))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.btnhw_veriler = QtGui.QPushButton(self.tab_9)
        self.btnhw_veriler.setGeometry(QtCore.QRect(620, 70, 161, 23))
        self.btnhw_veriler.setObjectName(_fromUtf8("btnhw_veriler"))
        self.tableWidget_3 = QtGui.QTableWidget(self.tab_9)
        self.tableWidget_3.setGeometry(QtCore.QRect(320, 10, 291, 391))
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.pushButton_4 = QtGui.QPushButton(self.tab_9)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 100, 161, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_19 = QtGui.QGroupBox(self.tab_9)
        self.groupBox_19.setGeometry(QtCore.QRect(20, 410, 761, 111))
        self.groupBox_19.setObjectName(_fromUtf8("groupBox_19"))
        self.label_7 = QtGui.QLabel(self.groupBox_19)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_19)
        self.label_8.setGeometry(QtCore.QRect(40, 40, 46, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_11 = QtGui.QLabel(self.groupBox_19)
        self.label_11.setGeometry(QtCore.QRect(40, 60, 46, 13))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_19)
        self.label_12.setGeometry(QtCore.QRect(40, 80, 46, 13))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_19)
        self.label_13.setGeometry(QtCore.QRect(360, 10, 46, 13))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_19)
        self.label_14.setGeometry(QtCore.QRect(360, 30, 46, 13))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_19)
        self.label_15.setGeometry(QtCore.QRect(360, 50, 46, 13))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_19)
        self.label_16.setGeometry(QtCore.QRect(360, 70, 46, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.tabWidget.addTab(self.tab_9, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "KNN HESAPLAMA", None))
        self.knn.setText(_translate("Dialog", "KNN_HESAPLA", None))
        self.dosyayukle_knn.setText(_translate("Dialog", "Verileri Dök", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "K Nearest Neigbors", None))
        self.groupBox_3.setTitle(_translate("Dialog", "K-Means", None))
        self.btn_kmeans.setText(_translate("Dialog", "K Means", None))
        self.btn_veriler.setText(_translate("Dialog", "Verileri Dök", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Verilerin Merkezi", None))
        self.label_4.setText(_translate("Dialog", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "K-Means", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Navie Bayes", None))
        self.label_2.setText(_translate("Dialog", "Kelime Giriniz:", None))
        self.groupBox_5.setTitle(_translate("Dialog", "Sonuç", None))
        self.label_3.setText(_translate("Dialog", " Kategori:", None))
        self.nb_label.setText(_translate("Dialog", "TextLabel", None))
        self.nb_bul.setText(_translate("Dialog", "Bul", None))
        self.naviebayes.setText(_translate("Dialog", "Navie Bayes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Navie Bayes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Dialog", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Page", None))
        self.groupBox_14.setTitle(_translate("Dialog", "Dengelenmemiş Veriler", None))
        self.groupBox_16.setTitle(_translate("Dialog", "İşlemleri Gerçekleştir", None))
        self.btnros.setText(_translate("Dialog", "ROS ile Dengele", None))
        self.pushButton_5.setText(_translate("Dialog", "RUS ile Dengele", None))
        self.btndengelenmemis.setText(_translate("Dialog", "Dengelenmemis Veriler", None))
        self.groupBox_15.setTitle(_translate("Dialog", "Dengelenmiş Veriler", None))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa007f;\">Random Over Sampling</span></p></body></html>", None))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa007f;\">Random Under Sampling</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Dialog", "ROS-RUS", None))
        self.groupBox_6.setTitle(_translate("Dialog", "Veriler", None))
        self.groupBox_7.setTitle(_translate("Dialog", "Train Veriler", None))
        self.groupBox_8.setTitle(_translate("Dialog", "İşlemi yap", None))
        self.dosyarandom.setText(_translate("Dialog", "Dosya Yükle", None))
        self.label_5.setText(_translate("Dialog", "Random Forest Başarısı:", None))
        self.label_6.setText(_translate("Dialog", "TextLabel", None))
        self.btn_traintest.setText(_translate("Dialog", "Train and Test", None))
        self.randomforest.setText(_translate("Dialog", "Sonuç", None))
        self.groupBox_9.setTitle(_translate("Dialog", " Test Veriler", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Randrom Forest", None))
        self.groupBox_10.setTitle(_translate("Dialog", "Veriler", None))
        self.normalizeyukle.setText(_translate("Dialog", "Verileri Yükle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog", "Normalizasyon", None))
        self.groupBox_11.setTitle(_translate("Dialog", "Train Veriler", None))
        self.groupBox_13.setTitle(_translate("Dialog", "Test Veriler", None))
        self.groupBox_17.setTitle(_translate("Dialog", "Veriler", None))
        self.groupBox_18.setTitle(_translate("Dialog", "İşlemler", None))
        self.btnveridok.setText(_translate("Dialog", "Verileri Dök", None))
        self.traintest.setText(_translate("Dialog", "Train/Test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Dialog", "Train/Test", None))
        self.groupBox_12.setTitle(_translate("Dialog", "GroupBox", None))
        self.btnhw_veriler.setText(_translate("Dialog", "hw_dataset", None))
        self.pushButton_4.setText(_translate("Dialog", "nw_dataset", None))
        self.groupBox_19.setTitle(_translate("Dialog", "GroupBox", None))
        self.label_7.setText(_translate("Dialog", "TextLabel", None))
        self.label_8.setText(_translate("Dialog", "TextLabel", None))
        self.label_11.setText(_translate("Dialog", "TextLabel", None))
        self.label_12.setText(_translate("Dialog", "TextLabel", None))
        self.label_13.setText(_translate("Dialog", "TextLabel", None))
        self.label_14.setText(_translate("Dialog", "TextLabel", None))
        self.label_15.setText(_translate("Dialog", "TextLabel", None))
        self.label_16.setText(_translate("Dialog", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Dialog", "PARKİNSON", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

