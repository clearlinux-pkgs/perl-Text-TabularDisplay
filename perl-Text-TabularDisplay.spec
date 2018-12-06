#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-TabularDisplay
Version  : 1.38
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/D/DA/DARREN/Text-TabularDisplay-1.38.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DARREN/Text-TabularDisplay-1.38.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-tabulardisplay-perl/libtext-tabulardisplay-perl_1.38-1.debian.tar.xz
Summary  : Display text in formatted table output
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Text-TabularDisplay-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Text::TabularDisplay - Display text in formatted table output
SYNOPSIS
use Text::TabularDisplay;

%package dev
Summary: dev components for the perl-Text-TabularDisplay package.
Group: Development
Provides: perl-Text-TabularDisplay-devel = %{version}-%{release}

%description dev
dev components for the perl-Text-TabularDisplay package.


%package license
Summary: license components for the perl-Text-TabularDisplay package.
Group: Default

%description license
license components for the perl-Text-TabularDisplay package.


%prep
%setup -q -n Text-TabularDisplay-1.38
cd ..
%setup -q -T -D -n Text-TabularDisplay-1.38 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Text-TabularDisplay-1.38/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-TabularDisplay
cp COPYING %{buildroot}/usr/share/package-licenses/perl-Text-TabularDisplay/COPYING
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1Text/TabularDisplay.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::TabularDisplay.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-TabularDisplay/COPYING
