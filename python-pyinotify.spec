%define 	module	pyinotify
Summary:	Pyinotify is a pure Python module used for monitoring filesystems changes
Summary(hu.UTF-8):	Pyinotify egy egyszerű Python modul, amellyel a fájlrendszer változásait lehet figyelni
Name:		python-%{module}
Version:	0.8.6
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://seb.dbzteam.org/pub/pyinotify/releases/%{module}-%{version}.tar.gz
# Source0-md5:	a82afcfd474b2540944d7dc63efeea33
URL:		http://trac.dbzteam.org/pyinotify/wiki
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS TODO
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/%{module}-*.egg-info