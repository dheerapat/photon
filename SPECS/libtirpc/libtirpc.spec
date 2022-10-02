Summary:        Libraries for Transport Independent RPC
Name:           libtirpc
Version:        1.1.4
Release:        3%{?dist}
License:        BSD
Group:          System Environment/Libraries
URL:            http://nfsv4.bullopensource.org/
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        http://downloads.sourceforge.net/project/libtirpc/libtirpc/0.3.2/%{name}-%{version}.tar.bz2
%define sha512  libtirpc=392f391f9fc1bd68d81dc44e4058831a64b32790b5c8c37338b0ab416fad2ae4d16389e632596734dba09780347918cc65c6f134e0c1afd09e81ec250785ed23

Patch0:         CVE-2021-46828.patch

BuildRequires:  krb5-devel
BuildRequires:  automake
BuildRequires:  e2fsprogs-devel

Requires:       krb5

%description
This package contains SunLib's implementation of transport-independent
RPC (TI-RPC) documentation.  This library forms a piece of the base of Open Network
Computing (ONC), and is derived directly from the Solaris 2.3 source.

TI-RPC is an enhanced version of TS-RPC that requires the UNIX System V
Transport Layer Interface (TLI) or an equivalent X/Open Transport Interface
(XTI).  TI-RPC is on-the-wire compatible with the TS-RPC, which is supported
by almost 70 vendors on all major operating systems.  TS-RPC source code
(RPCSRC 4.0) remains available from several internet sites.

%package    devel
Summary:    Development files for the libtirpc library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   krb5-devel

%description    devel
This package includes header files and libraries necessary for developing programs which use the tirpc library.

%prep
%autosetup -p1

%build
%configure
sed '/stdlib.h/a#include <stdint.h>' -i src/xdr_sizeof.c

make %{?_smp_mflags}

%install
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%config(noreplace) %{_sysconfdir}/netconfig
%config(noreplace) %{_sysconfdir}/bindresvport.blacklist
%{_mandir}/man5/*
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/tirpc/*
%{_mandir}/man3/*
%{_libdir}/*.a

%changelog
* Sun Oct 02 2022 Shreenidhi Shedi <sshedi@vmware.com> 1.1.4-3
- Remove .la files
* Wed Aug 3 2022 Shivani Agarwal <shivania2@vmware.com> 1.1.4-2
- Fix CVE-2021-46828
* Wed Sep 12 2018 Keerthana K <keerthanak@vmware.com> 1.1.4-1
- Update to version 1.1.4
* Thu Aug 24 2017 Alexey Makhalov <amakhalov@vmware.com> 1.0.1-7
- Fix compilation issue for glibc-2.26
* Thu May 18 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.0.1-6
- Fix CVE-2017-8779
* Wed Dec 07 2016 Xiaolin Li <xiaolinl@vmware.com> 1.0.1-5
- Moved man3 to devel subpackage.
* Thu Nov 24 2016 Alexey Makhalov <amakhalov@vmware.com> 1.0.1-4
- Required krb5-devel.
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.1-3
- GA - Bump release of all rpms
* Mon Feb 08 2016 Anish Swaminathan <anishs@vmware.com>  1.0.1-2
- Added patch for bindresvport blacklist
* Fri Jan 15 2016 Xiaolin Li <xiaolinl@vmware.com> 1.0.1-1
- Updated to version 1.0.1
* Thu Jul 23 2015 Divya Thaluru <dthaluru@vmware.com> 0.3.2-1
- Initial version
