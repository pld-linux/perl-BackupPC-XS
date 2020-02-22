#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	BackupPC
%define		pnam	XS
Summary:	BackupPC::XS - Perl extension for BackupPC libraries
Name:		perl-BackupPC-XS
Version:	0.59
Release:	1
License:	GPLv3+ and (GPL+ or Artistic) and zlib
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CB/CBARRATT/BackupPC-XS-%{version}.tar.gz
# Source0-md5:	1f64d8ced0095435849a7e771f025d84
URL:		https://metacpan.org/release/BackupPC-XS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BackupPC::XS provides various submodules that implement various
BackupPC library functions. The following sections describe each
submodule.

This documentation is very terse. BackupPC::XS is not intended to be a
general-purpose module - it is closely tied to BackupPC. Look in the
BackupPC code to see examples of using this module.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/BackupPC
%dir %{perl_vendorarch}/auto/BackupPC
%dir %{perl_vendorarch}/auto/BackupPC/XS
%{perl_vendorarch}/BackupPC/*.pm
%attr(755,root,root) %{perl_vendorarch}/auto/BackupPC/XS/*.so
%{_mandir}/man3/*
