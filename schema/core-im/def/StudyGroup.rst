**Computational Definition**

A collection of individuals or specimens from the same taxonomic class, selected for analysis in a scientific study based on their exhibiting one or more common characteristics  (e.g. species, race, age, gender, disease state, income). May be referred to as a 'cohort' or 'population' in specific research settings.

**Information Model**

Some StudyGroup attributes are inherited from :ref:`Entity`.

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
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - label
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - type
      - string
      - 1..1
      - Must be "StudyGroup"
   *  - memberCount
      - integer
      - 0..1
      - The total number of individual members in the StudyGroup.
   *  - isSubsetOf
      - :ref:`StudyGroup`
      - 0..m
      - A larger StudyGroup of which this StudyGroup represents a subset.
   *  - characteristics
      - :ref:`Characteristic`
      - 0..m
      - A feature or role shared by all members of the StudyGroup, representing a criterion for membership in the group.
