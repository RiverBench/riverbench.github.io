<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/dev/tasks/stream-throughput-end-to-end "Link to the permanent URL of this resource.")</div><div markdown>**[:material-file-edit: Edit this page](https://github.com/RiverBench/category-stream/edit/main/tasks/stream-throughput-end-to-end/index.md "Edit this page's source in Markdown on GitHub.")**</div><div markdown>**[:material-database-edit: Edit metadata](https://github.com/RiverBench/category-stream/edit/main/tasks/stream-throughput-end-to-end/metadata.ttl "Edit this page's metadata in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../../documentation/editing-docs.md "Need help with editing?")</div></div>

# Task: End-to-end RDF streaming throughput (development version)

Task identifier: `stream-throughput-end-to-end`

A benchmark task measuring the throughput of streaming elements in a grouped RDF stream over the network, including serialization, network communication, and deserialization.

## Methodology

### Data

Stream distributions of any dataset in the [`stream` category](../../categories/stream/index.md) of RiverBench may be used for this task.

### Workload

The task consists of setting up two network applications: the **producer** and the **consumer**. The producer is tasked with serializing a grouped RDF stream and sending it over the network to the consumer. The consumer receives the serialized data and deserializes it. This benchmark task measures the time taken of the entire end-to-end streaming process, including serialization, network communication, and deserialization.

To isolate the performance of the streaming process itself, the following steps are taken:

- The data (RDF graphs/datasets) is preloaded into the memory of the producer before the benchmark starts.
- The RDF data is stored by the producer in a data structure that is trivially iterable (e.g., an array of arrays or an array of sets).
- The experiment is repeated multiple times to amortize the cost of the initial setup, just-in-time code recompilation, and other external factors.
- The consumer receives the serialized data and deserializes it, but the deserialized statements are not inserted into any data structure or database, but just temporarily stored in memory and immediately discarded. This is to avoid the overhead of maintaining additional data structures.
    - When possible, the deserialized data should NOT be inserted into a data structure dedicated for RDF graphs or datasets, as these typically include additional processing steps (e.g., updating indexes) that are not part of the deserialization process. Instead, the deserialized statements should ideally be simply iterated over and discarded or inserted into an array.

### Technical notes

- Various streaming protocols may be used in the experiments, such as MQTT, Kafka, or gRPC. A common example of such a setup would be to send stream elements (RDF graphs) as Turtle files over MQTT.
- The network communication may be simulated locally (e.g., using loopback interfaces) or over a real network connection. The latter may introduce additional variability in the results due to network latency, bandwidth, and other factors.
    - Alternatively, specific network conditions may be simulated using tools like `tc` (Linux Traffic Control, NetEm kernel module) or network emulators.
- When both the consumer and the producer are on the same physical machine, the impact of possible resource contention (e.g., CPU time, CPU cache, memory bandwidth) should be considered. The impact will be very small for modern, multi-core machines with lots of memory bandwidth and cache, but for small devices (e.g., IoT devices) it may be very significant.

### Metrics

- **Streaming throughput (in statements)** – throughput of the streaming process, measured in RDF statements (triples or quads) per second. This is calculated as the total number of RDF statements streamed divided by the total time taken to serialize, transmit, and deserialized them.
- **Streaming throughput (in elements)** – additionally, the throughput may be measured in terms of stream elements (RDF graphs or RDF datasets) per second.

## Results

**See the results for this task reported by the community: [RESULTS](results.md).**

## This task in benchmarks outside of RiverBench

- In the paper about the Jelly streaming protocol, such a benchmark is performed in Section IV.D. The authors have measured the end-to-end throughput of several methods (over Kafka and gRPC) in terms of the number of triples transmitted per second. In the experiment, both the producer and the consumer were running on the same physical machine and various network conditions were simulated using the NetEm Linux kernel module.
    - Sowiński, P., Wasielewska-Michniewska, K., Ganzha, M., & Paprzycki, M. (2022, October). Efficient RDF streaming for the edge-cloud continuum. In 2022 IEEE 8th World Forum on Internet of Things (WF-IoT) (pp. 1-8). IEEE. [https://doi.org/10.1109/WF-IoT54382.2022.10152225](https://doi.org/10.1109/WF-IoT54382.2022.10152225)

## See also

- Version of this task focusing on stream latency, not throughput: [`stream-latency-end-to-end`](../stream-latency-end-to-end/index.md)
- Isolated serialization throughput task: [`stream-serialization-throughput`](../stream-serialization-throughput/index.md)
- Isolated deserialization throughput task: [`stream-deserialization-throughput`](../stream-deserialization-throughput/index.md)


## Metadata



!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/tasks/stream-throughput-end-to-end.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/tasks/stream-throughput-end-to-end.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/tasks/stream-throughput-end-to-end.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/tasks/stream-throughput-end-to-end.jelly)**
    <br>:material-github: Source repository: **[category-stream](https://github.com/RiverBench/category-stream)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/v/dev/tasks/stream-throughput-end-to-end`](https://w3id.org/riverbench/v/dev/tasks/stream-throughput-end-to-end)



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: End-to-end RDF streaming throughput _(<abbr title="English">en</abbr>)_
- **<abbr title="An account of the resource.">Description</abbr>**: A benchmark task measuring the throughput of streaming elements in a grouped RDF stream over the network, including serialization, network communication, and deserialization. _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-throughput-end-to-end`
- **<abbr title="The version indicator (name or identifier) of a resource.">Version</abbr>**: `dev`
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
    - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
    - **<abbr title="This axiom needed so that Protege loads DCAT 3 without errors.">Homepage</abbr>**:     
        -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
        - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [stream (dev)](https://w3id.org/riverbench/v/dev/categories/stream)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

