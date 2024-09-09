**Computational Definition**

An autonomous actor (person, organization, or software agent) that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.

**Information Model**

Some Agent attributes are inherited from :ref:`Entity`.

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
   *  - type
      - string
      - 1..1
      - MUST be "Agent".
   *  - name
      - string
      - 0..1
      - The given name of the Agent.
   *  - subtype
      - string
      - 0..1
      - A specific type of agent the Agent object represents. Must be one of {person, organization, software}.
