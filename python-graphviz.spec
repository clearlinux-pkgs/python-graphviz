#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-graphviz
Version  : 0.10.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/9a/4a/2d8dd8c0cc7f1711c6f76b8af31a206918f139f2f04f34de3109accc2cea/graphviz-0.10.1.zip
Source0  : https://files.pythonhosted.org/packages/9a/4a/2d8dd8c0cc7f1711c6f76b8af31a206918f139f2f04f34de3109accc2cea/graphviz-0.10.1.zip
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
========
        
        |PyPI version| |License| |Supported Python| |Format| |Docs|
        
        |Travis| |Codecov|
        
        This package facilitates the creation and rendering of graph descriptions in
        the DOT_ language of the Graphviz_ graph drawing software (`master repo`_) from
        Python.
        
        Create a graph object, assemble the graph by adding nodes and edges, and
        retrieve its DOT source code string. Save the source code to a file and render
        it with the Graphviz installation of your system.
        
        Use the ``view`` option/method to directly inspect the resulting (PDF, PNG,
        SVG, etc.) file with its default application. Graphs can also be rendered
        and displayed within `Jupyter notebooks`_ (formerly known as
        `IPython notebooks`_, example_) as well as the `Jupyter Qt Console`_.
        
        
        Links
        -----

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

%description python3
python3 components for the python-graphviz package.


%prep
%setup -q -n graphviz-0.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542251475
python3 setup.py build

%install
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
