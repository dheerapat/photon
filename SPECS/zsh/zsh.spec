# this file is encoded in UTF-8  -*- coding: utf-8 -*-
Summary:      Z shell
Name:         zsh
Version:      5.8.1
Release:      1%{?dist}
License:      MIT
URL:          http://zsh.org/
Group:        System Environment/Shells
Vendor:       VMware, Inc.
Distribution: Photon
Source0:      http://www.zsh.org/pub/%{name}-%{version}.tar.xz
%define sha1  zsh=82ac4a80c527bfe01c0bdd109f65edc403176fb8
Source1:      zprofile.rhs
Source2:      zshrc

Patch0:       ncurses-fix.patch

BuildRequires: coreutils
BuildRequires: tar
BuildRequires: patch
BuildRequires: diffutils
BuildRequires: make
BuildRequires: gcc
BuildRequires: binutils
BuildRequires: linux-api-headers
BuildRequires: sed
BuildRequires: ncurses-devel
BuildRequires: libcap-devel
BuildRequires: texinfo
BuildRequires: pcre-devel
BuildRequires: gawk
BuildRequires: elfutils
Requires(post): /bin/grep
Requires(postun): (coreutils or toybox) /bin/grep

Provides: /bin/zsh

%description
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

%package html
Summary: Zsh shell manual in html format
Group: System Environment/Shells

%description html
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

This package contains the Zsh manual in html format.

%prep
%autosetup  -p1
autoreconf -fiv

%build
# make loading of module's dependencies work again (#1277996)
export LIBLDFLAGS='-z lazy'

%configure --enable-etcdir=%{_sysconfdir} --with-tcsetpgrp --enable-maildir-support

make %{?_smp_mflags} all html

%install
rm -rf %{buildroot}

%makeinstall install.info \
  fndir=%{buildroot}%{_datadir}/%{name}/%{version}/functions \
  sitefndir=%{buildroot}%{_datadir}/%{name}/site-functions \
  scriptdir=%{buildroot}%{_datadir}/%{name}/%{version}/scripts \
  sitescriptdir=%{buildroot}%{_datadir}/%{name}/scripts \
  runhelpdir=%{buildroot}%{_datadir}/%{name}/%{version}/help

rm -f %{buildroot}%{_bindir}/zsh-%{version}
rm -f %{buildroot}%{_infodir}/dir

mkdir -p %{buildroot}%{_sysconfdir}
for i in %{SOURCE1}; do
    install -m 644 $i %{buildroot}%{_sysconfdir}/"$(basename $i .rhs)"
done

mkdir -p %{buildroot}%{_sysconfdir}/skel
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/skel/.zshrc

# This is just here to shut up rpmlint, and is very annoying.
# Note that we can't chmod everything as then rpmlint will complain about
# those without a she-bang line.
for i in checkmail harden run-help zcalc zkbd; do
    sed -i -e 's!/usr/local/bin/zsh!%{_bindir}/zsh!' \
    %{buildroot}%{_datadir}/zsh/%{version}/functions/$i
    chmod +x %{buildroot}%{_datadir}/zsh/%{version}/functions/$i
done

sed -i "s!%{buildroot}%{_datadir}/%{name}/%{version}/help!%{_datadir}/%{name}/%{version}/help!" \
    %{buildroot}%{_datadir}/zsh/%{version}/functions/{run-help,_run-help}

%clean
rm -rf %{buildroot}

%check
rm -f Test/C02cond.ztst
# avoid unnecessary failure of the test-suite in case ${RPS1} is set
unset RPS1
make %{?_smp_mflags} check

%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/%{name}" > %{_sysconfdir}/shells
    echo "/bin/%{name}" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/%{name}$" %{_sysconfdir}/shells || echo "%{_bindir}/%{name}" >> %{_sysconfdir}/shells
    grep -q "^/bin/%{name}$" %{_sysconfdir}/shells || echo "/bin/%{name}" >> %{_sysconfdir}/shells
  fi
fi

%preun

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/%{name}$!d' %{_sysconfdir}/shells
  sed -i '\!^/bin/%{name}$!d' %{_sysconfdir}/shells
fi

%files
%defattr(-,root,root)
%doc README LICENCE Etc/BUGS Etc/CONTRIBUTORS Etc/FAQ FEATURES MACHINES
%doc NEWS Etc/zsh-development-guide Etc/completion-style-guide
%attr(755,root,root) %{_bindir}/zsh
%{_mandir}/*/*
%{_infodir}/*
%{_datadir}/zsh
%{_libdir}/zsh
%config(noreplace) %{_sysconfdir}/skel/.z*
%config(noreplace) %{_sysconfdir}/z*

%files html
%defattr(-,root,root)
%doc Doc/*.html

%changelog
*   Mon Mar 21 2022 Harinadh D <hdommaraju@vmware.com> 5.8.1-1
-   Fix CVE-2021-45444
*   Wed Oct 07 2020 Ajay Kaher <akaher@vmware.com> 5.8-2
-   Fix ncurses compilation failure
*   Mon May 11 2020 Susant Sahani <ssahani@vmware.com> 5.8-1
-   Upgrading to 5.8
*   Thu Sep 13 2018 Siju Maliakkal <smaliakkal@vmware.com> 5.6.1-1
-   Upgrading to latest
*   Mon Mar 19 2018 Xiaolin Li <xiaolinl@vmware.com> 5.3.1-5
-   Fix CVE-2018-7548
*   Mon Sep 18 2017 Alexey Makhalov <amakhalov@vmware.com> 5.3.1-4
-   Requires coreutils or toybox and /bin/grep
*   Fri Sep 15 2017 Bo Gan <ganb@vmware.com> 5.3.1-3
-   Clean up check
*   Wed Aug 02 2017 Chang Lee <changlee@vmware.com> 5.3.1-2
-   Skip a test case that is not supported from photon OS chroot
*   Wed Apr 05 2017 Xiaolin Li <xiaolinl@vmware.com> 5.3.1-1
-   Updated to version 5.3.1.
*   Sun Jul 24 2016 Ivan Porto Carrero <icarrero@vmware.com> - 5.2-1
-   Initial zsh for photon os
