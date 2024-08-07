# stream-subject-graphs-nonstandard (development version)

Streaming unnamed subject graphs (with non-standard extensions)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs-nonstandard.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs-nonstandard.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs-nonstandard.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs-nonstandard.jelly)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming unnamed subject graphs (non-standard) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-subject-graphs-nonstandard`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [stream (dev)](https://w3id.org/riverbench/v/dev/categories/stream)
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: [stream-subject-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-graphs-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-graphs-nonstandard)
    - [stream-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-graphs-rdfstar-nonstandard)
    - [stream-mixed-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-nonstandard)
    - [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar-nonstandard)
    - [stream-subject-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs-rdfstar-nonstandard)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [digital-agenda-indicators (dev)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev)
    - [linked-spending (dev)](https://w3id.org/riverbench/datasets/linked-spending/dev)
    - [muziekweb (dev)](https://w3id.org/riverbench/datasets/muziekweb/dev)
    - [openaire-lod (dev)](https://w3id.org/riverbench/datasets/openaire-lod/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has dataset shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **Property (1)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
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
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | [10K (316.88 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_10K.tar.gz) | [100K (3.60 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_100K.tar.gz) | [1M (32.43 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_1M.tar.gz) | [Full (46.22 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_full.tar.gz)
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | [10K (1.26 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_10K.tar.gz) | [100K (10.04 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_100K.tar.gz) | [1M (139.86 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_1M.tar.gz) | [Full (345.98 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_full.tar.gz)
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | [10K (860.96 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_10K.tar.gz) | [100K (8.40 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_100K.tar.gz) | [1M (87.29 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_1M.tar.gz) | [Full (251.85 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_full.tar.gz)
[openaire-lod](https://w3id.org/riverbench/datasets/openaire-lod/dev) | [10K (3.00 MB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_10K.tar.gz) | [100K (43.17 MB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_100K.tar.gz) | [1M (1.08 GB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_1M.tar.gz) | [Full (1.58 GB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_full.tar.gz)

### Jelly streaming distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | [10K (188.14 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_10K.jelly.gz) | [100K (1.70 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_100K.jelly.gz) | [1M (16.44 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_1M.jelly.gz) | [Full (23.45 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_full.jelly.gz)
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | [10K (1.44 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_10K.jelly.gz) | [100K (13.43 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_100K.jelly.gz) | [1M (161.86 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_1M.jelly.gz) | [Full (398.51 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_full.jelly.gz)
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | [10K (765.19 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_10K.jelly.gz) | [100K (7.78 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_100K.jelly.gz) | [1M (85.49 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_1M.jelly.gz) | [Full (297.63 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_full.jelly.gz)
[openaire-lod](https://w3id.org/riverbench/datasets/openaire-lod/dev) | [10K (3.12 MB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_10K.jelly.gz) | [100K (45.00 MB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_100K.jelly.gz) | [1M (1.19 GB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_1M.jelly.gz) | [Full (1.70 GB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_full.jelly.gz)