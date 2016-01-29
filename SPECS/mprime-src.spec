Name:           mprime
Version:        28.7
Release:        2%{?dist}
Group:          Applications/System
Summary:        Great Internet Mersenne Prime Search
License:        GIMPS free software license
URL:            http://www.mersenne.org/
Requires:       libstdc++, libcurl
BuildRequires:  libstdc++-devel, libcurl-devel
Source0:        p95v287.source.zip
%ifarch %{ix86}
Source1:        p95v287.linux32.tar.gz
%endif
%ifarch x86_64
Source1:        p95v287.linux64.tar.gz
%endif
Patch0:         mprime-28.7-dynamic-link.patch

%description
Great Internet Mersenne Prime Search (GIMPS) is a distributed computing
project dedicated to finding Mersenne primes.

%prep
%setup -c -n %{name}-%{version}
%patch0 -p1
mkdir -p docs
tar xf %{SOURCE1} -C docs --exclude=mprime
chmod 644 docs/*

%build
%ifarch x86_64
cd gwnum
make -f make64
cd ../linux64
make -f makefile
cd ..
%endif
%ifarch %{ix86}
cd gwnum
make -f makefile
cd ../linux
make -f makefile
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ifarch %{ix86}
%{__install} -D -m 0755 linux/mprime %{buildroot}%{_bindir}/mprime
%endif
%ifarch x86_64
%{__install} -D -m 0755 linux64/mprime %{buildroot}%{_bindir}/mprime
%endif

%files
%defattr(-,root,root)
%{_bindir}/mprime
%doc docs/*.txt

%changelog
* Thu Jan 28 2016 Michael Mohr <akihana@gmail.com> - 28.7-2
- Add documentation, untested 32-bit support.
* Thu Jan 28 2016 Michael Mohr <akihana@gmail.com> - 28.7-1
- Initial package release.
