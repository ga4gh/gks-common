**Computational Definition**

A collection of data items from a single study that pertain to a particular subject or experimental unit in the study, along with optional provenance information describing how these data items were generated.

**Information Model**

Some StudyResult attributes are inherited from :ref:`InformationEntity`.

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
   *  - recordMetadata
      - :ref:`RecordMetadata`
      - 0..1
      - Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
   *  - focus
      - :ref:`DomainEntity` | `Coding </ga4gh/schema/gks-common/1.x/data-types/json/Coding>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..1
      - The specific subject or experimental unit in a Study that data in the StudyResult object is about - e.g. a particular variant in a population allele frequency dataset like ExAC or gnomAD.
   *  - sourceDataSet
      - :ref:`DataSet`
      - 0..m
      - A larger DataSet from which the content of the StudyResult was derived.
   *  - componentResult
      - :ref:`StudyResult`
      - 0..m
      - Another StudyResult comprised of data items about the same focus as its parent Result, but based on a more narrowly scoped analysis of the foundational data (e.g. an analysis based on data about a subset of the parent Results full study population) .
   *  - studyGroup
      - :ref:`StudyGroup`
      - 0..1
      - A description of a specific group or population of subjects interrogated in the ResearchStudy that produced the data captured in the StudyResult.
   *  - ancillaryResults
      - object
      - 0..1
      - 
   *  - qualityMeasures
      - object
      - 0..1
      - 
