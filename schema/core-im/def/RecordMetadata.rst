**Computational Definition**

A reusable structure that encapsulates provenance metadata about a serialized data record or object in a particular dataset (as opposed to provenance about the real world entity this record or object represents).

    **Information Model**
    
    .. list-table::
       :class: clean-wrap
       :header-rows: 1
       :align: left
       :widths: auto
       
       *  - Field
          - Type
          - Limits
          - Description
       *  - recordIdentifier
          - string
          - 0..1
          - The business identifier of the record described in the RecordMetadata object (required when the record described is not the one in the present system)
       *  - recordVersion
          - string
          - 0..1
          - The version number of the record-level artifact the object describes.
       *  - derivedFrom
          - string
          - 0..1
          - Another data record from which the record described here was derived.
       *  - dateRecordCreated
          - string
          - 0..1
          - The date the record was initially created.
       *  - contributions
          - :ref:`Contribution`
          - 0..m
          - Describes specific contributions made by an human or software agent to the creation, modification, or administrative management of a data record or object.
