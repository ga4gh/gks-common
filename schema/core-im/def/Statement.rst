**Computational Definition**

A Statement (aka "Assertion") represents a claim of purported truth as made by a particular agent, on a particular occasion.

**Information Model**

Some Statement attributes are inherited from :ref:`InformationEntity`.

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
      - 1..1
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
      - A specification that describes all or part of the process that led to creation of the  Information Entity (e.g. a specific experimental protocol or data analysis specification  that describe how data were generated, or an evidence interpretation guideline that  describes steps taken to interpret data in making a variant pathogenicity classification).
   *  - contributions
      - :ref:`Contribution`
      - 0..m
      - Specific actions taken by an Agent toward the creation, modification, validation, or  deprecation of an Information Entity.
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
      - Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a  specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
   *  - subject
      - object
      - 1..1
      - The subject of the Statement.
   *  - predicate
      - string
      - 0..1
      - The predicate of the Statement.
   *  - object
      - object
      - 0..1
      - The object of the Statement.
   *  - direction
      - string
      - 1..1
      - The direction of this Statement with respect to the predicate.
   *  - strength
      - `Coding </ga4gh/schema/gks-common/1.x/data-types/json/Coding>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..1
      - A qualitative term indicating the overall strength of support for or against the Statement based on all evidence assessed.
   *  - score
      - number
      - 0..1
      - A quantitative score indicating the overall strength of support for or against the Statement based on all evidence assessed.
   *  - statementText
      - string
      - 0..1
      - A natural-language expression of what a structured Statement object asserts to be true. e.g. for a Variant Pathogenicity statement, "BRCA2 c.8023A>G is pathogenic for Breast Cancer", or "there is moderate evidence supporting the pathogenicity of BRCA2 c.8023A>G for Breast Cancer".
   *  - subjectClassification
      - `Coding </ga4gh/schema/gks-common/1.x/data-types/json/Coding>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's proposition, in terms of a classification of the Statement's subject. Permissible values for this attribute are typically selected to be succinct and familiar in the target community of practice. e.g.  'likely pathogenic' in the domain of variant pathogenicity classification'.
   *  - hasEvidenceLines
      - :ref:`EvidenceLine`
      - 0..m
      - A discrete, independent argument relevant to the validity of the Proposition assessed or put forth in the Statement. This argument is based on the interpretation of one or more pieces of information as evidence. argument is based on the interpretation of one or more pieces of information as evidence.
