%global tl_name preview
%global tl_revision 71662

Name:		texlive-%{tl_name}
Epoch:		1
Version:	14.0.6
Release:	%{tl_revision}.1
Summary:	Extract bits of a LaTeX source for output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/preview
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/preview.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/preview.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/preview.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a free-standing part of the preview-latex bundle. The
package provides the support preview-latex needs, when it chooses the
matter it will preview. The output may reasonably be expected to have
other uses, as in html translators, etc.

