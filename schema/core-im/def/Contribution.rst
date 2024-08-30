**Computational Definition**

An action taken by an agent in contributing to the creation, modification, assessment, or deprecation of a particular entity (e.g. a Statement, EvidenceLine, DataItem, Publication, etc.)

**Information Model**

Some Contribution attributes are inherited from :ref:`Activity`.

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
      - `Extension </ga4gh/schema/gks-common/1.x/data-types/json/Extension>`_
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model. 
   *  - subtype
      - {'$ref': '/ga4gh/schema/gks-common/1.x/data-types/json/Coding'}
      - 0..1
      - A specific type of data set the Activity instance represents (e.g. 'research activity',  clinical activity', curation activity')
   *  - date
      - string
      - 0..1
      - The date that the Activity was completed. 
   *  - specifiedBy
      - :ref:`Method`
      - 0..m
      - A method that was followed in performing an Activity, that describes how it was executed.
   *  - type
      - string
      - 1..1
      - MUST be "Contribution".
   *  - contributor
      - :ref:`Agent`
      - 1..1
      - The agent that made the contribution.
   *  - activityType
      - `Coding </ga4gh/schema/gks-common/1.x/data-types/json/Coding>`_
      - 0..1
      - The type of activity performed or role realized in making the contribution. MAY use terms from the Contributor Role Ontology (https://www.ebi.ac.uk/ols4/ontologies/cro), e.g. 'author role', 'evaluator role', 'data collection role'.
