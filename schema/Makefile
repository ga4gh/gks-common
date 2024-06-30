all: gks-core gks-domain-entities
	
gks-domain-entities: 
	(cd domain-entities; make all)

gks-core:
	(cd core-im; make all)

clean:
	(cd core-im; make clean)
	(cd domain-entities; make clean)
