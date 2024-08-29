<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/2.1.0/tasks/stream-deserialization-throughput "Link to the permanent URL of this resource.")</div><div markdown><abbr title="This page corresponds to a stable release of RiverBench, so it cannot be edited. If you want to edit this page, go to the development version by selecting 'dev' from the version selector in the top navigation bar.">:material-lock-check: Stable: 2.1.0</abbr></div></div>

# Task: Grouped streaming deserialization throughput (2.1.0)

Task identifier: `stream-deserialization-throughput`

A benchmark task measuring the througput of deserializing a grouped RDF stream (that is, a stream in which the elements are either RDF graphs or RDF datasets) from a byte stream to memory.

## Methodology

### Data

Stream distributions of any dataset in the [`stream` category](../../categories/stream/index.md) of RiverBench may be used for this task.

### Workload

The task consists of deserializing RDF data stored in a byte stream to memory in a grouped form (that is, as a stream of RDF graphs or RDF datasets). To isolate the performance of the deserializer itself, the following steps are taken:

- The data (serialized RDF graphs/datasets in the tested serialization format) is preloaded into memory before the benchmark starts.
- The deserialization process is repeated multiple times to amortize the cost of the initial setup, just-in-time code recompilation, and other external factors.
- The deserialized statements are not inserted into any data structure or database, but just temporarily stored in memory and immediately discarded. This is to avoid the overhead of maintaining additional data structures.
    - When possible, the deserialized data should NOT be inserted into a data structure dedicated for RDF graphs or datasets, as these typically include additional processing steps (e.g., updating indexes) that are not part of the deserialization process. Instead, the deserialized statements should ideally be simply iterated over and discarded or inserted into an array.

### Metrics

- Throughput of the deserialization process, measured in RDF statements (triples or quads) per second. This is calculated as the total number of RDF statements deserialized divided by the total time taken to deserialize them.
- Additionally, the throughput may be measured in terms of stream elements (RDF graphs or RDF datasets) per second.

## Results

**See the results for this task reported by the community: [RESULTS](results.md).**

## This task in benchmarks outside of RiverBench

- In the paper about the Jelly streaming protocol, such a benchmark is performed in Section IV.B. The corresponding task in the paper is named "Raw deserialization throughput" and the performance in measured in terms of the number of triples deserialized per second.
    - Sowiński, P., Wasielewska-Michniewska, K., Ganzha, M., & Paprzycki, M. (2022, October). Efficient RDF streaming for the edge-cloud continuum. In 2022 IEEE 8th World Forum on Internet of Things (WF-IoT) (pp. 1-8). IEEE. [https://doi.org/10.1109/WF-IoT54382.2022.10152225](https://doi.org/10.1109/WF-IoT54382.2022.10152225)


## See also

- Version of this task for flat RDF streams: [`flat-deserialization-throughput`](../flat-deserialization-throughput/index.md)
- The inverse task: [`stream-serialization-throughput`](../stream-serialization-throughput/index.md)


## Metadata



!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/2.1.0/tasks/stream-deserialization-throughput.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/2.1.0/tasks/stream-deserialization-throughput.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/2.1.0/tasks/stream-deserialization-throughput.rdf)**, **[Jelly](https://w3id.org/riverbench/v/2.1.0/tasks/stream-deserialization-throughput.jelly)**
    <br>:material-github: Source repository: **[category-stream](https://github.com/RiverBench/category-stream)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/v/2.1.0/tasks/stream-deserialization-throughput`](https://w3id.org/riverbench/v/2.1.0/tasks/stream-deserialization-throughput)



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Grouped streaming deserialization throughput _(<abbr title="English">en</abbr>)_
- **<abbr title="An account of the resource.">Description</abbr>**: A benchmark task measuring the throughput of deserializing a grouped RDF stream (that is, a stream in which the elements are either RDF graphs or RDF datasets) from a byte stream to memory. _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-deserialization-throughput`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: 2.1.0
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
    - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
    - **<abbr title="This axiom needed so that Protege loads DCAT2 without errors.">Homepage</abbr>**:     
        -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
        - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [stream (2.1.0)](https://w3id.org/riverbench/v/2.1.0/categories/stream)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (2.1.0)](https://w3id.org/riverbench/v/2.1.0)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

