# NordVPN GUI

A graphical interface for controlling NordVPN.

## Requirements

- Python 3
- PyQt5
- NordVPN

## Installation

### Manually

1. Clone the repository:

    ```bash
    git clone https://github.com/tiagomanoel/nordvpn-gui.git
    cd nordvpn-gui
    ```

2. Install the dependencies:

    ```bash
    sudo pacman -S python python-pyqt5
    ```

3. Install `nordvpn-bin` from AUR:

    ```bash
    git clone https://aur.archlinux.org/nordvpn-bin.git
    cd nordvpn-bin
    makepkg -si
    ```

4. Copy the application files to `/opt`:

    ```bash
    sudo mkdir -p /opt/nordvpn-gui
    sudo cp -r * /opt/nordvpn-gui/
    ```

5. Create a launcher in the system:

    ```bash
    sudo cp nordvpn-gui.desktop /usr/share/applications/
    ```

6. Run the application:

    ```bash
    python /opt/nordvpn-gui/main.py
    ```

## Usage

After installation, you can start the application from your system's application menu. The NordVPN GUI icon will appear in the system tray. Right-click the icon to access settings and connection options.

## Contribution

Feel free to open issues and pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
