# flat-quads-rdfstar (development version)

Flat sequence of quads (with RDF-star)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/profiles/flat-quads-rdfstar/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/profiles/flat-quads-rdfstar/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/profiles/flat-quads-rdfstar/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/profiles/flat-quads-rdfstar/dev.jelly)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Flat sequence of quads (RDF-star)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-quads-rdfstar`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: [flat-quads (dev)](https://w3id.org/riverbench/profiles/flat-quads/dev)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [flat-mixed-rdfstar (dev)](https://w3id.org/riverbench/profiles/flat-mixed-rdfstar/dev)
    - [flat-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/flat-mixed-rdfstar-nonstandard/dev)
    - [flat-quads-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/flat-quads-rdfstar-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [assist-iot-weather-graphs (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev)
    - [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)
    - [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [https://w3id.org/riverbench/](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
    - **Has restriction (2)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - **Has restriction (3)**    
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is an RDF stream whose elements are quad statements.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))


## Download links

Below you will find links to download the profile's datasets in different lengths.

!!! warning
    Some datasets are shorter than others and a given distribution may not be available for all datasets.
    In that case, a link to the longest available distribution of the dataset is provided.

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | [10K (5.07 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_10K.nq.gz) | [100K (50.58 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_100K.nq.gz) | [Full (354.64 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_full.nq.gz) | [Full (354.64 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_full.nq.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | [10K (3.96 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_10K.nq.gz) | [100K (39.69 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_100K.nq.gz) | [1M (395.98 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_1M.nq.gz) | [Full (1.69 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_full.nq.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | [10K (3.47 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_10K.nq.gz) | [100K (35.73 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_100K.nq.gz) | [1M (384.61 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_1M.nq.gz) | [Full (1.68 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_full.nq.gz)