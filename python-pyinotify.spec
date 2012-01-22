%define 	module	pyinotify
Summary:	Pyinotify is a pure Python module used for monitoring filesystems changes
Summary(hu.UTF-8):	Pyinotify egy egyszerű Python modul, amellyel a fájlrendszer változásait lehet figyelni
Name:		python-%{module}
Version:	0.9.3
Release:	1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://seb.dbzteam.org/pub/pyinotify/releases/%{module}-%{version}.tar.gz
# Source0-md5:	b922aecb0ac532cfc51ab674e5f2e94c
URL:		http://trac.dbzteam.org/pyinotify/wiki
BuildRequires:	python-devel
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	glibc >= 2.4
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyinotify is a pure Python module used for monitoring filesystems
changes.

%description -l hu.UTF-8
Pyinotify egy egyszerű Python modul, amellyel a fájlrendszer
változásait lehet figyelni.

%package -n	python3-%{module}
Summary:	Pyinotify is a pure Python module used for monitoring filesystems changes
Version:	%{version}
Release:	%{release}
Group:		Development/Languages/Python

%description -n python3-%{module}
Pyinotify is a pure Python module used for monitoring filesystems
changes.

%description -n python3-%{module} -l hu.UTF-8
Pyinotify egy egyszerű Python modul, amellyel a fájlrendszer
változásait lehet figyelni.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build -b build_python2
%{__python3} setup.py build -b build_python3

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv build_python2 build
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

install python2/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} -r build
mv build_python3 build
%{__python3} setup.py \
        install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc old/ChangeLog old/NEWS README.md
%{_examplesdir}/%{name}-%{version}
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/%{module}-*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}*.py
%{py3_sitescriptdir}/__pycache__
%{py3_sitescriptdir}/%{module}-*.egg-info
