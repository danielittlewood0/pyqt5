import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

PDFJS = 'http://localhost:8888/web/viewer.html'
PDF = 'http://localhost:8888/test/pdfs/edexcel.pdf'

class Window(QtWebEngineWidgets.QWebEngineView):
    def __init__(self):
        super(Window, self).__init__()
        self.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (PDFJS, PDF)))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 50, 800, 600)
    window.show()
    sys.exit(app.exec_())
