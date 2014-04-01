%define upstream_name    Pod-Elemental-PerlMunger
%define upstream_version 0.200002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A thing that takes a string of Perl and rewrites its documentation

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Pod::Elemental)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
A thing that takes a string of Perl and rewrites its documentation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.93.330-2mdv2011.0
+ Revision: 654282
- rebuild for updated spec-helper

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.330-1mdv2011.0
+ Revision: 472246
- update to 0.093330

* Sat Nov 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.20-1mdv2010.1
+ Revision: 462456
- import perl-Pod-Elemental-PerlMunger


* Sat Nov 07 2009 cpan2dist 0.093020-1mdv
- initial mdv release, generated with cpan2dist



