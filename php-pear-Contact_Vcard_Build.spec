%define		_class		Contact_Vcard_Build
%define		_status		stable
%define		_pearname	%{_class}

Summary:	Build (create) and fetch vCard 2.1 and 3.0 text blocks
Name:		php-pear-%{_pearname}
Version:	1.1.2
Release:	%mkrel 3
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/Contact_Vcard_Build/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Allows you to programmatically create a vCard, version 2.1 or 3.0, and
fetch the vCard text.

In PEAR status of this package is: %{_status}.

%prep
%setup -q -c

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/pear
install -m 644 %{_pearname}-%{version}/Contact_Vcard_Build.php \
    %{buildroot}%{_datadir}/pear

install -d -m 755 %{buildroot}%{_datadir}/pear/Contact/Vcard
install -m 644 %{_pearname}-%{version}/Contact/Vcard/Build.php \
    %{buildroot}%{_datadir}/pear/Contact/Vcard

install -d -m 755 %{buildroot}%{_datadir}/pear/packages
install -m 644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pear/*.php
%{_datadir}/pear/Contact
%{_datadir}/pear/packages/%{_pearname}.xml


