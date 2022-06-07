%global debug_package %{nil}
%global dkms_name gcadapter_oc

Name:       %{dkms_name}-dkms
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    Kernel module for overclocking the Nintendo Wii U/Mayflash GameCube adapter.
License:    GPLv2
URL:        https://github.com/KyleGospo/gcadapter-oc-dkms
BuildArch:  noarch

# Source files:
# https://github.com/HannesMann/gcadapter-oc-kmod
Source0:    gcadapter_oc.c
Source1:    Makefile
Source2:    dkms.conf
Source3:    LICENSE
Source4:    README.md

Provides:   %{dkms_name}-dkms = %{version}
Requires:   dkms

%description
Kernel module for overclocking the Nintendo Wii U/Mayflash GameCube adapter. The default overclock is from 125 Hz to 1000 Hz.

%prep
%setup -q -T -c -n %{name}-%{version}
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build

%install
# Create empty tree
mkdir -p %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
cp -fr * %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

install -d %{buildroot}%{_sysconfdir}/modules-load.d
cat > %{buildroot}%{_sysconfdir}/modules-load.d/gcadapter_oc.conf << EOF
gcadapter_oc
EOF

%post
dkms add -m %{dkms_name} -v %{version} -q || :
# Rebuild and make available for the currently running kernel
dkms build -m %{dkms_name} -v %{version} -q || :
dkms install -m %{dkms_name} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{version} -q --all || :

%files
%license LICENSE
%doc README.md
%{_usrsrc}/%{dkms_name}-%{version}
%{_sysconfdir}/modules-load.d/gcadapter_oc.conf

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}