vpath %.yaml jsy

SOURCES := $(wildcard *-source.yaml)
TAGS := $(SOURCES:-source.yaml=.tag)
IMPORTS := $(wildcard imports/*-source.yaml)
CLASS_FILES = $(wildcard *.classes)
CLASSES = $(strip $(shell cat ${CLASS_FILES} | tr "\n" " "))
JSONS = $(CLASSES:%=%.json)

.SECONDARY:
.DELETE_ON_ERROR:

all: ${TAGS}

%.tag: %.json-tag %.defs-tag
	touch $@

%.classes: %-source.yaml
	source2classes.py <$< >$@

%.json-tag: %-source.yaml ${IMPORTS}
	source2splitjs.py $<
	touch $@

%.defs-tag: %-source.yaml ${IMPORTS}
	y2t.py $<
	touch $@

prune:
	echo "Write prune method."

clean:
	rm *.classes
	rm *tag
