Name:		xvinfo
Version:	1.1.5
Release:	2
Summary:	Print out X-Video extension adaptor information
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xorg-macros)

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
%doc %{_mandir}/man1/xvinfo.*
