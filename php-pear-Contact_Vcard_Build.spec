%define		_class		Contact
%define		_subclass	Vcard_Build
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.2
Release:	9
Summary:	Build (create) and fetch vCard 2.1 and 3.0 text blocks
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Contact_Vcard_Build/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch

%description
Allows you to programmatically create a vCard, version 2.1 or 3.0, and
fetch the vCard text.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{upstream_name}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-7mdv2012.0
+ Revision: 741830
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-6
+ Revision: 679269
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-5mdv2011.0
+ Revision: 613618
- the mass rebuild of 2010.1 packages

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.2-4mdv2010.1
+ Revision: 478358
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.2-3mdv2010.0
+ Revision: 446531
- spec cleanup
- ship missing file

* Fri Jul 24 2009 Raphaël Gertz <rapsys@mandriva.org> 1.1.2-2mdv2010.0
+ Revision: 399540
- Rebuild

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.2-1mdv2010.0
+ Revision: 394092
- update to new version 1.1.2

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-7mdv2009.1
+ Revision: 321932
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-6mdv2009.0
+ Revision: 236811
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-5mdv2007.0
+ Revision: 81416
- Import php-pear-Contact_Vcard_Build

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdk
- 1.1.1

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdk
- initial Mandriva package (PLD import)

