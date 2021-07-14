#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-graphviz
Version  : 0.17
Release  : 30
URL      : https://files.pythonhosted.org/packages/5c/23/13db6270cf0b508aff23012b9963190455a474565df6425c727c9a5386ec/graphviz-0.17.zip
Source0  : https://files.pythonhosted.org/packages/5c/23/13db6270cf0b508aff23012b9963190455a474565df6425c727c9a5386ec/graphviz-0.17.zip
Summary  : Simple Python interface for Graphviz
Group    : Development/Tools
License  : MIT
Requires: python-graphviz-python = %{version}-%{release}
Requires: python-graphviz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Graphviz
========
|PyPI version| |License| |Supported Python| |Format|
|Build| |Codecov| |Readthedocs-stable| |Readthedocs-latest|

%package python
Summary: python components for the python-graphviz package.
Group: Default
Requires: python-graphviz-python3 = %{version}-%{release}

%description python
python components for the python-graphviz package.


%package python3
Summary: python3 components for the python-graphviz package.
Group: Default
Requires: python3-core
Provides: pypi(graphviz)

%description python3
python3 components for the python-graphviz package.


%prep
%setup -q -n graphviz-0.17
cd %{_builddir}/graphviz-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626276001
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
