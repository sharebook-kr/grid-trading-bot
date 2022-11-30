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
        self.init_ui()

    def init_ui(self):
        self.label_lower_price = QLabel("Lower Price")
        self.label_upper_price = QLabel("Upper Price")
        self.label_grid_number = QLabel("Grid Number")
        self.label_margin_mode = QLabel("Margin Mode")
        self.label_leverage = QLabel("Adjust Leverage")
        self.label_symbol = QLabel("Symbol")
        self.label_init_margin = QLabel("Initial Margin")
        self.label_margin_balance = QLabel("Margin Balance")
        self.label_sell = QLabel("Sell")
        self.label_buy = QLabel("Buy")

        self.combo_margin = QComboBox()
        self.combo_margin.addItem("Cross")
        self.combo_margin.addItem("Isolated")

        self.combo_symbol = QComboBox()
        self.combo_symbol.addItem("BTC/USDT")
        self.combo_symbol.addItem("ETH/USDT")
        self.combo_symbol.addItem("XRP/USDT")
        self.combo_symbol.addItem("BNB/USDT")

        self.line_edit_lower_price = QLineEdit()
        self.line_edit_upper_price = QLineEdit()
        self.line_edit_grid_number = QLineEdit()
        self.line_edit_leverage = QLineEdit()
        self.line_edit_init_margin = QLineEdit()
        self.line_edit_margin_balance = QLineEdit()

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
        grid.addWidget(self.label_lower_price, 0, 0)
        grid.addWidget(self.line_edit_lower_price, 0, 1)
        grid.addWidget(self.label_margin_mode, 0, 2)
        grid.addWidget(self.combo_margin, 0, 3)

        grid.addWidget(self.label_upper_price, 1, 0)
        grid.addWidget(self.line_edit_upper_price, 1, 1)
        grid.addWidget(self.label_leverage, 1, 2)
        grid.addWidget(self.line_edit_leverage, 1, 3)

        grid.addWidget(self.label_grid_number, 2, 0)
        grid.addWidget(self.line_edit_grid_number, 2, 1)
        grid.addWidget(self.label_symbol, 2, 2)
        grid.addWidget(self.combo_symbol, 2, 3)

        grid.addWidget(self.label_init_margin, 3, 0)
        grid.addWidget(self.line_edit_init_margin, 3, 1)
        grid.addWidget(self.label_margin_balance, 3, 2)
        grid.addWidget(self.line_edit_margin_balance, 3, 3)

        grid.addWidget(self.label_sell, 4, 0)
        grid.addWidget(self.label_buy, 4, 2)

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