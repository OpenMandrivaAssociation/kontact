%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE kontact container
Name:		plasma6-kontact
Version:	24.01.95
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kontact-%{version}.tar.xz
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
Requires:	plasma6-kdepim-runtime
Suggests:	plasma6-kdepim-addons
Suggests:	plasma6-akonadi-import-wizard
Suggests:	plasma6-akregator
Suggests:	plasma6-kaddressbook
Suggests:	plasma6-kmail
Suggests:	plasma6-knotes
Suggests:	plasma6-korganizer

%description
The KDE Kontact Personal Information Management suite unites mature and
proven KDE applications under one roof. Thanks to the powerful KParts
technology, existing applications are seamlessly integrated into one.

%files -f kontact.lang
%{_datadir}/applications/org.kde.kontact.desktop
%{_bindir}/kontact
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/messageviewer/about/default/introduction_kontact.html
%{_datadir}/messageviewer/about/default/loading_kontact.html
%{_docdir}/*/*/kontact
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
%{_libdir}/libkontactprivate.so.5*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kontact-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kontact
