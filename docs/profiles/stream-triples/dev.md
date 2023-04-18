# stream-triples (development version)

Streaming triples (RDF 1.1 standard only)

- **InCatalog**: [https://riverbench.github.io/](https://riverbench.github.io/)

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming triples (standard)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-triples
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-triples-rdfstar (dev)](https://riverbench.github.io/profiles/stream-triples-rdfstar/dev)
    - [stream-triples-rdfstar-nonstandard (dev)](https://riverbench.github.io/profiles/stream-triples-rdfstar-nonstandard/dev)
    - [stream-triples-nonstandard (dev)](https://riverbench.github.io/profiles/stream-triples-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: [example-triples (dev)](https://riverbench.github.io/datasets/example-triples/dev)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Triple streams consist of elements, where each element is an RDF graph.">Triples</abbr> ([rb:triples](https://riverbench.github.io/schema/dataset#triples))
    - **Has restriction (2)**    
        - **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
    - **Has restriction (3)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://riverbench.github.io/schema/dataset#tripleStreamDistribution))
