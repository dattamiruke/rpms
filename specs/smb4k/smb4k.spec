# $Id$

# Authority: dries

Summary: SMB (samba) share browser for KDE
Name: smb4k
Version: 0.3.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://smb4k.berlios.de/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://download.berlios.de/smb4k/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make
BuildRequires: gcc-c++, XFree86-devel, qt-devel, fam-devel, fam
%{?fc2:BuildRequires:libselinux-devel}
Requires: kdelibs, fam

# Screenshot: http://smb4k.berlios.de/shots/0.3.0/Smb4K-0.3.0-1.png

%description
Smb4K is an SMB share browser for KDE. It uses the Samba software suite for
an easy access to the SMB shares of your local network neighborhood. 

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
export DESTDIR=$RPM_BUILD_ROOT
make install-strip
%find_lang %{name}
rm -f ${DESTDIR}/usr/share/applnk/Applications/smb4k.desktop
mkdir -p ${DESTDIR}/usr/share/applications
cat > ${DESTDIR}/usr/share/applications/smb4k.desktop <<EOF
[Desktop Entry]
Name=Smb4K
Icon=smb4k.png
Comment=SMB Share Browser
Exec=smb4k
Terminal=0
Type=Application
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Base;
EOF

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%{_bindir}/smb4k
%{_datadir}/applications/smb4k.desktop
%{_datadir}/apps/smb4k
%{_datadir}/doc/HTML/en/smb4k
%{_datadir}/icons/crystalsvg/*/apps/smb4k.png

%changelog
* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.3.1-1
- first packaging for Fedora Core 1
