%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	MXML
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Framework to build Macromedia Flex applications
Summary(pl):	%{_pearname} - Framework do budowania aplikacja Macromedia Flex
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5a0eedc90e97ce4b751d77b2046f69ae
URL:		http://pear.php.net/package/Class_Subclass/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flex enables enterprise-class Rich Internet Applications and is
designed to address a certain class of problems around multistep
processes, client-side validation, data manipulation, and data
visualization. This package allows you to build flex documents
programatically.

MXML is the XML language for writing Macromedia Flex applications that
you can use to lay out user-interface components.

You can also use MXML to declaratively define nonvisual aspects of an
application, such as access to server-side data sources and data
bindings between user-interface components and server-side data
sources.

The API follows closely Stephan Schmidts XUL-Package.

In PEAR status of this package is: %{_status}.

#%description -l pl
#...
#
#Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

cp -ar %{_pearname}-%{version}/%{_subclass} $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
