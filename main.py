#!/usr/bin/env python
import sys
from lib import physiology, conversions
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
from ui.ConversionWindow import Ui_ConversionWindow
from ui.AboutWindow import Ui_AboutWindow


class AboutWindow(QMainWindow, Ui_AboutWindow):

    def __init__(self, *args, **kwargs):
        super(AboutWindow, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())


class ConversionWindow(QMainWindow, Ui_ConversionWindow):

    def __init__(self, *args, **kwargs):
        super(ConversionWindow, self).__init__(*args, **kwargs)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        self.convert_temp.clicked.connect(self.handleConvertTemp)
        self.convert_mass.clicked.connect(self.handleConvertMass)
        self.clear_temp.clicked.connect(self.handleClearTemp)
        self.clear_mass.clicked.connect(self.handleClearMass)

    def handleConvertTemp(self):
        try:
            # celsius to fahrenheit
            if self.temp_input_combo.currentText() == 'Celsius' and \
                    self.temp_output_combo.currentText() == 'Fahrenheit':
                celsius = float(self.temp_input.text())
                if celsius <= -273.15:
                    self.temp_input.setText('-273.15, absolute zero.')

                result = conversions.celsius_to_fahrenheit(celsius)
                self.temp_output.setText(str(result))
            # celsius to kelvin
            elif self.temp_input_combo.currentText() == 'Celsius' and \
                    self.temp_output_combo.currentText() == 'Kelvin':
                celsius = float(self.temp_input.text())
                if celsius <= -273.15:
                    self.temp_input.setText('-273.15, absolute zero.')

                result = conversions.celsius_to_kelvin(celsius)
                self.temp_output.setText(str(result))
            # kelvin to celsius
            elif self.temp_input_combo.currentText() == 'Kelvin' and \
                    self.temp_output_combo.currentText() == 'Celsius':
                kelvin = float(self.temp_input.text())
                if kelvin <= 0.0:
                    self.temp_input.setText('0.0, absolute zero.')

                result = conversions.kelvin_to_celsius(kelvin)
                self.temp_output.setText(str(result))
            # kelvin to fahrenheit
            elif self.temp_input_combo.currentText() == 'Kelvin' and \
                    self.temp_output_combo.currentText() == 'Fahrenheit':
                kelvin = float(self.temp_input.text())
                if kelvin <= 0.0:
                    self.temp_input.setText('0.0, absolute zero.')

                result = conversions.kelvin_to_fahrenheit(kelvin)
                self.temp_output.setText(str(result))
            # fahrenheit to celsius
            elif self.temp_input_combo.currentText() == 'Fahrenheit' and \
                    self.temp_output_combo.currentText() == 'Celsius':
                fahrenheit = float(self.temp_input.text())
                if fahrenheit <= -459.67:
                    self.temp_input.setText('-459.67, absolute zero.')

                result = conversions.fahrenheit_to_celsius(fahrenheit)
                self.temp_output.setText(str(result))
            # fahrenheit to kelvin
            elif self.temp_input_combo.currentText() == 'Fahrenheit' and \
                    self.temp_output_combo.currentText() == 'Kelvin':
                fahrenheit = float(self.temp_input.text())
                if fahrenheit <= -459.67:
                    self.temp_input.setText('-459.67, absolute zero.')

                result = conversions.fahrenheit_to_kelvin(fahrenheit)
                self.temp_output.setText(str(result))
            elif self.temp_input_combo.currentText() == 'Celsius' and \
                    self.temp_output_combo.currentText() == 'Celsius':
                if float(self.temp_input.text()) <= -273.15:
                    self.temp_input.setText('-273.15, absolute zero.')
                    self.temp_output.setText('-273.15, absolute zero.')
                elif float(self.temp_input.text()) > -273.15:
                    self.temp_output.setText(self.temp_input.text())
            elif self.temp_input_combo.currentText() == 'Kelvin' and \
                    self.temp_output_combo.currentText() == 'Kelvin':
                if float(self.temp_input.text()) <= 0.0:
                    self.temp_input.setText('0.0, absolute zero.')
                    self.temp_output.setText('0.0, absolute zero.')
                elif float(self.temp_input.text()) > 0.0:
                    self.temp_output.setText(self.temp_input.text())
            elif self.temp_input_combo.currentText() == 'Fahrenheit' and \
                    self.temp_output_combo.currentText() == 'Fahrenheit':
                if float(self.temp_input.text()) <= -459.67:
                    self.temp_input.setText('-459.67, absolute zero.')
                    self.temp_output.setText('-459.67, absolute zero.')
                elif float(self.temp_input.text()) > -459.67:
                    self.temp_output.setText(self.temp_input.text())
        except ValueError:
            pass

    def handleClearTemp(self):
        self.temp_input.clear()
        self.temp_output.clear()

    def handleConvertMass(self):
        try:
            error = 'Error: negative weight.'
            # pound to gram
            if self.mass_input_combo.currentText() == 'Pound' and \
                    self.mass_output_combo.currentText() == 'Gram':
                pound = float(self.mass_input.text())
                if pound < 0:
                    self.mass_input.setText(error)

                result = conversions.pound_to_gram(pound)
                self.mass_output.setText(str(result))
            # pound to kilogram
            elif self.mass_input_combo.currentText() == 'Pound' and \
                    self.mass_output_combo.currentText() == 'Kilogram':
                pound = float(self.mass_input.text())
                if pound < 0:
                    self.mass_input.setText(error)

                result = conversions.pound_to_kilogram(pound)
                self.mass_output.setText(str(result))
            # gram to pound
            elif self.mass_input_combo.currentText() == 'Gram' and \
                    self.mass_output_combo.currentText() == 'Pound':
                gram = float(self.mass_input.text())
                if gram < 0:
                    self.mass_input.setText(error)

                result = conversions.gram_to_pound(gram)
                self.mass_output.setText(str(result))
            # gram to kilogram
            elif self.mass_input_combo.currentText() == 'Gram' and \
                    self.mass_output_combo.currentText() == 'Kilogram':
                gram = float(self.mass_input.text())
                if gram < 0:
                    self.mass_input.setText(error)

                result = conversions.gram_to_kilogram(gram)
                self.mass_output.setText(str(result))
            # kilogram to gram
            elif self.mass_input_combo.currentText() == 'Kilogram' and \
                    self.mass_output_combo.currentText() == 'Gram':
                kilogram = float(self.mass_input.text())
                if kilogram < 0:
                    self.mass_input.setText(error)

                result = conversions.kilogram_to_gram(kilogram)
                self.mass_output.setText(str(result))
            # kilogram to pound
            elif self.mass_input_combo.currentText() == 'Kilogram' and \
                    self.mass_output_combo.currentText() == 'Pound':
                kilogram = float(self.mass_input.text())
                if kilogram < 0:
                    self.mass_input.setText(error)

                result = conversions.kilogram_to_pound(kilogram)
                self.mass_output.setText(str(result))
            elif self.mass_input_combo.currentText() == 'Pound' and \
                    self.mass_output_combo.currentText() == 'Pound':
                if float(self.mass_input.text()) < 0:
                    self.mass_input.setText(error)
                    self.mass_output.setText(error)
                elif float(self.mass_input.text()) >= 0:
                    self.mass_output.setText(self.mass_input.text())
            elif self.mass_input_combo.currentText() == 'Gram' and \
                    self.mass_output_combo.currentText() == 'Gram':
                if float(self.mass_input.text()) < 0:
                    self.mass_input.setText(error)
                    self.mass_output.setText(error)
                elif float(self.mass_input.text()) >= 0:
                    self.mass_output.setText(self.mass_input.text())
            elif self.mass_input_combo.currentText() == 'Kilogram' and \
                    self.mass_output_combo.currentText() == 'Kilogram':
                if float(self.mass_input.text()) < 0:
                    self.mass_input.setText(error)
                    self.mass_output.setText(error)
                elif float(self.mass_input.text()) >= 0:
                    self.mass_output.setText(self.mass_input.text())
        except ValueError:
            pass

    def handleClearMass(self):
        self.mass_input.clear()
        self.mass_output.clear()


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
        try:
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
        except ValueError:
            pass

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
        try:
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
        except ValueError:
            pass

    def handleCalcImperial(self):
        try:
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
        except ValueError:
            pass

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
        try:
            x = float(self.mean_dist.text())
            d = float(self.diffuse.text())

            result = physiology.time_diffusion_distance(x, d)
            self.time.setText(str(result))
        except ValueError:
            pass

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
        try:
            t_1 = float(self.t_1.text())
            t_2 = float(self.t_2.text())
            r_1 = float(self.r_1.text())
            r_2 = float(self.r_2.text())

            result = physiology.temperature_coefficient(t_1, t_2, r_1, r_2)
            self.q_10.setText(str(result))
        except ValueError:
            pass

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
        try:
            veq = float(self.veq.text())
            vm = float(self.vm.text())

            result = physiology.electrochemical_driving_force(veq, vm)
            self.dforce.setText(str(result))
        except ValueError:
            pass

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
        self.clear.clicked.connect(self.handleClear)
        self.sample_data.clicked.connect(self.handleSampleData)

    def handleCalculate(self):
        try:
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
        except ValueError:
            pass

    def handleClear(self):
        self.temp.clear()
        self.k_perm.clear()
        self.na_perm.clear()
        self.cl_perm.clear()
        self.k_out.clear()
        self.k_in.clear()
        self.na_out.clear()
        self.na_in.clear()
        self.cl_out.clear()
        self.cl_in.clear()
        self.vm.clear()

    def handleSampleData(self):
        self.handleClear()
        self.temp.setText('310')
        self.k_perm.setText('1')
        self.na_perm.setText('0.05')
        self.cl_perm.setText('0.45')
        self.k_out.setText('4')
        self.k_in.setText('150')
        self.na_out.setText('145')
        self.na_in.setText('15')
        self.cl_out.setText('110')
        self.cl_in.setText('10')


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
        self.clear.clicked.connect(self.handleClear)

    def handleCalculate(self):
        try:
            systolic = float(self.systolic.text())
            diastolic = float(self.diastolic.text())

            result = physiology.mean_arterial_pressure(systolic, diastolic)
            self.pulsepress.setText(str(result[0]))
            self.map.setText(str(result[1]))
        except ValueError:
            pass

    def handleClear(self):
        self.systolic.clear()
        self.diastolic.clear()
        self.pulsepress.clear()
        self.map.clear()


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
        self.clear.clicked.connect(self.handleClear)

    def handleCalculate(self):
        try:
            t = float(self.temp.text())
            z = float(self.valence.text())
            x_out = float(self.xout.text())
            x_in = float(self.xin.text())

            result = physiology.nernst_potential(t, z, x_out, x_in)
            self.veq.setText(str(result))
        except ValueError:
            pass

    def handleClear(self):
        self.temp.clear()
        self.valence.clear()
        self.xout.clear()
        self.xin.clear()
        self.veq.clear()


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
        self.conversionButton.clicked.connect(self.handleConversionButton)
        self.aboutButton.clicked.connect(self.handleAboutButton)

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

    def handleConversionButton(self):
        conversion_window = ConversionWindow(self)
        conversion_window.show()

    def handleAboutButton(self):
        about_window = AboutWindow(self)
        about_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
