import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide2 import QtWidgets, QtCore


class FunctionPlotter(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.plot_button = None
        self.max_textbox = None
        self.max_label = None
        self.min_textbox = None
        self.min_label = None
        self.function_textbox = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Function Plotter")

        # Create a text box for the user to enter the function.
        self.function_textbox = QtWidgets.QLineEdit()

        # Create a label for the min value of x.
        self.min_label = QtWidgets.QLabel("Min:")

        # Create a text box for the user to enter the min value of x.
        self.min_textbox = QtWidgets.QLineEdit()

        # Create a label for the max value of x.
        self.max_label = QtWidgets.QLabel("Max:")

        # Create a text box for the user to enter the max value of x.
        self.max_textbox = QtWidgets.QLineEdit()

        # Create a button to plot the function.
        self.plot_button = QtWidgets.QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot_function)

        # Lay out the widgets.
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.function_textbox)
        layout.addWidget(self.min_label)
        layout.addWidget(self.min_textbox)
        layout.addWidget(self.max_label)
        layout.addWidget(self.max_textbox)
        layout.addWidget(self.plot_button)
        self.setLayout(layout)

    def plot_function(function, min_x, max_x):
        """Plots a function between min_x and max_x."""

        function = function.replace("*", "")
        function = function.replace("+", "")

        x = float(function)
        y_values = eval(function)
        plt.plot(x, y_values)
        plt.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    app.exec_()
