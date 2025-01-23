<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar "Link to the permanent URL of this resource.")</div><div markdown>**[:material-database-edit: Edit this page](https://github.com/RiverBench/category-stream/edit/main/profiles/stream-datasets-rdfstar.ttl "Edit this page's source in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../documentation/editing-docs.md "Need help with editing?")</div></div>

# Profile: stream-datasets-rdfstar (development version)

Streaming datasets (with RDF-star)

!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar.jelly)**
    <br>:material-github: Source repository: **[category-stream](https://github.com/RiverBench/category-stream)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar`](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar)



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming datasets (RDF-star) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-datasets-rdfstar`
- **<abbr title="The version indicator (name or identifier) of a resource.">Version</abbr>**: `dev`
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [stream (dev)](https://w3id.org/riverbench/v/dev/categories/stream)
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: 
    - [stream-datasets (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-datasets)
    - [stream-named-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-named-graphs)
    - [stream-named-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-named-graphs-rdfstar)
    - [stream-ts-named-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-ts-named-graphs)
    - [stream-ts-named-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-ts-named-graphs-rdfstar)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: [stream-mixed-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [assist-iot-weather-graphs (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev)
    - [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)
    - [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has dataset shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **Property (​1)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: yes
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr> ([rb:conformsToRdfStarDraft_20211217](https://w3id.org/riverbench/schema/metadata#conformsToRdfStarDraft_20211217))
        - **Property (​2)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**:     
                - <abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr> ([stax:hasStreamType](https://w3id.org/stax/ontology#hasStreamType))
                - <abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr> ([stax:hasStreamTypeUsage](https://w3id.org/stax/ontology#hasStreamTypeUsage))
                - **Path (​3)**    
                    - **<abbr title="The (single) value of this property represents a path that is matched zero or more times.">Zero or more path</abbr>**: [http://www.w3.org/2004/02/skos/core#broader](http://www.w3.org/2004/02/skos/core#broader)
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A dataset in the RiverBench benchmark suite">RiverBench dataset</abbr> ([rb:Dataset](https://w3id.org/riverbench/schema/metadata#Dataset))
- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has distribution shape</abbr>**: 
    - **<abbr title="Specifies a list of shapes so that the value nodes must conform to at least one of the shapes.">Or</abbr>**:     
        - **Or (​1)**    
            - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
                - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
                - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr> ([rb:hasDistributionType](https://w3id.org/riverbench/schema/metadata#hasDistributionType))
        - **Or (​2)**    
            - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
                - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
                - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr> ([rb:hasDistributionType](https://w3id.org/riverbench/schema/metadata#hasDistributionType))
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A distribution of a dataset in the RiverBench benchmark suite.">RiverBench dataset distribution</abbr> ([rb:Distribution](https://w3id.org/riverbench/schema/metadata#Distribution))


## Download links

Below you will find links to download this profile's datasets in different lengths. The length of the dataset
is measured in stream elements (individual graphs or datasets) and is indicated in the table.
To see the size in statements (triples or quads), hover your mouse over the download link.

!!! warning

    Some datasets are shorter than others and a given fixed-size distribution may not be available for all datasets.

!!! note

    There are two available types of distributions for this profile: plain streaming packages, and the universal distribution in the Jelly format. See the [documentation](../documentation/dataset-release-format.md) for details.

### Plain streaming distributions (TriG)

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | <abbr title="10,000 stream elements; 1,160,000 statements">[10K (1.3 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_10K.tar.gz)</abbr> | <abbr title="100,000 stream elements; 11,600,000 statements">[100K (13.4 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_100K.tar.gz)</abbr> | – | <abbr title="701,278 stream elements; 81,348,248 statements">[Full (93.8 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz)</abbr>
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | <abbr title="10,000 stream elements; 370,000 statements">[10K (2.0 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_10K.tar.gz)</abbr> | <abbr title="100,000 stream elements; 3,700,000 statements">[100K (20.6 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_100K.tar.gz)</abbr> | <abbr title="1,000,000 stream elements; 37,000,000 statements">[1M (204.4 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_1M.tar.gz)</abbr> | <abbr title="4,382,599 stream elements; 162,156,163 statements">[Full (899.0 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_full.tar.gz)</abbr>
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | <abbr title="10,000 stream elements; 340,000 statements">[10K (2.6 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz)</abbr> | <abbr title="100,000 stream elements; 3,307,350 statements">[100K (25.6 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz)</abbr> | <abbr title="1,000,000 stream elements; 33,423,542 statements">[1M (277.0 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz)</abbr> | <abbr title="5,000,000 stream elements; 171,885,662 statements">[Full (1.0 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz)</abbr>

### Jelly distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | <abbr title="10,000 stream elements; 1,160,000 statements">[10K (703.3 KB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 11,600,000 statements">[100K (6.8 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_100K.jelly.gz)</abbr> | – | <abbr title="701,278 stream elements; 81,348,248 statements">[Full (47.7 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz)</abbr>
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | <abbr title="10,000 stream elements; 370,000 statements">[10K (3.3 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 3,700,000 statements">[100K (32.9 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_100K.jelly.gz)</abbr> | <abbr title="1,000,000 stream elements; 37,000,000 statements">[1M (330.3 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_1M.jelly.gz)</abbr> | <abbr title="4,382,599 stream elements; 162,156,163 statements">[Full (1.4 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_full.jelly.gz)</abbr>
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | <abbr title="10,000 stream elements; 340,000 statements">[10K (2.9 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 3,307,350 statements">[100K (29.6 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_100K.jelly.gz)</abbr> | <abbr title="1,000,000 stream elements; 33,423,542 statements">[1M (332.7 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_1M.jelly.gz)</abbr> | <abbr title="5,000,000 stream elements; 171,885,662 statements">[Full (1.5 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_full.jelly.gz)</abbr>