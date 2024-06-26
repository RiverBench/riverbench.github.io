# Grouped RDF streaming

Benchmark category of generic tasks involving grouped RDF streams (elements are either RDF graphs or RDF datasets). This includes streaming throughput and latency benchmarks.
## Benchmark tasks

Below you will find a list of tasks that are part of this benchmark category.

!!! tip

    Benchmark tasks and profiles in RiverBench have machine-readable metadata in RDF.
    You can find RDF download links for each profile on its documentation page.
    You can also use the [HTTP content negotiation mechanism](../../documentation/metadata.md).

--8<-- "docs/categories/stream/task_table.md"

## Benchmark profiles

Profiles in RiverBench group datasets that share common technical characteristics.
For example, whether the datasets consist of triples or quads, if they use RDF-star, etc.
The profiles are intended to be used in benchmarks to compare the performance of different systems on a well-defined collection of datasets.

See the **[quick start guide](../../documentation/using.md)** for more information on how to use the profiles, tasks, and datasets.

--8<-- "docs/categories/stream/profile_table.md"



## Metadata



!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/categories/stream.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/categories/stream.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/categories/stream.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/categories/stream.jelly)**



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Grouped RDF streaming _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

### Content

- **<abbr title="For benchmark categories this property indicates tasks that belong to the category.">Has benchmark task</abbr>**: 
    - [stream-compression (dev)](https://w3id.org/riverbench/v/dev/tasks/stream-compression)
    - [stream-deserialization-throughput (dev)](https://w3id.org/riverbench/v/dev/tasks/stream-deserialization-throughput)
    - [stream-latency-end-to-end (dev)](https://w3id.org/riverbench/v/dev/tasks/stream-latency-end-to-end)
    - [stream-serialization-throughput (dev)](https://w3id.org/riverbench/v/dev/tasks/stream-serialization-throughput)
    - [stream-throughput-end-to-end (dev)](https://w3id.org/riverbench/v/dev/tasks/stream-throughput-end-to-end)
- **<abbr title="For benchmark categories this property indicates profiles that belong to the category.">Has benchmark profile</abbr>**: 
    - [stream-datasets (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-datasets)
    - [stream-datasets-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-nonstandard)
    - [stream-datasets-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar)
    - [stream-datasets-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-datasets-rdfstar-nonstandard)
    - [stream-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-graphs)
    - [stream-graphs-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-graphs-nonstandard)
    - [stream-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-graphs-rdfstar)
    - [stream-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-graphs-rdfstar-nonstandard)
    - [stream-mixed (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed)
    - [stream-mixed-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-nonstandard)
    - [stream-mixed-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar)
    - [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar-nonstandard)
    - [stream-named-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-named-graphs)
    - [stream-named-graphs-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-named-graphs-nonstandard)
    - [stream-named-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-named-graphs-rdfstar)
    - [stream-named-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-named-graphs-rdfstar-nonstandard)
    - [stream-subject-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs)
    - [stream-subject-graphs-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs-nonstandard)
    - [stream-subject-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs-rdfstar)
    - [stream-subject-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs-rdfstar-nonstandard)
    - [stream-ts-named-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-ts-named-graphs)
    - [stream-ts-named-graphs-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-ts-named-graphs-nonstandard)
    - [stream-ts-named-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-ts-named-graphs-rdfstar)
    - [stream-ts-named-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-ts-named-graphs-rdfstar-nonstandard)

