**Computational Definition**

An Entity that is specific to a particular biomedical domain such as disease, therapeutics, or genes. Domain Entities are considered as 'concept-level' entities, as opposed to particular instances. e.g. 'Lung Cancer', not 'patient123's lung cancer'. Or 'Erlotinib', not the particular doses given to a patient on a specific occasion.

    **Information Model**
    
Some DomainEntity attributes are inherited from :ref:`Entity`.

    .. list-table::
       :class: clean-wrap
       :header-rows: 1
       :align: left
       :widths: auto
       
       *  - Field
          - Type
          - Limits
          - Description
       *  - id
          - string
          - 0..1
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - label
          - string
          - 0..1
          - A primary name for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - mappings
          - :ref:`ConceptMapping`
          - 0..m
          - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
       *  - extensions
          - :ref:`Extension`
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - type
          - string
          - 1..1
          - 
       *  - aliases
          - string
          - 0..m
          - Aliases are alternate names for a Domain Entity.
