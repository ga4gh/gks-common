all: gks-data-types gks-core-im gks-domain-entities
	
gks-data-types:
	(cd data-types; make all)

gks-core-im:
	(cd core-im; make all)

gks-domain-entities: 
	(cd domain-entities; make all)

clean:
	(cd data-types; make clean)
	(cd core-im; make clean)
	(cd domain-entities; make clean)
