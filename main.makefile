ALL_FIGURE_NAMES=$(shell cat main.figlist)
ALL_FIGURES=$(ALL_FIGURE_NAMES:%=%.pdf)

allimages: $(ALL_FIGURES)
	@echo All images exist now. Use make -B to re-generate them.

FORCEREMAKE:

-include $(ALL_FIGURE_NAMES:%=%.dep)

%.dep:
	mkdir -p "$(dir $@)"
	touch "$@" # will be filled later.

./tikzfigs/main-figure0.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "./tikzfigs/main-figure0" "\def\tikzexternalrealjob{main}\input{main}"

./tikzfigs/main-figure0.pdf: ./tikzfigs/main-figure0.md5
./tikzfigs/main-figure1.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "./tikzfigs/main-figure1" "\def\tikzexternalrealjob{main}\input{main}"

./tikzfigs/main-figure1.pdf: ./tikzfigs/main-figure1.md5
./tikzfigs/main-figure2.pdf: 
	pdflatex -halt-on-error -interaction=batchmode -jobname "./tikzfigs/main-figure2" "\def\tikzexternalrealjob{main}\input{main}"

./tikzfigs/main-figure2.pdf: ./tikzfigs/main-figure2.md5
