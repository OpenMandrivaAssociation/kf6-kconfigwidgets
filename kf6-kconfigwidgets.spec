%define libname %mklibname KF6ConfigWidgets
%define devname %mklibname KF6ConfigWidgets -d
%define git 20230901

Name: kf6-kconfigwidgets
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kconfigwidgets/-/archive/master/kconfigwidgets-master.tar.bz2#/kconfigwidgets-%{git}.tar.bz2
Summary: Widgets for configuration dialogs
URL: https://invent.kde.org/frameworks/kconfigwidgets
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6Codecs)
# Just to make sure we don't pull the KF5 version
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

%description
Widgets for configuration dialogs

%package -n %{libname}
Summary: Widgets for configuration dialogs
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Widgets for configuration dialogs

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Widgets for configuration dialogs

%prep
%autosetup -p1 -n kconfigwidgets-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

D=$(pwd)
cd %{buildroot}
for i in .%{_datadir}/locale/*/kf6_entry.desktop; do
	echo "%%lang($(echo $i |cut -d/ -f5)) $(echo $i |cut -b2-)" >>$D/%{name}.lang
done
cd -

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kconfigwidgets.*

%files -n %{devname}
%{_includedir}/KF6/KConfigWidgets
%{_libdir}/cmake/KF6ConfigWidgets
%{_qtdir}/mkspecs/modules/qt_KConfigWidgets.pri
%{_qtdir}/doc/KF6ConfigWidgets.*

%files -n %{libname}
%{_libdir}/libKF6ConfigWidgets.so*

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kconfigwidgets6widgets.so
