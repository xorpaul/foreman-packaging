%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name diffy
%global rubyabi 1.9.1

Summary: Convenient diffing in ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.0.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/samg/diffy
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Need diffs in your ruby app? Diffy has you covered. It provides a convenient
way to generate a diff from two strings or files. Instead of reimplementing the
LCS diff algorithm Diffy uses battle tested Unix diff to generate diffs, and
focuses on providing a convenient interface, and getting out of your way.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/*.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/CONTRIBUTORS
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/VERSION

%changelog
* Wed Nov 20 2013 Dominic Cleal <dcleal@redhat.com> 3.0.1-1
- new package built with tito

