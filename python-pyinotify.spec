%define 	module	pyinotify
Summary:	Pyinotify is a pure Python module used for monitoring filesystems changes
Summary(hu.UTF-8):	Pyinotify egy egyszerű Python modul, amellyel a fájlrendszer változásait lehet figyelni
Name:		python-%{module}
Version:	0.8.8
Release:	0.2
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://seb.dbzteam.org/pub/pyinotify/releases/%{module}-%{version}.tar.gz
# Source0-md5:	3c4214f10955e6be0ac2d054efa55cf8
Patch0:		%{name}-glibc.patch
URL:		http://trac.dbzteam.org/pyinotify/wiki
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	glibc >= 2.4
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyinotify is a pure Python module used for monitoring filesystems
changes.

%description -l pl.UTF-8
Pyinotify egy egyszerű Python modul, amellyel a fájlrendszer
változásait lehet figyelni.

%prep
%setup -q -n %{module}
%patch0 -p1

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog_old NEWS TODO
%{_examplesdir}/%{name}-%{version}
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/%{module}-*.egg-info
