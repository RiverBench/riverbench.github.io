# Schemas & ontologies

RiverBench uses a few schemas and ontologies to describe and organize its datasets and profiles.

* **[Metadata ontology](metadata/dev.md)** – used for describing datasets and profiles.
* **[Topic scheme](theme/dev.md)** – a SKOS taxonomy of topics used to categorize datasets.
* **[Documentation ontology](documentation/dev.md)** – additional properties and assertions for generating documentation pages on this website.
* **SHACL**
    * Shapes for validating metadata files in dataset repositories: [Turtle](https://w3id.org/riverbench/schema/dataset-shacl.ttl), [N-Triples](https://w3id.org/riverbench/schema/dataset-shacl.nt), [RDF/XML](https://w3id.org/riverbench/schema/dataset-shacl.rdf)

!!! info

    The schemas and ontologies are versioned synchronously. The links above point to their latest development versions. You can find their stable versions in the menu on the left.

!!! tip

    You can find RDF download links for each schema/ontology on its documentation page. You can also use the [HTTP content negotation mechanism](../documentation/metadata.md) to retrieve the machine-readable information.
