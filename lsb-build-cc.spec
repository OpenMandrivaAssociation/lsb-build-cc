Summary: 	LSB Build environment lsbcc package
Name: 		lsb-build-cc
Version: 	3.1.1
Release: 	%mkrel 7
License: 	LGPL
Group: 		Development/C
Source: 	ftp://ftp.freestandards.org/pub/lsb/lsbdev/released-3.1.1/lsb-build-cc-%{version}.tar.bz2
Patch0:         lsb-build-cc-3.1.1-fhs.patch
URL:		http://www.linuxbase.org/build
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Requires: 	lsb-build-base = %{version}
Requires:	gcc gcc-c++
Obsoletes: 	lsbdev-cc
Provides:	lsbdev-cc

%description
This package provides lsbcc and lsbc++, which is one of the approaches 
that can be used to build LSB conforming applications.

%prep
%setup -q
%patch0 -p1 -b .fhs

%build
make LSBVERSION=${RPM_PACKAGE_VERSION} LSBLIBCHK_VERSION=${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE} BASE_PATH=%{_prefix}

%install
%ifarch sparc64 ppc64 x86_64
export LIB64=64
%endif
rm -rf $RPM_BUILD_ROOT
%makeinstall_std INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix} MANDIR=share/man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Licence
%{_bindir}/lsbcc
%{_bindir}/lsbc++
%{_mandir}/man1/lsbcc.1*
%{_mandir}/man1/lsbc++.1*
%{_libdir}/libgcc34compat.a



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1.1-7mdv2011.0
+ Revision: 620265
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.1.1-6mdv2010.0
+ Revision: 429874
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 3.1.1-5mdv2009.0
+ Revision: 251471
- rebuild
- fix spacing at top of description

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 3.1.1-3mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jun 22 2006 Stew Benedict <sbenedict@mandriva.com> 3.1.1-3mdv2007.0
- fix 64bit build

* Tue Jun 13 2006 Stew Benedict <sbenedict@mandriva.com> 3.1.1-2mdv2007.0
- fix requires, source path, P0

* Mon Jun 12 2006 Stew Benedict <sbenedict@mandriva.com> 3.1.1-1mdv2007.0
- 3.1.1, rediff P0

* Wed Jun 08 2005 Stew Benedict <sbenedict@mandriva.com> 3.0.0-1mdk
- 3.0.0 snapshot (not final)

* Thu Aug 26 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.4-1mdk
- 2.0.4

* Mon Jul 26 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.0.3-1mdk
- First Mandrakelinux packaging, move out of /opt (patch0)
- man pages to correct dir
- use doc macro, License, add URL

