# stream-datasets (development version)

Streaming datasets (RDF 1.1 standard only)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/profiles/stream-datasets.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/profiles/stream-datasets.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/profiles/stream-datasets.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/profiles/stream-datasets.jelly)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming datasets (standard) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-datasets`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [stream (dev)](https://w3id.org/riverbench/v/dev/categories/stream)
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: 
    - [stream-named-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-named-graphs)
    - [stream-ts-named-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-ts-named-graphs)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-datasets-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-nonstandard)
    - [stream-datasets-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar)
    - [stream-datasets-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar-nonstandard)
    - [stream-mixed (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed)
    - [stream-mixed-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-nonstandard)
    - [stream-mixed-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar)
    - [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar-nonstandard)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [assist-iot-weather-graphs (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev)
    - [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)
    - [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has dataset shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **Property (1)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**:     
                - <abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr> ([stax:hasStreamType](https://w3id.org/stax/ontology#hasStreamType))
                - <abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr> ([stax:hasStreamTypeUsage](https://w3id.org/stax/ontology#hasStreamTypeUsage))
                - **Path (3)**    
                    - **<abbr title="The (single) value of this property represents a path that is matched zero or more times.">Zero or more path</abbr>**: [http://www.w3.org/2004/02/skos/core#broader](http://www.w3.org/2004/02/skos/core#broader)
        - **Property (2)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: yes
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr> ([rb:conformsToRdf11](https://w3id.org/riverbench/schema/metadata#conformsToRdf11))
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
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | [10K (1.34 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_10K.tar.gz) | [100K (13.36 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_100K.tar.gz) | [Full (93.76 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz) | [Full (93.76 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (2.04 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_10K.tar.gz) | [100K (20.61 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_100K.tar.gz) | [1M (204.36 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_1M.tar.gz) | [Full (898.99 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_full.tar.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | [10K (2.55 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz) | [100K (25.57 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz) | [1M (277.04 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz) | [Full (1.02 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz)

### Jelly streaming distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | [10K (703.29 KB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_10K.jelly.gz) | [100K (6.79 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_100K.jelly.gz) | [Full (47.71 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz) | [Full (47.71 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (3.27 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_10K.jelly.gz) | [100K (32.91 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_100K.jelly.gz) | [1M (330.27 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_1M.jelly.gz) | [Full (1.42 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_full.jelly.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | [10K (2.88 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_10K.jelly.gz) | [100K (29.63 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_100K.jelly.gz) | [1M (332.66 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_1M.jelly.gz) | [Full (1.50 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_full.jelly.gz)