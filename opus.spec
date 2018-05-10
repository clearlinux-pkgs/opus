#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : opus
Version  : 1.2.1
Release  : 16
URL      : http://downloads.xiph.org/releases/opus/opus-1.2.1.tar.gz
Source0  : http://downloads.xiph.org/releases/opus/opus-1.2.1.tar.gz
Summary  : Opus IETF audio codec (@PC_BUILD@ build)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: opus-lib
Requires: opus-doc
BuildRequires : doxygen
BuildRequires : graphviz

%description
== Opus audio codec ==
Opus is a codec for interactive speech and audio transmission over the Internet.

%package dev
Summary: dev components for the opus package.
Group: Development
Requires: opus-lib
Provides: opus-devel

%description dev
dev components for the opus package.


%package doc
Summary: doc components for the opus package.
Group: Documentation

%description doc
doc components for the opus package.


%package lib
Summary: lib components for the opus package.
Group: Libraries

%description lib
lib components for the opus package.


%prep
%setup -q -n opus-1.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1504923157
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
%configure --disable-static --enable-intrinsics --enable-float-approx
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1504923157
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/opus/opus.h
/usr/include/opus/opus_defines.h
/usr/include/opus/opus_multistream.h
/usr/include/opus/opus_types.h
/usr/lib64/libopus.so
/usr/lib64/pkgconfig/opus.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/opus/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libopus.so.0
/usr/lib64/libopus.so.0.6.1
