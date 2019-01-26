#
# Conditional build:
%bcond_without	sn	# startup notification support
#
Summary:	Matchbox Desktop environment
Summary(pl.UTF-8):	Środowisko Matchbox Desktop
Name:		matchbox-desktop
Version:	2.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.yoctoproject.org/releases/matchbox/matchbox-desktop/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	b0a4a47130272e2adab4e9feb43a6c9c
URL:		https://www.yoctoproject.org/software-item/matchbox/
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	pkgconfig
%{?with_sn:BuildRequires:	startup-notification-devel}
BuildRequires:	zlib-devel
Obsoletes:	matchbox-desktop-devel < 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matchbox Desktop environment.

%description -l pl.UTF-8
Środowisko Matchbox Desktop.

%prep
%setup -q

%build
%configure \
	--enable-dnotify \
	%{?with_sn:--enable-startup-notification}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/matchbox-desktop
