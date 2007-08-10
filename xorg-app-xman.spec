Summary:	xman aplication - manual display program for the X Window System
Summary(pl.UTF-8):	Aplikacja xman - program do wyświetlania manuali dla systemu X Window
Name:		xorg-app-xman
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xman-%{version}.tar.bz2
# Source0-md5:	3d3a4b310a65ccce82472ef83acbbf97
Patch0:		%{name}-confname.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
# to get /etc/man.config path
BuildRequires:	man-config
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	man-config
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xman is a manual page browser.

%description -l pl.UTF-8
xman to przeglądarka stron manuala.

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
	--with-sysmanpath=/usr/share/man

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/xman
%{_datadir}/X11/app-defaults/Xman
%{_datadir}/X11/xman.help
%{_mandir}/man1/xman.1x*
