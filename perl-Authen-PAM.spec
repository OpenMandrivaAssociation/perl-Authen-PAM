%define upstream_name	 Authen-PAM
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Perl interface to the PAM library
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Authen/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	pam-devel
BuildRequires:  perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{version}

%description
The Authen::PAM module provides a Perl interface to the PAM library.
The only difference with the standard PAM interface is that the perl
one is simpler.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/auto/Authen/*
%{perl_vendorarch}/Authen/*
