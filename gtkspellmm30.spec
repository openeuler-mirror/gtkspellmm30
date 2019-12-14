Name:           gtkspellmm30
Version:        3.0.5
Release:        8
License:        GPLv2+
Summary:        C++ interface on top of the gtkspell C library
URL:            http://gtkspell.sourceforge.net/
Source0:        http://sourceforge.net/projects/gtkspell/files/gtkspellmm/gtkspellmm-%{version}.tar.xz
BuildRequires:  gcc-c++ gtkspell3-devel gtkmm30-devel gtkmm30-doc make

%description
The gtkspellmm C++ binding provides a C++ interface on top of the gtkspell C library.

%package        devel
Summary:        Development files for gtkspellmm30
Requires:       gtkspellmm30 = %{version}-%{release}

%description    devel
Development files for gtkspellmm30.

%package        help
Summary:        Documentation for gtkspellmm30
BuildArch:      noarch
Provides:       gtkspellmm30-doc = %{version}-%{release}
Obsoletes:      gtkspellmm30-doc < %{version}-%{release}
Requires:       gtkmm30-doc

%description    help
Documentation for gtkspellmm30.

%prep
%autosetup -n gtkspellmm-%{version}
%build
%configure
%make_build
%install
%make_install
%delete_la
%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%files
%doc AUTHORS ChangeLog NEWS README COPYING
%{_libdir}/libgtkspellmm-3.0.so.0*

%files devel
%{_includedir}/gtkspellmm-3.0
%{_libdir}/{libgtkspellmm-3.0.so,gtkspellmm-3.0}
%{_libdir}/pkgconfig/gtkspellmm-3.0.pc

%files help
%{_datadir}/devhelp/books/gtkspellmm-3.0
%{_datadir}/doc/gtkspellmm-3.0

%changelog
* Sat Dec 14 2019 Ling Yang <lingyang2@huawei.com> - 3.0.5-8
- Package init
