**Computational Definition**

An object holding a name-value pair used to describe a trait or role of an individual member of a StudyGroup.

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
   *  - name
      - string
      - 1..1
      - The type of the trait  or role described by the trait (e.g. 'ethnicity', 'sex', 'age', 'disease status').
   *  - value
      - string
      - 1..1
      - The specific value(s) that the indicated traitor role holds in all population members (e.g. 'east asian', 'female', 'adolescent', 'cancer').
   *  - valueOperator
      - boolean
      - 0..1
      - An operation that defines how to logically interpret a set of more than one Characteristic values ('AND', 'OR', 'NOT')
