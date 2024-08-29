<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/2.1.0/categories/stream "Link to the permanent URL of this resource.")</div><div markdown><abbr title="This page corresponds to a stable release of RiverBench, so it cannot be edited. If you want to edit this page, go to the development version by selecting 'dev' from the version selector in the top navigation bar.">:material-lock-check: Stable: 2.1.0</abbr></div></div>

# Grouped RDF streaming

Benchmark category of generic tasks involving grouped RDF streams (elements are either RDF graphs or RDF datasets). This includes streaming throughput and latency benchmarks.
## Benchmark tasks

Below you will find a list of tasks that are part of this benchmark category.

!!! tip

    Benchmark tasks and profiles in RiverBench have machine-readable metadata in RDF.
    You can find RDF download links for each profile on its documentation page.
    You can also use the [HTTP content negotiation mechanism](../../documentation/metadata.md).

--8<-- "docs/categories/stream/task_table.md"

<div style="text-align: center" markdown>[:material-invoice-text-plus: Propose a new benchmark task](../../documentation/creating-new-task.md){ .md-button }</div>

## Benchmark profiles

Profiles in RiverBench group datasets that share common technical characteristics.
For example, whether the datasets consist of triples or quads, if they use RDF-star, etc.
The profiles are intended to be used in benchmarks to compare the performance of different systems on a well-defined collection of datasets.

See the **[quick start guide](../../documentation/using.md)** for more information on how to use the profiles, tasks, and datasets.

--8<-- "docs/categories/stream/profile_table.md"



## Metadata



!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/2.1.0/categories/stream.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/2.1.0/categories/stream.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/2.1.0/categories/stream.rdf)**, **[Jelly](https://w3id.org/riverbench/v/2.1.0/categories/stream.jelly)**
    <br>:material-github: Source repository: **[category-stream](https://github.com/RiverBench/category-stream)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/v/2.1.0/categories/stream`](https://w3id.org/riverbench/v/2.1.0/categories/stream)



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Grouped RDF streaming _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: 2.1.0
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (2.1.0)](https://w3id.org/riverbench/v/2.1.0)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

### Content

- **<abbr title="For benchmark categories this property indicates tasks that belong to the category.">Has benchmark task</abbr>**: 
    - [stream-compression (2.1.0)](https://w3id.org/riverbench/v/2.1.0/tasks/stream-compression)
    - [stream-deserialization-throughput (2.1.0)](https://w3id.org/riverbench/v/2.1.0/tasks/stream-deserialization-throughput)
    - [stream-latency-end-to-end (2.1.0)](https://w3id.org/riverbench/v/2.1.0/tasks/stream-latency-end-to-end)
    - [stream-serialization-throughput (2.1.0)](https://w3id.org/riverbench/v/2.1.0/tasks/stream-serialization-throughput)
    - [stream-throughput-end-to-end (2.1.0)](https://w3id.org/riverbench/v/2.1.0/tasks/stream-throughput-end-to-end)
- **<abbr title="For benchmark categories this property indicates profiles that belong to the category.">Has benchmark profile</abbr>**: 
    - [stream-datasets (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-datasets)
    - [stream-datasets-rdfstar (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-datasets-rdfstar)
    - [stream-graphs (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-graphs)
    - [stream-graphs-rdfstar (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-graphs-rdfstar)
    - [stream-mixed (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-mixed)
    - [stream-mixed-rdfstar (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-mixed-rdfstar)
    - [stream-named-graphs (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-named-graphs)
    - [stream-named-graphs-rdfstar (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-named-graphs-rdfstar)
    - [stream-subject-graphs (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-subject-graphs)
    - [stream-subject-graphs-rdfstar (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-subject-graphs-rdfstar)
    - [stream-ts-named-graphs (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-ts-named-graphs)
    - [stream-ts-named-graphs-rdfstar (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-ts-named-graphs-rdfstar)

