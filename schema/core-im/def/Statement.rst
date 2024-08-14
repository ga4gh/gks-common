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
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
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
      - A free-text description of the entity.
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - `Extension </ga4gh/schema/gks-common/1.x/data-types/json/Extension>`_
      - 0..m
      - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
   *  - specifiedBy
      - :ref:`Method` | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..1
      - A :ref:`Method` that describes all or part of the process through which the information was generated.
   *  - contributions
      - :ref:`Contribution`
      - 0..m
      - A list of :ref:`Contribution` objects that describe the activities performed by agents upon this entity.
   *  - isReportedIn
      - :ref:`Document` | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..m
      - A document in which the information content is expressed.
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
      - Metadata that applies to a specific concrete record of information as encoded in a particular system.
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
