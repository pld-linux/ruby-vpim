Summary:	iCalendar and vCard parser and generator for Ruby
Summary(pl.UTF-8):	Analizator i generator formatu iCalendar i vCard dla języka Ruby
Name:		ruby-vpim
Version:	0.98
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/9497/vpim-0.360.gem
# Source0-md5:	6c7cfbcc76ac08663e32d29a1e1b62cf
URL:		http://vpim.rubyforge.org/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-builder
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a pure-ruby library for decoding and encoding vCard and
iCalendar data ("personal information") called vPim.

vCard (RFC 2426) is a format for personal information, see Vpim::Vcard
and Vpim::Maker::Vcard.

iCalendar (RFC 2445) is a format for calendar related information, see
Vpim::Icalendar.

vCard and iCalendar support is built on top of an implementation of
the MIME Content-Type for Directory Information (RFC 2425). The basic
RFC 2425 format is implemented by Vpim::DirectoryInfo and
Vpim::DirectoryInfo::Field.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/vpim*
%{ruby_ridir}/DateGen
%{ruby_ridir}/Vpim
