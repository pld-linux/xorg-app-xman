Summary:	xman aplication
Summary(pl):	Aplikacja xman
Name:		xorg-app-xman
Version:	0.99.3
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/app/xman-%{version}.tar.bz2
# Source0-md5:	0bd1276f1b105148eba05374ca42789d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
# to get /etc/man.config path
BuildRequires:	man-config
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	man-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xman application.

%description -l pl
Aplikacja xman.

%prep
%setup -q -n xman-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

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
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/*
%{_datadir}/xman.help
%{_mandir}/man1/*.1x*
