Summary:	Set the value reported for a network card MAC address
Name:		fakeif
Version:	0.1
Release:	0.1
License:	?
Group:		Applications
Source0:	http://www.chiark.greenend.org.uk/~peterb/linux/fakeif/%{name}-%{version}.tar.bz2
# Source0-md5:	1ff69e4d383a9473ce94c50b16701001
URL:		http://www.chiark.greenend.org.uk/~peterb/linux/fakeif/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set the value reported for a network card MAC address.

This program demonstrates the use of LD_PRELOAD to override the value
returned by the library call. The library call in question is ioctl.
When called with cmd set to SIOCGIFHWADDR, we override the value
returned by the system call with the value from an environment
variable.

To use the program, first set the environment variable
HWADDR_interface to the MAC address you would like to be returned. For
example, to set eth0 to 11:22:33:44:55:66, do

HWADDR_eth0=11:22:33:44:55:66 export HWADDR_eth0 Then set LD_PRELOAD
to the absolute path of fakeif.so and call your test program.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmcppflags} -s -shared -o libfakeif.so %{rpmldflags} fakeif.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -p libfakeif.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfakeif.so
