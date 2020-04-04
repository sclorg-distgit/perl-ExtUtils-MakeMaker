%{?scl:%scl_package perl-%{cpan_name}}

# Run optional test
%bcond_without perl_ExtUtils_MakeMaker_enables_optional_test

%global cpan_name ExtUtils-MakeMaker

Name:           %{?scl_prefix}perl-%{cpan_name}
Epoch:          2
Version:        7.42
Release:        3%{?dist}
Summary:        Create a module Makefile
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
# Do not set RPATH to perl shared-library modules by default. Bug #773622.
# This is copy from `perl' package. This is a distributor extension.
Patch0:         %{cpan_name}-7.36-USE_MM_LD_RUN_PATH.patch
# Link to libperl.so explicitly. Bug #960048.
Patch1:         %{cpan_name}-7.30-Link-to-libperl-explicitly-on-Linux.patch
# Unbundle version modules
Patch2:         %{cpan_name}-7.04-Unbundle-version.patch
# Unbundle Encode::Locale module
Patch3:         %{cpan_name}-7.22-Unbundle-Encode-Locale.patch
# Provide maybe_command independently, bug #1129443
Patch4:         %{cpan_name}-7.11-Provide-ExtUtils-MM-methods-as-standalone-ExtUtils-M.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
# Makefile.Pl uses ExtUtils::MakeMaker from ./lib
# B needed only for CPAN::Meta::Requirements
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
# CPAN::Meta::Requirements has a fallback
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.8
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(version)
BuildRequires:  %{?scl_prefix}perl(warnings)
# If an XS module is compiled, xsubpp(1) is needed
BuildRequires:  %{?scl_prefix}perl-ExtUtils-ParseXS
# Tests:
BuildRequires:  %{?scl_prefix}perl(AutoSplit)
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta) >= 2.143240
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Install) >= 1.52
# ExtUtils::Installed not used at tests
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Manifest) >= 1.70
# ExtUtils::Packlist not used at tests
# ExtUtils::XSSymSet is not needed (VMS only)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Temp) >= 0.22
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
# IO::File not used at tests
# IO::Handle not used
BuildRequires:  %{?scl_prefix}perl(less)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Parse::CPAN::Meta) >= 1.4414
BuildRequires:  %{?scl_prefix}perl(Pod::Man)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(subs)
BuildRequires:  %{?scl_prefix}perl(Test::Harness)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(Text::ParseWords)
# threads::shared not used
BuildRequires:  %{?scl_prefix}perl(utf8)
# XSLoader not used
%if %{with perl_ExtUtils_MakeMaker_enables_optional_test}
# Optional tests
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl(B)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::CBuilder)
BuildRequires:  %{?scl_prefix}perl(PerlIO)
# Keep YAML optional
# Keep YAML::Tiny optional
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(B)
Requires:       %{?scl_prefix}perl(CPAN::Meta) >= 2.143240
Requires:       %{?scl_prefix}perl(CPAN::Meta::Converter) >= 2.141170
# CPAN::Meta::Requirements to support version ranges
Requires:       %{?scl_prefix}perl(CPAN::Meta::Requirements) >= 2.130
Requires:       %{?scl_prefix}perl(Data::Dumper)
Requires:       %{?scl_prefix}perl(DynaLoader)
# Encode is needed for producing POD with =encoding statement correctly
Requires:       %{?scl_prefix}perl(Encode)
%if !%{defined perl_bootstrap}
Requires:       %{?scl_prefix}perl(Encode::Locale)
%endif
Requires:       %{?scl_prefix}perl(ExtUtils::Command) >= 1.19
Requires:       %{?scl_prefix}perl(ExtUtils::Install) >= 1.54
Requires:       %{?scl_prefix}perl(ExtUtils::Manifest) >= 1.70
# ExtUtils::XSSymSet is not needed (VMS only)
Requires:       %{?scl_prefix}perl(File::Find)
Requires:       %{?scl_prefix}perl(File::Spec) >= 0.8
Requires:       %{?scl_prefix}perl(Getopt::Long)
Requires:       %{?scl_prefix}perl(JSON::PP)
# Optional Pod::Man is needed for generating manual pages from POD
Requires:       %{?scl_prefix}perl(Pod::Man)
Requires:       %{?scl_prefix}perl(POSIX)
Requires:       %{?scl_prefix}perl(Test::Harness)
Requires:       %{?scl_prefix}perl(Time::HiRes)
Requires:       %{?scl_prefix}perl(Text::ParseWords)
# VMS::Filespec is not needed (VMS only)
# Win32 is not needed (Win32 only)
# If an XS module is compiled, xsubpp(1) is needed
Requires:       %{?scl_prefix}perl-ExtUtils-ParseXS
# These dependencies are weak in order to relieve building noarch
# packages from perl-devel and gcc. See bug #1547165.
# If an XS module is built, code generated from XS will be compiled and it
# includes Perl header files.
Requires:       %{?scl_prefix}perl-devel
# If an XS module is built, the generated Makefile executes gcc.
Requires:       gcc

