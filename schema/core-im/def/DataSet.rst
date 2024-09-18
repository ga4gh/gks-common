**Computational Definition**

A collection of related data items or records that are organized together in a common format or structure, to enable their computational manipulation as a unit.

**Information Model**

Some DataSet attributes are inherited from :ref:`InformationEntity`.

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
   *  - specifiedBy
      - :ref:`Method` | :ref:`IRI`
      - 0..1
      - A specification that describes all or part of the process that led to creation of the Information Entity
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
      - MUST be "DataSet".
   *  - subtype
      - :ref:`Coding`
      - 0..1
      - A specific type of data set the DataSet instance represents (e.g. a 'clinical data set', a 'sequencing data set', a 'gene expression data set', a 'genome annotation data set')
   *  - releaseDate
      - string
      - 0..1
      - Indicates when a version of a Data Set was formally released.
   *  - version
      - string
      - 0..1
      - The version of the Data Set, as assigned by its creator.
   *  - license
      - string
      - 0..1
      - A specific license that dictates legal permissions for how a data set can be used (by whom, where, for what purposes, with what additional requirements, etc.)
