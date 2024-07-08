all: gks-commons gks-domain-entities
	
gks-domain-entities: 
	(cd domain-entities; make all)

gks-commons:
	(cd commons; make all)

clean:
	(cd commons; make clean)
	(cd domain-entities; make clean)
