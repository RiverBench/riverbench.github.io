# stream-triples-rdfstar (development version)

Streaming triples (with RDF-star)

- **InCatalog**: [https://riverbench.github.io/](https://riverbench.github.io/)

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming triples (RDF-star)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-triples-rdfstar
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: [stream-triples (dev)](https://riverbench.github.io/profiles/stream-triples/dev)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: [stream-triples-rdfstar-nonstandard (dev)](https://riverbench.github.io/profiles/stream-triples-rdfstar-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: [example-triples (dev)](https://riverbench.github.io/datasets/example-triples/dev)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://riverbench.github.io/schema/dataset#tripleStreamDistribution))
    - **Has restriction (2)**    
        - **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
    - **Has restriction (3)**    
        - **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Triple streams consist of elements, where each element is an RDF graph.">Triples</abbr> ([rb:triples](https://riverbench.github.io/schema/dataset#triples))

