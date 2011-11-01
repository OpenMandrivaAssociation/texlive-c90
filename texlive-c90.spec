Name:		texlive-c90
Version:	20111101
Release:	1
Summary:	TeXLive c90 package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/c90.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/c90.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/c90.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
TeXLive c90 package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
