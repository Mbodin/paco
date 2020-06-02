COQMODULE    := Paco
COQTHEORIES  := *.v
COQMAKEFILEOPTIONS ?=

.PHONY: all theories clean doc

all: Makefile.coq
	export HOME=`pwd`; $(MAKE) -f Makefile.coq all

quick: Makefile.coq
	export HOME=`pwd`; $(MAKE) -f Makefile.coq quick

_CoqProject: Makefile $(COQTHEORIES)
	(echo "-R . $(COQMODULE)"; \
	 echo $(COQTHEORIES)) > $@

Makefile.coq: _CoqProject
	coq_makefile -f _CoqProject -o Makefile.coq $(COQMAKEFILEOPTIONS)

doc: Makefile.coq
	$(MAKE) -f Makefile.coq html
	cp index.html main.css html

install:
	$(MAKE) -f Makefile.coq install

install-doc: doc
	$(MAKE) -f Makefile.coq install-doc

clean: Makefile.coq
	$(MAKE) -f Makefile.coq cleanall
	rm -f _CoqProject Makefile.coq Makefile.coq.conf

