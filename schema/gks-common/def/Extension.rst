**Computational Definition**

The Extension class provides entities with a means to include additional attributes that are outside of the specified standard but needed by a given content provider or system implementer. These extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.

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
       *  - type
          - string
          - 0..1
          - MUST be "Extension".
       *  - name
          - string
          - 1..1
          - A name for the Extension
       *  - value
          - ['number', 'string', 'boolean', 'object', 'array', 'null']
          - 0..1
          - Any primitive or structured object
