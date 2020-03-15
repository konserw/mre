from PySide2.QtWidgets import QApplication

app = QApplication()
print(f"My pid: {app.applicationPid()}")
app.quit()
