Summary:        libgpg-error
Name:           libgpg-error
Version:        1.32
Release:        2%{?dist}
License:        GPLv2+
URL:            ftp://ftp.gnupg.org/gcrypt/alpha/libgpg-error/
Group:      Development/Libraries
Source0:    ftp://ftp.gnupg.org/gcrypt/alpha/libgpg-error/%{name}-%{version}.tar.bz2
%define sha512 libgpg-error=0130af48fe81f4db401635757d22a330455aab5dc27edfffad44b7c7c5c439399e92d234c9e00f4d3a399646b52e06c95d53196ea19f5a166817e2032511cb20
Vendor:     VMware, Inc.
Distribution:   Photon

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%package devel
Summary:    Libraries and header files for libgpg-error
Requires:   %{name} = %{version}-%{release}
%description devel
Static libraries and header files for the support library for libgpg-error

%package lang
Summary: Additional language files for libgpg-error
Group:      Applications/System
Requires: %{name} = %{version}-%{release}
%description lang
These are the additional language files of libgpg-error.

%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm -rf %{buildroot}%{_infodir} \
       %{buildroot}%{_libdir}/*.la

%find_lang %{name}

%check
make %{?_smp_mflags} check

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/gpg-error
%{_bindir}/yat2m
%{_libdir}/libgpg-error.so.*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_bindir}/gpg-error-config
%{_bindir}/gpgrt-config
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/libgpg-error
%{_datadir}/aclocal/*
%{_datadir}/common-lisp/source/gpg-error

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
* Sun Oct 02 2022 Shreenidhi Shedi <sshedi@vmware.com> 1.32-2
- Remove .la files
* Mon Sep 10 2018 Bo Gan <ganb@vmware.com> 1.32-1
- Update to 1.32
* Tue Apr 04 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.27-1
- Upgraded to new version 1.27
* Wed Nov 23 2016 Alexey Makhalov <amakhalov@vmware.com> 1.21-3
- Added -lang subpackage
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.21-2
- GA - Bump release of all rpms
* Fri Jan 15 2016 Xiaolin Li <xiaolinl@vmware.com> 1.21-1
- Updated to version 1.21
* Tue Nov 10 2015 Xiaolin Li <xiaolinl@vmware.com> 1.17-2
- Handled locale files with macro find_lang
* Tue Dec 30 2014 Priyesh Padmavilasom <ppadmavilasom@vmware.com>
- initial specfile.
