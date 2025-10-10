#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE kontact container
Name:		kontact
Version:	25.08.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kontact/-/archive/%{gitbranch}/kontact-%{gitbranchd}.tar.bz2#/kontact-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kontact-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KPim6TextEdit)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6KontactInterface)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KPim6GrantleeTheme)
BuildRequires:	cmake(KPim6PimCommonAkonadi)
BuildRequires:	sasl-devel
BuildRequires:	boost-devel
Requires:	kdepim-runtime >= 6.0
Suggests:	kdepim-addons >= 6.0
Suggests:	akonadi-import-wizard >= 6.0
Suggests:	akregator >= 6.0
Suggests:	kaddressbook >= 6.0
Suggests:	kmail >= 6.0
Suggests:	knotes >= 6.0
Suggests:	korganizer >= 6.0

%rename plasma6-kontact

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
The KDE Kontact Personal Information Management suite unites mature and
proven KDE applications under one roof. Thanks to the powerful KParts
technology, existing applications are seamlessly integrated into one.

%files -f %{name}.lang
%{_datadir}/applications/org.kde.kontact.desktop
%{_bindir}/kontact
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/messageviewer/about/default/introduction_kontact.html
%{_datadir}/messageviewer/about/default/loading_kontact.html
%{_iconsdir}/hicolor/*/apps/kontact.*
%{_datadir}/qlogging-categories6/kontact.categories
%{_datadir}/qlogging-categories6/kontact.renamecategories
%{_datadir}/metainfo/org.kde.kontact.appdata.xml
%{_datadir}/dbus-1/services/org.kde.kontact.service
%{_libdir}/qt6/plugins/pim6/kcms/kontact/kcm_kontact.so

#----------------------------------------------------------------------------

%define kontactprivate_major 6
%define libkontactprivate %mklibname kontactprivate

%package -n %{libkontactprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libkontactprivate}
KDE PIM shared library.

%files -n %{libkontactprivate}
%{_libdir}/libkontactprivate.so.%{kontactprivate_major}*