# Do not export underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(File::Spec\\)\s*$
# Do not export private redefinitions
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^%{?scl_prefix}perl\\(DynaLoader|ExtUtils::MakeMaker::_version\\)

%description
This utility is designed to write a Makefile for an extension module from a
Makefile.PL. It is based on the Makefile.SH model provided by Andy
Dougherty and the perl5-porters.

%package -n %{?scl_prefix}perl-ExtUtils-Command
Summary:        Perl routines to replace common UNIX commands in Makefiles
License:        GPL+ or Artistic
BuildArch:      noarch
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Carp)
Requires:       %{?scl_prefix}perl(File::Copy)
Requires:       %{?scl_prefix}perl(File::Find)
Requires:       %{?scl_prefix}perl(File::Path)
# File::Spec not used
# VMS::Feature not used

%description -n %{?scl_prefix}perl-ExtUtils-Command
This Perl module is used to replace common UNIX commands. In all cases the
functions work with @ARGV rather than taking arguments. This makes them
easier to deal with in Makefiles.

%package -n %{?scl_prefix}perl-ExtUtils-MM-Utils
Summary:        ExtUtils::MM methods without dependency on ExtUtils::MakeMaker
License:        GPL+ or Artistic
BuildArch:      noarch
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description -n %{?scl_prefix}perl-ExtUtils-MM-Utils
This is a collection of ExtUtils::MM subroutines that are used by many
other modules but that do not need full-featured ExtUtils::MakeMaker. The
issue with ExtUtils::MakeMaker is it pulls in Perl header files and that
is an overkill for small subroutines.

%prep
%setup -q -n ExtUtils-MakeMaker-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
# Remove bundled modules
rm -rf bundled
%{?scl:scl enable %{scl} '}perl -i -ne %{?scl:'"}'%{?scl:"'}print $_ unless m{^bundled/}%{?scl:'"}'%{?scl:"'} MANIFEST%{?scl:'}
rm -rf t/lib/Test
%{?scl:scl enable %{scl} '}perl -i -ne %{?scl:'"}'%{?scl:"'}print $_ unless m{^t/lib/Test/}%{?scl:'"}'%{?scl:"'} MANIFEST%{?scl:'}
rm -rf lib/ExtUtils/MakeMaker/version{,.pm}
%{?scl:scl enable %{scl} '}perl -i -ne %{?scl:'"}'%{?scl:"'}print $_ unless m{^lib/ExtUtils/MakeMaker/version(?:/|\.pm)}%{?scl:'"}'%{?scl:"'} MANIFEST%{?scl:'}
rm -rf lib/ExtUtils/MakeMaker/Locale.pm
%{?scl:scl enable %{scl} '}perl -i -ne %{?scl:'"}'%{?scl:"'}print $_ unless m{^lib/ExtUtils/MakeMaker/Locale\.pm}%{?scl:'"}'%{?scl:"'} MANIFEST%{?scl:'}

