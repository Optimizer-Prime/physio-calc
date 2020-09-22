#!/usr/bin/env python
import sys
from lib import physiology
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5 import QtCore
from ui.MainWindow import Ui_MainWindow
from ui.NernstWindow import Ui_NernstWindow
from ui.ArterialWindow import Ui_ArterialWindow
from ui.GhkWindow import Ui_GhkWindow
from ui.EdfWindow import Ui_EdfWindow
from ui.TempcoWindow import Ui_TempcoWindow
from ui.TimediffuseWindow import Ui_TimediffuseWindow
from ui.BmiWindow import Ui_BmiWindow
from ui.BodyfatWindow import Ui_BodyfatWindow


class BodyfatWindow(QMainWindow, Ui_BodyfatWindow):

    def __init__(self, *args, **kwargs):
        super(BodyfatWindow, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        self.calculate.clicked.connect(self.handleCalculate)
        self.clear.clicked.connect(self.handleClear)

    def handleCalculate(self):
        if self.sex.currentText() == 'Male':
            height = (float(self.feet.currentText()) * 12) + (float(self.inches.currentText()))
            neck = float(self.neck_circum.text())
            waist = float(self.waist_circum.text())
            age = int(self.age.text())

            result = physiology.body_fat_male(height, neck, waist)
            if 18 <= age <= 21 and result <= 22.0:
                self.bodyfat.setText('{:.2f}%'.format(result) + ", you meet US Navy standards!")
            elif 22 <= age <= 29 and result <= 23.0:
                self.bodyfat.setText('{:.2f}%'.format(result) + ", you meet US Navy standards!")
            elif 30 <= age <= 39 and result <= 24.0:
                self.bodyfat.setText('{:.2f}%'.format(result) + ", you meet US Navy standards!")
            elif age > 40 and result <= 26.0:
                self.bodyfat.setText('{:.2f}%'.format(result) + ", you meet US Navy standards!")
            else:
                self.bodyfat.setText('{:.2f}%'.format(result) + ", you do not meet standards.")
        elif self.sex.currentText() == 'Female':
            height = (float(self.feet.currentText()) * 12) + (float(self.inches.currentText()))
            neck = float(self.neck_circum.text())
            waist = float(self.waist_circum.text())
            hip = float(self.hip_circum.text())
            age = int(self.age.text())

            result = physiology.body_fat_female(height, neck, waist, hip)
            if 18 <= age <= 21 and result <= 33.0:
                self.bodyfat.setText('{:.2f}%'.format(result) + ", you meet US Navy standards!")
            elif 22 <= age <= 29 and result <= 34.0:
                self.bodyfat.setText('{:.2f}%'.format(result) + ", you meet US Navy standards!")
            elif 30 <= age <= 39 and result <= 35.0:
                self.bodyfat.setText('{:.2f}%'.format(result) + ", you meet US Navy standards!")
            elif age > 40 and result <= 36.0:
                self.bodyfat.setText('{:.2f}%'.format(result) + ", you meet US Navy standards!")
            else:
                self.bodyfat.setText('{:.2f}%'.format(result) + ", you do not meet standards.")

    def handleClear(self):
        self.age.clear()
        self.neck_circum.clear()
        self.waist_circum.clear()
        self.hip_circum.clear()
        self.bodyfat.clear()


class BmiWindow(QMainWindow, Ui_BmiWindow):

    def __init__(self, *args, **kwargs):
        super(BmiWindow, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        self.calc_metric.clicked.connect(self.handleCalcMetric)
        self.calc_imperial.clicked.connect(self.handleCalcImperial)
        self.clear_metric.clicked.connect(self.handleClearMetric)
        self.clear_imperial.clicked.connect(self.handleClearImperial)

    def handleCalcMetric(self):
        kg = float(self.weight_metric.text())
        m = float(self.height_metric.text())

        result = physiology.bmi_metric(kg, m)
        if result < 18.5:
            self.bmi_metric.setText('{:.2f}'.format(result) + ", Underweight")
        elif 18.5 <= result <= 24.9:
            self.bmi_metric.setText('{:.2f}'.format(result) + ", Normal")
        elif 25.0 <= result <= 29.9:
            self.bmi_metric.setText('{:.2f}'.format(result) + ", Overweight")
        elif 30.0 <= result <= 34.9:
            self.bmi_metric.setText('{:.2f}'.format(result) + ", Obese - Class I")
        elif 35.0 <= result <= 39.9:
            self.bmi_metric.setText('{:.2f}'.format(result) + ", Obese - Class II")
        elif result >= 40.0:
            self.bmi_metric.setText('{:.2f}'.format(result) + ", Extremely Obese - Class III")

    def handleCalcImperial(self):
        lb = float(self.weight_imperial.text())
        inches = (float(self.feet.currentText()) * 12) + (float(self.inches.currentText()))

        result = physiology.bmi_imperial(lb, inches)
        if result < 18.5:
            self.bmi_imperial.setText('{:.2f}'.format(result) + ", Underweight")
        elif 18.5 <= result <= 24.9:
            self.bmi_imperial.setText('{:.2f}'.format(result) + ", Normal")
        elif 25.0 <= result <= 29.9:
            self.bmi_imperial.setText('{:.2f}'.format(result) + ", Overweight")
        elif 30.0 <= result <= 34.9:
            self.bmi_imperial.setText('{:.2f}'.format(result) + ", Obese - Class I")
        elif 35.0 <= result <= 39.9:
            self.bmi_imperial.setText('{:.2f}'.format(result) + ", Obese - Class II")
        elif result >= 40.0:
            self.bmi_imperial.setText('{:.2f}'.format(result) + ", Extremely Obese - Class III")

    def handleClearMetric(self):
        self.weight_metric.clear()
        self.height_metric.clear()
        self.bmi_metric.clear()

    def handleClearImperial(self):
        self.weight_imperial.clear()
        self.bmi_imperial.clear()


class TimediffuseWindow(QMainWindow, Ui_TimediffuseWindow):

    def __init__(self, *args, **kwargs):
        super(TimediffuseWindow, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        self.calculate.clicked.connect(self.handleCalculate)
        self.clear.clicked.connect(self.handleClear)

    def handleCalculate(self):
        x = float(self.mean_dist.text())
        d = float(self.diffuse.text())

        result = physiology.time_diffusion_distance(x, d)
        self.time.setText(str(result))

    def handleClear(self):
        self.mean_dist.clear()
        self.diffuse.clear()
        self.time.clear()


class TempcoWindow(QMainWindow, Ui_TempcoWindow):

    def __init__(self, *args, **kwargs):
        super(TempcoWindow, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        self.calculate.clicked.connect(self.handleCalculate)
        self.clear.clicked.connect(self.handleClear)

    def handleCalculate(self):
        t_1 = float(self.t_1.text())
        t_2 = float(self.t_2.text())
        r_1 = float(self.r_1.text())
        r_2 = float(self.r_2.text())

        result = physiology.temperature_coefficient(t_1, t_2, r_1, r_2)
        self.q_10.setText(str(result))

    def handleClear(self):
        self.t_1.clear()
        self.t_2.clear()
        self.r_1.clear()
        self.r_2.clear()
        self.q_10.clear()


class EdfWindow(QMainWindow, Ui_EdfWindow):

    def __init__(self, *args, **kwargs):
        super(EdfWindow, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        self.calculate.clicked.connect(self.handleCalculate)
        self.clear.clicked.connect(self.handleClear)

    def handleCalculate(self):
        veq = float(self.veq.text())
        vm = float(self.vm.text())

        result = physiology.electrochemical_driving_force(veq, vm)
        self.dforce.setText(str(result))

    def handleClear(self):
        self.veq.clear()
        self.vm.clear()
        self.dforce.clear()


class GhkWindow(QMainWindow, Ui_GhkWindow):

    def __init__(self, *args, **kwargs):
        super(GhkWindow, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        self.calculate.clicked.connect(self.handleCalculate)

    def handleCalculate(self):
        t = float(self.temp.text())
        p_k = float(self.k_perm.text())
        p_na = float(self.na_perm.text())
        p_cl = float(self.cl_perm.text())
        k_out = float(self.k_out.text())
        k_in = float(self.k_in.text())
        na_out = float(self.na_out.text())
        na_in = float(self.na_in.text())
        cl_out = float(self.cl_out.text())
        cl_in = float(self.cl_in.text())

        result = physiology.goldman_hodgkin_katz(t, p_k, p_na, p_cl, k_out, k_in,
                                                 na_out, na_in, cl_out, cl_in)
        if self.millivolt.isChecked():
            self.vm.setText(str(result * 1000))
        elif self.volt.isChecked():
            self.vm.setText(str(result))


class ArterialWindow(QMainWindow, Ui_ArterialWindow):

    def __init__(self, *args, **kwargs):
        super(ArterialWindow, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        self.calculate.clicked.connect(self.handleCalculate)

    def handleCalculate(self):
        systolic = int(self.systolic.text())
        diastolic = int(self.diastolic.text())

        result = physiology.mean_arterial_pressure(systolic, diastolic)
        self.pulsepress.setText(str(result[0]))
        self.map.setText(str(result[1]))


class NernstWindow(QMainWindow, Ui_NernstWindow):

    def __init__(self, *args, **kwargs):
        super(NernstWindow, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        self.calculate.clicked.connect(self.handleCalculate)

    def handleCalculate(self):
        t = float(self.temp.text())
        z = float(self.valence.text())
        x_out = float(self.xout.text())
        x_in = float(self.xin.text())

        result = physiology.nernst_potential(t, z, x_out, x_in)
        self.veq.setText(str(result))


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # centers window
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

        self.nernstButton.clicked.connect(self.handleNernstButton)
        self.mapButton.clicked.connect(self.handleMapButton)
        self.ghkButton.clicked.connect(self.handleGhkButton)
        self.edfButton.clicked.connect(self.handleEdfButton)
        self.tempcoButton.clicked.connect(self.handleTempcoButton)
        self.timediffuseButton.clicked.connect(self.handleTimeDiffuseButton)
        self.bmiButton.clicked.connect(self.handleBmiButton)
        self.bodyfatButton.clicked.connect(self.handleBodyfatButton)

    def handleNernstButton(self):
        # allows multiple windows to be opened
        nernst_window = NernstWindow(self)
        nernst_window.show()

    def handleMapButton(self):
        map_window = ArterialWindow(self)
        map_window.show()

    def handleGhkButton(self):
        ghk_window = GhkWindow(self)
        ghk_window.show()

    def handleEdfButton(self):
        edf_window = EdfWindow(self)
        edf_window.show()

    def handleTempcoButton(self):
        tempco_window = TempcoWindow(self)
        tempco_window.show()

    def handleTimeDiffuseButton(self):
        time_diffuse_window = TimediffuseWindow(self)
        time_diffuse_window.show()

    def handleBmiButton(self):
        bmi_window = BmiWindow(self)
        bmi_window.show()

    def handleBodyfatButton(self):
        bodyfat_window = BodyfatWindow(self)
        bodyfat_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
