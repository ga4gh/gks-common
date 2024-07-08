all: gks-common gks-domain-entities
	
gks-domain-entities: 
	(cd domain-entities; make all)

gks-common:
	(cd common; make all)

clean:
	(cd common; make clean)
	(cd domain-entities; make clean)
