Summary:	audioscrobbler.com plugin for XMMS
Summary(pl):	Wtyczka dla XMMS-a obs³uguj±ca serwis audioscrobbler.com
Name:		xmms-general-audioscrobbler
Version:	0.3.6
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://static.audioscrobbler.com/plugins/xmms-scrobbler-%{version}.tar.bz2
# Source0-md5:	eb5b53815eb91f5294f76ca424369b7f
URL:		http://www.audioscrobbler.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libmusicbrainz-devel >= 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin adds audioscrobbler.com profile support to xmms.

%description -l pl
Ta wtyczka pozwala XMMS-owi na obs³ugê profili audioscrobbler.com.

%prep
%setup -q -n xmms-scrobbler-%{version}

%build
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure \
	--disable-bmp-plugin

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{xmms_general_plugindir}/*
