#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-graphviz
Version  : 0.16
Release  : 25
URL      : https://files.pythonhosted.org/packages/cc/a3/8f49063fee2037892f66f1a4d55da8ba25235e76dc27887f7edf95272154/graphviz-0.16.zip
Source0  : https://files.pythonhosted.org/packages/cc/a3/8f49063fee2037892f66f1a4d55da8ba25235e76dc27887f7edf95272154/graphviz-0.16.zip
Summary  : Simple Python interface for Graphviz
Group    : Development/Tools
License  : MIT
Requires: python-graphviz-license = %{version}-%{release}
Requires: python-graphviz-python = %{version}-%{release}
Requires: python-graphviz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
========
        
        |PyPI version| |License| |Supported Python| |Format|
        
        |Travis| |Codecov| |Readthedocs-stable| |Readthedocs-latest|
        
        This package facilitates the creation and rendering of graph descriptions in
        the DOT_ language of the Graphviz_ graph drawing software (`master repo`_) from
        Python.
        
        Create a graph object, assemble the graph by adding nodes and edges, and
        retrieve its DOT source code string. Save the source code to a file and render
        it with the Graphviz installation of your system.
        
        Use the ``view`` option/method to directly inspect the resulting (PDF, PNG,
        SVG, etc.) file with its default application. Graphs can also be rendered
        and displayed within `Jupyter notebooks`_ (formerly known as
        `IPython notebooks`_, example_, nbviewer_) as well as the `Jupyter Qt Console`_.
        
        
        Links
        -----

%package license
Summary: license components for the python-graphviz package.
Group: Default

%description license
license components for the python-graphviz package.


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
%setup -q -n graphviz-0.16
cd %{_builddir}/graphviz-0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610129745
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
mkdir -p %{buildroot}/usr/share/package-licenses/python-graphviz
cp %{_builddir}/graphviz-0.16/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-graphviz/1f08db7230df3793d0b60d818464578883a16227
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-graphviz/1f08db7230df3793d0b60d818464578883a16227

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
