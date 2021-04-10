%define		kdeframever	5.81
%define		qtver		5.14.0
%define		kfname		kpty

Summary:	Interfacing with pseudo terminal devices
Name:		kf5-%{kfname}
Version:	5.81.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	12c21d74af63e1fa918039c369a01881
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	cmake >= 3.5
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	libutempter-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qtver}
Requires:	kf5-dirs
Requires:	kf5-kcoreaddons >= %{version}
Requires:	kf5-ki18n >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This library provides primitives to interface with pseudo terminal
devices as well as a KProcess derived class for running child
processes and communicating with them using a pty.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kf5-kcoreaddons-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF5Pty.so.5
%attr(755,root,root) %{_libdir}/libKF5Pty.so.*.*
%{_datadir}/qlogging-categories5/kpty.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KPty
%{_includedir}/KF5/kpty_version.h
%{_libdir}/cmake/KF5Pty
%{_libdir}/libKF5Pty.so
%{qt5dir}/mkspecs/modules/qt_KPty.pri
