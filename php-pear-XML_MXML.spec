%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	MXML
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Framework to build Macromedia Flex applications
Summary(pl):	%{_pearname} - Szkielet do budowania aplikacji Macromedia Flex
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	3
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5a0eedc90e97ce4b751d77b2046f69ae
URL:		http://pear.php.net/package/XML_MXML/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:5.0.0
Requires:	php-pear
Requires:	php-pear-XML_Util >= 0.5.2
Requires:	php-pear-XML_Parser >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flex enables enterprise-class Rich Internet Applications and is
designed to address a certain class of problems around multistep
processes, client-side validation, data manipulation, and data
visualization. This package allows you to build Flex documents
programatically.

MXML is the XML language for writing Macromedia Flex applications that
you can use to lay out user-interface components.

You can also use MXML to declaratively define nonvisual aspects of an
application, such as access to server-side data sources and data
bindings between user-interface components and server-side data
sources.

The API follows closely Stephan Schmidts XUL-Package.

In PEAR status of this package is: %{_status}.

%description -l pl
Flex daje mo�liwo�� tworzenia bogatych aplikacji internetowych klasy
korporacyjnej i jest zaprojektowany do rozwi�zywania pewnej klasy
problem�w zwi�zanych z procesami wielokrokowymi, kontrol� poprawno�ci
po stronie klienta, obr�bk� danych i wizualizacj� ich. Ten pakiet
umo�liwia programowe budowanie dokument�w Fleksa.

MXML to j�zyk XML do pisania aplikacji Macromedia Flex, kt�rych mo�na
u�ywa� do uk�adania komponent�w interfejsu u�ytkownika.

Mo�na tak�e u�ywa� MXML to deklaratywnego definiowania niewizualnych
aspekt�w aplikacji, takich jak dost�p do �r�de� danych po stronie
serwera i wi�za� danych mi�dzy komponentami interfejsu u�ytkownika a
�r�d�ami danych po stronie serwera.

To API jest zgodne z XUL-Package Stephana Schmidta.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

install -d docs/%{_pearname}
mv ./%{php_pear_dir}/tests/%{_pearname}/examples docs/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
