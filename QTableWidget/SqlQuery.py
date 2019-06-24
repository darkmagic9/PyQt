#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年5月15日
@author: Irony
@site: https://pyqt5.com , https://github.com/892768447
@email: 892768447@qq.com
@file: SqlQuery
@description: 
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Text
from Lib.mainui import Ui_Form
import os
os.chdir(os.path.dirname(__file__))

__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"

# engine = create_engine('mysql+mysqldb://root@localhost:3306/tourist?charset=utf8')
engine = create_engine('sqlite:///Data/data.sqlite3', echo=True)  # echo 表示开启命令显示
Base = declarative_base()


class Tourist(Base):

    __tablename__ = 'tourist'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    license = Column(Text)
    flightnumber = Column(Text)
    flightdate = Column(Text)
    seatnumber = Column(Text)
    boardingport = Column(Text)
    no = Column(Text)
    departurestation = Column(Text)
    destinationstation = Column(Text)


class Window(QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # Splicing field of sql
        self.sql = {}
        # Database linkage
        self.session = sessionmaker(bind=engine)()

    @pyqtSlot()
    def on_pushButtonQuery_clicked(self):
        """查询按钮"""
        self.applyName()
        self.applySeat()
        self.applyLicense()
        self.applyPort()
        if not self.sql:
            return QMessageBox.warning(self, 'Prompt', 'No input is made')
        # Clear data
        self.tableWidget.clear()
        # Reset the header
        self.tableWidget.setHorizontalHeaderLabels(
            ['number', 'name', 'document number', 'flight number', 'flight date', 'seat number', 'departure', 'serial number', 'departure place', 'destination'])
        # Parallel query based on selected fields
        rets = self.session.query(Tourist).filter(
            and_(*(key == value for key, value in self.sql.items()))).all()
        if not rets:
            return QMessageBox.information(self, 'Prompt', 'Not found results')
        self.tableWidget.setRowCount(len(rets))
        # Add to the table based on the results of the query
        for row, tourist in enumerate(rets):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(tourist.id)))
            self.tableWidget.setItem(
                row, 1, QTableWidgetItem(str(tourist.name)))
            self.tableWidget.setItem(
                row, 2, QTableWidgetItem(str(tourist.license)))
            self.tableWidget.setItem(
                row, 3, QTableWidgetItem(str(tourist.flightnumber)))
            self.tableWidget.setItem(
                row, 4, QTableWidgetItem(str(tourist.flightdate)))
            self.tableWidget.setItem(
                row, 5, QTableWidgetItem(str(tourist.seatnumber)))
            self.tableWidget.setItem(
                row, 6, QTableWidgetItem(str(tourist.boardingport)))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(str(tourist.no)))
            self.tableWidget.setItem(
                row, 8, QTableWidgetItem(str(tourist.departurestation)))
            self.tableWidget.setItem(
                row, 9, QTableWidgetItem(str(tourist.destinationstation)))

    def applyName(self):
        """Name"""
        if not self.checkBoxName.isChecked():
            if Tourist.name in self.sql:
                # Remove
                self.sql.pop(Tourist.name)
        # Update or add to the dictionary
        else:
            self.sql[Tourist.name] = self.lineEditName.text().strip()

    def applySeat(self):
        """seat number"""
        if not self.checkBoxSeat.isChecked():
            if Tourist.seatnumber in self.sql:
                # Remove
                self.sql.pop(Tourist.seatnumber)
        # Update or add to the dictionary
        else:
            self.sql[Tourist.seatnumber] = self.lineEditSeat.text().strip()

    def applyLicense(self):
        """license number"""
        if not self.checkBoxLicense.isChecked():
            if Tourist.license in self.sql:
                # Remove
                self.sql.pop(Tourist.license)
        # Update or add to the dictionary
        else:
            self.sql[Tourist.license] = self.lineEditLicense.text().strip()

    def applyPort(self):
        """Boarding port"""
        if not self.checkBoxPort.isChecked():
            if Tourist.boardingport in self.sql:
                # Remove
                self.sql.pop(Tourist.boardingport)
        # Update or add to the dictionary
        else:
            self.sql[Tourist.boardingport] = self.lineEditPort.text().strip()


if __name__ == '__main__':
    import sys
    import cgitb
    sys.excepthook = cgitb.Hook(1, None, 5, sys.stderr, 'text')
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
