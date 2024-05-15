# stream-mixed-rdfstar (development version)

Streaming graphs or datasets (with RDF-star)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar.jelly)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming graphs or datasets (RDF-star) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-mixed-rdfstar`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [stream (dev)](https://w3id.org/riverbench/v/dev/categories/stream)
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: 
    - [stream-datasets (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-datasets)
    - [stream-datasets-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar)
    - [stream-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-graphs)
    - [stream-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-graphs-rdfstar)
    - [stream-mixed (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed)
    - [stream-named-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-named-graphs)
    - [stream-named-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-named-graphs-rdfstar)
    - [stream-subject-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs)
    - [stream-subject-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs-rdfstar)
    - [stream-ts-named-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-ts-named-graphs)
    - [stream-ts-named-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-ts-named-graphs-rdfstar)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar-nonstandard)
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
    - [yago-annotated-facts (dev)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has dataset shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **Property (1)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="A grouped RDF stream is an RDF stream whose elements are either RDF graphs or RDF datasets.">Grouped RDF stream</abbr> ([stax:groupedStream](https://w3id.org/stax/ontology#groupedStream))
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**:     
                - <abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr> ([stax:hasStreamType](https://w3id.org/stax/ontology#hasStreamType))
                - <abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr> ([stax:hasStreamTypeUsage](https://w3id.org/stax/ontology#hasStreamTypeUsage))
                - **Path (3)**    
                    - **<abbr title="The (single) value of this property represents a path that is matched zero or more times.">Zero or more path</abbr>**: [http://www.w3.org/2004/02/skos/core#broader](http://www.w3.org/2004/02/skos/core#broader)
        - **Property (2)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: yes
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr> ([rb:conformsToRdfStarDraft_20211217](https://w3id.org/riverbench/schema/metadata#conformsToRdfStarDraft_20211217))
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A dataset in the RiverBench benchmark suite">RiverBench dataset</abbr> ([rb:Dataset](https://w3id.org/riverbench/schema/metadata#Dataset))
- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has distribution shape</abbr>**: 
    - **<abbr title="Specifies a list of shapes so that the value nodes must conform to at least one of the shapes.">Or</abbr>**:     
        - **Or (1)**    
            - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
                - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
                - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr> ([rb:hasDistributionType](https://w3id.org/riverbench/schema/metadata#hasDistributionType))
        - **Or (2)**    
            - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
                - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
                - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr> ([rb:hasDistributionType](https://w3id.org/riverbench/schema/metadata#hasDistributionType))
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A distribution of a dataset in the RiverBench benchmark suite.">RiverBench dataset distribution</abbr> ([rb:Distribution](https://w3id.org/riverbench/schema/metadata#Distribution))


## Download links

Below you will find links to download the profile's datasets in different lengths.

!!! warning

    Some datasets are shorter than others and a given distribution may not be available for all datasets.
    In that case, a link to the longest available distribution of the dataset is provided.

!!! note

    For stream profiles, there are two available types of distributions: plain streaming, and streaming in the Jelly format. See the [documentation](../documentation/dataset-release-format.md) for details.

### Plain streaming distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather](https://w3id.org/riverbench/datasets/assist-iot-weather/dev) | [10K (2.34 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/stream_10K.tar.gz) | [100K (23.29 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/stream_100K.tar.gz) | [Full (163.33 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/stream_full.tar.gz) | [Full (163.33 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/stream_full.tar.gz)
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | [10K (1.31 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_10K.tar.gz) | [100K (13.01 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_100K.tar.gz) | [Full (91.26 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz) | [Full (91.26 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz)
[citypulse-traffic](https://w3id.org/riverbench/datasets/citypulse-traffic/dev) | [10K (1.89 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_10K.tar.gz) | [100K (18.73 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_100K.tar.gz) | [1M (187.36 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_1M.tar.gz) | [Full (820.70 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_full.tar.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (2.06 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_10K.tar.gz) | [100K (20.35 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_100K.tar.gz) | [1M (204.32 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_1M.tar.gz) | [Full (902.25 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_full.tar.gz)
[dbpedia-live](https://w3id.org/riverbench/datasets/dbpedia-live/dev) | [10K (66.88 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_10K.tar.gz) | [100K (209.48 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_100K.tar.gz) | [Full (256.92 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_full.tar.gz) | [Full (256.92 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_full.tar.gz)
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | [10K (316.79 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_10K.tar.gz) | [100K (3.60 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_100K.tar.gz) | [1M (32.46 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_1M.tar.gz) | [Full (46.28 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_full.tar.gz)
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | [10K (1.26 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_10K.tar.gz) | [100K (10.11 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_100K.tar.gz) | [1M (140.17 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_1M.tar.gz) | [Full (346.64 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_full.tar.gz)
[lod-katrina](https://w3id.org/riverbench/datasets/lod-katrina/dev) | [10K (727.78 KB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_10K.tar.gz) | [100K (9.62 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_100K.tar.gz) | [1M (102.03 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_1M.tar.gz) | [Full (594.38 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_full.tar.gz)
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | [10K (862.16 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_10K.tar.gz) | [100K (8.41 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_100K.tar.gz) | [1M (87.39 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_1M.tar.gz) | [Full (252.23 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_full.tar.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | [10K (2.55 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz) | [100K (25.59 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz) | [1M (277.17 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz) | [Full (1.02 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz)
[politiquices](https://w3id.org/riverbench/datasets/politiquices/dev) | [10K (1.38 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_10K.tar.gz) | [Full (2.46 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_full.tar.gz) | [Full (2.46 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_full.tar.gz) | [Full (2.46 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_full.tar.gz)
[yago-annotated-facts](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev) | [10K (376.45 KB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/stream_10K.tar.gz) | [100K (3.57 MB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/stream_100K.tar.gz) | [Full (36.16 MB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/stream_full.tar.gz) | [Full (36.16 MB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/stream_full.tar.gz)

### Jelly streaming distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather](https://w3id.org/riverbench/datasets/assist-iot-weather/dev) | [10K (1.55 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/jelly_10K.jelly.gz) | [100K (15.39 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/jelly_100K.jelly.gz) | [Full (108.00 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/jelly_full.jelly.gz) | [Full (108.00 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/jelly_full.jelly.gz)
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | [10K (805.72 KB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_10K.jelly.gz) | [100K (7.79 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_100K.jelly.gz) | [Full (54.75 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz) | [Full (54.75 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz)
[citypulse-traffic](https://w3id.org/riverbench/datasets/citypulse-traffic/dev) | [10K (3.14 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/jelly_10K.jelly.gz) | [100K (31.45 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/jelly_100K.jelly.gz) | [1M (314.89 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/jelly_1M.jelly.gz) | [Full (1.36 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/jelly_full.jelly.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (3.34 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_10K.jelly.gz) | [100K (33.37 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_100K.jelly.gz) | [1M (334.48 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_1M.jelly.gz) | [Full (1.44 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_full.jelly.gz)
[dbpedia-live](https://w3id.org/riverbench/datasets/dbpedia-live/dev) | [10K (93.04 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_10K.jelly.gz) | [100K (294.25 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_100K.jelly.gz) | [Full (358.08 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_full.jelly.gz) | [Full (358.08 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_full.jelly.gz)
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | [10K (202.14 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_10K.jelly.gz) | [100K (1.90 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_100K.jelly.gz) | [1M (17.45 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_1M.jelly.gz) | [Full (24.75 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_full.jelly.gz)
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | [10K (1.51 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_10K.jelly.gz) | [100K (13.77 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_100K.jelly.gz) | [1M (167.62 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_1M.jelly.gz) | [Full (413.61 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_full.jelly.gz)
[lod-katrina](https://w3id.org/riverbench/datasets/lod-katrina/dev) | [10K (762.81 KB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/jelly_10K.jelly.gz) | [100K (11.22 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/jelly_100K.jelly.gz) | [1M (123.16 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/jelly_1M.jelly.gz) | [Full (716.03 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/jelly_full.jelly.gz)
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | [10K (822.71 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_10K.jelly.gz) | [100K (8.11 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_100K.jelly.gz) | [1M (88.39 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_1M.jelly.gz) | [Full (305.90 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_full.jelly.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | [10K (3.01 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_10K.jelly.gz) | [100K (30.89 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_100K.jelly.gz) | [1M (347.02 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_1M.jelly.gz) | [Full (1.56 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_full.jelly.gz)
[politiquices](https://w3id.org/riverbench/datasets/politiquices/dev) | [10K (1.50 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/jelly_10K.jelly.gz) | [Full (2.67 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/jelly_full.jelly.gz) | [Full (2.67 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/jelly_full.jelly.gz) | [Full (2.67 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/jelly_full.jelly.gz)
[yago-annotated-facts](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev) | [10K (301.51 KB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/jelly_10K.jelly.gz) | [100K (2.98 MB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/jelly_100K.jelly.gz) | [Full (29.91 MB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/jelly_full.jelly.gz) | [Full (29.91 MB)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/jelly_full.jelly.gz)