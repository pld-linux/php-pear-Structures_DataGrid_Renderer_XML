%define		_status		beta
%define		_pearname	Structures_DataGrid_Renderer_XML
%define		subver	dev1
%define		rel		1
Summary:	%{_pearname} - Renderer driver that generates a XML string
Summary(pl.UTF-8):	%{_pearname} - sterownik renderera generujący ciąg znaków XML
Name:		php-pear-%{_pearname}
Version:	0.1.4
Release:	0.%{subver}.%{rel}
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	2a4368ad825ab627abb5cc4cf20647e4
URL:		http://pear.php.net/package/Structures_DataGrid_Renderer_XML/
BuildRequires:	php-pear-PEAR >= 1:1.4.9
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Structures_DataGrid >= 0.7.0
Requires:	php-pear-XML_Util >= 1.1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Renderer driver for Structures_DataGrid that generates a XML
string.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza sterownik renderera dla Structures_DataGrid
generujący ciąg znaków XML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/Renderer/XML.php
