Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.13.2 and [RiverBench CI worker](https://github.com/RiverBench/ci-worker)
# RiverBench metadata ontology


## Metadata
* **URI**
    * `https://w3id.org/riverbench/schema/metadata`
* **Creators(s)**
    * [Piotr Sowiński](https://orcid.org/0000-0002-2543-9461)
    [[0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461)]
* **License**
    * [https://spdx.org/licenses/CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0)


!!! info

    Download this ontology in RDF: **[Turtle](https://w3id.org/riverbench/schema/metadata/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/schema/metadata/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/schema/metadata/dev.rdf)**


### Description
Ontology for describing datasets and profiles in the RiverBench benchmark suite.


## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#object-properties)
1. [Datatype Properties](#datatype-properties)
1. [Named Individuals](#named-individuals)
1. [Namespaces](#namespaces)
1. [Legend](#legend)




## Classes
* [Dataset series](#DatasetSeries)
* [Blank node count statistics](#BlankNodeCountStatistics)
* [RiverBench dataset](#Dataset)
* [Datatype literal count statistics](#DatatypeLiteralCountStatistics)
* [RiverBench dataset distribution](#Distribution)
* [RiverBench distribution type](#DistributionType)
* [Graph count statistics](#GraphCountStatistics)
* [IRI count statistics](#IriCountStatistics)
* [Language string count statistics](#LanguageLiteralCountStatistics)
* [Literal count statistics](#LiteralCountStatistics)
* [Object count statistics](#ObjectCountStatistics)
* [Predicate count statistics](#PredicateCountStatistics)
* [Benchmark profile](#Profile)
* [Profile restriction](#ProfileRestriction)
* [Quoted triple count statistics](#QuotedTripleCountStatistics)
* [RiverBench suite](#RiverBench)
* [Simple literal count statistics](#SimpleLiteralCountStatistics)
* [Statement count statistics](#StatementCountStatistics)
* [Stream elements split by statement count](#StatementCountStreamElementSplit)
* [Statistics](#Statistics)
* [Stream element split](#StreamElementSplit)
* [Stream element type](#StreamElementType)
* [Subject count statistics](#SubjectCountStatistics)
* [Stream elements split by time](#TimeStreamElementSplit)
* [Stream elements split by topic](#TopicStreamElementSplit)

### Dataset series <a name="DatasetSeries"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#DatasetSeries`
Sub-classes |[Benchmark profile](#Profile) (c)<br />

### Blank node count statistics <a name="BlankNodeCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics`
Description | Statistics about the number of blank nodes in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### RiverBench dataset <a name="Dataset"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#Dataset`
Description | A dataset in the RiverBench benchmark suite
Super-classes |[dcat:Dataset](http://www.w3.org/ns/dcat#Dataset) (c)<br />
In domain of |[Uses ontology](#usesOntology) (op)<br />[Has stream element split](#hasStreamElementSplit) (op)<br />

### Datatype literal count statistics <a name="DatatypeLiteralCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics`
Description | Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### RiverBench dataset distribution <a name="Distribution"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#Distribution`
Description | A distribution of a dataset in the RiverBench benchmark suite.
Super-classes |[dcat:Distribution](http://www.w3.org/ns/dcat#Distribution) (c)<br />
In domain of |[Has statistics](#hasStatistics) (op)<br />[Has file name](#hasFileName) (dp)<br />

### RiverBench distribution type <a name="DistributionType"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#DistributionType`
Description | Type of dataset distribution, indicating the corresponding streaming task formulation.
In range of |[Has distribution type](#hasDistributionType) (op)<br />
Has members |[Graph stream distribution](#graphStreamDistribution)<br />[Quad stream distribution](#quadStreamDistribution)<br />[Full distribution](#fullDistribution)<br />[Partial distribution](#partialDistribution)<br />[Flat distribution](#flatDistribution)<br />[Triple stream distribution](#tripleStreamDistribution)<br />

### Graph count statistics <a name="GraphCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#GraphCountStatistics`
Description | Statistics about the number of RDF graphs in the dataset, including the default graph.
Super-classes |[Statistics](#Statistics) (c)<br />

### IRI count statistics <a name="IriCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#IriCountStatistics`
Description | Statistics about the number of IRIs in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Language string count statistics <a name="LanguageLiteralCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics`
Description | Statistics about the number of language literals in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Literal count statistics <a name="LiteralCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics`
Description | Statistics about the number of literals in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Object count statistics <a name="ObjectCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics`
Description | Statistics about the number of objects in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Predicate count statistics <a name="PredicateCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics`
Description | Statistics about the number of predicates in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Benchmark profile <a name="Profile"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#Profile`
Description | Benchmark profile grouping several datasets in RiverBench
Super-classes |[Dataset series](#DatasetSeries) (c)<br />
In domain of |[Has restriction](#hasRestriction) (op)<br />[Is superset of profile](#isSupersetOfProfile) (op)<br />[Is subset of profile](#isSubsetOfProfile) (op)<br />
In range of |[Is superset of profile](#isSupersetOfProfile) (op)<br />[Is subset of profile](#isSubsetOfProfile) (op)<br />[Has benchmark profile](#hasProfile) (op)<br />

### Profile restriction <a name="ProfileRestriction"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#ProfileRestriction`
Description | Resource with properties that specify conditions for datasets to be included in the profile. The conditions are joined with the OR operator.
In range of |[Has restriction](#hasRestriction) (op)<br />

### Quoted triple count statistics <a name="QuotedTripleCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics`
Description | Statistics about the number of quoted triples in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### RiverBench suite <a name="RiverBench"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#RiverBench`
Description | RiverBench – RDF streaming benchmark suite
Super-classes |[dcat:Catalog](http://www.w3.org/ns/dcat#Catalog) (c)<br />
In domain of |[Has benchmark profile](#hasProfile) (op)<br />

### Simple literal count statistics <a name="SimpleLiteralCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics`
Description | Statistics about the number of simple literals (of type xsd:string) in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Statement count statistics <a name="StatementCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#StatementCountStatistics`
Description | Statistics about the number of RDF statements in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Stream elements split by statement count <a name="StatementCountStreamElementSplit"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#StatementCountStreamElementSplit`
Super-classes |[Stream element split](#StreamElementSplit) (c)<br />

### Statistics <a name="Statistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#Statistics`
Description | Class for statistics objects about distributions
Sub-classes |[IRI count statistics](#IriCountStatistics) (c)<br />[Language string count statistics](#LanguageLiteralCountStatistics) (c)<br />[Predicate count statistics](#PredicateCountStatistics) (c)<br />[Literal count statistics](#LiteralCountStatistics) (c)<br />[Statement count statistics](#StatementCountStatistics) (c)<br />[Quoted triple count statistics](#QuotedTripleCountStatistics) (c)<br />[Graph count statistics](#GraphCountStatistics) (c)<br />[Simple literal count statistics](#SimpleLiteralCountStatistics) (c)<br />[Subject count statistics](#SubjectCountStatistics) (c)<br />[Datatype literal count statistics](#DatatypeLiteralCountStatistics) (c)<br />[Blank node count statistics](#BlankNodeCountStatistics) (c)<br />[Object count statistics](#ObjectCountStatistics) (c)<br />
In domain of |[Statistical property](#statisticalProperty) (dp)<br />
In range of |[Has statistics](#hasStatistics) (op)<br />

### Stream element split <a name="StreamElementSplit"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#StreamElementSplit`
Description | Describes how was the stream split into individual elements.
Sub-classes |[Stream elements split by time](#TimeStreamElementSplit) (c)<br />[Stream elements split by statement count](#StatementCountStreamElementSplit) (c)<br />[Stream elements split by topic](#TopicStreamElementSplit) (c)<br />
In range of |[Has stream element split](#hasStreamElementSplit) (op)<br />

### Stream element type <a name="StreamElementType"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#StreamElementType`
Description | Indicates the type of the contents of stream elements
In range of |[Has stream element type](#hasStreamElementType) (op)<br />
Has members |[Graphs](#graphs)<br />[Triples](#triples)<br />[Quads](#quads)<br />

### Subject count statistics <a name="SubjectCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics`
Description | Statistics about the number of subjects in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Stream elements split by time <a name="TimeStreamElementSplit"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#TimeStreamElementSplit`
Super-classes |[Stream element split](#StreamElementSplit) (c)<br />
In domain of |[Has temporal property](#hasTemporalProperty) (op)<br />

### Stream elements split by topic <a name="TopicStreamElementSplit"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit`
Super-classes |[Stream element split](#StreamElementSplit) (c)<br />


## Object Properties
[Includes dataset](#seriesMember),
[Has distribution type](#hasDistributionType),
[Has benchmark profile](#hasProfile),
[Has restriction](#hasRestriction),
[Has statistics](#hasStatistics),
[Has stream element split](#hasStreamElementSplit),
[Has stream element type](#hasStreamElementType),
[Has temporal property](#hasTemporalProperty),
[Is subset of profile](#isSubsetOfProfile),
[Is superset of profile](#isSupersetOfProfile),
[Uses ontology](#usesOntology),

### Includes dataset <a name="seriesMember"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#seriesMember`
Description | Indicates which datasets are included in the profile

### Has distribution type <a name="hasDistributionType"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasDistributionType`
Description | Indicates the type of RiverBench dataset distribution
Range(s) |[RiverBench distribution type](#DistributionType) (c)<br />

### Has benchmark profile <a name="hasProfile"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasProfile`
Description | Indicates benchmark profiles that belong to this benchmark suite.
Super-properties |[dcat:resource](http://www.w3.org/ns/dcat#resource)<br />
Domain(s) |[RiverBench suite](#RiverBench) (c)<br />
Range(s) |[Benchmark profile](#Profile) (c)<br />

### Has restriction <a name="hasRestriction"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasRestriction`
Description | Has profile restriction. The restrictions are joined with the AND operator.
Domain(s) |[Benchmark profile](#Profile) (c)<br />
Range(s) |[Profile restriction](#ProfileRestriction) (c)<br />

### Has statistics <a name="hasStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasStatistics`
Description | Has a dataset statistics object
Domain(s) |[RiverBench dataset distribution](#Distribution) (c)<br />
Range(s) |[Statistics](#Statistics) (c)<br />

### Has stream element split <a name="hasStreamElementSplit"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasStreamElementSplit`
Super-properties |[owl:topObjectProperty](http://www.w3.org/2002/07/owl#topObjectProperty)<br />
Domain(s) |[RiverBench dataset](#Dataset) (c)<br />
Range(s) |[Stream element split](#StreamElementSplit) (c)<br />

### Has stream element type <a name="hasStreamElementType"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasStreamElementType`
Description | Indicates the type of contents of each stream element
Range(s) |[Stream element type](#StreamElementType) (c)<br />

### Has temporal property <a name="hasTemporalProperty"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasTemporalProperty`
Description | The IRI of the property that is used in the stream to denote time at which the event occured.
Domain(s) |[Stream elements split by time](#TimeStreamElementSplit) (c)<br />

### Is subset of profile <a name="isSubsetOfProfile"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#isSubsetOfProfile`
Description | Indicates that this profile's datasets are all in the other profile
Domain(s) |[Benchmark profile](#Profile) (c)<br />
Range(s) |[Benchmark profile](#Profile) (c)<br />

### Is superset of profile <a name="isSupersetOfProfile"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#isSupersetOfProfile`
Description | Indicates that this profile contains all datasets of the other profile
Domain(s) |[Benchmark profile](#Profile) (c)<br />
Range(s) |[Benchmark profile](#Profile) (c)<br />

### Uses ontology <a name="usesOntology"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#usesOntology`
Description | Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.
Domain(s) |[RiverBench dataset](#Dataset) (c)<br />


## Datatype Properties
[Conformance property](#conformanceProperty),
[Conforms to W3C RDF 1.1 specification](#conformsToRdf11),
[Conforms to W3C RDF-star draft specification as of December 17, 2021](#conformsToRdfStarDraft_20211217),
[Has file name](#hasFileName),
[Has stream element count](#hasStreamElementCount),
[Has version](#hasVersion),
[Maximum](#maximum),
[Mean](#mean),
[Minimum](#minimum),
[Standard deviation](#standardDeviation),
[Statistical property](#statisticalProperty),
[Sum](#sum),
[Unique count (estimated)](#uniqueCount),
[Uses generalized RDF datasets](#usesGeneralizedRdfDatasets),
[Uses generalized triples](#usesGeneralizedTriples),
[Uses RDF-star](#usesRdfStar),

### Conformance property <a name="conformanceProperty"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#conformanceProperty`
Description | Base property for all conformance data properties
Super-properties |[owl:topDataProperty](http://www.w3.org/2002/07/owl#topDataProperty)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />

### Conforms to W3C RDF 1.1 specification <a name="conformsToRdf11"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#conformsToRdf11`
Description | Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.
Super-properties |[Conformance property](#conformanceProperty) (dp)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />

### Conforms to W3C RDF-star draft specification as of December 17, 2021 <a name="conformsToRdfStarDraft_20211217"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#conformsToRdfStarDraft_20211217`
Description | Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.
Super-properties |[Conformance property](#conformanceProperty) (dp)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />

### Has file name <a name="hasFileName"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasFileName`
Description | Canonical file name of this distribution
Domain(s) |[RiverBench dataset distribution](#Distribution) (c)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />

### Has stream element count <a name="hasStreamElementCount"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasStreamElementCount`
Description | Number of elements in the stream
Super-properties |[owl:topDataProperty](http://www.w3.org/2002/07/owl#topDataProperty)<br />

### Has version <a name="hasVersion"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasVersion`
Description | Version tag of an artifact
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />

### Maximum <a name="maximum"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#maximum`
Description | Maximum value of a distribution
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />

### Mean <a name="mean"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#mean`
Description | Arithmetic mean of a distribution
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />

### Minimum <a name="minimum"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#minimum`
Description | Minimum value of a distribution
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />

### Standard deviation <a name="standardDeviation"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#standardDeviation`
Description | Standard deviation of a distribution
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />

### Statistical property <a name="statisticalProperty"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#statisticalProperty`
Domain(s) |[Statistics](#Statistics) (c)<br />

### Sum <a name="sum"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#sum`
Description | Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />

### Unique count (estimated) <a name="uniqueCount"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#uniqueCount`
Description | Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />

### Uses generalized RDF datasets <a name="usesGeneralizedRdfDatasets"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#usesGeneralizedRdfDatasets`
Description | Whether the dataset uses the non-standard generalized datasets feature. A "dataset" here is used in the same meaning as in the RDF 1.1 specification.
Super-properties |[Conformance property](#conformanceProperty) (dp)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />

### Uses generalized triples <a name="usesGeneralizedTriples"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#usesGeneralizedTriples`
Description | Whether the dataset uses the non-standard generalized triples feature
Super-properties |[Conformance property](#conformanceProperty) (dp)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />

### Uses RDF-star <a name="usesRdfStar"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#usesRdfStar`
Description | Whether the dataset uses RDF-star features.
Super-properties |[Conformance property](#conformanceProperty) (dp)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />


## Named Individuals
[Flat distribution](#flatDistribution),
[Full distribution](#fullDistribution),
[Graph stream distribution](#graphStreamDistribution),
[Graphs](#graphs),
[Partial distribution](#partialDistribution),
[Quad stream distribution](#quadStreamDistribution),
[Quads](#quads),
[Triple stream distribution](#tripleStreamDistribution),
[Triples](#triples),

### Flat distribution <a name="flatDistribution"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#flatDistribution`
Class(es) | [RiverBench distribution type](#DistributionType)
Description | The dataset is distributed as a single flat file.

### Full distribution <a name="fullDistribution"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#fullDistribution`
Class(es) | [RiverBench distribution type](#DistributionType)
Description | A full distribution, including all data in the dataset.

### Graph stream distribution <a name="graphStreamDistribution"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#graphStreamDistribution`
Class(es) | [RiverBench distribution type](#DistributionType)
Description | The dataset is distributed as a stream of named RDF graphs.

### Graphs <a name="graphs"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#graphs`
Class(es) | [Stream element type](#StreamElementType)
Description | Graph streams are a special case of quad streams, where each element contains exactly one named RDF graph.

### Partial distribution <a name="partialDistribution"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#partialDistribution`
Class(es) | [RiverBench distribution type](#DistributionType)
Description | A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.

### Quad stream distribution <a name="quadStreamDistribution"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#quadStreamDistribution`
Class(es) | [RiverBench distribution type](#DistributionType)
Description | The dataset is distributed as a stream of RDF quads.

### Quads <a name="quads"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#quads`
Class(es) | [Stream element type](#StreamElementType)
Description | Quad streams consist of elements, where each element is an RDF dataset.

### Triple stream distribution <a name="tripleStreamDistribution"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution`
Class(es) | [RiverBench distribution type](#DistributionType)
Description | The dataset is distributed as a stream of RDF triples.

### Triples <a name="triples"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#triples`
Class(es) | [Stream element type](#StreamElementType)
Description | Triple streams consist of elements, where each element is an RDF graph.

## Namespaces
* **default (rb)**
    * `https://w3id.org/riverbench/schema/metadata`
* **dcat**
    * `http://www.w3.org/ns/dcat#`
* **foaf**
    * `http://xmlns.com/foaf/0.1/`
* **owl**
    * `http://www.w3.org/2002/07/owl#`
* **rdf**
    * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
    * `http://www.w3.org/2000/01/rdf-schema#`
* **vann**
    * `http://purl.org/vocab/vann/`
* **xsd**
    * `http://www.w3.org/2001/XMLSchema#`


## Legend
* Classes: c
* Object Properties: op
* Functional Properties: fp
* Data Properties: dp
* Annotation Properties: ap
* Properties: p
* Named Individuals: ni