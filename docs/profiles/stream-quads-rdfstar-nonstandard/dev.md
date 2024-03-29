# stream-quads-rdfstar-nonstandard (development version)

Streaming quads (with RDF-star and non-standard extensions)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/profiles/stream-quads-rdfstar-nonstandard/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/profiles/stream-quads-rdfstar-nonstandard/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/profiles/stream-quads-rdfstar-nonstandard/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/profiles/stream-quads-rdfstar-nonstandard/dev.jelly)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming quads (RDF-star, non-standard)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-quads-rdfstar-nonstandard`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: 
    - [stream-graphs (dev)](https://w3id.org/riverbench/profiles/stream-graphs/dev)
    - [stream-graphs-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-graphs-nonstandard/dev)
    - [stream-graphs-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-graphs-rdfstar/dev)
    - [stream-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-graphs-rdfstar-nonstandard/dev)
    - [stream-quads (dev)](https://w3id.org/riverbench/profiles/stream-quads/dev)
    - [stream-quads-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-quads-nonstandard/dev)
    - [stream-quads-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-quads-rdfstar/dev)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [assist-iot-weather-graphs (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev)
    - [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)
    - [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [https://w3id.org/riverbench/](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**:     
            - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
            - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
    - **Has restriction (2)**    
        - **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**:     
            - <abbr title="Graph streams are a special case of quad streams, where each element contains exactly one named RDF graph.">Graphs</abbr> ([rb:graphs](https://w3id.org/riverbench/schema/metadata#graphs))
            - <abbr title="Quad streams consist of elements, where each element is an RDF dataset.">Quads</abbr> ([rb:quads](https://w3id.org/riverbench/schema/metadata#quads))


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
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | [10K (1.31 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_10K.tar.gz) | [100K (13.01 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_100K.tar.gz) | [Full (91.25 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz) | [Full (91.25 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (2.06 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_10K.tar.gz) | [100K (20.35 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_100K.tar.gz) | [1M (204.31 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_1M.tar.gz) | [Full (902.23 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_full.tar.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | [10K (2.55 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz) | [100K (25.59 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz) | [1M (277.18 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz) | [Full (1.02 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz)

### Jelly streaming distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | [10K (805.72 KB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_10K.jelly.gz) | [100K (7.79 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_100K.jelly.gz) | [Full (54.75 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz) | [Full (54.75 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (3.34 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_10K.jelly.gz) | [100K (33.38 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_100K.jelly.gz) | [1M (334.55 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_1M.jelly.gz) | [Full (1.44 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_full.jelly.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | [10K (3.01 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_10K.jelly.gz) | [100K (30.89 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_100K.jelly.gz) | [1M (347.02 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_1M.jelly.gz) | [Full (1.56 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_full.jelly.gz)