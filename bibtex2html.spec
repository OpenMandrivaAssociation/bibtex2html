%define name	bibtex2html
%define version 1.95

Name:		%{name}
Version:	%{version}
Release:	%mkrel 2
Summary:	A Tool for translating from BibTeX to HTML
Group:		Publishing
License:	GPLv2
URL:		http://www.lri.fr/~filliatr/bibtex2html
Source:		http://www.lri.fr/~filliatr/ftp/bibtex2html/%{name}-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	hevea
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-cmsuper
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%prep
%setup -q

%build
%configure
%make
%make doc

%install
%__rm -rf %{buildroot}
%__install -d -m 755 %{buildroot}%{_bindir}
%__install -d -m 755 %{buildroot}%{_mandir}/man1
%__install -m 755 aux2bib bib2bib bibtex2html %{buildroot}%{_bindir}
%__install -m 644 aux2bib.1 bib2bib.1 bibtex2html.1 %{buildroot}%{_mandir}/man1

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING README manual.pdf manual.html
%{_bindir}/*
%{_mandir}/man1/*



