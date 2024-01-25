Name:		texlive-preview
Version:	69470
Release:	1
Summary:	Extract bits of a LaTeX source for output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/preview
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/preview.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/preview.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/preview.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
