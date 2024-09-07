**Computational Definition**

An action or set of actions performed by an agent, that occurs over a period of time. Activities may use, generate, modify, move, or destroy one or more entities.

**Information Model**

Some Activity attributes are inherited from :ref:`Entity`.

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
      - The name of the class that is instantiated by a data object representing the Entity.
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
   *  - subtype
      - {'$ref': '/ga4gh/schema/gks-common/1.x/data-types/json/Coding'}
      - 0..1
      - A specific type of activity the Activity instance represents.
   *  - date
      - string
      - 0..1
      - The date that the Activity was completed.
   *  - performedBy
      - :ref:`Agent`
      - 0..m
      - An Agent who participated in executing the Activity.
   *  - specifiedBy
      - :ref:`Method`
      - 0..m
      - A method that was followed in performing an Activity, that describes how it was executed.
