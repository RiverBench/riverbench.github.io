# End-to-end streaming latency

A benchmark task measuring the latency of streaming elements in a grouped RDF stream over the network, including serialization, network communication, and deserialization.

## Methodology

### Data

Stream distributions of any dataset in the [`stream` category](../../categories/stream/index.md) of RiverBench may be used for this task.

### Workload

The task consists of setting up two network applications: the **producer** and the **consumer**. The producer is tasked with serializing a grouped RDF stream and sending it over the network to the consumer. The consumer receives the serialized data and deserializes it. This benchmark task measures the time taken to serialize, transmit, and deserialize each individual element in the stream.

The task may be considered in the constrained or unconstrained variant:

- **Constrained** – the producer sends stream elements at a fixed rate, and the consumer processes them as they arrive. This simulates a scenario in which the stream is not saturated, found for example in IoT sensor networks.
- **Unconstrained** – the producer sends stream elements as fast as possible, and the consumer processes them as they arrive. This simulates a scenario in which the stream is saturated, found for example in large cloud-based systems.

In both cases, the producer should reactively slow down to not overload the consumer or the network. The producer may use various backpressure mechanisms to achieve this.

To isolate the performance of the streaming process itself, the following steps are taken:

- The data (RDF graphs/datasets) is preloaded into the memory of the producer before the benchmark starts.
- The RDF data is stored by the producer in a data structure that is trivially iterable (e.g., an array of arrays or an array of sets).
- The experiment is repeated multiple times to amortize the cost of the initial setup, just-in-time code recompilation, and other external factors.
- The test stream should be large enough to reasonably emulate a real-world scenario. A run of at least 1000 stream elements should be enough to trigger any potential performance issues.
- The consumer receives the serialized data and deserializes it, but the deserialized statements are not inserted into any data structure or database, but just temporarily stored in memory and immediately discarded. This is to avoid the overhead of maintaining additional data structures.
    - When possible, the deserialized data should NOT be inserted into a data structure dedicated for RDF graphs or datasets, as these typically include additional processing steps (e.g., updating indexes) that are not part of the deserialization process. Instead, the deserialized statements should ideally be simply iterated over and discarded or inserted into an array.

### Technical notes

- Various streaming protocols may be used in the experiments, such as MQTT, Kafka, or gRPC. A common example of such a setup would be to send stream elements (RDF graphs) as Turtle files over MQTT.
- The network communication may be simulated locally (e.g., using loopback interfaces) or over a real network connection. The latter may introduce additional variability in the results due to network latency, bandwidth, and other factors.
    - Alternatively, specific network conditions may be simulated using tools like `tc` (Linux Traffic Control, NetEm kernel module) or network emulators.
- When both the consumer and the producer are on the same physical machine, the impact of possible resource contention (e.g., CPU time, CPU cache, memory bandwidth) should be considered. The impact will be very small for modern, multi-core machines with lots of memory bandwidth and cache, but for small devices (e.g., IoT devices) it may be very significant.
- When the producer and the consumer are on different physical machines, achieving sub-millisecond accuracy in latency measurement will be very challenging. Specialized timing hardware may be used for this purpose.
    - Alternatively, the producer and the consumer may be placed on the same machine (or even in the same process) so that they can share a common monotonic clock for latency measurements. Such a clock is available, e.g., in Java as `System.nanoTime()`.

### Metrics

- Latency of streaming a stream element, measured typically in milliseconds. The measurement starts when the producer begins serializing the element and ends when the consumer finishes deserializing it.

## Results

There are no results with RiverBench available for this task yet.

## Examples and references

- In the paper about the Jelly streaming protocol, such a benchmark is performed in Section IV.E. The authors have measured the end-to-end latency of several methods (over Kafka and gRPC) in terms of the number of triples transmitted per second. In the experiment, both the producer and the consumer were running on the same physical machine (in the same Java Virtual Machine) and various network conditions were simulated using the NetEm Linux kernel module. The latency measurement was done using the machine's monotonic clock.
    - Sowiński, P., Wasielewska-Michniewska, K., Ganzha, M., & Paprzycki, M. (2022, October). Efficient RDF streaming for the edge-cloud continuum. In 2022 IEEE 8th World Forum on Internet of Things (WF-IoT) (pp. 1-8). IEEE.
    - https://doi.org/10.1109/WF-IoT54382.2022.10152225

## See also

- Version of this task focusing on stream throughput, not latency: [`stream-throughput-end-to-end`](../stream-throughput-end-to-end/index.md)


## Metadata



!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/tasks/stream-latency-end-to-end.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/tasks/stream-latency-end-to-end.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/tasks/stream-latency-end-to-end.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/tasks/stream-latency-end-to-end.jelly)**



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: End-to-end streaming latency _(<abbr title="English">en</abbr>)_
- **<abbr title="An account of the resource.">Description</abbr>**: A benchmark task measuring the latency of streaming elements in a grouped RDF stream over the network, including serialization, network communication, and deserialization. _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-latency-end-to-end`
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

