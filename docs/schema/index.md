{{ top_buttons() }}

# Schemas & ontologies

RiverBench uses a few schemas and ontologies to describe and organize its datasets and profiles.

* **[Metadata ontology](metadata.md)** – used for describing datasets and profiles.
* **[Documentation ontology](documentation.md)** – additional properties and assertions for generating documentation pages on this website.
* **SHACL**
    * Shapes for validating metadata files in dataset repositories: [Turtle](https://w3id.org/riverbench/schema/dataset-shacl.ttl), [N-Triples](https://w3id.org/riverbench/schema/dataset-shacl.nt), [RDF/XML](https://w3id.org/riverbench/schema/dataset-shacl.rdf), [Jelly](https://w3id.org/riverbench/schema/dataset-shacl.jelly)
    * Shapes for validating category metadata files in category repositories: [Turtle](https://w3id.org/riverbench/schema/category-shacl.ttl), [N-Triples](https://w3id.org/riverbench/schema/category-shacl.nt), [RDF/XML](https://w3id.org/riverbench/schema/category-shacl.rdf), [Jelly](https://w3id.org/riverbench/schema/category-shacl.jelly)
    * Shapes for validating profile metadata files in category repositories: [Turtle](https://w3id.org/riverbench/schema/profile-shacl.ttl), [N-Triples](https://w3id.org/riverbench/schema/profile-shacl.nt), [RDF/XML](https://w3id.org/riverbench/schema/profile-shacl.rdf), [Jelly](https://w3id.org/riverbench/schema/profile-shacl.jelly)
    * Shapes for validating collections of profiles (all profiles within a category) in category repositories: [Turtle](https://w3id.org/riverbench/schema/profile-collection-shacl.ttl), [N-Triples](https://w3id.org/riverbench/schema/profile-collection-shacl.nt), [RDF/XML](https://w3id.org/riverbench/schema/profile-collection-shacl.rdf), [Jelly](https://w3id.org/riverbench/schema/profile-collection-shacl.jelly)
    * Shapes for validating task metadata files in category repositories: [Turtle](https://w3id.org/riverbench/schema/task-shacl.ttl), [N-Triples](https://w3id.org/riverbench/schema/task-shacl.nt), [RDF/XML](https://w3id.org/riverbench/schema/task-shacl.rdf), [Jelly](https://w3id.org/riverbench/schema/task-shacl.jelly)

<!-- 
    TODO: remove these manual links, put SHACL docs in subpages 
    https://github.com/RiverBench/RiverBench/issues/78
-->

!!! info

    The schemas and ontologies are versioned synchronously with each other, but independently of RiverBench itself. For a stable RiverBench release, the latest stable version of schemas/ontologies are used. For the development version of RiverBench, the latest development version of schemas/ontologies are used.

!!! tip

    You can find RDF download links for each schema/ontology on its documentation page. You can also use the [HTTP content negotation mechanism](../documentation/metadata.md) to retrieve the machine-readable information.
