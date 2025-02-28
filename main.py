# Import Libraries
import sys
from PySide6.QtWidgets import QApplication
from easyai_app import easyai_app

# Define application object
app = QApplication(sys.argv)

# Generate window (MainWindow)
window = easyai_app(app)

# Show Window
window.show()

# Start the event loop
sys.exit(app.exec())  