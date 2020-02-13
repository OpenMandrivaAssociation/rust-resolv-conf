# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate resolv-conf

Name:           rust-%{crate}
Version:        0.6.2
Release:        4%{?dist}
Summary:        Resolv.conf file parser

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/resolv-conf
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Resolv.conf file parser.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+hostname-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hostname-devel %{_description}

This package contains library source intended for building other packages
which use "hostname" feature of "%{crate}" crate.

%files       -n %{name}+hostname-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+system-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+system-devel %{_description}

This package contains library source intended for building other packages
which use "system" feature of "%{crate}" crate.

%files       -n %{name}+system-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# /etc/resolv.conf is not in mock
%cargo_test || :
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 10:34:28 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-2
- Regenerate

* Thu May 30 21:00:54 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-1
- Initial package
