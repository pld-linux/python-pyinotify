%define 	module	pyinotify
Summary:	Pyinotify - pure Python module used for monitoring filesystems changes
Summary(hu.UTF-8):	Pyinotify egy egyszerű Python modul, amellyel a fájlrendszer változásait lehet figyelni
Summary(pl.UTF-8):	Pyinotify - moduł w czystym Pythonie do monitorowania zmian w systemie plików
Name:		python-%{module}
Version:	0.9.6
Release:	9
License:	MIT
Group:		Development/Languages/Python
Source0:	http://seb.dbzteam.org/pub/pyinotify/releases/%{module}-%{version}.tar.gz
# Source0-md5:	8e580fa1ff3971f94a6f81672b76c406
URL:		https://github.com/seb-m/pyinotify
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	glibc >= 2.4
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyinotify is a pure Python module used for monitoring filesystems
changes.

%description -l hu.UTF-8
Pyinotify egy egyszerű Python modul, amellyel a fájlrendszer
változásait lehet figyelni.

%description -l pl.UTF-8
Pyinotify to moduł w czystym Pythonie służący do monitorowania zmian w
systemie plików.

%package -n python3-%{module}
Summary:	Pyinotify is a pure Python module used for monitoring filesystems changes
Summary(pl.UTF-8):	Pyinotify - moduł w czystym Pythonie do monitorowania zmian w systemie plików
Group:		Development/Languages/Python

%description -n python3-%{module}
Pyinotify is a pure Python module used for monitoring filesystems
changes.

%description -n python3-%{module} -l hu.UTF-8
Pyinotify egy egyszerű Python modul, amellyel a fájlrendszer
változásait lehet figyelni.

%description -n python3-%{module} -l pl.UTF-8
Pyinotify to moduł w czystym Pythonie służący do monitorowania zmian w
systemie plików.

%prep
%setup -q -n %{module}-%{version}

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' \
	python2/examples/autocompile.py

%build
%py_build -b build_python2
%py3_build -b build_python3

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv build_python2 build
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

install python2/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} -r build
mv build_python3 build
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc old/ChangeLog old/NEWS README.md
%{py_sitescriptdir}/pyinotify.py[co]
%{py_sitescriptdir}/pyinotify-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}

%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/pyinotify.py
%{py3_sitescriptdir}/__pycache__
%{py3_sitescriptdir}/pyinotify-%{version}-py*.egg-info
