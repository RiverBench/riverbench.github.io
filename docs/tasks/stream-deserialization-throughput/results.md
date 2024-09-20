<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/dev/tasks/stream-deserialization-throughput/results "Link to the permanent URL of this resource.")</div><div markdown><abbr title="This page is entirely automatically generated and cannot be edited.">:material-lock-reset: Auto-generated</abbr></div></div>

# Benchmark results for task stream-deserialization-throughput

[:octicons-arrow-left-24: Back to task definition](index.md)

<div style="text-align: center" markdown>[:material-star-plus: Report your benchmark results](../../documentation/reporting-results.md){ .md-button }</div>

### RiverBench results for task stream-deserialization-throughput with profile stream-mixed-rdfstar

<span id="RAvhuNcn-wJqqlt62ICv5Z5mjCGcZTFMV8U7CNWeOPjTo"></span>

!!! info

    :fontawesome-solid-diagram-project: This benchmark result was reported in a Nanopublication: [https://w3id.org/np/RAvhuNcn-wJqqlt62ICv5Z5mjCGcZTFMV8U7CNWeOPjTo](https://w3id.org/np/RAvhuNcn-wJqqlt62ICv5Z5mjCGcZTFMV8U7CNWeOPjTo).

    The documentation here was generated automatically.




- **<abbr title="A description of the subject resource.">Comment</abbr>**: Grouped streaming deserialization (parsing) throughput benchmark, comparing Jelly to W3C serializations implemented in Apache Jena, as well as Jena's own binary formats. The benchmark was run on a modern x86-64 workstation.
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**:  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
- **<abbr title="Date of creation of the resource.">Date Created</abbr>**: `2024-09-13T07:24:29.089Z`
- **<abbr title="The citing entity cites the cited entity as source of data.">Cites as data source</abbr>**: [https://w3id.org/jelly/1.0.x/performance/#grouped-streaming-deserialization-throughput](https://w3id.org/jelly/1.0.x/performance/#grouped-streaming-deserialization-throughput)
- **<abbr title="This property specifies the protocol that a benchmark follows">Has followed protocol</abbr>**: 
    - **Type**:     
        - <abbr title="The parameters of a performed benchmark (rb:PerformedBenchmark). Instances of this class specify the RiverBench profile, task, systems, and metrics that were used in the benchmark.">Benchmark protocol</abbr> ([rb:BenchmarkProtocol](https://w3id.org/riverbench/schema/metadata#BenchmarkProtocol))
        - <abbr title="A protocol is used to provide guidelines to execute certain tasks">Protocol</abbr> ([irao:Protocol](http://ontology.ethereal.cz/irao/Protocol))
    - **<abbr title="Indicates that the subject is using a specific RiverBench benchmark task.">Uses benchmark task</abbr>**: [stream-deserialization-throughput (2.1.0)](https://w3id.org/riverbench/v/2.1.0/tasks/stream-deserialization-throughput)
    - **<abbr title="Indicates that the subject is using a specific RiverBench benchmark profile.">Uses benchmark profile</abbr>**: [stream-mixed-rdfstar (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/stream-mixed-rdfstar)
    - **<abbr title="Indicates a benchmark metric that is used in a benchmark. Values of this property should be specified as the name of the metric, in the exact spelling as in the corresponding task definition. For example: 'Loading throughput'.">Uses metric</abbr>**: Deserialization throughput (in statements)
    - **<abbr title="Indicates that the subject is using a specific system (e.g., an RDF store).">Uses system under test</abbr>**:     
        - JSON-LD (Apache Jena) (5.0.0)
        - Jelly (Jelly-JVM) (0.14.2)
        - N-Triples/N-Quads (Apache Jena) (5.0.0)
        - RDF binary Protobuf (Apache Jena) (5.0.0)
        - RDF binary Thrift (Apache Jena) (5.0.0)
        - RDF/XML (Apache Jena) (5.0.0)
        - Turtle/TriG (Apache Jena) (5.0.0)
- **<abbr title="This property specifies a system that measures a benchmark">Has measuring system</abbr>**: [https://github.com/Jelly-RDF/jvm-benchmarks/tree/88d936a87d0dcd9f7fb5f3dc98af7d4c270711e9](https://github.com/Jelly-RDF/jvm-benchmarks/tree/88d936a87d0dcd9f7fb5f3dc98af7d4c270711e9)
