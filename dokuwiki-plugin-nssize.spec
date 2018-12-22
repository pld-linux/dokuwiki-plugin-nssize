%define		subver	2013-02-03
%define		ver		%(echo %{subver} | tr -d -)
%define		plugin		nssize
%define		php_min_version 5.3.0
%include	/usr/lib/rpm/macros.php
Summary:	DokuWiki plugin to Show disk usage of a namespace
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/iobataya/dokuwiki-plugin-nssize/archive/6bccd121/%{plugin}-%{subver}.tar.gz
# Source0-md5:	8b3d5f57c2e2045e92a593464bd08022
URL:		https://www.dokuwiki.org/plugin:nssize
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unzip
Requires:	dokuwiki >= 20061106
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
NSsize DokuWiki plugin calculates and displays the disk usage of a
particular namespace.

This plugin can display the disk space of the 'pages', 'media',
'meta', 'cache', 'attic' directories. These displaying items are
selectable in the plugin-configuration page.

%prep
%setup -qc
mv *-%{plugin}-*/* .

%build
version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/README

# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/conf
