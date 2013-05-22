%define upstream_name	 Authen-PAM
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 6

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.160.0-5mdv2012.0
+ Revision: 765067
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.160.0-4
+ Revision: 763483
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.160.0-3
+ Revision: 667031
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 564358
- rebuild for perl 5.12.1

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.1
+ Revision: 406837
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.16-6mdv2009.1
+ Revision: 351671
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.16-5mdv2009.0
+ Revision: 223565
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.16-4mdv2008.1
+ Revision: 151345
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.16-3mdv2008.0
+ Revision: 67587
- rebuild


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.16-2mdv2007.0
+ Revision: 108547
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Authen-PAM

* Tue Oct 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.16-1mdk
- 0.16
- fix url

* Sat Jun 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.15-2mdk
- Rebuild

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.15-1mdk
- 1.15

* Fri Nov 12 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.14-5mdk
- Rebuild for new perl

* Wed Apr 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.14-4mdk
- rebuild for new perl

