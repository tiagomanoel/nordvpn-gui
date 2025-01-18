pkgname=nordvpn-gui
pkgver=1.0.0
pkgrel=1
pkgdesc="A GUI for controlling NordVPN from the system tray"
arch=('any')
url="https://github.com/tiagomanoel/nordvpn-gui"
license=('MIT')
depends=('python' 'python-pyqt5' 'nordvpn-bin')
source=("$pkgname-$pkgver.tar.gz::https://github.com/tiagomanoel/nordvpn-gui/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    # Verificar e instalar dependências Python
    pip install -r requirements.txt --target "$srcdir/$pkgname-$pkgver"
    
    # Verificar se nordvpn-bin está instalado, caso contrário, instalar do AUR
    if ! command -v nordvpn &> /dev/null; then
        git clone https://aur.archlinux.org/nordvpn-bin.git
        cd nordvpn-bin
        makepkg -si --noconfirm
        cd ..
    fi
}

package() {
    install -d "$pkgdir/opt/$pkgname"
    cp -r "$srcdir/$pkgname-$pkgver/"* "$pkgdir/opt/$pkgname/"
    
    install -Dm644 "$srcdir/$pkgname-$pkgver/nordvpn-gui.desktop" "$pkgdir/usr/share/applications/nordvpn-gui.desktop"
    install -Dm644 "$srcdir/$pkgname-$pkgver/nordvpn.png" "$pkgdir/opt/$pkgname/nordvpn.png"
    
    install -Dm755 "$srcdir/$pkgname-$pkgver/nordvpn-gui" "$pkgdir/opt/$pkgname/nordvpn-gui"
}
