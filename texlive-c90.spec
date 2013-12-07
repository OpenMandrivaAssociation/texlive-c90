# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-c90
Version:	20111103
Release:	5
Summary:	TeXLive c90 package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/c90.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/c90.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/c90.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive c90 package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/c90/c90.enc
%doc %{_texmfdistdir}/doc/fonts/enc/c90/c90.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/enc/c90/c90.etx
%doc %{_texmfdistdir}/source/fonts/enc/c90/c90.mtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 749915
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 717992
- texlive-c90
- texlive-c90
- texlive-c90
- texlive-c90
- texlive-c90

