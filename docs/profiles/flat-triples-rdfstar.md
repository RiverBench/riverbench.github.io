# flat-triples-rdfstar (development version)

Flat sequence of triples (with RDF-star)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/profiles/flat-triples-rdfstar.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/profiles/flat-triples-rdfstar.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/profiles/flat-triples-rdfstar.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/profiles/flat-triples-rdfstar.jelly)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Flat sequence of triples (RDF-star) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-triples-rdfstar`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [flat (dev)](https://w3id.org/riverbench/v/dev/categories/flat)
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: [flat-triples (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-triples)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [flat-mixed-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-mixed-rdfstar)
    - [flat-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-mixed-rdfstar-nonstandard)
    - [flat-triples-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-triples-rdfstar-nonstandard)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [assist-iot-weather (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev)
    - [citypulse-traffic (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev)
    - [dbpedia-live (dev)](https://w3id.org/riverbench/datasets/dbpedia-live/dev)
    - [digital-agenda-indicators (dev)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev)
    - [linked-spending (dev)](https://w3id.org/riverbench/datasets/linked-spending/dev)
    - [lod-katrina (dev)](https://w3id.org/riverbench/datasets/lod-katrina/dev)
    - [muziekweb (dev)](https://w3id.org/riverbench/datasets/muziekweb/dev)
    - [politiquices (dev)](https://w3id.org/riverbench/datasets/politiquices/dev)
    - [yago-annotated-facts (dev)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has dataset shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **Property (1)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: yes
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr> ([rb:conformsToRdfStarDraft_20211217](https://w3id.org/riverbench/schema/metadata#conformsToRdfStarDraft_20211217))
        - **Property (2)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**:     
                - <abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr> ([stax:hasStreamType](https://w3id.org/stax/ontology#hasStreamType))
                - <abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr> ([stax:hasStreamTypeUsage](https://w3id.org/stax/ontology#hasStreamTypeUsage))
                - **Path (3)**    
                    - **<abbr title="The (single) value of this property represents a path that is matched zero or more times.">Zero or more path</abbr>**: [http://www.w3.org/2004/02/skos/core#broader](http://www.w3.org/2004/02/skos/core#broader)
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A dataset in the RiverBench benchmark suite">RiverBench dataset</abbr> ([rb:Dataset](https://w3id.org/riverbench/schema/metadata#Dataset))
- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has distribution shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
        - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr> ([rb:hasDistributionType](https://w3id.org/riverbench/schema/metadata#hasDistributionType))
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A distribution of a dataset in the RiverBench benchmark suite.">RiverBench dataset distribution</abbr> ([rb:Distribution](https://w3id.org/riverbench/schema/metadata#Distribution))


## Download links

Below you will find links to download the profile's datasets in different lengths.

!!! warning

    Some datasets are shorter than others and a given distribution may not be available for all datasets.
    In that case, a link to the longest available distribution of the dataset is provided.

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather](https://w3id.org/riverbench/datasets/assist-iot-weather/dev) | [10K (4.72 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/flat_10K.nt.gz) | [100K (47.14 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/flat_100K.nt.gz) | [Full (330.68 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/flat_full.nt.gz) | [Full (330.68 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/flat_full.nt.gz)
[citypulse-traffic](https://w3id.org/riverbench/datasets/citypulse-traffic/dev) | [10K (3.76 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_10K.nt.gz) | [100K (37.59 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_100K.nt.gz) | [1M (375.83 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_1M.nt.gz) | [Full (1.61 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_full.nt.gz)
[dbpedia-live](https://w3id.org/riverbench/datasets/dbpedia-live/dev) | [10K (73.69 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_10K.nt.gz) | [100K (230.12 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_100K.nt.gz) | [Full (282.16 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_full.nt.gz) | [Full (282.16 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_full.nt.gz)
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | [10K (425.32 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/flat_10K.nt.gz) | [100K (4.49 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/flat_100K.nt.gz) | [1M (40.89 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/flat_1M.nt.gz) | [Full (58.25 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/flat_full.nt.gz)
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | [10K (2.00 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/flat_10K.nt.gz) | [100K (17.38 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/flat_100K.nt.gz) | [1M (234.35 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/flat_1M.nt.gz) | [Full (578.85 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/flat_full.nt.gz)
[lod-katrina](https://w3id.org/riverbench/datasets/lod-katrina/dev) | [10K (978.40 KB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_10K.nt.gz) | [100K (13.88 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_100K.nt.gz) | [1M (148.15 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_1M.nt.gz) | [Full (861.85 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_full.nt.gz)
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | [10K (860.15 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/flat_10K.nt.gz) | [100K (8.40 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/flat_100K.nt.gz) | [1M (91.62 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/flat_1M.nt.gz) | [Full (299.99 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/flat_full.nt.gz)
[politiquices](https://w3id.org/riverbench/datasets/politiquices/dev) | [10K (1.65 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_10K.nt.gz) | [Full (2.93 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_full.nt.gz) | [Full (2.93 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_full.nt.gz) | [Full (2.93 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_full.nt.gz)
[yago-annotated-facts](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev) | [10K (256.83 KB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/flat_10K.nt.gz) | [100K (2.38 MB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/flat_100K.nt.gz) | [Full (28.75 MB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/flat_full.nt.gz) | [Full (28.75 MB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/flat_full.nt.gz)