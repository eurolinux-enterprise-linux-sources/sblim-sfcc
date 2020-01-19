#
# $Id: sblim-sfcc.spec,v 1.4 2010/03/03 07:57:28 vcrhonek Exp $
#
# Package spec for sblim-sfcc
#

Summary: Small Footprint CIM Client Library
Name: sblim-sfcc
Version: 2.2.5
Release: 6%{?dist}
Group: Applications/System
License: EPL
URL: http://www.sblim.org
Source0: http://downloads.sourceforge.net/project/sblim/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: curl-devel chrpath

%Description
Small Footprint CIM Client Library Runtime Libraries

%package devel
Summary: Small Footprint CIM Client Library
Group: Applications/System
Requires: %{name} >= %{version}

%Description devel
Small Footprint CIM Client Library Header Files and Link Libraries


%prep

%setup -q

%build
chmod a-x backend/cimxml/*.[ch]

%configure
make %{?_smp_flags}

%install
make DESTDIR=%{buildroot} install
# remove unused libtool files
rm -rf %{buildroot}/%{_libdir}/*a
# remove rpath
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libcmpisfcc.so.1.0.0

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_libdir}/*.so.*
%{_libdir}/libcimcClientXML.so
%{_mandir}/man3/*.3.gz
%{_docdir}/*

%files devel
%{_includedir}/CimClientLib/*
%{_includedir}/cimc/*
%{_libdir}/libcimcclient.so
%{_libdir}/libcmpisfcc.so

%changelog
* Wed Jan 29 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.5-6
- Move libcimcClientXML.so from -devel to main package - it's needed for proper function
  Resolves: #1056407

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2.2.5-5
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2.5-4
- Mass rebuild 2013-12-27

* Mon Jul 22 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.5-3
- Remove rpath from libcmpisfcc library again

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.5-1
- Update to sblim-sfcc-2.2.5

* Mon Nov 19 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.4-4
- Remove rpath from libcmpisfcc library

* Thu Sep 06 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.4-3
- Fix issues found by fedora-review utility in the spec file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.4-1
- Update to sblim-sfcc-2.2.4
- Fix source link, remove build root tag

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.3-1
- Update to sblim-sfcc-2.2.3

* Tue May 24 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.2-1
- Update to sblim-sfcc-2.2.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar  3 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.1-1
- Update to sblim-sfcc-2.2.1
- Fix Source field
- Move documentation files from -devel to main package

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Tue Aug 19 2008  <srinivas_ramanatha@dell.com> - 2.1.0-0%{?dist}
- Modified the spec file to adhere to fedora packaging guidelines.

* Fri Feb 16 2007  <mihajlov@dyn-9-152-143-45.boeblingen.de.ibm.com> - 2.0.0-0
- Initial Version

