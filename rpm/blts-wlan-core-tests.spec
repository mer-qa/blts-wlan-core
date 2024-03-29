Summary: BLTS WLAN low-level test set
Name: blts-wlan-core-tests
Version: 0.1.12
Release: 1
License: GPLv2
Group: Development/Testing
URL: https://github.com/mer-qa/blts-wlan-core
Source0: %{name}-%{version}.tar.gz
BuildRequires: libbltscommon-devel
BuildRequires: libnl-devel
Requires: blts-wlan-core-tests-config
%define _prefix /opt/tests/%{name}

%package config-example
Summary: BLTS WLAN low-level test config example
Provides: blts-wlan-core-tests-config
Requires: blts-tools

%description
This package contains functional tests for WLAN.

%description config-example
This package contains configuration example for WLAN functional tests.

%prep
%setup -q

%build
./autogen.sh
%configure --prefix=%{_prefix} --libdir=%{_prefix}
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_prefix}/bin/*

%files config-example
%defattr(-,root,root,-)
%{_prefix}/cnf/blts-wlan-core-tests.cnf
%{_prefix}/tests.xml
