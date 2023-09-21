Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)  and [RiverBench CI worker](https://github.com/RiverBench/ci-worker)
# RiverBench topic scheme

### A taxonomy


## Metadata
* **URI**
    * `https://w3id.org/riverbench/schema/theme#conceptScheme`
* **Creators(s)**
    * [Piotr Sowiński](https://orcid.org/0000-0002-2543-9461)
    [[0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461)]
* **License**
    * [https://spdx.org/licenses/CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0)



!!! info

    Download this taxonomy in RDF: **[Turtle](https://w3id.org/riverbench/schema/theme/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/schema/theme/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/schema/theme/dev.rdf)**


### Description
Collection of topic concepts used to annotate RiverBench datasets.



## Table of Contents
1. [Object Concepts](#concepts)
1. [Namespaces](#namespaces)
1. [Legend](#legend)




## Concepts
* [Root concept](#rootConcept) (con)
* [Data type](#dataType) (con)
* [Spatial](#spatial) (con)
* [Temporal](#temporal) (con)
* [Domain](#domain) (con)
* [Abstract data](#abstract) (con)
* [Bibliographical](#bibliographical) (con)
* [Encyclopedic](#encyclopedic) (con)
* [Government](#government) (con)
* [Meteorological](#meteorological) (con)
* [Musical](#musical) (con)
* [News](#news) (con)
* [Political](#political) (con)
* [Scientific](#scientific) (con)
* [Biomedical](#biomedical) (con)
* [Sensor data](#sensorData) (con)
* [Statistical](#statistical) (con)

### Abstract data <a name="abstract"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#abstract`
Preferred Labels |Abstract data (en)<br />
Definitions |Datasets with abstract information (unrelated to the real world).<br />
Broader Concepts |[Domain](#domain) (con)<br />

### Bibliographical <a name="bibliographical"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#bibliographical`
Preferred Labels |Bibliographical (en)<br />
Definitions |Datasets with bibliographical information.<br />
Broader Concepts |[Domain](#domain) (con)<br />

### Biomedical <a name="biomedical"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#biomedical`
Preferred Labels |Biomedical (en)<br />
Definitions |Datasets with biomedical information.<br />
Broader Concepts |[Scientific](#scientific) (con)<br />

### Data type <a name="dataType"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#dataType`
Preferred Labels |Data type (en)<br />
Definitions |Datasets by types of data used.<br />
Broader Concepts |[Root concept](#rootConcept) (con)<br />
Narrower Concepts |[Temporal](#temporal) (con)<br />[Spatial](#spatial) (con)<br />

### Domain <a name="domain"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#domain`
Preferred Labels |Domain (en)<br />
Definitions |Datasets by domain.<br />
Broader Concepts |[Root concept](#rootConcept) (con)<br />
Narrower Concepts |[Abstract data](#abstract) (con)<br />[Scientific](#scientific) (con)<br />[Sensor data](#sensorData) (con)<br />[Musical](#musical) (con)<br />[Encyclopedic](#encyclopedic) (con)<br />[Political](#political) (con)<br />[Government](#government) (con)<br />[Statistical](#statistical) (con)<br />[News](#news) (con)<br />[Meteorological](#meteorological) (con)<br />[Bibliographical](#bibliographical) (con)<br />

### Encyclopedic <a name="encyclopedic"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#encyclopedic`
Preferred Labels |Encyclopedic (en)<br />
Definitions |Datasets with encyclopedic information.<br />
Broader Concepts |[Domain](#domain) (con)<br />

### Government <a name="government"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#government`
Preferred Labels |Government (en)<br />
Definitions |Datasets with information on governments or produced by governments.<br />
Broader Concepts |[Domain](#domain) (con)<br />

### Meteorological <a name="meteorological"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#meteorological`
Preferred Labels |Meteorological (en)<br />
Definitions |Datasets with meteorological information.<br />
Broader Concepts |[Domain](#domain) (con)<br />

### Musical <a name="musical"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#musical`
Preferred Labels |Musical (en)<br />
Definitions |Datasets with information about music.<br />
Broader Concepts |[Domain](#domain) (con)<br />

### News <a name="news"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#news`
Preferred Labels |News (en)<br />
Definitions |Datasets with news information.<br />
Broader Concepts |[Domain](#domain) (con)<br />

### Political <a name="political"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#political`
Preferred Labels |Political (en)<br />
Definitions |Datasets with political information.<br />
Broader Concepts |[Domain](#domain) (con)<br />

### Root concept <a name="rootConcept"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#rootConcept`
Preferred Labels |Root concept (en)<br />
Narrower Concepts |[Data type](#dataType) (con)<br />[Domain](#domain) (con)<br />

### Scientific <a name="scientific"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#scientific`
Preferred Labels |Scientific (en)<br />
Definitions |Datasets with scientific information.<br />
Broader Concepts |[Domain](#domain) (con)<br />
Narrower Concepts |[Biomedical](#biomedical) (con)<br />

### Sensor data <a name="sensorData"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#sensorData`
Preferred Labels |Sensor data (en)<br />
Definitions |Datasets with data from sensors, sensor networks, IoT devices, etc.<br />
Broader Concepts |[Domain](#domain) (con)<br />

### Spatial <a name="spatial"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#spatial`
Preferred Labels |Spatial (en)<br />
Definitions |Datasets with spatial information.<br />
Broader Concepts |[Data type](#dataType) (con)<br />

### Statistical <a name="statistical"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#statistical`
Preferred Labels |Statistical (en)<br />
Definitions |Datasets with statistical information.<br />
Broader Concepts |[Domain](#domain) (con)<br />

### Temporal <a name="temporal"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/theme#temporal`
Preferred Labels |Temporal (en)<br />
Definitions |Datasets with temporal information.<br />
Broader Concepts |[Data type](#dataType) (con)<br />


## Namespaces
* **default (rbt)**
    * `https://w3id.org/riverbench/schema/theme#`
* **dcterms**
    * `http://purl.org/dc/terms/`
* **foaf**
    * `http://xmlns.com/foaf/0.1/`
* **skos**
    * `http://www.w3.org/2004/02/skos/core#`
* **vann**
    * `http://purl.org/vocab/vann/`


## Legend
* Collections: col
* Concepts: con