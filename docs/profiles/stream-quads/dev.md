# stream-quads (development version)

Streaming quads (RDF 1.1 standard only)

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming quads (standard)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-quads
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: [stream-graphs (dev)](https://w3id.org/riverbench/profiles/stream-graphs/dev)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-quads-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-quads-rdfstar-nonstandard/dev)
    - [stream-mixed (dev)](https://w3id.org/riverbench/profiles/stream-mixed/dev)
    - [stream-mixed-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-nonstandard/dev)
    - [stream-quads-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-quads-nonstandard/dev)
    - [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar-nonstandard/dev)
    - [stream-quads-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-quads-rdfstar/dev)
    - [stream-mixed-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [https://w3id.org/riverbench/](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**:     
            - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
            - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
    - **Has restriction (2)**    
        - **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
    - **Has restriction (3)**    
        - **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**:     
            - <abbr title="Graph streams are a special case of quad streams, where each element contains exactly one named RDF graph.">Graphs</abbr> ([rb:graphs](https://w3id.org/riverbench/schema/metadata#graphs))
            - <abbr title="Quad streams consist of elements, where each element is an RDF dataset.">Quads</abbr> ([rb:quads](https://w3id.org/riverbench/schema/metadata#quads))
