# gks-common

Common classes and schemas used by all GKS specifications (ie. VR, Cat-VRS, VA, etc..)

For more info
[GKS Repository Organization](https://docs.google.com/document/d/16SrjqPJ1ct_z8OK6kNcu3KO1ia6LAyVriSbuDLXRAI8/edit)

## Installing for development

Fork the repo at <https://github.com/ga4gh/gks-common>.

    git clone git@github.com:YOUR_GITHUB_ID/gks-common.git
    cd gks-common
    make devready
    source venv/3.12/bin/activate
    pre-commit install

## Contributing to the schema

GKS Common uses the following source documents for JSON Schema:

* [core-im/core-im-source.yaml](./schema/gks-common/core-im/core-im-source.yaml)
* [domain-entities-source.yaml](./schema/gks-common/domain-entities/domain-entities-source.yaml)

To create the corresponding def and json files after making changes to any of of the
source documents, from the root directory:

    cd schema
    make all

> _Note: We have a custom pre-commit hook to run these commands after you stage a source
> document_

## Testing

To run the tests:

    (from the root directory of the project)
    make test
