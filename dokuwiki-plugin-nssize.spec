%define		plugin		nssize
Summary:	DokuWiki plugin to Show disk usage of a namespace
Name:		dokuwiki-plugin-%{plugin}
Version:	20080322
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://wiki.symplus.com/_media/computer/source/nssize.zip
# Source0-md5:	288b06bc6765f9b51e5a3aa11b99b3b7
URL:		http://www.dokuwiki.org/plugin:nssize
Patch0:		doku-conf.patch
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	dokuwiki >= 20061106
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
mv %{plugin}/* .
%undos *.css *.php
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/conf
