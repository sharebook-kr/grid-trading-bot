import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QWidget,
    QLabel, QLineEdit, QComboBox, QTableWidget, QPushButton,
    QGridLayout, QHBoxLayout, QVBoxLayout
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(":: PYSTOCK Grid Trading Bot v1.0 ::")
        self.resize(750, 800)

        self.label_init_margin = QLabel("Initial Margin")
        self.label0 = QLabel("Lower Price")
        self.label1 = QLabel("Upper Price")
        self.label2 = QLabel("Grid Number")
        self.label3 = QLabel("Margin Mode")
        self.label4 = QLabel("Adjust Leverage")
        self.label5 = QLabel("Symbol")

        self.combo_margin = QComboBox()
        self.combo_margin.addItem("Cross")
        self.combo_margin.addItem("Isolated")

        self.combo_symbol = QComboBox()
        self.combo_symbol.addItem("BTC/USDT")
        self.combo_symbol.addItem("ETH/USDT")
        self.combo_symbol.addItem("XRP/USDT")
        self.combo_symbol.addItem("BNB/USDT")
        self.combo_symbol.addItem("BTC/BUSD")
        self.combo_symbol.addItem("ETH/BUSD")
        self.combo_symbol.addItem("XRP/BUSD")
        self.combo_symbol.addItem("BNB/BUSD")

        self.line_edit_init_margine = QLineEdit()
        self.line_edit0 = QLineEdit()
        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit3 = QLineEdit()

        # table widet
        labels = ["Price", "Side", "Amount"]
        self.tw_sell = QTableWidget()
        self.tw_sell.setColumnCount(3)
        self.tw_sell.setRowCount(30)
        self.tw_sell.setHorizontalHeaderLabels(labels)

        self.tw_buy = QTableWidget()
        self.tw_buy.setColumnCount(3)
        self.tw_buy.setRowCount(30)
        self.tw_buy.setHorizontalHeaderLabels(labels)

        # button
        self.btn_stop = QPushButton("Stop")
        self.btn_restart = QPushButton("Restart")

        # top grid
        grid = QGridLayout()
        grid.addWidget(self.label0, 0, 0)
        grid.addWidget(self.line_edit0, 0, 1)
        grid.addWidget(self.label3, 0, 2)
        grid.addWidget(self.combo_margin, 0, 3)

        grid.addWidget(self.label1, 1, 0)
        grid.addWidget(self.line_edit1, 1, 1)
        grid.addWidget(self.label4, 1, 2)
        grid.addWidget(self.line_edit3, 1, 3)

        grid.addWidget(self.label2, 2, 0)
        grid.addWidget(self.line_edit2, 2, 1)
        grid.addWidget(self.label5, 2, 2)
        grid.addWidget(self.combo_symbol, 2, 3)

        grid.addWidget(self.label_init_margin, 3, 0)
        grid.addWidget(self.line_edit_init_margine, 3, 1)

        # hbox
        hbox = QHBoxLayout()
        hbox.addWidget(self.tw_sell)
        hbox.addWidget(self.tw_buy)

        # bottom grid
        grid_bottom = QGridLayout()
        grid_bottom.addWidget(self.btn_stop, 0, 0)
        grid_bottom.addWidget(self.btn_restart, 0, 1)

        # vbox
        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(hbox)
        vbox.addLayout(grid_bottom)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()