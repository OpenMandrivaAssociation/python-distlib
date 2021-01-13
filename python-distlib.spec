%global srcname distlib
# tests require network access
%bcond_with check

Name:       python-distlib
Version:	0.3.1
Release:	2
Summary:    Low-level components of distutils2/packaging, augmented with higher-level APIs

License:    Python
URL:        https://readthedocs.org/projects/distlib/
Source0:	https://files.pythonhosted.org/packages/2f/83/1eba07997b8ba58d92b3e51445d5bf36f9fba9cb8166bcae99b9c3464841/distlib-0.3.1.zip

Patch0: distlib_unbundle.patch

BuildArch:  noarch
BuildRequires:  python3-devel

%description
Distlib contains the implementations of the packaging PEPs and other low-level
features which relate to packaging, distribution and deployment of Python
software. If Distlib can be made genuinely useful, then it is possible for
third-party packaging tools to transition to using it. Their developers and
users then benefit from standardised implementation of low-level functions,
time saved by not having to reinvent wheels, and improved interoperability
between tools.

%package -n python3-%{srcname}
Summary: Low-level components of distutils2/packaging, augmented with higher-level APIs
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Distlib contains the implementations of the packaging PEPs and other low-level
features which relate to packaging, distribution and deployment of Python
software. If Distlib can be made genuinely useful, then it is possible for
third-party packaging tools to transition to using it. Their developers and
users then benefit from standardised implementation of low-level functions,
time saved by not having to reinvent wheels, and improved interoperability
between tools.

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

rm distlib/*.exe
rm -rf distlib/_backport
rm tests/test_shutil.py*
rm tests/test_sysconfig.py*

%build
%py3_build

%if %{with check}
%check
export PYTHONHASHSEED=0
%{python3} setup.py test
%endif # with_tests

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
