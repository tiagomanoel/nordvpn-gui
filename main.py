# main.py
import sys
import os
from PyQt5.QtWidgets import QApplication, QMessageBox
from tray_app import TrayApp

def check_nordvpn_installed():
    return os.system("which nordvpn > /dev/null 2>&1") == 0

def show_installation_instructions():
    distro = os.popen("lsb_release -is").read().strip()
    instructions = {
        "Ubuntu": "sudo apt-get install nordvpn",
        "Debian": "sudo apt-get install nordvpn",
        "Fedora": "sudo dnf install nordvpn",
        "Arch": "sudo pacman -S nordvpn",
        "Manjaro": "sudo pacman -S nordvpn"
    }
    instruction = instructions.get(distro, "Please refer to the NordVPN website for installation instructions.")
    
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle("NordVPN Not Installed")
    msg.setText("NordVPN is not installed on your system.")
    msg.setInformativeText(f"To install NordVPN on {distro}, run the following command:\n\n{instruction}")
    msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    if check_nordvpn_installed():
        trayApp = TrayApp()
        sys.exit(app.exec_())
    else:
        show_installation_instructions()
        sys.exit(1)
