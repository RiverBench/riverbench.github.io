<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/dev/tasks/stream-serialization-throughput "Link to the permanent URL of this resource.")</div><div markdown>**[:material-file-edit: Edit this page](https://github.com/RiverBench/category-stream/edit/main/tasks/stream-serialization-throughput/index.md "Edit this page's source in Markdown on GitHub.")**</div><div markdown>**[:material-database-edit: Edit metadata](https://github.com/RiverBench/category-stream/edit/main/tasks/stream-serialization-throughput/metadata.ttl "Edit this page's metadata in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../../documentation/editing-docs.md "Need help with editing?")</div></div>

# Task: Grouped RDF stream serialization throughput (development version)

Task identifier: `stream-serialization-throughput`

A benchmark task measuring the througput of serializing a grouped RDF stream (that is, a stream in which the elements are either RDF graphs or RDF datasets).

## Methodology

### Data

Stream distributions of any dataset in the [`stream` category](../../categories/stream/index.md) of RiverBench may be used for this task.

### Workload

The task consists of serializing RDF data stored in memory in a grouped form (that is, as a stream of RDF graphs or RDF datasets) to a byte stream. The data is stored in memory in the form of an array of RDF graphs or datasets, or similar. To isolate the performance of the serializer itself, the following steps are taken:

- The data (RDF graphs/datasets) is preloaded into memory before the benchmark starts.
- The RDF data is stored in a data structure that is trivially iterable (e.g., an array of arrays or an array of sets).
- The serialization process is repeated multiple times to amortize the cost of the initial setup, just-in-time code recompilation, and other external factors.
- The serialized data is typically not written to disk, but just temporarily stored in memory and immediately discarded. This is to avoid the overhead of disk I/O.
    - Alternatively, in benchmarks that wish to evaluate the performance of writing to disk, especially considering the impact of different disk usage patterns (e.g., sequential vs. random access), the data may be written to disk.

### Metrics

- **Serialization throughput (in statements)** – throughput of the serialization process, measured in RDF statements (triples or quads) per second. This is calculated as the total number of RDF statements serialized divided by the total time taken to serialize them.
- **Serialization throughput (in elements)** – additionally, the throughput may be measured in terms of stream elements (RDF graphs or RDF datasets) per second.

## Results

**See the results for this task reported by the community: [RESULTS](results.md).**

## This task in benchmarks outside of RiverBench

- In the paper about the Jelly streaming protocol, such a benchmark is performed in Section IV.B. The corresponding task in the paper is named "Raw serialization throughput" and the performance in measured in terms of the number of triples serialized per second.
    - Sowiński, P., Wasielewska-Michniewska, K., Ganzha, M., & Paprzycki, M. (2022, October). Efficient RDF streaming for the edge-cloud continuum. In 2022 IEEE 8th World Forum on Internet of Things (WF-IoT) (pp. 1-8). IEEE. [https://doi.org/10.1109/WF-IoT54382.2022.10152225](https://doi.org/10.1109/WF-IoT54382.2022.10152225)


## See also

- Version of this task for flat RDF streams: [`flat-serialization-throughput`](../flat-serialization-throughput/index.md)
- The inverse task: [`stream-deserialization-throughput`](../stream-deserialization-throughput/index.md)


## Metadata



!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/tasks/stream-serialization-throughput.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/tasks/stream-serialization-throughput.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/tasks/stream-serialization-throughput.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/tasks/stream-serialization-throughput.jelly)**
    <br>:material-github: Source repository: **[category-stream](https://github.com/RiverBench/category-stream)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/v/dev/tasks/stream-serialization-throughput`](https://w3id.org/riverbench/v/dev/tasks/stream-serialization-throughput)



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Grouped RDF stream serialization throughput _(<abbr title="English">en</abbr>)_
- **<abbr title="An account of the resource.">Description</abbr>**: A benchmark task measuring the throughput of serializing a grouped RDF stream (that is, a stream in which the elements are either RDF graphs or RDF datasets). _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-serialization-throughput`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
    - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
    - **<abbr title="A homepage for some thing.">Homepage</abbr>**:     
        -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
        - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [stream (dev)](https://w3id.org/riverbench/v/dev/categories/stream)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

