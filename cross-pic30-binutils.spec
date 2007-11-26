%define name		cross-pic30-elf-binutils
%define version		2.14.mplab.2.01
%define release		%mkrel 2

Summary:	GNU Binary Utility Development Utilities
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
URL:		http://ww1.microchip.com/downloads/en/DeviceDoc/mplabalc30v2_01.tgz
Source0:	mplabalc30v2_01.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	byacc gcc4.1 gettext texinfo dos2unix
Patch0:		pic30-binutils-makefile-in.diff.bz2
Patch1:		cross-pic30-binutils-gcc4.patch.bz2

%description
Microchip binutils for dsPICs.

%description
This package contains the library needed to run programs dynamically
linked with binutils.

%prep
%setup -q -n acme
find . -type f -exec dos2unix '{}' ';'
%patch0 -p0 -b .makefile-in
%patch1 -p1 -b .gcc4

%build
CC=gcc-`gcc4.1-version` ./configure --target=pic30-elf --prefix=%{_prefix}
%make tooldir=%{_prefix} all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_prefix}/share
rm -rf $RPM_BUILD_ROOT%{_prefix}/pic30-elf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_mandir}/man1/*


