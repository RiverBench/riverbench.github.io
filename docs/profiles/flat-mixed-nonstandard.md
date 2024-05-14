# flat-mixed-nonstandard (development version)

Flat sequence of triples or quads (with non-standard extensions)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/profiles/flat-mixed-nonstandard.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/profiles/flat-mixed-nonstandard.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/profiles/flat-mixed-nonstandard.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/profiles/flat-mixed-nonstandard.jelly)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Flat sequence of triples or quads (non-standard) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-mixed-nonstandard`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [flat (dev)](https://w3id.org/riverbench/v/dev/categories/flat)
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: 
    - [flat-mixed (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-mixed)
    - [flat-quads (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-quads)
    - [flat-quads-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-quads-nonstandard)
    - [flat-triples (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-triples)
    - [flat-triples-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-triples-nonstandard)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: [flat-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-mixed-rdfstar-nonstandard)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [assist-iot-weather (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev)
    - [assist-iot-weather-graphs (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev)
    - [citypulse-traffic (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev)
    - [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)
    - [dbpedia-live (dev)](https://w3id.org/riverbench/datasets/dbpedia-live/dev)
    - [digital-agenda-indicators (dev)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev)
    - [linked-spending (dev)](https://w3id.org/riverbench/datasets/linked-spending/dev)
    - [lod-katrina (dev)](https://w3id.org/riverbench/datasets/lod-katrina/dev)
    - [muziekweb (dev)](https://w3id.org/riverbench/datasets/muziekweb/dev)
    - [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
    - [politiquices (dev)](https://w3id.org/riverbench/datasets/politiquices/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has dataset shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **Property (1)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="A flat RDF stream is an RDF stream whose elements are statements (either RDF triples or RDF quads).">Flat RDF stream</abbr> ([stax:flatStream](https://w3id.org/stax/ontology#flatStream))
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**:     
                - <abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr> ([stax:hasStreamType](https://w3id.org/stax/ontology#hasStreamType))
                - <abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr> ([stax:hasStreamTypeUsage](https://w3id.org/stax/ontology#hasStreamTypeUsage))
                - **Path (3)**    
                    - **<abbr title="The (single) value of this property represents a path that is matched zero or more times.">Zero or more path</abbr>**: [http://www.w3.org/2004/02/skos/core#broader](http://www.w3.org/2004/02/skos/core#broader)
        - **Property (2)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: no
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr> ([rb:usesRdfStar](https://w3id.org/riverbench/schema/metadata#usesRdfStar))
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
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | [10K (5.07 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_10K.nq.gz) | [100K (50.58 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_100K.nq.gz) | [Full (354.64 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_full.nq.gz) | [Full (354.64 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_full.nq.gz)
[citypulse-traffic](https://w3id.org/riverbench/datasets/citypulse-traffic/dev) | [10K (3.76 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_10K.nt.gz) | [100K (37.58 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_100K.nt.gz) | [1M (375.83 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_1M.nt.gz) | [Full (1.61 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_full.nt.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (3.96 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_10K.nq.gz) | [100K (39.69 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_100K.nq.gz) | [1M (395.98 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_1M.nq.gz) | [Full (1.69 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_full.nq.gz)
[dbpedia-live](https://w3id.org/riverbench/datasets/dbpedia-live/dev) | [10K (73.69 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_10K.nt.gz) | [100K (230.12 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_100K.nt.gz) | [Full (282.16 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_full.nt.gz) | [Full (282.16 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_full.nt.gz)
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | [10K (425.32 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/flat_10K.nt.gz) | [100K (4.49 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/flat_100K.nt.gz) | [1M (40.89 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/flat_1M.nt.gz) | [Full (58.25 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/flat_full.nt.gz)
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | [10K (2.00 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/flat_10K.nt.gz) | [100K (17.39 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/flat_100K.nt.gz) | [1M (234.35 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/flat_1M.nt.gz) | [Full (578.85 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/flat_full.nt.gz)
[lod-katrina](https://w3id.org/riverbench/datasets/lod-katrina/dev) | [10K (978.40 KB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_10K.nt.gz) | [100K (13.88 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_100K.nt.gz) | [1M (148.15 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_1M.nt.gz) | [Full (861.85 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_full.nt.gz)
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | [10K (860.15 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/flat_10K.nt.gz) | [100K (8.40 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/flat_100K.nt.gz) | [1M (91.62 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/flat_1M.nt.gz) | [Full (299.99 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/flat_full.nt.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | [10K (3.47 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_10K.nq.gz) | [100K (35.73 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_100K.nq.gz) | [1M (384.61 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_1M.nq.gz) | [Full (1.68 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_full.nq.gz)
[politiquices](https://w3id.org/riverbench/datasets/politiquices/dev) | [10K (1.65 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_10K.nt.gz) | [Full (2.93 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_full.nt.gz) | [Full (2.93 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_full.nt.gz) | [Full (2.93 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_full.nt.gz)