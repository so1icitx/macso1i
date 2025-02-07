# Maintainer: sol1icitx <tojitiktok@proton.me>
pkgname=macso1i
pkgver=1.0.0
pkgrel=1
pkgdesc="A simple MAC address changer for Arch Linux"
arch=('any')
url="https://github.com/trxycs/macso1i"
license=('MIT')
depends=('python' 'sudo')
source=("$url/archive/v$pkgver.tar.gz")
sha256sums=('5a0b48e53fc97938ea2999d6dedb0daaf45cac53c064b16646c1e5ed42567f23')  

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}
