Summary:	Apache Tomcat Connector
Name:		httpd-mod_jk
Version:	1.2.42
Release:	3%{?dist}
License:	Apache
URL:		http://tomcat.apache.org/connectors-doc
Group:		Applications/System
Vendor:		VMware, Inc.
Distribution: 	Photon

Source0:	http://www.apache.org/dist/tomcat/tomcat-connectors/jk/tomcat-connectors-%{version}-src.tar.gz
%define sha1 tomcat-connectors=a1a6b284b0bd5577f76b497687af01771faff902

Requires:	httpd

BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
BuildRequires:	httpd-devel
BuildRequires:	httpd-tools

%description
The Apache Tomcat Connectors project is part of the Tomcat project and provides web server plugins to connect web servers with Tomcat and other backends.
mod_jk is a module connecting Tomcat and Apache

%prep
%autosetup -n tomcat-connectors-%{version}-src -p1

%build
cd native
sh ./configure --with-apxs=%{_bindir}/apxs

make %{?_smp_mflags}

%install
install -vdm 755 %{buildroot}
install -D -m 755 native/apache-2.0/mod_jk.so %{buildroot}%{_libdir}/httpd/modules/mod_jk.so
install -D -m 644 conf/workers.properties  %{buildroot}%{_sysconfdir}/httpd/conf/workers.properties
install -D -m 644 conf/httpd-jk.conf  %{buildroot}%{_sysconfdir}/httpd/conf/httpd_jk.conf

%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%files
%defattr(-,root,root)
%{_libdir}/httpd/modules/mod_jk.so
%config(noreplace) %{_sysconfdir}/httpd/conf/httpd_jk.conf
%config(noreplace) %{_sysconfdir}/httpd/conf/workers.properties

%changelog
* Tue Oct 19 2021 Shreenidhi Shedi <sshedi@vmware.com> 1.2.42-3
- Bump version as a part of httpd upgrade
* Tue Apr 25 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.42-2
- Ensure non empty debuginfo
* Tue Feb 21 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.2.42-1
- Initial build. First version
