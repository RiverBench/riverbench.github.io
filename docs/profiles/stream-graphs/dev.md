# stream-graphs (development version)

Streaming graphs (RDF 1.1 standard only)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/profiles/stream-graphs/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/profiles/stream-graphs/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/profiles/stream-graphs/dev.rdf)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming graphs (standard)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-graphs
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-graphs-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-graphs-nonstandard/dev)
    - [stream-graphs-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-graphs-rdfstar/dev)
    - [stream-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-graphs-rdfstar-nonstandard/dev)
    - [stream-mixed (dev)](https://w3id.org/riverbench/profiles/stream-mixed/dev)
    - [stream-mixed-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-nonstandard/dev)
    - [stream-mixed-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar/dev)
    - [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar-nonstandard/dev)
    - [stream-quads (dev)](https://w3id.org/riverbench/profiles/stream-quads/dev)
    - [stream-quads-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-quads-nonstandard/dev)
    - [stream-quads-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-quads-rdfstar/dev)
    - [stream-quads-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-quads-rdfstar-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [https://w3id.org/riverbench/](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Graph streams are a special case of quad streams, where each element contains exactly one named RDF graph.">Graphs</abbr> ([rb:graphs](https://w3id.org/riverbench/schema/metadata#graphs))
    - **Has restriction (2)**    
        - **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
    - **Has restriction (3)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))


## Download links

Below you will find links to download the profile's datasets in different lengths.

!!! warning
    Some datasets are shorter than others and a given distribution may not be available for all datasets.
    In that case, a link to the longest available distribution of the dataset is provided.

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (2.06 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_10K.tar.gz) | [100K (20.35 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_100K.tar.gz) | [1M (205.29 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_1M.tar.gz) | [Full (902.25 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_full.tar.gz)