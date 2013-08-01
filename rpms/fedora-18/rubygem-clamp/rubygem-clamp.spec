%global gemname clamp

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: a minimal framework for command-line utilities
Name: rubygem-%{gemname}
Version: 0.6.1
Release: 3%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: http://github.com/mdub/clamp
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi)
Requires: ruby(rubygems)
BuildRequires: ruby(abi)
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Clamp provides an object-model for command-line utilities.  
It handles parsing of command-line options, and generation of usage help.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -pa .%{gemdir}/* \
        %{buildroot}%{gemdir}/


%files
%dir %{geminstdir}
%{geminstdir}/lib
%{geminstdir}/spec
%{geminstdir}/examples
%{geminstdir}/.rspec
%{geminstdir}/Gemfile
%{geminstdir}/Rakefile
%{geminstdir}/%{gemname}.gemspec


%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%exclude %{geminstdir}/.travis.yml
%exclude %{geminstdir}/.gitignore
%exclude %{geminstdir}/.autotest
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%{geminstdir}/README.md
%{geminstdir}/CHANGES.md


%changelog
* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.6.1-3
- Rebuild

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.6.1-2
- Import the package into tito

* Wed Jul 31 2013  <shk@linux.com> - 0.6.1-1
- Initial package