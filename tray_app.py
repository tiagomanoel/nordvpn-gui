import os
import locale
from PyQt5.QtWidgets import QMainWindow, QAction, QSystemTrayIcon, QMenu, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QScrollArea
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class TrayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.translations = self.load_translations()
        self.initWindow()
        self.initTray()

    def load_translations(self):
        language, _ = locale.getdefaultlocale()
        translations = {
            "en": {
                "firewall": "Firewall",
                "routing": "Routing",
                "analytics": "Analytics",
                "lan_discovery": "LAN Discovery",
                "killswitch": "Kill Switch",
                "threat_protection": "Threat Protection Lite",
                "auto_connect": "Auto-connect",
                "ipv6": "IPv6",
                "meshnet": "Meshnet",
                "dns": "DNS",
                "virtual_location": "Virtual Location",
                "post_quantum_vpn": "Post-quantum VPN",
                "notify": "Notify",
                "quit": "Quit",
                "status_disconnected": "Status: Disconnected",
                "status_connected": "Status: <span style='color: green;'>Connected</span>",
                "country": "Country",
                "connect": "Connect",
                "disconnect": "Disconnect",
                "quick_connect": "Quick Connect"
            },
            "pt_BR": {
                "firewall": "Firewall",
                "routing": "Roteamento",
                "analytics": "Análise",
                "lan_discovery": "Descoberta de LAN",
                "killswitch": "Kill Switch",
                "threat_protection": "Proteção contra ameaças Lite",
                "auto_connect": "Conexão automática",
                "ipv6": "IPv6",
                "meshnet": "Meshnet",
                "dns": "DNS",
                "virtual_location": "Localização virtual",
                "post_quantum_vpn": "VPN pós-quântica",
                "notify": "Notificar",
                "quit": "Sair",
                "status_disconnected": "Status: Desconectado",
                "status_connected": "Status: <span style='color: green;'>Conectado</span>",
                "country": "País",
                "connect": "Conectar",
                "disconnect": "Desconectar",
                "quick_connect": "Conexão Rápida"
            }
        }
        return translations.get(language, translations["en"])

    def initTray(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon.fromTheme("nordvpn"))

        tray_menu = QMenu()

        self.firewall_action = QAction(self.translations["firewall"], self, checkable=True)
        self.firewall_action.triggered.connect(lambda: self.toggle_setting("firewall", self.firewall_action.isChecked()))
        tray_menu.addAction(self.firewall_action)

        self.routing_action = QAction(self.translations["routing"], self, checkable=True)
        self.routing_action.triggered.connect(lambda: self.toggle_setting("routing", self.routing_action.isChecked()))
        tray_menu.addAction(self.routing_action)

        self.analytics_action = QAction(self.translations["analytics"], self, checkable=True)
        self.analytics_action.triggered.connect(lambda: self.toggle_setting("analytics", self.analytics_action.isChecked()))
        tray_menu.addAction(self.analytics_action)

        self.lan_discovery_action = QAction(self.translations["lan_discovery"], self, checkable=True)
        self.lan_discovery_action.triggered.connect(lambda: self.toggle_setting("lan-discovery", self.lan_discovery_action.isChecked()))
        tray_menu.addAction(self.lan_discovery_action)

        self.killswitch_action = QAction(self.translations["killswitch"], self, checkable=True)
        self.killswitch_action.triggered.connect(lambda: self.toggle_setting("killswitch", self.killswitch_action.isChecked()))
        tray_menu.addAction(self.killswitch_action)

        self.threat_protection_action = QAction(self.translations["threat_protection"], self, checkable=True)
        self.threat_protection_action.triggered.connect(lambda: self.toggle_setting("threat-protection-lite", self.threat_protection_action.isChecked()))
        tray_menu.addAction(self.threat_protection_action)

        self.auto_connect_action = QAction(self.translations["auto_connect"], self, checkable=True)
        self.auto_connect_action.triggered.connect(lambda: self.toggle_setting("auto-connect", self.auto_connect_action.isChecked()))
        tray_menu.addAction(self.auto_connect_action)

        self.ipv6_action = QAction(self.translations["ipv6"], self, checkable=True)
        self.ipv6_action.triggered.connect(lambda: self.toggle_setting("ipv6", self.ipv6_action.isChecked()))
        tray_menu.addAction(self.ipv6_action)

        self.meshnet_action = QAction(self.translations["meshnet"], self, checkable=True)
        self.meshnet_action.triggered.connect(lambda: self.toggle_setting("meshnet", self.meshnet_action.isChecked()))
        tray_menu.addAction(self.meshnet_action)

        self.dns_action = QAction(self.translations["dns"], self, checkable=True)
        self.dns_action.triggered.connect(lambda: self.toggle_setting("dns", self.dns_action.isChecked()))
        tray_menu.addAction(self.dns_action)

        self.virtual_location_action = QAction(self.translations["virtual_location"], self, checkable=True)
        self.virtual_location_action.triggered.connect(lambda: self.toggle_setting("virtual-location", self.virtual_location_action.isChecked()))
        tray_menu.addAction(self.virtual_location_action)

        self.post_quantum_vpn_action = QAction(self.translations["post_quantum_vpn"], self, checkable=True)
        self.post_quantum_vpn_action.triggered.connect(lambda: self.toggle_setting("post-quantum-vpn", self.post_quantum_vpn_action.isChecked()))
        tray_menu.addAction(self.post_quantum_vpn_action)

        self.notify_action = QAction(self.translations["notify"], self, checkable=True)
        self.notify_action.triggered.connect(lambda: self.toggle_setting("notify", self.notify_action.isChecked()))
        tray_menu.addAction(self.notify_action)

        quit_action = QAction(self.translations["quit"], self)
        quit_action.setIcon(QIcon.fromTheme("application-exit"))
        quit_action.triggered.connect(self.quit_application)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        self.tray_icon.show()

        self.update_vpn_status()
        self.load_tray_settings()

    def initWindow(self):
        self.window = QWidget()
        self.window.setWindowTitle("NordVPN Control")
        self.window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
        self.window.setWindowIcon(QIcon.fromTheme("nordvpn"))
        self.window.resize(300, 200)
        self.window.closeEvent = self.on_window_close

        layout = QVBoxLayout()

        self.status_label = QLabel(self.translations["status_disconnected"], self.window)
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        self.quick_connect_button = QPushButton(self.translations["quick_connect"], self.window)
        self.quick_connect_button.setIcon(QIcon.fromTheme("network-vpn"))
        self.quick_connect_button.clicked.connect(self.quick_connect)
        layout.addWidget(self.quick_connect_button)
        self.quick_connect_button.hide()

        self.country_label = QLabel("", self.window)
        self.country_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.country_label)

        self.country_selector = QComboBox(self.window)
        self.setup_country_selector()
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        
        content = QWidget()
        layout_content = QVBoxLayout(content)
        layout_content.addWidget(self.country_selector)
        
        scroll.setWidget(content)
        layout.addWidget(scroll)
        
        self.country_selector.setMaxVisibleItems(3)  # Limitar para 3 opções visíveis
        self.country_selector.setStyleSheet("QComboBox { min-width: 150px; }")  # Definir largura mínima

        self.connect_disconnect_button = QPushButton(self.translations["connect"], self.window)
        self.connect_disconnect_button.setIcon(QIcon.fromTheme("network-vpn-disconnected"))
        self.connect_disconnect_button.clicked.connect(self.toggle_vpn)
        layout.addWidget(self.connect_disconnect_button)

        self.window.setLayout(layout)

    def setup_country_selector(self):
        countries = self.get_countries()
        for country in countries:
            self.country_selector.addItem(country)

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.window.show()

    def on_window_close(self, event):
        event.ignore()
        self.window.hide()

    def load_tray_settings(self):
        settings = {
            "firewall": self.firewall_action,
            "routing": self.routing_action,
            "analytics": self.analytics_action,
            "lan-discovery": self.lan_discovery_action,
            "killswitch": self.killswitch_action,
            "threat-protection-lite": self.threat_protection_action,
            "auto-connect": self.auto_connect_action,
            "ipv6": self.ipv6_action,
            "meshnet": self.meshnet_action,
            "dns": self.dns_action,
            "virtual-location": self.virtual_location_action,
            "post-quantum-vpn": self.post_quantum_vpn_action,
            "notify": self.notify_action
        }

        output = os.popen("nordvpn settings").read().strip().split('\n')
        for line in output:
            for setting, action in settings.items():
                if setting.replace("-", " ") in line.lower():
                    status = line.split()[-1]
                    action.setChecked(status.lower() == "enabled")

    def toggle_setting(self, setting, enabled):
        command = f"nordvpn set {setting} {'on' if enabled else 'off'}"
        os.system(command)
        print(f"{setting.capitalize()} {'enabled' if enabled else 'disabled'}")

    def toggle_vpn(self):
        country = self.country_selector.currentText().split(" ")[0]
        if self.connect_disconnect_button.text() == self.translations["connect"]:
            os.system(f"nordvpn connect {country}")
            print(f"VPN connected to {country}")
        else:
            os.system("nordvpn disconnect")
            print("VPN disconnected")
        self.update_vpn_status()

    def quick_connect(self):
        os.system("nordvpn connect")
        print("Quick Connect initiated")
        self.update_vpn_status()

    def on_country_changed(self):
        if self.status_label.text().find(self.translations["status_connected"]) != -1:
            country = self.country_selector.currentText().split(" ")[0]
            os.system(f"nordvpn connect {country}")
            print(f"VPN connected to {country}")
            self.update_vpn_status()

    def update_vpn_status(self):
        status_output = os.popen("nordvpn status").read().strip().split('\n')
        status = "Disconnected"
        country = ""
        for line in status_output:
            if "Status" in line:
                status = line.split()[-1]
            if "Country" in line:
                country = line.split()[-1]

        if status.lower() == "connected":
            self.connect_disconnect_button.setText(self.translations["disconnect"])
            self.connect_disconnect_button.setIcon(QIcon.fromTheme("network-vpn-connected"))
            self.status_label.setText(self.translations["status_connected"])
            self.country_label.setText(f"{self.translations['country']}: {country}")
            self.quick_connect_button.hide()
        else:
            self.connect_disconnect_button.setText(self.translations["connect"])
            self.connect_disconnect_button.setIcon(QIcon.fromTheme("network-vpn-disconnected"))
            self.status_label.setText(self.translations["status_disconnected"])
            self.country_label.setText("")
            self.quick_connect_button.show()

    def quit_application(self):
        os.system("nordvpn disconnect")
        QApplication.instance().quit()

    def get_countries(self):
        countries = [
            "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",
            "Bahamas", "Bahrain", "Bangladesh", "Belgium", "Belize", "Bermuda", "Bhutan", "Bolivia", "Bosnia_And_Herzegovina",
            "Brazil", "Brunei_Darussalam", "Bulgaria", "Cambodia", "Canada", "Cayman_Islands", "Chile", "Colombia",
            "Costa_Rica", "Croatia", "Cyprus", "Czech_Republic", "Denmark", "Dominican_Republic", "Ecuador", "Egypt",
            "El_Salvador", "Estonia", "Finland", "France", "Georgia", "Germany", "Ghana", "Greece", "Greenland", "Guam",
            "Guatemala", "Honduras", "Hong_Kong", "Hungary", "Iceland", "India", "Indonesia", "Ireland", "Isle_Of_Man",
            "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kuwait",
            "Lao_Peoples_Democratic_Republic", "Latvia", "Lebanon", "Liechtenstein", "Lithuania", "Luxembourg", "Malaysia",
            "Malta", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Nepal",
            "Netherlands", "New_Zealand", "Nigeria", "North_Macedonia", "Norway", "Pakistan", "Panama", "Papua_New_Guinea",
            "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto_Rico", "Romania", "Senegal", "Serbia",
            "Singapore", "Slovakia", "Slovenia", "South_Africa", "South_Korea", "Spain", "Sri_Lanka", "Sweden", "Switzerland",
            "Taiwan", "Thailand", "Trinidad_And_Tobago", "Tunisia", "Turkey", "Ukraine", "United_Arab_Emirates",
            "United_Kingdom", "United_States", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam"
        ]
        return countries
