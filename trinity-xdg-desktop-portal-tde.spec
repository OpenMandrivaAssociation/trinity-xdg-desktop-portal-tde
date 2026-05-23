%bcond clang 1

# TDE variables
%define tde_pkg xdg-desktop-portal-tde
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity
%global toolchain %(readlink /usr/bin/cc)


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	This is an implementation of the FreeDesktop Portals API for TDE
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/system/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig 
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-1-tqt)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)

%description
This implementation exposes TDE APIs to applications which use the 
Portals API. As a result, these applications can transparently 
use native APIs and dialogs.

%files
%doc README.md
%{tde_prefix}/%{_lib}/trinity/libexec/%{tde_pkg}
%{tde_prefix}/share/applications/tde/%{tde_pkg}.desktop
%{_datadir}/xdg-desktop-portal/
%{_datadir}/dbus-1/services/
