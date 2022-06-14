%global srcname distlib
# tests require network access
%bcond_with check

Name:       python-distlib
Version:	0.3.4
Release:	1
Summary:    Low-level components of distutils2/packaging, augmented with higher-level APIs

License:    Python
URL:        https://readthedocs.org/projects/distlib/
Source0:	https://files.pythonhosted.org/packages/source/d/distlib/distlib-%{version}.zip

Patch0: distlib_unbundle.patch

BuildArch:  noarch
BuildRequires:  python3-devel
%rename python3-%{srcname}

%description
Distlib contains the implementations of the packaging PEPs and other low-level
features which relate to packaging, distribution and deployment of Python
software. If Distlib can be made genuinely useful, then it is possible for
third-party packaging tools to transition to using it. Their developers and
users then benefit from standardised implementation of low-level functions,
time saved by not having to reinvent wheels, and improved interoperability
between tools.

%prep
%autosetup -p1 -n %{srcname}-%{version}
rm distlib/*.exe

%build
%py3_build

%if %{with check}
%check
export PYTHONHASHSEED=0
%{python3} setup.py test
%endif # with_tests

%install
%py3_install

%files
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info
