AC_PREREQ([2.62])

AC_INIT([gtrakt], [0.1.0], [mfs-dm-2011@igalia.com],
	[gtrakt], [https://github.com/ceyusa/mfs2012])

AC_CONFIG_SRCDIR([backend/feed-service.c])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_MACRO_DIR([m4])

AM_INIT_AUTOMAKE([-Wall foreign])

AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_LIBTOOL

AC_HEADER_STDC

AM_GLIB_DEFINE_LOCALEDIR(GNOMELOCALEDIR)
AM_GLIB_GNU_GETTEXT
IT_PROG_INTLTOOL([0.50.0])

GETTEXT_PACKAGE=AC_PACKAGE_NAME
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [Gettext package.])

PKG_CHECK_MODULES([DEPS],  [glib-2.0
			    gio-2.0
			    gobject-2.0
			    libsoup-2.4
			    json-glib-1.0])

AC_CONFIG_FILES([
	Makefile
	backend/Makefile
	po/Makefile.in
	ui/gtk/traktor/config.py
])

AC_OUTPUT
