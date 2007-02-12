Summary:	Note Editor - an editor for music notation
Summary(pl.UTF-8):   Note Editor - edytor notacji muzycznej
Name:		noteedit
Version:	2.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.berlios.de/noteedit/%{name}-%{version}.tar.gz
# Source0-md5:	c707a0c67254784b912dabc6545e8125
Patch0:		%{name}-desktop.patch
URL:		http://noteedit.berlios.de/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	tse3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Note Editor is an editor for music notation that supports an unlimited
number of staffs and up to 9 voices per staff. The import formats are
MIDI files, recorded from MIDI keyboards and TSE3. The export formats
are MIDI, MusiXTeX, LilyPond, PMX, MUP, and TSE3.

%description -l pl.UTF-8
Note Editor jest edytorem notacji muzycznej. Obsługiwane formaty to
pliki MIDI, TSE3 (import), MIDI, MusiXTeX, LilyPond, PMX, MUP, i TSE3
(eksport).

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir} \
	--with-libtse3-include=%{_includedir} \
	--with-libtse3-libs=%{_libdir} \
	--with-printing
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D noteedit/noteedit.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

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
%{_desktopdir}/%{name}.desktop
%{_datadir}/apps/%{name}
