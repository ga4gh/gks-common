vpath %.yaml jsy

SOURCES := $(wildcard *-source.yaml)
TAGS := $(SOURCES:-source.yaml=.tag)
IMPORTS := $(wildcard imports/*-source.yaml)
CLASS_FILES = $(wildcard *.classes)
CLASSES = $(strip $(shell cat ${CLASS_FILES} | tr "\n" " "))
JSONS = $(CLASSES:%=%.json)

all: ${TAGS}

%.tag: %.classes %.yaml-tag %.json-tag %.defs-tag prune
	touch $@

%.classes: %-source.yaml
	source2classes.py <$<

%.yaml-tag: %-source.yaml ${IMPORTS}
	source2jsy.py <$< --out jsy
	touch $@

%.defs-tag: %-source.yaml ${IMPORTS}
	y2t.py <$< --out defs
	touch $@

%.json-tag: ${JSONS}
	touch $@

%.json: jsy/%.yaml
	jsy2js.py <$< >json/$@

prune:
	echo "Write prune method."

clean:
	rm *.classes
	rm *tag
