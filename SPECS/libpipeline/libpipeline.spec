Summary:	Library for manipulating pipelines
Name:		libpipeline
Version:	1.5.3
Release:	2%{?dist}
License:	GPLv3+
URL:		http://libpipeline.nongnu.org
Group:		Applications/System
Vendor:		VMware, Inc.
Distribution: 	Photon
Source0:	http://download.savannah.gnu.org/releases/libpipeline/%{name}-%{version}.tar.gz
%define sha512 libpipeline=db0796bffbcdd8e875902385c7cdc140e3e0e045b3d0eba1017e55b4c66027c20cc2cd0fccaf52f59fa941d0925134011317b9c27986765a1ec2a73132ebaec6

%if %{with_check}
BuildRequires: check
BuildRequires: pkg-config
%endif

%description
Contains a library for manipulating pipelines of sub processes
in a flexible and convenient way.

%package devel
Summary:        Library providing headers and static libraries to libpipeline
Group:          Development/Libraries
Requires:       libpipeline = %{version}-%{release}
Provides:       pkgconfig(libpipeline)

%description devel
Development files for libpipeline

%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm -f %{buildroot}%{_libdir}/*.la

%check
make -C tests check %{?_smp_mflags}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*

%changelog
* Mon Oct 03 2022 Shreenidhi Shedi <sshedi@vmware.com> 1.5.3-2
- Remove .la files
* Mon Dec 14 2020 Gerrit Photon <photon-checkins@vmware.com> 1.5.3-1
- Automatic Version Bump
* Mon Aug 19 2019 Shreenidhi Shedi <sshedi@vmware.com> 1.5.0-2
- Fix make check
* Mon Sep 10 2018 Bo Gan <ganb@vmware.com> 1.5.0-1
- Update to 1.5.0
- Split development files to devel package
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.4.1-2
- GA - Bump release of all rpms
* Wed Feb 24 2016 Kumar Kaushik <kaushikk@vmware.com> 1.4.1-1
- Initial build. First version
* Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 1.2.6-1
- Initial build. First version
