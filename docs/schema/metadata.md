Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.13.2 and [RiverBench CI worker](https://github.com/RiverBench/ci-worker)
# RiverBench metadata ontology


## Metadata
* **URI**
    * `https://w3id.org/riverbench/schema/metadata`
* **Creators(s)**
    * [Piotr Sowiński](https://orcid.org/0000-0002-2543-9461)
    [[0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461)]
* **Created**
    * 2023-04-30T00:00:00
* **Issued**
    * 2023-05-05T00:00:00
* **Version URI**
    * [https://w3id.org/riverbench/schema/metadata/dev](https://w3id.org/riverbench/schema/metadata/dev)
* **Imports**
    * [http://www.w3.org/ns/dcat](http://www.w3.org/ns/dcat)
    * [https://w3id.org/stax/1.1.0/ontology](https://w3id.org/stax/1.1.0/ontology)
* **License**
    * [https://spdx.org/licenses/CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0)


!!! info

    Download this ontology in RDF: **[Turtle](https://w3id.org/riverbench/schema/metadata/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/schema/metadata/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/schema/metadata/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/schema/metadata/dev.jelly)**


### Description
Ontology for describing datasets and profiles in the RiverBench benchmark suite.


## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#object-properties)
1. [Functional Properties](#functionalproperties)
1. [Datatype Properties](#datatype-properties)
1. [Named Individuals](#named-individuals)
1. [Namespaces](#namespaces)
1. [Legend](#legend)




## Classes
* [Dataset series](#DatasetSeries)
* [Blank node count statistics](#BlankNodeCountStatistics)
* [Benchmark category](#Category)
* [Member of a benchmark category](#CategoryMember)
* [Custom SHACL target](#CustomShaclTarget)
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
* [Quoted triple count statistics](#QuotedTripleCountStatistics)
* [RiverBench suite](#RiverBench)
* [Simple literal count statistics](#SimpleLiteralCountStatistics)
* [Statement count statistics](#StatementCountStatistics)
* [Stream elements split by statement count](#StatementCountStreamElementSplit)
* [Statistics](#Statistics)
* [Statistics set](#StatisticsSet)
* [Stream element split](#StreamElementSplit)
* [Subject count statistics](#SubjectCountStatistics)
* [Benchmark task](#Task)
* [Stream elements split by time](#TimeStreamElementSplit)
* [Stream elements split by topic](#TopicStreamElementSplit)

### Dataset series <a name="DatasetSeries"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#DatasetSeries`
Super-classes |[dcat:Dataset](http://www.w3.org/ns/dcat#Dataset) (c)<br />
Sub-classes |[Benchmark profile](#Profile) (c)<br />

### Blank node count statistics <a name="BlankNodeCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics`
Description | Statistics about the number of blank nodes in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Benchmark category <a name="Category"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#Category`
Description | Class for benchmark categories in RiverBench. A category groups tasks and profiles that are compatible with each other. Each task and profile in a category has a name prefixed with the name of the category (e.g., all tasks in the "stream" category start with "stream-").
Super-classes |[dcat:Resource](http://www.w3.org/ns/dcat#Resource) (c)<br />
In domain of |[Has category member](#hasCategoryMember) (op)<br />[Has benchmark profile](#hasProfile) (op)<br />[Has benchmark task](#hasTask) (op)<br />
In range of |[In benchmark category](#inCategory) (fp)<br />[Has benchmark category](#hasCategory) (op)<br />

### Member of a benchmark category <a name="CategoryMember"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#CategoryMember`
Description | Superclass for both profiles and tasks
Super-classes |[dcat:Resource](http://www.w3.org/ns/dcat#Resource) (c)<br />
Sub-classes |[Benchmark profile](#Profile) (c)<br />[Benchmark task](#Task) (c)<br />
In domain of |[In benchmark category](#inCategory) (fp)<br />
In range of |[Has category member](#hasCategoryMember) (op)<br />

### Custom SHACL target <a name="CustomShaclTarget"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#CustomShaclTarget`
Description | A class for all custom SHACL-like node targets in RiverBench. See also rb:targetCustom.
In range of |[Target custom](#targetCustom) (op)<br />
Has members |[YAGO annotated facts target](#yagoTarget)<br />

### RiverBench dataset <a name="Dataset"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#Dataset`
Description | A dataset in the RiverBench benchmark suite
Super-classes |[dcat:Dataset](http://www.w3.org/ns/dcat#Dataset) (c)<br />
Restrictions |[https://w3id.org/stax/ontology#hasStreamTypeUsage](https://w3id.org/stax/ontology#hasStreamTypeUsage) **some** [https://w3id.org/stax/ontology#ConcreteRdfStreamType](https://w3id.org/stax/ontology#ConcreteRdfStreamType) (c)<br />
In domain of |[Has stream element split](#hasStreamElementSplit) (op)<br />

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
Restrictions |[https://w3id.org/stax/ontology#hasStreamTypeUsage](https://w3id.org/stax/ontology#hasStreamTypeUsage) **some** [https://w3id.org/stax/ontology#ConcreteRdfStreamType](https://w3id.org/stax/ontology#ConcreteRdfStreamType) (c)<br />
In domain of |[Has statistics set](#hasStatisticsSet) (op)<br />[Has file name](#hasFileName) (dp)<br />[Has distribution type](#hasDistributionType) (op)<br />

### RiverBench distribution type <a name="DistributionType"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#DistributionType`
Description | Type of dataset distribution, indicating the corresponding streaming task formulation.
In range of |[Has distribution type](#hasDistributionType) (op)<br />
Has members |[Partial distribution](#partialDistribution)<br />[Jelly distribution](#jellyDistribution)<br />[Flat distribution](#flatDistribution)<br />[Full distribution](#fullDistribution)<br />[Stream distribution](#streamDistribution)<br />

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
Description | Benchmark profile grouping several datasets in RiverBench. Each profile belongs to one benchmark category (rb:Category).
Super-classes |[Member of a benchmark category](#CategoryMember) (c)<br />[Dataset series](#DatasetSeries) (c)<br />
In domain of |[Has distribution shape](#hasDistributionShape) (op)<br />[Is subset of profile](#isSubsetOfProfile) (op)<br />[Has dataset shape](#hasDatasetShape) (op)<br />[Is superset of profile](#isSupersetOfProfile) (op)<br />
In range of |[Has benchmark profile](#hasProfile) (op)<br />[Is subset of profile](#isSubsetOfProfile) (op)<br />[Is superset of profile](#isSupersetOfProfile) (op)<br />

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
In domain of |[Has benchmark category](#hasCategory) (op)<br />

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
Description | The number of statements in an element was the criterion for splitting the stream elements.
Super-classes |[Stream element split](#StreamElementSplit) (c)<br />

### Statistics <a name="Statistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#Statistics`
Description | Class for statistics objects about distributions
Sub-classes |[Object count statistics](#ObjectCountStatistics) (c)<br />[Quoted triple count statistics](#QuotedTripleCountStatistics) (c)<br />[Datatype literal count statistics](#DatatypeLiteralCountStatistics) (c)<br />[Statement count statistics](#StatementCountStatistics) (c)<br />[Subject count statistics](#SubjectCountStatistics) (c)<br />[Predicate count statistics](#PredicateCountStatistics) (c)<br />[Simple literal count statistics](#SimpleLiteralCountStatistics) (c)<br />[Graph count statistics](#GraphCountStatistics) (c)<br />[Language string count statistics](#LanguageLiteralCountStatistics) (c)<br />[IRI count statistics](#IriCountStatistics) (c)<br />[Blank node count statistics](#BlankNodeCountStatistics) (c)<br />[Literal count statistics](#LiteralCountStatistics) (c)<br />
In domain of |[Statistical property](#statisticalProperty) (dp)<br />
In range of |[Has statistics](#hasStatistics) (op)<br />

### Statistics set <a name="StatisticsSet"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#StatisticsSet`
Description | Class for groupings (sets) of statistics about distributions
In domain of |[Has statistics](#hasStatistics) (op)<br />
In range of |[Has statistics set](#hasStatisticsSet) (op)<br />

### Stream element split <a name="StreamElementSplit"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#StreamElementSplit`
Description | Describes how was the stream split into individual elements.
Sub-classes |[Stream elements split by time](#TimeStreamElementSplit) (c)<br />[Stream elements split by topic](#TopicStreamElementSplit) (c)<br />[Stream elements split by statement count](#StatementCountStreamElementSplit) (c)<br />
In range of |[Has stream element split](#hasStreamElementSplit) (op)<br />

### Subject count statistics <a name="SubjectCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics`
Description | Statistics about the number of subjects in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Benchmark task <a name="Task"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#Task`
Description | Class for specific benchmark tasks (e.g., end-to-end streaming latency). Each task belongs to one benchmark category (rb:Category).
Super-classes |[Member of a benchmark category](#CategoryMember) (c)<br />
In range of |[Has benchmark task](#hasTask) (op)<br />

### Stream elements split by time <a name="TimeStreamElementSplit"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#TimeStreamElementSplit`
Description | The elements correspond to different instants or intervals of time.
Super-classes |[Stream element split](#StreamElementSplit) (c)<br />
In domain of |[Has temporal property](#hasTemporalProperty) (op)<br />

### Stream elements split by topic <a name="TopicStreamElementSplit"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit`
Description | The elements correspond to different topics/subjects in the dataset.
Super-classes |[Stream element split](#StreamElementSplit) (c)<br />
In domain of |[Has subject shape](#hasSubjectShape) (op)<br />


## Object Properties
[isPartOf](#isPartOf),
[inCatalog](#inCatalog),
[resource](#resource),
[Includes dataset](#seriesMember),
[Has benchmark category](#hasCategory),
[Has category member](#hasCategoryMember),
[Has dataset shape](#hasDatasetShape),
[Has distribution shape](#hasDistributionShape),
[Has distribution type](#hasDistributionType),
[Has benchmark profile](#hasProfile),
[Has shape](#hasShape),
[Has statistics](#hasStatistics),
[Has statistics set](#hasStatisticsSet),
[Has stream element split](#hasStreamElementSplit),
[Has subject shape](#hasSubjectShape),
[Has benchmark task](#hasTask),
[Has temporal property](#hasTemporalProperty),
[Is subset of profile](#isSubsetOfProfile),
[Is superset of profile](#isSupersetOfProfile),
[Target custom](#targetCustom),

### isPartOf <a name="isPartOf"></a>
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/isPartOf`
Super-properties |[dct:relation](http://purl.org/dc/terms/relation)<br />

### inCatalog <a name="inCatalog"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#inCatalog`
Super-properties |[isPartOf](#isPartOf) (op)<br />
Domain(s) |[dcat:Resource](http://www.w3.org/ns/dcat#Resource) (c)<br />
Range(s) |[dcat:Catalog](http://www.w3.org/ns/dcat#Catalog) (c)<br />

### resource <a name="resource"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#resource`
Super-properties |[dct:hasPart](http://purl.org/dc/terms/hasPart)<br />

### Includes dataset <a name="seriesMember"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#seriesMember`
Description | Indicates which datasets are included in the profile
Super-properties |[dct:relation](http://purl.org/dc/terms/relation)<br />

### Has benchmark category <a name="hasCategory"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasCategory`
Description | Indicates that a benchmark category belongs to this benchmark suite.
Super-properties |[resource](#resource) (op)<br />
Domain(s) |[RiverBench suite](#RiverBench) (c)<br />
Range(s) |[Benchmark category](#Category) (c)<br />

### Has category member <a name="hasCategoryMember"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasCategoryMember`
Description | For benchmark categories, indicates their members (profiles or tasks).
Super-properties |[dct:hasPart](http://purl.org/dc/terms/hasPart)<br />
Domain(s) |[Benchmark category](#Category) (c)<br />
Range(s) |[Member of a benchmark category](#CategoryMember) (c)<br />

### Has dataset shape <a name="hasDatasetShape"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasDatasetShape`
Description | Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.
Super-properties |[Has shape](#hasShape) (op)<br />
Domain(s) |[Benchmark profile](#Profile) (c)<br />
Range(s) |[sh:NodeShape](http://www.w3.org/ns/shacl#NodeShape) (c)<br />

### Has distribution shape <a name="hasDistributionShape"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasDistributionShape`
Description | Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.
Super-properties |[Has shape](#hasShape) (op)<br />
Domain(s) |[Benchmark profile](#Profile) (c)<br />
Range(s) |[sh:NodeShape](http://www.w3.org/ns/shacl#NodeShape) (c)<br />

### Has distribution type <a name="hasDistributionType"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasDistributionType`
Description | Indicates the type of RiverBench dataset distribution
Domain(s) |[RiverBench dataset distribution](#Distribution) (c)<br />
Range(s) |[RiverBench distribution type](#DistributionType) (c)<br />

### Has benchmark profile <a name="hasProfile"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasProfile`
Description | For benchmark categories this property indicates profiles that belong to the category.
Super-properties |[Has category member](#hasCategoryMember) (op)<br />
Domain(s) |[Benchmark category](#Category) (c)<br />
Range(s) |[Benchmark profile](#Profile) (c)<br />

### Has shape <a name="hasShape"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasShape`
Description | Property for specifying the desired SHACL shape of something (e.g., a dataset or a distribution).
Range(s) |[sh:NodeShape](http://www.w3.org/ns/shacl#NodeShape) (c)<br />

### Has statistics <a name="hasStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasStatistics`
Description | Has a dataset statistics object
Domain(s) |[Statistics set](#StatisticsSet) (c)<br />
Range(s) |[Statistics](#Statistics) (c)<br />

### Has statistics set <a name="hasStatisticsSet"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasStatisticsSet`
Description | Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.
Domain(s) |[RiverBench dataset distribution](#Distribution) (c)<br />
Range(s) |[Statistics set](#StatisticsSet) (c)<br />

### Has stream element split <a name="hasStreamElementSplit"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasStreamElementSplit`
Description | Indicates how the stream was split into elements.
Super-properties |[owl:topObjectProperty](http://www.w3.org/2002/07/owl#topObjectProperty)<br />
Domain(s) |[RiverBench dataset](#Dataset) (c)<br />
Range(s) |[Stream element split](#StreamElementSplit) (c)<br />

### Has subject shape <a name="hasSubjectShape"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasSubjectShape`
Description | Indicates the subject node in an RDF subject graph stream, using SHACL. The value of this property should be a SHACL sh:NodeShape with a specified target (e.g., sh:targetSubjectsOf). Only the target will be considered, restrictions on the shape will be ignored.  This property is required for RDF subject graph streams. Only sh:targetClass, sh:targetSubjectsOf, and sh:targetObjectsOf are allowed as the target specification.  This property can be specified multiple times. The different target specifications will then be treated as alternatives.
Super-properties |[Has shape](#hasShape) (op)<br />
Domain(s) |[Stream elements split by topic](#TopicStreamElementSplit) (c)<br />
Range(s) |[sh:NodeShape](http://www.w3.org/ns/shacl#NodeShape) (c)<br />

### Has benchmark task <a name="hasTask"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasTask`
Description | For benchmark categories this property indicates tasks that belong to the category.
Super-properties |[Has category member](#hasCategoryMember) (op)<br />
Domain(s) |[Benchmark category](#Category) (c)<br />
Range(s) |[Benchmark task](#Task) (c)<br />

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
Super-properties |[dct:relation](http://purl.org/dc/terms/relation)<br />
Domain(s) |[Benchmark profile](#Profile) (c)<br />
Range(s) |[Benchmark profile](#Profile) (c)<br />

### Is superset of profile <a name="isSupersetOfProfile"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#isSupersetOfProfile`
Description | Indicates that this profile contains all datasets of the other profile
Super-properties |[dct:relation](http://purl.org/dc/terms/relation)<br />
Domain(s) |[Benchmark profile](#Profile) (c)<br />
Range(s) |[Benchmark profile](#Profile) (c)<br />

### Target custom <a name="targetCustom"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#targetCustom`
Description | Custom SHACL-like node target used in RiverBench for datasets where SHACL does not provide adequate means for targeting them (e.g., for RDF-star).
Domain(s) |[sh:NodeShape](http://www.w3.org/ns/shacl#NodeShape) (c)<br />
Range(s) |[Custom SHACL target](#CustomShaclTarget) (c)<br />


## Functional Properties
[In benchmark category](#inCategory),

### In benchmark category <a name="inCategory"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#inCategory`
Description | Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).
Super-properties |[isPartOf](#isPartOf) (op)<br />
Domain(s) |[Member of a benchmark category](#CategoryMember) (c)<br />
Range(s) |[Benchmark category](#Category) (c)<br />


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
Description | The base statistical property.
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
[Jelly distribution](#jellyDistribution),
[Partial distribution](#partialDistribution),
[Stream distribution](#streamDistribution),
[YAGO annotated facts target](#yagoTarget),

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

### Jelly distribution <a name="jellyDistribution"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#jellyDistribution`
Class(es) | [RiverBench distribution type](#DistributionType)
Description | A streaming distribution in the Jelly binary format.

### Partial distribution <a name="partialDistribution"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#partialDistribution`
Class(es) | [RiverBench distribution type](#DistributionType)
Description | A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.

### Stream distribution <a name="streamDistribution"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#streamDistribution`
Class(es) | [RiverBench distribution type](#DistributionType)
Description | The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).

### YAGO annotated facts target <a name="yagoTarget"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#yagoTarget`
Class(es) | [Custom SHACL target](#CustomShaclTarget)
Description | Custom SHACL-like target for the yago-annotated-facts dataset in RiverBench. Targets the subject of any quoted triple in the graph. There is always exactly one such unique subject.

## Namespaces
* **default (rb)**
    * `https://w3id.org/riverbench/schema/metadata#`
* **dc**
    * `http://purl.org/dc/elements/1.1/`
* **dcat**
    * `http://www.w3.org/ns/dcat#`
* **dct**
    * `http://purl.org/dc/terms/`
* **foaf**
    * `http://xmlns.com/foaf/0.1/`
* **owl**
    * `http://www.w3.org/2002/07/owl#`
* **rdf**
    * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
    * `http://www.w3.org/2000/01/rdf-schema#`
* **sh**
    * `http://www.w3.org/ns/shacl#`
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