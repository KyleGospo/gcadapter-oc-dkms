%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     gcadapter_oc
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Kernel module for overclocking the Nintendo Wii U/Mayflash GameCube adapter.
License:  GPLv2
URL:      https://github.com/KyleGospo/gcadapter_oc-dkms

Source:   %{url}/archive/refs/heads/master.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Kernel module for overclocking the Nintendo Wii U/Mayflash GameCube adapter. The default overclock is from 125 Hz to 1000 Hz.

%prep
%setup -q -c gcadapter_oc-dkms-master

%build
install -D -m 0644 gcadapter_oc-dkms-master/%{name}.conf %{buildroot}%{_modulesloaddir}/%{name}.conf

%files
%doc gcadapter_oc-dkms-master/README.md
%license gcadapter_oc-dkms-master/LICENSE
%{_modulesloaddir}/%{name}.conf

%changelog
{{{ git_dir_changelog }}}
