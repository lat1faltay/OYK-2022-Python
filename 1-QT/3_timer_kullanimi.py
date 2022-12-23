from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication, QPushButton


def tiklama():
    print("Tikladin.")


# Uygulamayi olustur
app = QApplication()

# Formu Olustur.
button = QPushButton("Sakin Tiklama Pisman Olursun")
button.resize(500, 100)
button.show()  # Onemli formu goster.
button.clicked.connect(tiklama)


fonk = lambda x, y: print(x, y)

timer = QTimer()
timer.setInterval(1010)
timer.start()
timer.timeout.connect(fonk("Hello", "World"))

# Event dondugusunu baslat.
app.exec_()
