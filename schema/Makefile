vpath %tag build
vpath %.classes build

SOURCES := $(wildcard *-source.yaml)
TAGS := $(SOURCES:-source.yaml=.tag)
BUILD_DIR := build/
IMPORTS := $(wildcard imports/*-source.yaml)
CLASS_FILTER_FILES = $(wildcard ${BUILD_DIR}*.classes)
FILTER_CLASSES = $(shell cat ${CLASS_FILTER_FILES})
FILTER_JSONS = $(FILTER_CLASSES:%=json/%.json)
FILTER_DEFS = $(FILTER_CLASSES:%=def/%.rst)


.SECONDARY:
.DELETE_ON_ERROR:

all: build-ordered ${TAGS} prune

build-ordered: | $(BUILD_DIR)

build:
	mkdir $(BUILD_DIR)

%.tag: %.json-tag %.defs-tag
	touch $(BUILD_DIR)$@

%.classes: %-source.yaml
	source2classes.py <$< >$(BUILD_DIR)$@

%.json-tag: %-source.yaml ${IMPORTS}
	source2splitjs.py $<
	touch $(BUILD_DIR)$@

%.defs-tag: %-source.yaml ${IMPORTS}
	y2t.py $<
	touch $(BUILD_DIR)$@

prune: $(filter-out ${FILTER_JSONS} ${FILTER_DEFS},$(wildcard def/* json/*))
	rm $^

clean:
	rm $(BUILD_DIR)*
