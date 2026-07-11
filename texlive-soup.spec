%global tl_name soup
%global tl_revision 50815

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.2
Release:	%{tl_revision}.1
Summary:	Generate alphabet soup puzzles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/soup
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/soup.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/soup.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/soup.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Generate alphabet soup puzzles (aka word search puzzles), and variations
using numbers or other symbols. Provides macros to generate an alphabet
soup style puzzle (also known as word search puzzles or "find-the-word"
puzzles). Allow creating numbersoup and soups with custom symbol sets.

