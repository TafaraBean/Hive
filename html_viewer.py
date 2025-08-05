import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTreeView, QFileSystemModel, QSplitter, QWidget, QVBoxLayout
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QDir, QUrl, Qt

class HtmlViewer(QMainWindow):
    def __init__(self, root_folder):
        super().__init__()
        self.setWindowTitle("HTML Viewer with Navigation")
        self.setGeometry(100, 100, 1000, 600)

        # Main container widget
        main_widget = QWidget()
        layout = QVBoxLayout()
        splitter = QSplitter(Qt.Horizontal)

        # File browser
        self.model = QFileSystemModel()
        self.model.setRootPath(root_folder)
        self.model.setNameFilters(["*.html", "*.htm"])
        self.model.setNameFilterDisables(False)

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(root_folder))
        self.tree.clicked.connect(self.on_file_clicked)
        self.tree.setColumnWidth(0, 300)

        # HTML Viewer
        self.browser = QWebEngineView()
        self.browser.setHtml("<h2>Select an HTML file from the left</h2>")

        # Add widgets to splitter
        splitter.addWidget(self.tree)
        splitter.addWidget(self.browser)
        splitter.setStretchFactor(1, 1)

        layout.addWidget(splitter)
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def on_file_clicked(self, index):
        path = self.model.filePath(index)
        if path.lower().endswith((".html", ".htm")):
            self.browser.load(QUrl.fromLocalFile(path))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set the root folder to navigate
    base_folder = os.path.abspath("uploads")
    viewer = HtmlViewer(base_folder)
    viewer.show()
    sys.exit(app.exec_())
