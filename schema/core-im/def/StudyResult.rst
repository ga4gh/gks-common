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
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - specifiedBy
      - :ref:`Method` | :ref:`IRI`
      - 0..1
      - A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
   *  - contributions
      - :ref:`Contribution`
      - 0..m
      - Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
   *  - reportedIn
      - :ref:`Document` | :ref:`IRI`
      - 0..m
      - A document in which the the Information Entity is reported.
   *  - dateAuthored
      - string
      - 0..1
      - Indicates when the information content expressed in the Information Entity was generated.
   *  - recordMetadata
      - :ref:`RecordMetadata`
      - 0..1
      - Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
   *  - focus
      - :ref:`DomainEntity` | :ref:`Coding` | :ref:`IRI`
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
