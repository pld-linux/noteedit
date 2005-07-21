Summary:	Note Editor is an editor for music notation
Summary(pl):	Note Editor jest edytorem notacji muzycznej
Name:		noteedit
Version:	2.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.berlios.de/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	c707a0c67254784b912dabc6545e8125
URL:		http://noteedit.berlios.de/
BuildRequires:	kdelibs-devel
BuildRequires:	tse3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
Note Editor is an editor for music notation that supports an unlimited
number of staffs and up to 9 voices per staff. The import formats are
MIDI files, recorded from MIDI keyboards and TSE3. The export formats
are MIDI, MusiXTeX, LilyPond, PMX, MUP, and TSE3.

%description -l pl
Note Editor jest edytorem notacji muzycznej. Obs³ugiwane formaty to
pliki MIDI, TSE3 (import), MIDI, MusiXTeX, LilyPond, PMX, MUP, i TSE3
(export)

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure \
	--with-printing
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

# no -devel - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/libnoteedit.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README
%lang(de) %doc FAQ.de
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_applnkdir}/Utilities/%{name}.desktop
%{_datadir}/apps/%{name}
