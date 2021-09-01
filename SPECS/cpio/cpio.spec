Summary:	cpio-2.13
Name:		cpio
Version:	2.13
Release:	1%{?dist}
License:	GPLv3+
URL:		http://www.gnu.org/software/cpio/
Group:		System Environment/System utilities
Vendor:		VMware, Inc.
Distribution: 	Photon
Source0:	http://ftp.gnu.org/pub/gnu/cpio/%{name}-%{version}.tar.bz2
%define sha1 cpio=4dcefc0e1bc36b11506a354768d82b15e3fe6bb8
Patch0:         newca-new-archive-format.patch
Patch1:         cpio-2.12-gcc-10.patch
Patch2:         cpio-CVE-2021-38185.patch
Patch3:         cpio-CVE-2021-38185_2.patch
Patch4:         cpio-CVE-2021-38185_3.patch
Conflicts:      toybox
%description
The cpio package contains tools for archiving.

%package lang
Summary: Additional language files for cpio
Group:   System Environment/System utilities
Requires: %{name} = %{version}-%{release}
%description lang
These are the additional language files of cpio

%prep
# Using autosetup is not feasible
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%build
sed -i -e '/gets is a/d' gnu/stdio.in.h
%configure \
        --enable-mt   \
        --with-rmt=/usr/libexec/rmt
make %{?_smp_mflags}
makeinfo --html            -o doc/html      doc/cpio.texi
makeinfo --html --no-split -o doc/cpio.html doc/cpio.texi
makeinfo --plaintext       -o doc/cpio.txt  doc/cpio.texi
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/%{_docdir}/%{name}-%{version}/html
install -v -m644    doc/html/* %{buildroot}/%{_docdir}/%{name}-%{version}/html
install -v -m644    doc/cpio.{html,txt} %{buildroot}/%{_docdir}/%{name}-%{version}
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_docdir}/%{name}-%{version}/*

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
* Thu Sep 02 2021 Ashwin Dayanand Kamat <kashwindayan@vmware.com> 2.13-1
- Updated to version 2.13 along with additional fixes for CVE-2021-38185
* Fri Aug 20 2021 Ashwin Dayanand Kamat <kashwindayan@vmware.com> 2.12-6
- Adding security patch for CVE-2021-38185
* Thu Jan 23 2020 Siju Maliakkal <smaliakkal@vmware.com> 2.12-5
- Patch for CVE-2019-14866
* Mon Oct 02 2017 Alexey Makhalov <amakhalov@vmware.com> 2.12-4
- Added conflicts toybox
* Tue May 02 2017 Anish Swaminathan <anishs@vmware.com> 2.12-3
- Add lang package
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.12-2
- GA - Bump release of all rpms
* Thu Jan 14 2016 Xiaolin Li <xiaolinl@vmware.com> 2.12-1
- Updated to version 2.12
* Fri Aug 14 2015 Divya Thaluru <dthaluru@vmware.com> 2.11-2
- Adding security patch for CVE-2014-9112
* Tue Nov 04 2014 Divya Thaluru <dthaluru@vmware.com> 2.11-1
- Initial build. First version
