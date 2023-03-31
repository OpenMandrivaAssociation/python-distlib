%global srcname distlib

Name:		python-distlib
Version:	0.3.6
Release:	2
Summary:	Low-level components of distutils2/packaging, augmented with higher-level APIs
License:	Python
URL:		https://readthedocs.org/projects/distlib/
Source0:	https://files.pythonhosted.org/packages/source/d/distlib/distlib-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  python-devel
BuildRequires:	python-pip
BuildRequires:	python-wheel
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
mkdir wheels
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}.dist-info
