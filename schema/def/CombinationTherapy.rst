**Computational Definition**

A therapeutic procedure that involves multiple different therapeutic procedures  performed in combination.

    **Information Model**
    
Some CombinationTherapy attributes are inherited from :ref:`core:DomainEntity`.

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
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - label
          - string
          - 0..1
          - A primary label for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - extensions
          - `Extension <core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - mappings
          - `Mapping <core.json#/$defs/Mapping>`_
          - 0..m
          - 
       *  - aliases
          - string
          - 0..m
          - Aliases are alternate labels for a Domain Entity.
       *  - type
          - string
          - 1..1
          - MUST be "CombinationTherapy".
       *  - components
          - :ref:`TherapeuticSubstituteGroup` | :ref:`TherapeuticAction` | :ref:`TherapeuticAgent`
          - 2..m
          - The individual therapeutic procedure components that constitute the combination therapy.
