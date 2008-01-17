Name: xvinfo
Version: 1.0.2
Release: %mkrel 2
Summary: Print out X-Video extension adaptor information
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: libxv-devel	>= 1.0.3

%description
Xvinfo prints out the capabilities of any video adaptors associated with the
display that are accesible through the X-Video extension.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xvinfo
%{_mandir}/man1/xvinfo.*
