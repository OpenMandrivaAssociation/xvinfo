Name: xvinfo
Version: 1.1.4
Release: 1
Summary: Print out X-Video extension adaptor information
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xv)
BuildRequires: x11-util-macros >= 1.0.1

%description
Xvinfo prints out the capabilities of any video adaptors associated with the
display that are accesible through the X-Video extension.

%prep
%autosetup -p1

%build
%configure \
		--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xvinfo
%{_mandir}/man1/xvinfo.*
