# Metadata

RiverBench includes rich RDF metadata for each dataset, profile, schema, and the suite itself. This metadata is used to generate the website, and can also be used by other tools. The metadata is [permissively licensed](licensing.md).

## Accessing metadata

On each dataset, profile, and schema page in this website you will find a box with links to the RDF metadata. You can also use the [HTTP content negotation mechanism](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation) to request the machine-readable metadata instead of the HTML page. This functionality is supported only when using the permanent URLs (starting with `https://w3id.org/riverbench/`).

Examples of URLs that will return the metadata with content negotiation:

* [https://w3id.org/riverbench/](https://w3id.org/riverbench/)
* [https://w3id.org/riverbench/v/dev](https://w3id.org/riverbench/v/dev)
* [https://w3id.org/riverbench/profiles/stream-triples](https://w3id.org/riverbench/profiles/stream-triples)
* [https://w3id.org/riverbench/profiles/stream-triples/dev](https://w3id.org/riverbench/profiles/stream-triples/dev)
* [https://w3id.org/riverbench/datasets/nanopubs](https://w3id.org/riverbench/datasets/nanopubs)
* [https://w3id.org/riverbench/datasets/nanopubs/dev](https://w3id.org/riverbench/datasets/nanopubs/dev)
* [https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata)
* [https://w3id.org/riverbench/schema/metadata/dev](https://w3id.org/riverbench/schema/metadata/dev)

To request a metadata file in a given format explicitly, you can also append `.nt`, `.ttl`, `.rdf`, or `.jelly` to these URLs.

The following metadata formats are supported:

- [N-Triples](https://www.w3.org/TR/n-triples/) (`.nt`, content type `application/n-triples`)
- [Turtle](https://www.w3.org/TR/turtle/) (`.ttl`, content type `text/turtle`)
- [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/) (`.rdf`, content type `application/rdf+xml`)
- [Jelly](https://github.com/Jelly-RDF) (`.jelly`, content type `application/x-jelly-rdf`)

*You can find the rules that make this work [here](https://github.com/perma-id/w3id.org/tree/master/riverbench).*

## Metadata dumps

Starting from RiverBench version 2.0.0, the entire metadata of RiverBench is published in easily accessible dumps. The dumps can be downladed from the [main page of RiverBench](https://w3id.org/riverbench/) and from the pages of the [suite releases](https://w3id.org/riverbench/v). The links to download the dump are in the "Info" box near the top of the page.

The dumps can also be downloaded directly from:

```https://w3id.org/riverbench/dumps/{version}.{extension}.gz```

where `{version}` is the version tag of the suite release (e.g., `dev` or `2.0.0`), and `{extension}` is one of `nt`, `ttl`, `rdf`, or `jelly`.

## Editing metadata

A large portion of the metadata is automatically generated. However, the rest is written manually in Turtle files in various repositories:

- [RiverBench main repo / metadata.ttl](https://github.com/RiverBench/RiverBench/blob/main/metadata.ttl) – metadata about the suite itself
- [RiverBench main repo / profiles](https://github.com/RiverBench/RiverBench/tree/main/profiles) – metadata about the profiles
- {Dataset repo} / metatada.ttl – metadata about the dataset

Feel free to submit pull requests to these files to fix errors or add new information. After the pull request is accepted, the changes will be reflected automatically in the website and the READMEs.

The metadata uses mainly these ontologies:

- [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/)
- [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
- [FOAF](http://xmlns.com/foaf/0.1/)
- [RiverBench metadata ontology](../schema/metadata/dev.md)
- [RiverBench documentation ontology](../schema/documentation/dev.md)
- [RiverBench topic classification scheme](../schema/theme/dev.md)