%build
BUILDING_AS_PACKAGE=1 %{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 && %{make_build}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}%{make_install}%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes CONTRIBUTING README
%{_bindir}/*
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/ExtUtils/Command.pm
%exclude %dir %{perl_vendorlib}/ExtUtils/MM
%exclude %{perl_vendorlib}/ExtUtils/MM/Utils.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/ExtUtils::Command.*
%exclude %{_mandir}/man3/ExtUtils::MM::Utils.*

%files -n %{?scl_prefix}perl-ExtUtils-Command
%dir %{perl_vendorlib}/ExtUtils
%{perl_vendorlib}/ExtUtils/Command.pm
%{_mandir}/man3/ExtUtils::Command.*

%files -n %{?scl_prefix}perl-ExtUtils-MM-Utils
%dir %{perl_vendorlib}/ExtUtils
%dir %{perl_vendorlib}/ExtUtils/MM
%{perl_vendorlib}/ExtUtils/MM/Utils.pm
%{_mandir}/man3/ExtUtils::MM::Utils.*

%changelog
* Tue Jan 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2:7.42-3
- Re-rebuild of bootstrapped packages

* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:7.42-2
- SCL

* Wed Dec 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:7.42-1
- 7.42 bump

* Tue Dec 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:7.40-1
- 7.40 bump

* Wed Sep 11 2019 Petr Pisar <ppisar@redhat.com> - 2:7.38-1
- 7.38 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:7.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:7.36-3
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:7.36-2
- Perl 5.30 rebuild

* Mon Apr 29 2019 Petr Pisar <ppisar@redhat.com> - 1:7.36-1
- 7.36 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.34-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.34-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:7.34-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:7.34-416
- Increase release to favour standalone package

* Mon Mar 19 2018 Petr Pisar <ppisar@redhat.com> - 1:7.34-1
- 7.34 bump

* Wed Feb 28 2018 Petr Pisar <ppisar@redhat.com> - 1:7.32-2
- Recommend gcc and perl-devel instead of a hard dependency (bug #1547165)

* Mon Feb 19 2018 Petr Pisar <ppisar@redhat.com> - 1:7.32-1
- 7.32 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Petr Pisar <ppisar@redhat.com> - 1:7.30-3
- Rebase patches
- Do not recommend non-core Encode::Locale on bootstrapping

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Petr Pisar <ppisar@redhat.com> - 1:7.30-1
- 7.30 bump

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:7.28-2
- Perl 5.26 rebuild

* Wed May 31 2017 Petr Pisar <ppisar@redhat.com> - 7.28-1
- 7.28 bump

* Mon May 29 2017 Petr Pisar <ppisar@redhat.com> - 7.26-1
- 7.26 bump
- Fix META generation (CPAN RT#121913)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 7.24-1
- 7.24 bump

* Tue Aug 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 7.22-1
- 7.22 bump

* Tue May 24 2016 Petr Pisar <ppisar@redhat.com> - 7.18-1
- 7.18 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 7.16-2
- Perl 5.24 rebuild

* Mon May 09 2016 Petr Pisar <ppisar@redhat.com> - 7.16-1
- 7.16 bump

* Mon Apr 25 2016 Petr Pisar <ppisar@redhat.com> - 7.14-1
- 7.14 bump

* Wed Apr 20 2016 Petr Pisar <ppisar@redhat.com> - 7.12-1
- 7.12 bump

* Tue Apr 19 2016 Petr Pisar <ppisar@redhat.com> - 7.10-5
- Own ExtUtils/MM directory by perl-ExtUtils-MM-Utils only
- Require perl-devel by perl-ExtUtils-MakeMaker

* Mon Apr 18 2016 Petr Pisar <ppisar@redhat.com> - 7.10-4
- Provide maybe_command independently (bug #1129443)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 03 2015 Petr Pisar <ppisar@redhat.com> - 7.10-2
- Declare optional dependencies on Recommends level

* Fri Sep 11 2015 Petr Pisar <ppisar@redhat.com> - 7.10-1
- 7.10 bump

* Wed Sep 09 2015 Petr Pisar <ppisar@redhat.com> - 7.08-1
- 7.08 bump

* Tue Sep 01 2015 Jitka Plesnikova <jplesnik@redhat.com> - 7.06-2
- Remove new line from INC (CPAN RT#106808)

* Tue Sep 01 2015 Petr Pisar <ppisar@redhat.com> - 7.06-1
- 7.06 bump
- ExtUtils::Command module is distributed by ExtUtils-MakeMaker

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.04-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 7.04-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 7.04-2
- Perl 5.22 rebuild

* Fri Dec 05 2014 Petr Pisar <ppisar@redhat.com> - 7.04-1
- 7.04 bump

* Tue Nov 11 2014 Petr Pisar <ppisar@redhat.com> - 7.02-1
- 7.02 bump
- Cope with missing Encode::Locale

* Wed Nov 05 2014 Petr Pisar <ppisar@redhat.com> - 7.00-2
- Fix building with older xsubpp

* Mon Oct 27 2014 Petr Pisar <ppisar@redhat.com> - 7.00-1
- 7.00 bump

* Fri Oct 24 2014 Petr Pisar <ppisar@redhat.com> - 6.98-311
- Require perl-ExtUtils-ParseXS because of xsubpp

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.98-310
- Increase release to favour standalone package

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.98-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Petr Pisar <ppisar@redhat.com> - 6.98-1
- 6.98 bump

* Mon Apr 14 2014 Petr Pisar <ppisar@redhat.com> - 6.96-1
- 6.96 bump

* Wed Mar 26 2014 Petr Pisar <ppisar@redhat.com> - 6.94-1
- 6.94 bump

* Fri Mar 14 2014 Petr Pisar <ppisar@redhat.com> - 6.92-1
- 6.92 bump

* Fri Feb 21 2014 Petr Pisar <ppisar@redhat.com> - 6.90-1
- 6.90 bump

* Mon Feb 03 2014 Petr Pisar <ppisar@redhat.com> - 6.88-1
- 6.88 bump

* Mon Jan 06 2014 Petr Pisar <ppisar@redhat.com> - 6.86-1
- 6.86 bump

* Mon Dec 02 2013 Petr Pisar <ppisar@redhat.com> - 6.84-1
- 6.84 bump

* Tue Nov 05 2013 Petr Pisar <ppisar@redhat.com> - 6.82-1
- 6.82 bump

* Wed Oct 16 2013 Petr Pisar <ppisar@redhat.com> - 6.80-1
- 6.80 bump

* Tue Sep 24 2013 Petr Pisar <ppisar@redhat.com> - 6.78-1
- 6.78 bump

* Mon Sep 16 2013 Petr Pisar <ppisar@redhat.com> - 6.76-2
- Specify all dependencies (bug #1007755)

* Tue Sep 10 2013 Petr Pisar <ppisar@redhat.com> - 6.76-1
- 6.76 bump

* Mon Sep 02 2013 Petr Pisar <ppisar@redhat.com> - 6.74-1
- 6.74 bump

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 6.72-1
- 6.72 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.68-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 6.68-4
- Perl 5.18 rebuild

* Tue Jul 02 2013 Petr Pisar <ppisar@redhat.com> - 6.68-3
- Link to libperl.so explicitly (bug #960048)

* Thu Jun 27 2013 Jitka Plesnikova <jplesnik@redhat.com> - 6.68-2
- Update BRs

* Mon Jun 17 2013 Petr Pisar <ppisar@redhat.com> - 6.68-1
- 6.68 bump

* Mon Apr 22 2013 Petr Pisar <ppisar@redhat.com> - 6.66-1
- 6.66 bump

* Tue Jan 29 2013 Petr Pisar <ppisar@redhat.com> - 6.64-2
- Run-require POD convertors to get manual pages when building other packages

* Mon Dec 17 2012 Petr Pisar <ppisar@redhat.com> - 6.64-1
- 6.64 bump

* Tue Aug 28 2012 Petr Pisar <ppisar@redhat.com> - 6.63.02-241
- Compute RPM version
- Do not build-require itself, the build script runs from ./lib

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 6.63.02-240
- update version to the same as in perl.srpm
- Bump release to override sub-package from perl.spec

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 6.62-3
- Perl 5.16 rebuild

* Thu Jan 12 2012 Petr Pisar <ppisar@redhat.com> - 6.62-2
- Do not set RPATH to perl shared-library modules by default (bug #773622)

* Fri Nov 25 2011 Petr Pisar <ppisar@redhat.com> 6.62-1
- Specfile autogenerated by cpanspec 1.78.
- Remove defattr and BuildRoot from spec.
