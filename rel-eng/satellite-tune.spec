Name:          satellite-tune
Version:       master
Release:       1%{?dist}
Summary:       Various tunings for Red Hat Satellite 6
License:       GPLv3
Group:         Development/Tools
URL:           https://github.com/redhat-performance/satellite-tune
Source0:       https://github.com/redhat-performance/satellite-tune/archive/%{name}-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:     noarch
Requires:      ansible


%description
Ansible playbooks to tune various aspects of Red Hat Satellite 6 or its Capsule


%prep
%setup -qc


%build


%install
rm -rf %{buildroot}
pushd %{name}-%{version}
rm -rf rel-eng
mkdir -p %{buildroot}/usr/%{name}
cp README.md %{buildroot}/usr/%{name}
cp LICENSE %{buildroot}/usr/%{name}
cp -r adhoc-scripts %{buildroot}/usr/%{name}
cp -r ansible %{buildroot}/usr/%{name}
cp -r docs %{buildroot}/usr/%{name}
mkdir %{buildroot}/usr/%{name}/conf
cp conf/hosts.ini.sample %{buildroot}/usr/%{name}/conf
cp conf/tunings.yaml %{buildroot}/usr/%{name}/conf
popd


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/%{name}


%changelog
* Fri Jun 2 2017 Jan Hutar <jhutar@redhat.com> 1.1-1
- Init
