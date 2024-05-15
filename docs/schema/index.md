# Schemas & ontologies

RiverBench uses a few schemas and ontologies to describe and organize its datasets and profiles.

* **[Metadata ontology](metadata.md)** – used for describing datasets and profiles.
* **[Documentation ontology](documentation.md)** – additional properties and assertions for generating documentation pages on this website.
* **SHACL**
    * Shapes for validating metadata files in dataset repositories: [Turtle](https://w3id.org/riverbench/schema/dataset-shacl.ttl), [N-Triples](https://w3id.org/riverbench/schema/dataset-shacl.nt), [RDF/XML](https://w3id.org/riverbench/schema/dataset-shacl.rdf)

<!-- TODO: remove these manual links, put SHACL docs in subpages -->

!!! info

    The schemas and ontologies are versioned synchronously with each other, but independently of RiverBench itself. For a stable RiverBench release, the latest stable version of schemas/ontologies are used. For the development version of RiverBench, the latest development version of schemas/ontologies are used.

!!! tip

    You can find RDF download links for each schema/ontology on its documentation page. You can also use the [HTTP content negotation mechanism](../documentation/metadata.md) to retrieve the machine-readable information.
