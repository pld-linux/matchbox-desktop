#
# Conditional build:
%bcond_with	sn	# startup notification support
#
Summary:	Matchbox Desktop environment
Summary(pl.UTF-8):	Środowisko Matchbox Desktop
Name:		matchbox-desktop
Version:	0.9.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://projects.o-hand.com/matchbox/sources/matchbox-desktop/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	8e8ba0ee170a9ac78fdc583b00ccf76b
Patch0:		%{name}-desktop.patch
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	libmatchbox-devel >= 1.5
BuildRequires:	pkgconfig
%{?with_sn:BuildRequires:	startup-notification-devel}
BuildRequires:	zlib-devel
Requires:	libmatchbox >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matchbox Desktop environment.

%description -l pl.UTF-8
Środowisko Matchbox Desktop.

%package devel
Summary:	Header files for Matchbox Desktop modules
Summary(pl.UTF-8):	Pliki nagłówkowe dla modułów Matchbox Desktop
Group:		X11/Development/Libraries
Requires:	libmatchbox-devel >= 1.5
# doesn't require base

%description devel
Header files for Matchbox Desktop modules.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla modułów Matchbox Desktop.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-static \
	--enable-dnotify \
	%{?with_sn:--enable-startup-notification}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/matchbox/{mbdesktop_filebrowser,vfolders}
rm -f $RPM_BUILD_ROOT%{_libdir}/matchbox/desktop/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog modules/simplefilebrowser-example.desktop
%attr(755,root,root) %{_bindir}/matchbox-desktop
%dir %{_libdir}/matchbox
%dir %{_libdir}/matchbox/desktop
%attr(755,root,root) %{_libdir}/matchbox/desktop/dotdesktop.so
%attr(755,root,root) %{_libdir}/matchbox/desktop/simplefilebrowser.so
%attr(755,root,root) %{_libdir}/matchbox/desktop/tasks.so
%dir %{_datadir}/matchbox
%dir %{_datadir}/matchbox/mbdesktop_filebrowser
%dir %{_datadir}/matchbox/vfolders
%dir %{_sysconfdir}/matchbox
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/matchbox/mbdesktop_modules
%{_desktopdir}/mb-show-desktop.desktop
%{_pixmapsdir}/mbdesktop.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/matchbox-desktop
%{_pkgconfigdir}/matchbox-desktop.pc
