Summary:	audioscrobbler.com plugin for XMMS
Summary(pl.UTF-8):	Wtyczka dla XMMS-a obsługująca serwis audioscrobbler.com
Name:		xmms-general-audioscrobbler
Version:	0.3.6
Release:	5
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://static.audioscrobbler.com/plugins/xmms-scrobbler-%{version}.tar.bz2
# Source0-md5:	eb5b53815eb91f5294f76ca424369b7f
URL:		http://www.audioscrobbler.com/
BuildRequires:	bc
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

%description -l pl.UTF-8
Ta wtyczka pozwala XMMS-owi na obsługę profili audioscrobbler.com.

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
