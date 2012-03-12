Summary:	xman aplication - manual display program for the X Window System
Summary(pl.UTF-8):	Aplikacja xman - program do wyświetlania manuali dla systemu X Window
Name:		xorg-app-xman
Version:	1.1.2
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xman-%{version}.tar.bz2
# Source0-md5:	17d89b043083cba9e335379fc61981c0
Patch0:		%{name}-confname.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	man-db
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xman is a graphical manual page browser using the Athena Widgets (Xaw)
toolkit.

%description -l pl.UTF-8
xman to graficzna przeglądarka stron manuala, wykorzystująca toolkit
X Athena Widgets (Xaw).

%prep
%setup -q -n xman-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-localmanpath=/usr/local/man \
	--with-sysmanpath=/usr/share/man \
	--with-manconfig=/etc/man_db.conf

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xman
%{_datadir}/X11/app-defaults/Xman
%{_datadir}/X11/xman.help
%{_mandir}/man1/xman.1x*
