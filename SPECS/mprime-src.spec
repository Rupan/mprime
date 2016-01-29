Name:           mprime
Version:        28.7
Release:        1%{?dist}
Group:          Applications/System
Summary:        Great Internet Mersenne Prime Search
License:        GIMPS free software license
URL:            http://www.mersenne.org/
Requires:       libstdc++, libcurl
BuildRequires:  libstdc++-devel, libcurl-devel
Source0:        p95v287.source.zip
Patch0:         mprime-28.7-dynamic-link.patch

%description
Great Internet Mersenne Prime Search (GIMPS) is a distributed computing
project dedicated to finding Mersenne primes.

%prep
%setup -c -n %{name}-%{version}
%patch0 -p1
#cp %{SOURCE1} README.mprime

%build
%ifarch x86_64
cd gwnum
make -f make64
cd ../linux64
make -f makefile
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ifarch x86_64
%{__install} -D -m 0755 linux64/mprime %{buildroot}%{_bindir}/mprime
%endif

%files
%defattr(-,root,root)
%{_bindir}/mprime

%changelog
* Thu Jan 28 2016 Michael Mohr <akihana@gmail.com> - 28.7-1
- Initial package release.
