**Computational Definition**

An independent, evidence-based argument that may support or refute the validity of a specific proposition. The strength and direction of this argument is based on an interpretation of one or more pieces of information as evidence for or against the target proposition.

**Information Model**

Some EvidenceLine attributes are inherited from :ref:`InformationEntity`.

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
   *  - specifiedBy
      - :ref:`Method` | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..1
      - A specification that describes all or part of the process that led to creation of the Information Entity 
   *  - contributions
      - :ref:`Contribution`
      - 0..m
      - Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
   *  - reportedIn
      - :ref:`Document` | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..m
      - A document in which the the Information Entity is reported.
   *  - dateAuthored
      - string
      - 0..1
      - Indicates when the information content expressed in the Information Entity was generated.
   *  - derivedFrom
      - :ref:`InformationEntity`
      - 0..m
      - Another Information Entity from which this Information Entity is derived, in whole or in part.
   *  - recordMetadata
      - :ref:`RecordMetadata`
      - 0..1
      - Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
   *  - type
      - string
      - 1..1
      - Must be "EvidenceLine"
   *  - hasEvidenceItems
      - :ref:`InformationEntity`
      - 0..m
      - An individual piece of information that was evaluated as evidence in building the argument represented by an Evidence Line.
   *  - directionOfEvidenceProvided
      - string
      - 0..1
      - The direction of support that the Evidence Line is determined to provide toward its target Proposition (supports, disputes, neutral)
   *  - strengthOfEvidenceProvided
      - `Coding </ga4gh/schema/gks-common/1.x/data-types/json/Coding>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..1
      - The strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the directionOfEvidenceProvided value.
   *  - scoreOfEvidenceProvided
      - number
      - 0..1
      - A quantitative score indicating the strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the directionOfEvidenceProvided value.
