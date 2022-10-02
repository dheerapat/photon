Summary: User-space access to Linux Kernel SCTP
Name: lksctp-tools
Version: 1.0.18
Release: 2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://lksctp.sourceforge.net
Source0: %{name}-%{version}.tar.gz
Vendor: VMware, Inc.
Distribution: Photon
%define sha512 lksctp-tools=1d7275fadc0f2270865307cff2645810e9bab6c1a97e70be6115cace737334dbdd87a072fae25b89dd9cac2e05974556542de70ea8ef70b9e4f14873c82a5055

Patch0: 0001-build-fix-netinet-sctp.h-not-to-be-installed.patch
Patch1: 0002-automake-fix-include-dir-for-the-now-autogenerated-header.patch

BuildRequires: gcc
BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf

%description
This is the lksctp-tools package for Linux Kernel SCTP Reference
Implementation.
This package contains the base run-time library & command-line tools.

%package devel
Summary: Development kit for lksctp-tools
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glibc-devel

%description devel
Development kit for lksctp-tools

%package doc
Summary: Documents pertaining to SCTP
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description doc
Documents pertaining to LKSCTP & SCTP in general

%prep
%autosetup -p1

%build
autoreconf -i
%configure --enable-shared --enable-static
%make_build

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog COPYING.lib
%{_bindir}/*
%{_libdir}/libsctp.so.*
%{_libdir}/%{name}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}
%{_libdir}/libsctp.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libsctp.a
%{_datadir}/%{name}/*
%{_mandir}/*

%files doc
%defattr(-,root,root,-)
%doc doc/*.txt

%changelog
* Mon Oct 03 2022 Shreenidhi Shedi <sshedi@vmware.com> 1.0.18-2
- Remove .la files
* Wed Jun 17 2020 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 1.0.18-1
- Initial version.
