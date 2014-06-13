Name: xvinfo
Version: 1.1.2
Release: 6
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
%setup -q -n %{name}-%{version}

%build
autoreconf -fi
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xvinfo
%{_mandir}/man1/xvinfo.*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdv2011.0
+ Revision: 671375
- mass rebuild

* Sun Nov 07 2010 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 594631
- new release

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2010.1
+ Revision: 463591
- new release

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-3mdv2009.1
+ Revision: 350744
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2009.0
+ Revision: 166810
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 154296
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 64836
- fix man pages
- new release


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:24:58 (31400)
- fill in a couple of missing descriptions

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:16:37 (31397)
- fix summary

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

