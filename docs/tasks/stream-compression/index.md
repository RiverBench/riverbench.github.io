<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/dev/tasks/stream-compression "Link to the permanent URL of this resource.")</div><div markdown>**[:material-file-edit: Edit this page](https://github.com/RiverBench/category-stream/edit/main/tasks/stream-compression/index.md "Edit this page's source in Markdown on GitHub.")**</div><div markdown>**[:material-database-edit: Edit metadata](https://github.com/RiverBench/category-stream/edit/main/tasks/stream-compression/metadata.ttl "Edit this page's metadata in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../../documentation/editing-docs.md "Need help with editing?")</div></div>

# Task: Grouped RDF stream compression (development version)

Task identifier: `stream-compression`

A benchmark task measuring the compression efficiency of serializations for grouped RDF streams.

## Methodology

### Data

Stream distributions of any dataset in the [`stream` category](../../categories/stream/index.md) of RiverBench may be used for this task.

### Workload

The task consists of serializing RDF data in a grouped form (that is, as a stream of RDF graphs or RDF datasets) to bytes and measuring the size of the obtained representation.

In this task, the time taken to serialize and deserialize the data is not considered – see the [`stream-serialization-throughput`](../stream-serialization-throughput/index.md) and [`stream-deserialization-throughput`](../stream-deserialization-throughput/index.md) tasks for that aspect.

### Metrics

- **Serialized representation size** – the primary metric, size of the serialized RDF data, in bytes.
- **Compression ratio** – additionally, the compression ratio can be calculated as the ratio of the reference size to the compressed size. The reference size is the size of the same data serialized using a baseline method, e.g., the N-Triples serialization format.
    - In the RDF literature, the "compression ratio" is often defined as the inverse of the above definition and expressed as a percentage. For example, a compression ratio of (50%) means that the compressed data is half the size of the reference data.

## Results

**See the results for this task reported by the community: [RESULTS](results.md).**

## This task in benchmarks outside of RiverBench

- In the paper about the Jelly streaming protocol, such a benchmark is performed in Section IV.C. The authors have measured the output size of several methods. The presented "Compression ratio" metric there refers to the ratio between the compressed data size and the reference data size, with N-Triples used as the reference.
    - Sowiński, P., Wasielewska-Michniewska, K., Ganzha, M., & Paprzycki, M. (2022, October). Efficient RDF streaming for the edge-cloud continuum. In 2022 IEEE 8th World Forum on Internet of Things (WF-IoT) (pp. 1-8). IEEE. [https://doi.org/10.1109/WF-IoT54382.2022.10152225](https://doi.org/10.1109/WF-IoT54382.2022.10152225)

## See also

- Version of this task for flat RDF streams: [`flat-compression`](../flat-compression/index.md)


## Metadata



!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/tasks/stream-compression.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/tasks/stream-compression.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/tasks/stream-compression.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/tasks/stream-compression.jelly)**
    <br>:material-github: Source repository: **[category-stream](https://github.com/RiverBench/category-stream)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/v/dev/tasks/stream-compression`](https://w3id.org/riverbench/v/dev/tasks/stream-compression)



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Grouped RDF stream compression _(<abbr title="English">en</abbr>)_
- **<abbr title="An account of the resource.">Description</abbr>**: A benchmark task measuring the compression efficiency of serializations for grouped RDF streams. _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-compression`
- **<abbr title="The version indicator (name or identifier) of a resource.">Version</abbr>**: `dev`
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
    - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
    - **<abbr title="This axiom needed so that Protege loads DCAT 3 without errors.">Homepage</abbr>**:     
        -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
        - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [stream (dev)](https://w3id.org/riverbench/v/dev/categories/stream)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

