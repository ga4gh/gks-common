**Computational Definition**

A structured representation of a code for a defined concept in a terminology or code system.

    **Information Model**
    
    .. list-table::
       :class: clean-wrap
       :header-rows: 1
       :align: left
       :widths: auto
       
       *  - Field
          - Type
          - Limits
          - Description
       *  - label
          - string
          - 0..1
          - The human-readable name for the coded concept, as defined by the code system.
       *  - system
          - string
          - 1..1
          - The terminology/code system that defined the code. May be reported as a free-text name (e.g. 'Sequence Ontology'), but it is preferable to provide a uri/url for the system. When the 'code' is reported as a CURIE, the 'system' should be reported as the uri that the CURIE's prefix expands to (e.g. 'http://purl.obofoundry.org/so.owl/' for the Sequence Ontology).
       *  - version
          - string
          - 0..1
          - Version of the terminology or code system that provided the code.
       *  - code
          - :ref:`Code`
          - 1..1
          - A symbol uniquely identifying the concept, as in a syntax defined by the code system. CURIE format is preferred where possible (e.g. 'SO:0000704' is the CURIE form of the Sequence Ontology code for 'gene').
