# revision 17118
# category Package
# catalog-ctan /macros/latex/contrib/preview
# catalog-date 2010-02-22 08:57:39 +0100
# catalog-license gpl
# catalog-version 11.86
Name:		texlive-preview
Version:	11.86
Release:	2
Summary:	Extract bits of a LaTeX source for output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/preview
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/preview.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/preview.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/preview.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is a free-standing part of the preview-latex
bundle. The package provides the support preview-latex needs,
when it chooses the matter it will preview. The output may
reasonably be expected to have other uses, as in html
translators, etc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/preview/prauctex.cfg
%{_texmfdistdir}/tex/latex/preview/prauctex.def
%{_texmfdistdir}/tex/latex/preview/prcounters.def
%{_texmfdistdir}/tex/latex/preview/preview.sty
%{_texmfdistdir}/tex/latex/preview/prfootnotes.def
%{_texmfdistdir}/tex/latex/preview/prlyx.def
%{_texmfdistdir}/tex/latex/preview/prshowbox.def
%{_texmfdistdir}/tex/latex/preview/prshowlabels.def
%{_texmfdistdir}/tex/latex/preview/prtightpage.def
%{_texmfdistdir}/tex/latex/preview/prtracingall.def
%doc %{_texmfdistdir}/doc/latex/preview/README
%doc %{_texmfdistdir}/doc/latex/preview/preview.pdf
#- source
%doc %{_texmfdistdir}/source/latex/preview/preview.drv
%doc %{_texmfdistdir}/source/latex/preview/preview.dtx
%doc %{_texmfdistdir}/source/latex/preview/preview.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 11.86-2
+ Revision: 755065
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 11.86-1
+ Revision: 719299
- texlive-preview
- texlive-preview
- texlive-preview
- texlive-preview

