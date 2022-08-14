#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : opus
Version  : 1.3.1
Release  : 31
URL      : http://downloads.xiph.org/releases/opus/opus-1.3.1.tar.gz
Source0  : http://downloads.xiph.org/releases/opus/opus-1.3.1.tar.gz
Summary  : Opus IETF audio codec (@PC_BUILD@ build)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: opus-lib = %{version}-%{release}
Requires: opus-license = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : graphviz

%description
== Opus audio codec ==
Opus is a codec for interactive speech and audio transmission over the Internet.

%package dev
Summary: dev components for the opus package.
Group: Development
Requires: opus-lib = %{version}-%{release}
Provides: opus-devel = %{version}-%{release}
Requires: opus = %{version}-%{release}

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
Requires: opus-license = %{version}-%{release}

%description lib
lib components for the opus package.


%package license
Summary: license components for the opus package.
Group: Default

%description license
license components for the opus package.


%prep
%setup -q -n opus-1.3.1
cd %{_builddir}/opus-1.3.1
pushd ..
cp -a opus-1.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656449995
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
%configure --disable-static --enable-intrinsics --enable-float-approx
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-intrinsics --enable-float-approx
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656449995
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/opus
cp %{_builddir}/opus-1.3.1/COPYING %{buildroot}/usr/share/package-licenses/opus/dfada97ba32cb44804736a7768104a06be91a4f7
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/opus/opus.h
/usr/include/opus/opus_defines.h
/usr/include/opus/opus_multistream.h
/usr/include/opus/opus_projection.h
/usr/include/opus/opus_types.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libopus.so
/usr/lib64/libopus.so
/usr/lib64/pkgconfig/opus.pc
/usr/share/aclocal/*.m4
/usr/share/man/man3/opus_ctlvalues.3
/usr/share/man/man3/opus_custom.3
/usr/share/man/man3/opus_custom.h.3
/usr/share/man/man3/opus_decoder.3
/usr/share/man/man3/opus_decoderctls.3
/usr/share/man/man3/opus_defines.h.3
/usr/share/man/man3/opus_encoder.3
/usr/share/man/man3/opus_encoderctls.3
/usr/share/man/man3/opus_errorcodes.3
/usr/share/man/man3/opus_genericctls.3
/usr/share/man/man3/opus_libinfo.3
/usr/share/man/man3/opus_multistream.3
/usr/share/man/man3/opus_multistream.h.3
/usr/share/man/man3/opus_multistream_ctls.3
/usr/share/man/man3/opus_repacketizer.3
/usr/share/man/man3/opus_types.h.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/opus/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libopus.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libopus.so.0.8.0
/usr/lib64/libopus.so.0
/usr/lib64/libopus.so.0.8.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/opus/dfada97ba32cb44804736a7768104a06be91a4f7
