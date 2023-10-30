# stream-datasets-nonstandard (development version)

Streaming datasets (with non-standard extensions)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/profiles/stream-datasets-nonstandard/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/profiles/stream-datasets-nonstandard/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/profiles/stream-datasets-nonstandard/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/profiles/stream-datasets-nonstandard/dev.jelly)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming datasets (non-standard)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-datasets-nonstandard`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: 
    - [stream-datasets (dev)](https://w3id.org/riverbench/profiles/stream-datasets/dev)
    - [stream-named-graphs (dev)](https://w3id.org/riverbench/profiles/stream-named-graphs/dev)
    - [stream-named-graphs-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-named-graphs-nonstandard/dev)
    - [stream-ts-named-graphs (dev)](https://w3id.org/riverbench/profiles/stream-ts-named-graphs/dev)
    - [stream-ts-named-graphs-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-ts-named-graphs-nonstandard/dev)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-datasets-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-datasets-rdfstar-nonstandard/dev)
    - [stream-mixed-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-nonstandard/dev)
    - [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [assist-iot-weather-graphs (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev)
    - [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)
    - [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [https://w3id.org/riverbench/](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**:     
            - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
            - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
    - **Has restriction (2)**    
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**:     
            - <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
            - <abbr title="An RDF named graph stream is an RDF dataset stream in which every element has exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph node. Apart from graph G, the dataset may contain any number of triples in the default graph.">RDF named graph stream</abbr> ([stax:namedGraphStream](https://w3id.org/stax/ontology#namedGraphStream))
            - <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph node; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
    - **Has restriction (3)**    
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
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | [10K (1.31 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_10K.tar.gz) | [100K (13.01 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_100K.tar.gz) | [Full (91.26 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz) | [Full (91.26 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (2.06 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_10K.tar.gz) | [100K (20.36 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_100K.tar.gz) | [1M (204.33 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_1M.tar.gz) | [Full (902.27 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_full.tar.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | [10K (2.55 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz) | [100K (25.59 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz) | [1M (277.17 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz) | [Full (1.02 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz)

### Jelly streaming distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | [10K (805.72 KB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_10K.jelly.gz) | [100K (7.79 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_100K.jelly.gz) | [Full (54.75 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz) | [Full (54.75 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (3.34 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_10K.jelly.gz) | [100K (33.38 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_100K.jelly.gz) | [1M (334.56 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_1M.jelly.gz) | [Full (1.44 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_full.jelly.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | [10K (3.01 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_10K.jelly.gz) | [100K (30.89 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_100K.jelly.gz) | [1M (347.02 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_1M.jelly.gz) | [Full (1.56 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_full.jelly.gz)