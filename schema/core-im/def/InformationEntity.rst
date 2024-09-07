**Computational Definition**

An abstract (non-physical) entity that is about something. It represents the abstract 'information content' conveyed by physical or digital information artifacts like books, web pages, data tables, or photographs.

**Information Model**

Some InformationEntity attributes are inherited from :ref:`Entity`.

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
   *  - type
      - string
      - 1..1
      - MUST be "InformationEntity".
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
      - `Extension </ga4gh/schema/gks-common/1.0.0-ballot.2024.08.1/data-types/json/Extension>`_
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - specifiedBy
      - :ref:`Method` | `IRI </ga4gh/schema/gks-common/1.0.0-ballot.2024.08.1/data-types/json/IRI>`_
      - 0..1
      - A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
   *  - contributions
      - :ref:`Contribution`
      - 0..m
      - Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
   *  - reportedIn
      - :ref:`Document` | `IRI </ga4gh/schema/gks-common/1.0.0-ballot.2024.08.1/data-types/json/IRI>`_
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
      - Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
