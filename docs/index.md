{{ top_buttons('https://github.com/RiverBench/RiverBench/tree/main/doc') }}

[![RiverBench logo](https://w3id.org/riverbench/assets/riverbench_vector_logo.png){ align=right width="150" }](https://w3id.org/riverbench)

# RiverBench

RiverBench is an open, community-driven RDF streaming benchmark suite. It includes a varied collection of datasets and tasks, representing many real-life use cases.

<div class="grid cards" style="clear: right;" markdown>

-   :material-invoice-text:{ .lg .middle } __Benchmark task definitions__

    ---

    RiverBench gathers benchmark tasks for testing streaming and non-streaming RDF systems

    **[:octicons-arrow-right-24: Getting started](documentation/using.md)**

-   :material-database:{ .lg .middle } __Diverse, validated datasets__

    ---

    RiverBench collects real-life, rigourously validated datasets for a wide range of use cases, in easy-to-use formats

    **[:octicons-arrow-right-24: Datasets](datasets/index.md)**

-   :material-human-handsup:{ .lg .middle } __Community-driven__

    ---

    <u>You</u> can contribute new datasets, tasks, or edit any part of RiverBench

    **[:octicons-arrow-right-24: Contributing](documentation/contribute.md)**

-   :material-timer-star:{ .lg .middle } __Repository of benchmark results__

    ---

    Anyone can report their benchmark results – we collect, organize, and showcase them

    **[:octicons-arrow-right-24: Benchmark results](results/index.md)**

-   :fontawesome-solid-diagram-project:{ .lg .middle } __Machine-readable RDF metadata__

    ---

    Everything has extensive RDF metadata, for easy integration with other tools

    **[:octicons-arrow-right-24: Metadata documentation](documentation/metadata.md)**

-   :material-open-source-initiative:{ .lg .middle } __Open licenses__

    ---

    All parts of RiverBench are clearly licensed and you can reuse them for any purpose

    **[:octicons-arrow-right-24: Licensing](documentation/licensing.md)**

</div>

Not sure where to start? Check out the **[quick start guide](documentation/using.md)** first. Alternatively, you can explore the following sections:

- **[Documentation](documentation/index.md)** – how to use RiverBench in your research and how to contribute to it.
- **[Benchmarks](categories/index.md)** – benchmark task descriptions, along with applicable profiles (collections of datasets).
- **[Datasets](datasets/index.md)** – packaged and tested datasets, ready to use.
- **[Benchmark results](results/index.md)** – results reported by the community.
- **[Code on GitHub](https://github.com/RiverBench)**
- **[Citing RiverBench and its datasets](documentation/licensing.md)**
- **[Paper about RiverBench](https://arxiv.org/abs/2305.06226)** (preprint)

----


!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev.jelly)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/v/dev`](https://w3id.org/riverbench/v/dev)

    :material-database: A complete dump of all metadata in RiverBench (without benchmark results) is available:
    <br>**[Turtle](https://w3id.org/riverbench/dumps/dev.ttl.gz)**, **[N-Triples](https://w3id.org/riverbench/dumps/dev.nt.gz)**, **[RDF/XML](https://w3id.org/riverbench/dumps/dev.rdf.gz)**, **[Jelly](https://w3id.org/riverbench/dumps/dev.jelly.gz)**
    <br>:material-database-plus: A dump including community-contributed benchmark results (via nanopublications) is also available:
    <br>**[TriG](https://w3id.org/riverbench/dumps-with-results/dev.trig.gz)**, **[N-Quads](https://w3id.org/riverbench/dumps-with-results/dev.nq.gz)**, **[Jelly](https://w3id.org/riverbench/dumps-with-results/dev.jelly.gz)**



## General information

- **<abbr title="Information about rights held in and over the resource.">Rights</abbr>**: The metadata, documentation, and ontologies of RiverBench are licensed under the [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) license. The source code of RiverBench is licensed under the [Apache License, Version 2.0](https://spdx.org/licenses/Apache-2.0). The included datasets are licensed under their respective free licenses, listed in their documentation pages. _(<abbr title="English">en</abbr>)_
- **<abbr title="This axiom needed so that Protege loads DCAT2 without errors.">Homepage</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)
- **<abbr title="The knowledge organization system (KOS) used to classify catalog's datasets.">Theme taxonomy</abbr>**: EuroVoc ([eurovoc:100141](http://eurovoc.europa.eu/100141))

## Content

- **<abbr title="Indicates that a benchmark category belongs to this benchmark suite.">Has benchmark category</abbr>**: 
    - [flat (dev)](https://w3id.org/riverbench/v/dev/categories/flat)
    - [stream (dev)](https://w3id.org/riverbench/v/dev/categories/stream)
- **<abbr title="A collection of data that is listed in the catalog.">Has dataset</abbr>**: 
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
    - [openaire-lod (dev)](https://w3id.org/riverbench/datasets/openaire-lod/dev)
    - [politiquices (dev)](https://w3id.org/riverbench/datasets/politiquices/dev)
    - [yago-annotated-facts (dev)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev)



----

<figure markdown>
  ![RiverBench logo as a painting](https://w3id.org/riverbench/assets/riverbench_painting.png){ width="420" loading=lazy }
  <figcaption>Impression of RiverBench generated with DALL-E.</figcaption>
</figure>
