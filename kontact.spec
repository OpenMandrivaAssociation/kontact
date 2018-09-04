%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE kontact container
Name:		kontact
Version:	18.08.1
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5KontactInterface)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5GrantleeTheme)
BuildRequires:	cmake(KF5KdepimDBusInterfaces)
BuildRequires:	sasl-devel
BuildRequires:	boost-devel
Requires:	kdepim-runtime
Suggests:	kdepim-addons
Suggests:	akonadi-import-wizard
Suggests:	akregator
Suggests:	kaddressbook
Suggests:	kmail
Suggests:	knotes
Suggests:	korganizer

%description
The KDE Kontact Personal Information Management suite unites mature and
proven KDE applications under one roof. Thanks to the powerful KParts
technology, existing applications are seamlessly integrated into one.

%files -f %{name}.lang
%{_kde5_applicationsdir}/org.kde.kontact.desktop
%{_bindir}/kontact
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/kconf_update/kontact*
%{_datadir}/messageviewer/about/default/introduction_kontact.html
%{_datadir}/messageviewer/about/default/loading_kontact.html
%{_docdir}/*/*/kontact
%{_iconsdir}/hicolor/*/apps/kontact.*
%{_kde5_services}/kontactconfig.desktop
%{_sysconfdir}/xdg/kontact.categories
%{_sysconfdir}/xdg/kontact.renamecategories
%{_datadir}/metainfo/org.kde.kontact.appdata.xml
%{_qt5_plugindir}/kcm_kontact.so

#----------------------------------------------------------------------------

%define kontactprivate_major 5
%define libkontactprivate %mklibname kontactprivate %{kontactprivate_major}

%package -n %{libkontactprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libkontactprivate}
KDE PIM shared library.

%files -n %{libkontactprivate}
%{_libdir}/libkontactprivate.so.%{kontactprivate_major}*

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}
