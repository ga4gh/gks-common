.PHONY: defs FORCE
.SECONDARY:
.SUFFIXES:
.DELETE_ON_ERROR:

JSYAMLS:=gks.common.yaml
JSONS:=${JSYAMLS:.yaml=.json}

all: ${JSONS} defs

%.json: %.yaml
	jsy2js.py <$< >$@

%.yaml: %-source.yaml
	source2jsy.py $< >$@

defs:
	rm -rf defs
	y2t.py gks.common-source.yaml

watch:
	-while true; do ls -1 *.yaml | entr -dn make ${JSONS}; done
