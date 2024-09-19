<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/schema/documentation/dev "Link to the permanent URL of this resource.")</div><div markdown>**[:material-database-edit: Edit ontology](https://github.com/RiverBench/schema/edit/main/src/documentation.ttl "Edit this page's ontology in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../documentation/editing-docs.md "Need help with editing?")</div></div>

Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.13.2 and [RiverBench CI worker](https://github.com/RiverBench/ci-worker).
# RiverBench documentation ontology


## Metadata
* **URI**
    * `https://w3id.org/riverbench/schema/documentation`
* **Creators(s)**
    * [Piotr Sowiński](https://orcid.org/0000-0002-2543-9461)
    [[0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461)]
* **Created**
    * 2023-04-30T00:00:00
* **Issued**
    * 2023-05-05T00:00:00
* **Version URI**
    * [https://w3id.org/riverbench/schema/documentation/dev](https://w3id.org/riverbench/schema/documentation/dev)
* **Imports**
    * [https://w3id.org/riverbench/schema/metadata/dev](https://w3id.org/riverbench/schema/metadata/dev)
* **License**
    * [https://spdx.org/licenses/CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0)


!!! info

    :fontawesome-solid-diagram-project: Download this ontology in RDF: **[Turtle](https://w3id.org/riverbench/schema/documentation/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/schema/documentation/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/schema/documentation/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/schema/documentation/dev.jelly)**
    <br>:material-github: Source repository: **[schema](https://github.com/RiverBench/schema)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/schema/documentation/dev`](https://w3id.org/riverbench/schema/documentation/dev)


### Description
Ontology with metadata needed to generate documentation of datasets, distributions, profiles, etc. in RiverBench


## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#object-properties)
1. [Annotation Properties](#annotationproperties)
1. [Named Individuals](#named-individuals)
1. [Namespaces](#namespaces)
1. [Legend](#legend)




## Classes
* [Documentation group](#DocGroup)

### Documentation group <a name="DocGroup"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/documentation#DocGroup`
Description | Documentation group, corresponding to a heading in the generated document.
In range of |[Has documentation group](#hasDocGroup) (ap)<br />
Has members |[Content](#groupContent)<br />[Distributions](#groupDistributions)<br />[Technical metadata](#groupTechnicalMetadata)<br />[General information](#groupGeneralInfo)<br />


## Object Properties
[hasMeasuringSystem](#hasMeasuringSystem),
[hasProducedDataset](#hasProducedDataset),
[citesAsDataSource](#citesAsDataSource),
[vocabulary](#vocabulary),
[dataset](#dataset),
[In suite](#inCatalog),

### hasMeasuringSystem <a name="hasMeasuringSystem"></a>
Property | Value
--- | ---
URI | `http://ontology.ethereal.cz/irao/hasMeasuringSystem`

### hasProducedDataset <a name="hasProducedDataset"></a>
Property | Value
--- | ---
URI | `http://ontology.ethereal.cz/irao/hasProducedDataset`

### citesAsDataSource <a name="citesAsDataSource"></a>
Property | Value
--- | ---
URI | `http://purl.org/spar/cito/citesAsDataSource`

### vocabulary <a name="vocabulary"></a>
Property | Value
--- | ---
URI | `http://rdfs.org/ns/void#vocabulary`
Description | A vocabulary that is used in the dataset.

### dataset <a name="dataset"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#dataset`

### In suite <a name="inCatalog"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#inCatalog`
Description | Indicates the benchmark suite to which a dataset or profile belongs


## Annotation Properties
[conformsTo](#conformsTo),
[contributor](#contributor),
[creator](#creator),
[description](#description),
[identifier](#identifier),
[issued](#issued),
[license](#license),
[modified](#modified),
[rights](#rights),
[source](#source),
[title](#title),
[checksum](#checksum),
[type](#type),
[byteSize](#byteSize),
[compressFormat](#compressFormat),
[distribution](#distribution),
[downloadUrl](#downloadUrl),
[landingPage](#landingPage),
[mediaType](#mediaType),
[packageFormat](#packageFormat),
[temporalResolution](#temporalResolution),
[theme](#theme),
[themeTaxonomy](#themeTaxonomy),
[homepage](#homepage),
[name](#name),
[nick](#nick),
[Has documentation group](#hasDocGroup),
[Has documentation weight](#hasDocWeight),
[Has label override](#hasLabelOverride),
[Is hidden in documentation](#isHiddenInDoc),

### conformsTo <a name="conformsTo"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/conformsTo`

### contributor <a name="contributor"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/contributor`

### creator <a name="creator"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/creator`

### description <a name="description"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/description`

### identifier <a name="identifier"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/identifier`

### issued <a name="issued"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/issued`

### license <a name="license"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/license`

### modified <a name="modified"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/modified`

### rights <a name="rights"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/rights`

### source <a name="source"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/source`

### title <a name="title"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/title`

### checksum <a name="checksum"></a>
Property | Value
--- | ---
URI | `http://spdx.org/rdf/terms#checksum`

### type <a name="type"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`

### byteSize <a name="byteSize"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#byteSize`

### compressFormat <a name="compressFormat"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#compressFormat`

### distribution <a name="distribution"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#distribution`

### downloadUrl <a name="downloadUrl"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#downloadUrl`

### landingPage <a name="landingPage"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#landingPage`

### mediaType <a name="mediaType"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#mediaType`

### packageFormat <a name="packageFormat"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#packageFormat`

### temporalResolution <a name="temporalResolution"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#temporalResolution`

### theme <a name="theme"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#theme`

### themeTaxonomy <a name="themeTaxonomy"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#themeTaxonomy`

### homepage <a name="homepage"></a>
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/homepage`

### name <a name="name"></a>
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/name`

### nick <a name="nick"></a>
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/nick`

### Has documentation group <a name="hasDocGroup"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/documentation#hasDocGroup`
Description | Indicates the documentation group (heading) of a property
Range(s) |[Documentation group](#DocGroup) (c)<br />

### Has documentation weight <a name="hasDocWeight"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/documentation#hasDocWeight`
Description | Weight of a given property or item when generating documentation (integer). Properties or items with lower values will be shown first in the generated docs.
Range(s) |[xsd:int](http://www.w3.org/2001/XMLSchema#int) (c)<br />

### Has label override <a name="hasLabelOverride"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/documentation#hasLabelOverride`
Description | Top-priority label to be used in documentation pages.

### Is hidden in documentation <a name="isHiddenInDoc"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/documentation#isHiddenInDoc`
Description | Whether a given property should be omitted in the generated documentation.
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />


## Named Individuals
[Content](#groupContent),
[Distributions](#groupDistributions),
[General information](#groupGeneralInfo),
[Technical metadata](#groupTechnicalMetadata),

### Content <a name="groupContent"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/documentation#groupContent`
Class(es) | [Documentation group](#DocGroup)

### Distributions <a name="groupDistributions"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/documentation#groupDistributions`
Class(es) | [Documentation group](#DocGroup)

### General information <a name="groupGeneralInfo"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/documentation#groupGeneralInfo`
Class(es) | [Documentation group](#DocGroup)

### Technical metadata <a name="groupTechnicalMetadata"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/documentation#groupTechnicalMetadata`
Class(es) | [Documentation group](#DocGroup)

## Namespaces
* **default (rbdoc)**
    * `https://w3id.org/riverbench/schema/documentation#`
* **cito**
    * `http://purl.org/spar/cito/`
* **dc**
    * `http://purl.org/dc/elements/1.1/`
* **dcat**
    * `http://www.w3.org/ns/dcat#`
* **dcterms**
    * `http://purl.org/dc/terms/`
* **foaf**
    * `http://xmlns.com/foaf/0.1/`
* **irao**
    * `http://ontology.ethereal.cz/irao/`
* **owl**
    * `http://www.w3.org/2002/07/owl#`
* **rb**
    * `https://w3id.org/riverbench/schema/metadata#`
* **rdf**
    * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
    * `http://www.w3.org/2000/01/rdf-schema#`
* **spdx**
    * `http://spdx.org/rdf/terms#`
* **vann**
    * `http://purl.org/vocab/vann/`
* **void**
    * `http://rdfs.org/ns/void#`
* **xsd**
    * `http://www.w3.org/2001/XMLSchema#`


## Legend
* Classes: c
* Object Properties: op
* Functional Properties: fp
* Data Properties: dp
* Annotation Properties: ap
* Properties: p
* Named Individuals: ni