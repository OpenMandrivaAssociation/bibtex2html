%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A Tool for translating from BibTeX to HTML
Name:		bibtex2html
Version:	1.99
Release:	1
License:	GPLv2+
Group:		Publishing
Url:		http://www.lri.fr/~filliatr/bibtex2html
Source0:	http://www.lri.fr/~filliatr/ftp/bibtex2html/%{name}-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	hevea
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-cmsuper
BuildRequires:	texlive

%description
bibtex2html is a collection of tools for translating bibliographies
in BibTeX format to HTML. Here are some of these tools' more important
features:

* Handle any BibTeX style (even those producing multiple bibliographies);
* Use additional fields like abstract, url, ps, etc. to insert web links;
* Crossrefs are also replaced by links;
* Sort by dates or authors, in increasing or decreasing order;
* Read simple macros in TeX or LaTeX files;
* Show syntax errors in BibTeX files;
* Extract from one or several BibTeX files the set of entries satisfying
  a given criterion.

%files
%doc CHANGES COPYING README manual.pdf manual.html
%{_bindir}/*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q
# Removing unused lib from makefile
sed -i 's/-cclib -lstr//' Makefile.in

%build
%configure
%make
%make doc

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 aux2bib bib2bib bibtex2html %{buildroot}%{_bindir}
install -m 644 aux2bib.1 bib2bib.1 bibtex2html.1 %{buildroot}%{_mandir}/man1
