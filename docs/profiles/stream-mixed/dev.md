# stream-mixed (development version)

Streaming triples or quads (RDF 1.1 standard only)

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming triples or quads (standard)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-mixed
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: 
    - [stream-triples (dev)](https://w3id.org/riverbench/profiles/stream-triples/dev)
    - [stream-quads (dev)](https://w3id.org/riverbench/profiles/stream-quads/dev)
    - [stream-graphs (dev)](https://w3id.org/riverbench/profiles/stream-graphs/dev)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-mixed-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar/dev)
    - [stream-mixed-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-nonstandard/dev)
    - [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: [example-triples (dev)](https://w3id.org/riverbench/datasets/example-triples/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [https://w3id.org/riverbench/](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
    - **Has restriction (2)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**:     
            - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
            - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
            - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
