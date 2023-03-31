Name:		texlive-soup
Version:	50815
Release:	2
Summary:	Generate alphabet soup puzzles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/soup
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soup.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soup.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soup.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Generate alphabet soup puzzles (aka word search puzzles), and
variations using numbers or other symbols. Provides macros to
generate an alphabet soup style puzzle (also known as word
search puzzles or "find-the-word" puzzles). Allow creating
numbersoup and soups with custom symbol sets.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/soup
%{_texmfdistdir}/tex/latex/soup
%doc %{_texmfdistdir}/doc/latex/soup

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
