LEXICON ?= new
COMMONLEX=$(shell ls lexicon/*.lexc)
ROOTLEX=$(COMMONLEX) $(shell ls lexicon/$(LEXICON)/*.lexc)
CPP=gcc -E -traditional -P -w -x c
MAKEDEP=gcc -MD
MAKEDEP=./makedepend.sh
TARGETS=kurjmorph.fst 
LEXCSRC=analyzer.lexc morph.lexc
XFSTSRC=analyzer.xfst 
DEPDIR=.dep

%.cpp.lexc: %.lexc $(DEPDIR)/%.lexc.P
	$(CPP) -o $@ $<

%.cpp.xfst: %.xfst $(DEPDIR)/%.xfst.P
	$(CPP) -o $@ $<

$(DEPDIR)/%.lexc.P: %.lexc
	mkdir -p $(DEPDIR)
	$(MAKEDEP) $< $@

$(DEPDIR)/%.xfst.P: %.xfst
	mkdir -p $(DEPDIR)
	$(MAKEDEP) $< $@


analyzer: kurjmorph.fst

all: analyzer 

kurjmorph.fst: analyzer.cpp.xfst analyzer.cpp.lexc 
	foma -f analyzer.cpp.xfst


#
#
#
options.h: options.h-default
	test -e $@ && echo "your $@ may be out of date, you need to update it manually." \
		|| cp $< $@ 

#
# housekeeping goes below
#
clean:
	rm -rf $(TARGETS) *.cpp.* .dep

-include $(LEXCSRC:%.lexc=$(DEPDIR)/%.lexc.P) $(XFSTSRC:%.xfst=$(DEPDIR)/%.xfst.P)
