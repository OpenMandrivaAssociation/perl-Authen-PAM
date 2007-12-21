%define module	Authen-PAM
%define version 0.16
%define release %mkrel 3

Summary:	Perl interface to the PAM library
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	pam-devel perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
The Authen::PAM module provides a Perl interface to the PAM library.
The only difference with the standard PAM interface is that the perl
one is simpler.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/auto/Authen/*
%{perl_vendorarch}/Authen/*


