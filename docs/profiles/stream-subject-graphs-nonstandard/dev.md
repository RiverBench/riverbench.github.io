# stream-subject-graphs-nonstandard (development version)

Streaming unnamed subject graphs (with non-standard extensions)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/profiles/stream-subject-graphs-nonstandard/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/profiles/stream-subject-graphs-nonstandard/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/profiles/stream-subject-graphs-nonstandard/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/profiles/stream-subject-graphs-nonstandard/dev.jelly)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming unnamed subject graphs (non-standard)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-subject-graphs-nonstandard`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: [stream-subject-graphs (dev)](https://w3id.org/riverbench/profiles/stream-subject-graphs/dev)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-graphs-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-graphs-nonstandard/dev)
    - [stream-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-graphs-rdfstar-nonstandard/dev)
    - [stream-mixed-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-nonstandard/dev)
    - [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar-nonstandard/dev)
    - [stream-subject-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-subject-graphs-rdfstar-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [digital-agenda-indicators (dev)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev)
    - [linked-spending (dev)](https://w3id.org/riverbench/datasets/linked-spending/dev)
    - [muziekweb (dev)](https://w3id.org/riverbench/datasets/muziekweb/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

## Technical metadata

- **HasRestriction**: 
    - **HasRestriction (1)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**:     
            - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
            - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
    - **HasRestriction (2)**    
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
    - **HasRestriction (3)**    
        - **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no


## Download links

Below you will find links to download the profile's datasets in different lengths.

!!! warning
    Some datasets are shorter than others and a given distribution may not be available for all datasets.
    In that case, a link to the longest available distribution of the dataset is provided.

!!! note

    For stream profiles, there are two available types of distributions: plain streaming, and streaming in the Jelly format. See the [documentation](../../documentation/dataset-release-format.md) for details.

### Plain streaming distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | [10K (316.88 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_10K.tar.gz) | [100K (3.60 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_100K.tar.gz) | [1M (32.46 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_1M.tar.gz) | [Full (46.28 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_full.tar.gz)
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | [10K (1.26 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_10K.tar.gz) | [100K (10.11 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_100K.tar.gz) | [1M (140.17 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_1M.tar.gz) | [Full (346.64 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_full.tar.gz)
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | [10K (862.19 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_10K.tar.gz) | [100K (8.41 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_100K.tar.gz) | [1M (87.39 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_1M.tar.gz) | [Full (252.24 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_full.tar.gz)

### Jelly streaming distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | [10K (202.14 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_10K.jelly.gz) | [100K (1.90 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_100K.jelly.gz) | [1M (17.45 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_1M.jelly.gz) | [Full (24.75 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_full.jelly.gz)
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | [10K (1.51 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_10K.jelly.gz) | [100K (13.76 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_100K.jelly.gz) | [1M (167.62 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_1M.jelly.gz) | [Full (413.61 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_full.jelly.gz)
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | [10K (822.71 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_10K.jelly.gz) | [100K (8.11 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_100K.jelly.gz) | [1M (88.39 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_1M.jelly.gz) | [Full (305.90 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_full.jelly.gz)