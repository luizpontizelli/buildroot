################################################################################
#
# xlib_libXi
#
################################################################################

XLIB_LIBXI_VERSION = 1.7.10
XLIB_LIBXI_SOURCE = libXi-$(XLIB_LIBXI_VERSION).tar.bz2
XLIB_LIBXI_SITE = https://xorg.freedesktop.org/releases/individual/lib
XLIB_LIBXI_LICENSE = MIT
XLIB_LIBXI_LICENSE_FILES = COPYING
XLIB_LIBXI_CPE_ID_VENDOR = x.org
XLIB_LIBXI_CPE_ID_PRODUCT = libxi
XLIB_LIBXI_INSTALL_STAGING = YES
XLIB_LIBXI_DEPENDENCIES = \
	host-pkgconf \
	xlib_libX11 \
	xlib_libXext \
	xlib_libXfixes \
	xorgproto

XLIB_LIBXI_CONF_OPTS = --disable-malloc0returnsnull

$(eval $(autotools-package))
