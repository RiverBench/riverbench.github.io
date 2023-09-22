# stream-triples (development version)

Streaming triples (RDF 1.1 standard only)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/profiles/stream-triples/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/profiles/stream-triples/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/profiles/stream-triples/dev.rdf)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming triples (standard)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-triples`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-mixed (dev)](https://w3id.org/riverbench/profiles/stream-mixed/dev)
    - [stream-mixed-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-nonstandard/dev)
    - [stream-mixed-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar/dev)
    - [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar-nonstandard/dev)
    - [stream-triples-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-triples-nonstandard/dev)
    - [stream-triples-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-triples-rdfstar/dev)
    - [stream-triples-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-triples-rdfstar-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [assist-iot-weather (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev)
    - [citypulse-traffic (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev)
    - [dbpedia-live (dev)](https://w3id.org/riverbench/datasets/dbpedia-live/dev)
    - [digital-agenda-indicators (dev)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev)
    - [linked-spending (dev)](https://w3id.org/riverbench/datasets/linked-spending/dev)
    - [lod-katrina (dev)](https://w3id.org/riverbench/datasets/lod-katrina/dev)
    - [muziekweb (dev)](https://w3id.org/riverbench/datasets/muziekweb/dev)
    - [politiquices (dev)](https://w3id.org/riverbench/datasets/politiquices/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [https://w3id.org/riverbench/](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
    - **Has restriction (2)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
    - **Has restriction (3)**    
        - **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Triple streams consist of elements, where each element is an RDF graph.">Triples</abbr> ([rb:triples](https://w3id.org/riverbench/schema/metadata#triples))


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
[assist-iot-weather](https://w3id.org/riverbench/datasets/assist-iot-weather/dev) | [10K (2.34 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/stream_10K.tar.gz) | [100K (23.30 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/stream_100K.tar.gz) | [Full (163.34 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/stream_full.tar.gz) | [Full (163.34 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/stream_full.tar.gz)
[citypulse-traffic](https://w3id.org/riverbench/datasets/citypulse-traffic/dev) | [10K (1.89 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_10K.tar.gz) | [100K (18.73 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_100K.tar.gz) | [1M (187.36 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_1M.tar.gz) | [Full (820.68 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_full.tar.gz)
[dbpedia-live](https://w3id.org/riverbench/datasets/dbpedia-live/dev) | [10K (66.88 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_10K.tar.gz) | [100K (209.48 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_100K.tar.gz) | [Full (256.91 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_full.tar.gz) | [Full (256.91 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_full.tar.gz)
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | [10K (316.97 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_10K.tar.gz) | [100K (3.60 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_100K.tar.gz) | [1M (32.47 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_1M.tar.gz) | [Full (46.29 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_full.tar.gz)
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | [10K (1.26 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_10K.tar.gz) | [100K (10.11 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_100K.tar.gz) | [1M (140.17 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_1M.tar.gz) | [Full (346.63 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_full.tar.gz)
[lod-katrina](https://w3id.org/riverbench/datasets/lod-katrina/dev) | [10K (728.03 KB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_10K.tar.gz) | [100K (9.62 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_100K.tar.gz) | [1M (102.03 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_1M.tar.gz) | [Full (594.41 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_full.tar.gz)
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | [10K (862.31 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_10K.tar.gz) | [100K (8.41 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_100K.tar.gz) | [1M (87.39 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_1M.tar.gz) | [Full (252.23 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_full.tar.gz)
[politiquices](https://w3id.org/riverbench/datasets/politiquices/dev) | [10K (1.38 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_10K.tar.gz) | [Full (2.46 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_full.tar.gz) | [Full (2.46 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_full.tar.gz) | [Full (2.46 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_full.tar.gz)

### Jelly streaming distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather](https://w3id.org/riverbench/datasets/assist-iot-weather/dev) | [10K (1.55 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/jelly_10K.jelly.gz) | [100K (15.39 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/jelly_100K.jelly.gz) | [Full (108.00 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/jelly_full.jelly.gz) | [Full (108.00 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather/dev/files/jelly_full.jelly.gz)
[citypulse-traffic](https://w3id.org/riverbench/datasets/citypulse-traffic/dev) | [10K (3.14 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/jelly_10K.jelly.gz) | [100K (31.45 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/jelly_100K.jelly.gz) | [1M (314.86 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/jelly_1M.jelly.gz) | [Full (1.36 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/jelly_full.jelly.gz)
[dbpedia-live](https://w3id.org/riverbench/datasets/dbpedia-live/dev) | [10K (93.04 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_10K.jelly.gz) | [100K (294.25 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_100K.jelly.gz) | [Full (358.08 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_full.jelly.gz) | [Full (358.08 MB)](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_full.jelly.gz)
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | [10K (202.14 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_10K.jelly.gz) | [100K (1.90 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_100K.jelly.gz) | [1M (17.45 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_1M.jelly.gz) | [Full (24.75 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_full.jelly.gz)
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | [10K (1.51 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_10K.jelly.gz) | [100K (13.76 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_100K.jelly.gz) | [1M (167.62 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_1M.jelly.gz) | [Full (413.60 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_full.jelly.gz)
[lod-katrina](https://w3id.org/riverbench/datasets/lod-katrina/dev) | [10K (762.80 KB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/jelly_10K.jelly.gz) | [100K (11.22 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/jelly_100K.jelly.gz) | [1M (123.16 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/jelly_1M.jelly.gz) | [Full (716.03 MB)](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/jelly_full.jelly.gz)
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | [10K (822.71 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_10K.jelly.gz) | [100K (8.11 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_100K.jelly.gz) | [1M (88.39 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_1M.jelly.gz) | [Full (305.90 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_full.jelly.gz)
[politiquices](https://w3id.org/riverbench/datasets/politiquices/dev) | [10K (1.50 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/jelly_10K.jelly.gz) | [Full (2.67 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/jelly_full.jelly.gz) | [Full (2.67 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/jelly_full.jelly.gz) | [Full (2.67 MB)](https://w3id.org/riverbench/datasets/politiquices/dev/files/jelly_full.jelly.gz)