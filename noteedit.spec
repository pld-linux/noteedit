Summary:	Note Editor is an editor for music notation
Summary(pl):	Note Editor jest edytorem notacji muzycznej
Name:		noteedit
Version:	2.3.3
Release:	1
License:	GPL
Group:		Multimedia
######		Unknown group!
Source0:	http://tan.informatik.tu-chemnitz.de/cgi-bin/nph-sendbin.cgi/~jan/%{name}/%{name}-%{version}.tgz
# Source0-md5:	e876bc7ec9a711aab8125b0b950ca098
URL:		http://rnvs.informatik.tu-chemnitz.de/~jan/noteedit/noteedit.html
BuildRequires:	tse3-devel
Requires:	tse3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
Note Editor is an editor for music notation that supports an unlimited
number of staffs and up to 9 voices per staff. The import formats are
MIDI files, recorded from MIDI keyboards and TSE3. The export formats
are MIDI, MusiXTeX, LilyPond, PMX, MUP, and TSE3.

%description -l pl
Note Editor jest edytorem notacji muzycznej. Obs�ugiwane formaty to
pliki MIDI, TSE3 (import), MIDI, MusiXTeX, LilyPond, PMX, MUP, i TSE3
(export)

%prep
%setup -q
#%patch0 -p1

%build
kde_icondir="%{_pixmapsdir}"; export kde_icondir
kde_htmldir="%{_htmldir}"; export kde_htmldir
%configure2_13 --with-printing
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities/
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/%{name}.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities/

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/lib%{name}*
%{_applnkdir}/Utilities/%{name}.desktop
%{_datadir}/apps/%{name}