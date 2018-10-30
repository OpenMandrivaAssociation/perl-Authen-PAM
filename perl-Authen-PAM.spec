%define upstream_name	 Authen-PAM
%define upstream_version 0.16

Summary:	Perl interface to the PAM library
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	18
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Authen::PAM
Source0:	http://www.cpan.org/modules/by-module/Authen/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Authen-PAM-0.16-fix-build.patch
BuildRequires:	pam-devel
BuildRequires:	perl-devel

%description
The Authen::PAM module provides a Perl interface to the PAM library.
The only difference with the standard PAM interface is that the perl
one is simpler.

%prep
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/auto/Authen/*
%{perl_vendorarch}/Authen/*
%{_mandir}/man3/*
