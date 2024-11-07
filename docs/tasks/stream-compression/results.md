<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/dev/tasks/stream-compression/results "Link to the permanent URL of this resource.")</div><div markdown><abbr title="This page is entirely automatically generated and cannot be edited.">:material-lock-reset: Auto-generated</abbr></div></div>

# Benchmark results for task stream-compression

[:octicons-arrow-left-24: Back to task definition](index.md)

<div style="text-align: center" markdown>[:material-star-plus: Report your benchmark results](../../documentation/reporting-results.md){ .md-button }</div>

### RiverBench results for task stream-compression with profile stream-mixed-rdfstar

<span id="RADdkUASknbkyfui0sONytgVueLz-U7ZgjXvvaMICoK7Y"></span>

!!! info

    :fontawesome-solid-diagram-project: This benchmark result was reported in a Nanopublication: [https://w3id.org/np/RADdkUASknbkyfui0sONytgVueLz-U7ZgjXvvaMICoK7Y](https://w3id.org/np/RADdkUASknbkyfui0sONytgVueLz-U7ZgjXvvaMICoK7Y).

    The documentation here was generated automatically.




- **<abbr title="A description of the subject resource.">Comment</abbr>**: Serialized representation size benchmark for grouped streams, comparing Jelly to W3C serializations implemented in Apache Jena, as well as Jena's own binary formats, and the RDF4J Binary RDF Format. The benchmark was run on a modern x86-64 workstation.
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**:  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
- **<abbr title="Date of creation of the resource.">Date Created</abbr>**: `2024-11-07T14:32:44.019Z`
- **<abbr title="The citing entity cites the cited entity as source of data.">Cites as data source</abbr>**: [https://w3id.org/jelly/1.0.x/performance/#grouped-streaming-serialized-size](https://w3id.org/jelly/1.0.x/performance/#grouped-streaming-serialized-size)
- **<abbr title="This property specifies the protocol that a benchmark follows">Has followed protocol</abbr>**: 
    - **Type**:     
        - <abbr title="The parameters of a performed benchmark (rb:PerformedBenchmark). Instances of this class specify the RiverBench profile, task, systems, and metrics that were used in the benchmark.">Benchmark protocol</abbr> ([rb:BenchmarkProtocol](https://w3id.org/riverbench/schema/metadata#BenchmarkProtocol))
        - <abbr title="A protocol is used to provide guidelines to execute certain tasks">Protocol</abbr> ([irao:Protocol](http://ontology.ethereal.cz/irao/Protocol))
    - **<abbr title="Indicates that the subject is using a specific RiverBench benchmark task.">Uses benchmark task</abbr>**: [stream-compression (2.1.0)](https://w3id.org/riverbench/v/2.1.0/tasks/stream-compression)
    - **<abbr title="Indicates that the subject is using a specific RiverBench benchmark profile.">Uses benchmark profile</abbr>**: [stream-mixed-rdfstar (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-mixed-rdfstar)
    - **<abbr title="Indicates a benchmark metric that is used in a benchmark. Values of this property should be specified as the name of the metric, in the exact spelling as in the corresponding task definition. For example: 'Loading throughput'.">Uses metric</abbr>**: Compression ratio
    - **<abbr title="Indicates that the subject is using a specific system (e.g., an RDF store).">Uses system under test</abbr>**:     
        - JSON-LD (Apache Jena) (5.2.0)
        - Jelly (Jelly-JVM) (2.2.2)
        - N-Triples/N-Quads (Apache Jena) (5.2.0)
        - RDF binary Protobuf (Apache Jena) (5.2.0)
        - RDF binary Thrift (Apache Jena) (5.2.0)
        - RDF/XML (Apache Jena) (5.2.0)
        - RDF4J Binary RDF Format (5.0.2)
        - Turtle/TriG (Apache Jena) (5.2.0)
- **<abbr title="This property specifies a system that measures a benchmark">Has measuring system</abbr>**: [https://github.com/Jelly-RDF/jvm-benchmarks/tree/dd58f5de0916c1223ca115052567c1fb39f4cd62](https://github.com/Jelly-RDF/jvm-benchmarks/tree/dd58f5de0916c1223ca115052567c1fb39f4cd62)

