# ME:sol1icitx <tojitiktok@proton.me>
pkgname=macso1i
pkgver=1.0.0
pkgrel=1
pkgdesc="A simple MAC address changer for Arch Linux"
arch=('any')
url="https://github.com/trxycs/macso1i.git"
license=('MIT')
depends=('python' 'sudo')
source=("$url/archive/v$pkgver.tar.gz")
sha256sums=('REPLACE_WITH_YOUR_SOURCE_TARBALL_SHA256')

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}
