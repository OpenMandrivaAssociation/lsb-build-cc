Summary: 	LSB Build environment lsbcc package
Name: 		lsb-build-cc
Version: 	3.1.1
Release: 	%mkrel 3
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

