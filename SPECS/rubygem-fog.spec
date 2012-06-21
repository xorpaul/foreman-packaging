# Generated from fog-1.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog
%global rubyabi 1.9.1

Summary: brings clouds to you
Name: rubygem-%{gem_name}
Version: 1.3.1
Release: 4%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/fog/fog
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(builder) 
Requires: rubygem(excon) >= 0.14.0
Requires: rubygem(formatador) => 0.2.0
Requires: rubygem(formatador) < 0.3
Requires: rubygem(multi_json) => 1.0
Requires: rubygem(multi_json) < 2
Requires: rubygem(mime-types) 
Requires: rubygem(net-scp) => 1.0.4
Requires: rubygem(net-scp) < 1.1
Requires: rubygem(net-ssh) >= 2.1.3
Requires: rubygem(nokogiri) => 1.5.0
Requires: rubygem(nokogiri) < 1.6
Requires: rubygem(ruby-hmac) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
The Ruby cloud services library. Supports all major cloud providers including
AWS, Rackspace, Linode, Blue Box, StormOnDemand, and many others. Full support
for most AWS services including EC2, S3, CloudWatch, SimpleDB, ELB, and RDS.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0} 

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x


%files
%dir %{gem_instdir}
%{_bindir}/fog
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/fog-1.3.1/.document
/usr/share/gems/gems/fog-1.3.1/.gitignore
/usr/share/gems/gems/fog-1.3.1/.irbrc
/usr/share/gems/gems/fog-1.3.1/Gemfile
/usr/share/gems/gems/fog-1.3.1/Rakefile
/usr/share/gems/gems/fog-1.3.1/benchs/fog_vs.rb
/usr/share/gems/gems/fog-1.3.1/benchs/params.rb
/usr/share/gems/gems/fog-1.3.1/benchs/parse_vs_push.rb
/usr/share/gems/gems/fog-1.3.1/changelog.txt
/usr/share/gems/gems/fog-1.3.1/docs/
/usr/share/gems/gems/fog-1.3.1/fog.gemspec
/usr/share/gems/gems/fog-1.3.1/spec/
/usr/share/gems/gems/fog-1.3.1/tests/

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Jun 14 2012 jason - 1.3.1-1
- Initial package
