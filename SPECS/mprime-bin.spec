%define debug_package %{nil}

Name:           mprime
Version:        28.7
Release:        2%{?dist}
Group:          Applications/System
Summary:        Great Internet Mersenne Prime Search
License:        GIMPS free software license
URL:            http://www.mersenne.org/
Requires:       libstdc++, libgcc
%ifarch %{ix86}
Source0:        p95v287.linux32.tar.gz
%endif
%ifarch x86_64
Source0:        p95v287.linux64.tar.gz
%endif

%description
Great Internet Mersenne Prime Search (GIMPS) is a distributed computing
project dedicated to finding Mersenne primes.

%prep
%setup -c -n %{name}-%{version}

%build
chmod 644 *.txt
chmod 755 mprime

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -D -m 0755 mprime %{buildroot}%{_bindir}/mprime

%files
%defattr(-,root,root)
%{_bindir}/mprime
%doc license.txt readme.txt stress.txt undoc.txt whatsnew.txt

%changelog
* Thu Jan 28 2016 Michael Mohr <akihana@gmail.com> - 28.7-2
- Minor enhancements & cleanups.
* Tue Jan 19 2016 Michael Mohr <akihana@gmail.com> - 28.7-1
- Initial package release.