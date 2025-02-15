<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/schema/metadata/dev "Link to the permanent URL of this resource.")</div><div markdown>**[:material-database-edit: Edit ontology](https://github.com/RiverBench/schema/edit/main/src/metadata.ttl "Edit this page's ontology in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../documentation/editing-docs.md "Need help with editing?")</div></div>

Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.13.2 and [RiverBench CI worker](https://github.com/RiverBench/ci-worker).
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

    :fontawesome-solid-diagram-project: Download this ontology in RDF: **[Turtle](https://w3id.org/riverbench/schema/metadata/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/schema/metadata/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/schema/metadata/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/schema/metadata/dev.jelly)**
    <br>:material-github: Source repository: **[schema](https://github.com/RiverBench/schema)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/schema/metadata/dev`](https://w3id.org/riverbench/schema/metadata/dev)


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
* [ASCII control character count statistics](#AsciiControlCharacterCountStatistics)
* [Benchmark protocol](#BenchmarkProtocol)
* [Blank node count statistics](#BlankNodeCountStatistics)
* [Bytes per triple (byte density) statistics](#ByteDensityStatistics)
* [Benchmark category](#Category)
* [Member of a benchmark category](#CategoryMember)
* [Custom SHACL target](#CustomShaclTarget)
* [RiverBench dataset](#Dataset)
* [Datatype count statistics](#DatatypeCountStatistics)
* [Datatype literal count statistics](#DatatypeLiteralCountStatistics)
* [RiverBench dataset distribution](#Distribution)
* [RiverBench distribution type](#DistributionType)
* [Graph count statistics](#GraphCountStatistics)
* [IRI count statistics](#IriCountStatistics)
* [Language string count statistics](#LanguageLiteralCountStatistics)
* [Literal count statistics](#LiteralCountStatistics)
* [Object count statistics](#ObjectCountStatistics)
* [Performed benchmark](#PerformedBenchmark)
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
* [System under test](#SystemUnderTest)
* [Benchmark task](#Task)
* [Stream elements split by time](#TimeStreamElementSplit)
* [Stream elements split by topic](#TopicStreamElementSplit)

### Dataset series <a name="DatasetSeries"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#DatasetSeries`
Super-classes |[dcat:Dataset](http://www.w3.org/ns/dcat#Dataset) (c)<br />
Sub-classes |[Benchmark profile](#Profile) (c)<br />

### ASCII control character count statistics <a name="AsciiControlCharacterCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#AsciiControlCharacterCountStatistics`
Description | Statistics about the number of ASCII control characters except HT, LF, and CR (0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F) in literals. These characters are allowed in RDF literals, but some serializations (e.g., RDF/XML) may not be able to encode them. See the documentation page "Dataset compatibility notes" for more details.
Super-classes |[Statistics](#Statistics) (c)<br />

### Benchmark protocol <a name="BenchmarkProtocol"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#BenchmarkProtocol`
Description | The parameters of a performed benchmark (rb:PerformedBenchmark). Instances of this class specify the RiverBench profile, task, systems, and metrics that were used in the benchmark.
Super-classes |[irao:Protocol](http://ontology.ethereal.cz/irao/Protocol) (c)<br />
Restrictions |[Uses system under test](#usesSystemUnderTest) (op) **some** [System under test](#SystemUnderTest) (c)<br />[Uses benchmark profile](#usesProfile) (op) **some** [Benchmark profile](#Profile) (c)<br />[Uses benchmark task](#usesTask) (op) **some** [Benchmark task](#Task) (c)<br />[Uses metric](#usesMetric) (dp) **some** [xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />

### Blank node count statistics <a name="BlankNodeCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics`
Description | Statistics about the number of blank nodes in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### Bytes per triple (byte density) statistics <a name="ByteDensityStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#ByteDensityStatistics`
Description | Statistics about the number of bytes needed to encode a single statement in the N-Triples/N-Quads formats. One newline character is included for each statement.  This statistic can be used as a proxy to estimate how much "information" is in an average statement in the dataset when it is uncompressed.
Super-classes |[Statistics](#Statistics) (c)<br />

### Benchmark category <a name="Category"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#Category`
Description | Class for benchmark categories in RiverBench. A category groups tasks and profiles that are compatible with each other. Each task and profile in a category has a name prefixed with the name of the category (e.g., all tasks in the "stream" category start with "stream-").
Super-classes |[dcat:Resource](http://www.w3.org/ns/dcat#Resource) (c)<br />
In domain of |[Has benchmark task](#hasTask) (op)<br />[Has category member](#hasCategoryMember) (op)<br />[Has benchmark profile](#hasProfile) (op)<br />
In range of |[Has benchmark category](#hasCategory) (op)<br />[In benchmark category](#inCategory) (fp)<br />

### Member of a benchmark category <a name="CategoryMember"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#CategoryMember`
Description | Superclass for both profiles and tasks
Super-classes |[dcat:Resource](http://www.w3.org/ns/dcat#Resource) (c)<br />
Sub-classes |[Benchmark task](#Task) (c)<br />[Benchmark profile](#Profile) (c)<br />
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
Super-classes |[irao:Dataset](http://ontology.ethereal.cz/irao/Dataset) (c)<br />[dcat:Dataset](http://www.w3.org/ns/dcat#Dataset) (c)<br />
Restrictions |[https://w3id.org/stax/ontology#hasStreamTypeUsage](https://w3id.org/stax/ontology#hasStreamTypeUsage) **some** [https://w3id.org/stax/ontology#ConcreteRdfStreamType](https://w3id.org/stax/ontology#ConcreteRdfStreamType) (c)<br />
In domain of |[Has stream element split](#hasStreamElementSplit) (op)<br />

### Datatype count statistics <a name="DatatypeCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#DatatypeCountStatistics`
Description | Statistics about the count of datatypes (NOT datatype literals) in the dataset. This statistic does not include rdf:langString and xsd:string.
Super-classes |[Statistics](#Statistics) (c)<br />

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
In domain of |[Has statistics set](#hasStatisticsSet) (op)<br />[Has distribution type](#hasDistributionType) (op)<br />[Has file name](#hasFileName) (dp)<br />

### RiverBench distribution type <a name="DistributionType"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#DistributionType`
Description | Type of dataset distribution, indicating the corresponding streaming task formulation.
In range of |[Has distribution type](#hasDistributionType) (op)<br />
Has members |[Partial distribution](#partialDistribution)<br />[Flat distribution](#flatDistribution)<br />[Jelly distribution](#jellyDistribution)<br />[Stream distribution](#streamDistribution)<br />[Full distribution](#fullDistribution)<br />

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

### Performed benchmark <a name="PerformedBenchmark"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#PerformedBenchmark`
Description | A benchmark that was performed with a specific set of systems under test, using a RiverBench task and a RiverBench profile (collection of datasets). Instances of this class refer to, for examples, specific benchmarks described in research papers.
Super-classes |[irao:Benchmark](http://ontology.ethereal.cz/irao/Benchmark) (c)<br />
Restrictions |[irao:hasFollowedProtocol](http://ontology.ethereal.cz/irao/hasFollowedProtocol) **some** [Benchmark protocol](#BenchmarkProtocol) (c)<br />

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
Super-classes |[Dataset series](#DatasetSeries) (c)<br />[Member of a benchmark category](#CategoryMember) (c)<br />
In domain of |[Has distribution shape](#hasDistributionShape) (op)<br />[Is subset of profile](#isSubsetOfProfile) (op)<br />[Is superset of profile](#isSupersetOfProfile) (op)<br />[Has dataset shape](#hasDatasetShape) (op)<br />
In range of |[Is subset of profile](#isSubsetOfProfile) (op)<br />[Is superset of profile](#isSupersetOfProfile) (op)<br />[Has benchmark profile](#hasProfile) (op)<br />[Uses benchmark profile](#usesProfile) (op)<br />

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
Sub-classes |[Datatype literal count statistics](#DatatypeLiteralCountStatistics) (c)<br />[Statement count statistics](#StatementCountStatistics) (c)<br />[Object count statistics](#ObjectCountStatistics) (c)<br />[Blank node count statistics](#BlankNodeCountStatistics) (c)<br />[ASCII control character count statistics](#AsciiControlCharacterCountStatistics) (c)<br />[IRI count statistics](#IriCountStatistics) (c)<br />[Quoted triple count statistics](#QuotedTripleCountStatistics) (c)<br />[Predicate count statistics](#PredicateCountStatistics) (c)<br />[Bytes per triple (byte density) statistics](#ByteDensityStatistics) (c)<br />[Subject count statistics](#SubjectCountStatistics) (c)<br />[Simple literal count statistics](#SimpleLiteralCountStatistics) (c)<br />[Datatype count statistics](#DatatypeCountStatistics) (c)<br />[Literal count statistics](#LiteralCountStatistics) (c)<br />[Graph count statistics](#GraphCountStatistics) (c)<br />[Language string count statistics](#LanguageLiteralCountStatistics) (c)<br />
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
Sub-classes |[Stream elements split by statement count](#StatementCountStreamElementSplit) (c)<br />[Stream elements split by time](#TimeStreamElementSplit) (c)<br />[Stream elements split by topic](#TopicStreamElementSplit) (c)<br />
In range of |[Has stream element split](#hasStreamElementSplit) (op)<br />

### Subject count statistics <a name="SubjectCountStatistics"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics`
Description | Statistics about the number of subjects in the dataset.
Super-classes |[Statistics](#Statistics) (c)<br />

### System under test <a name="SystemUnderTest"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#SystemUnderTest`
Description | A system that is tested in a benchmark (for example, an RDF store).  Instances of this class should at least have a label (rdfs:label) and a version tag (rb:hasVersion).
Super-classes |[irao:System](http://ontology.ethereal.cz/irao/System) (c)<br />[dcat:Resource](http://www.w3.org/ns/dcat#Resource) (c)<br />
In range of |[Uses system under test](#usesSystemUnderTest) (op)<br />

### Benchmark task <a name="Task"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#Task`
Description | Class for specific benchmark tasks (e.g., end-to-end streaming latency). Each task belongs to one benchmark category (rb:Category).
Super-classes |[Member of a benchmark category](#CategoryMember) (c)<br />[irao:Methodology](http://ontology.ethereal.cz/irao/Methodology) (c)<br />
In range of |[Uses benchmark task](#usesTask) (op)<br />[Has benchmark task](#hasTask) (op)<br />

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
[Uses benchmark profile](#usesProfile),
[Uses resource](#usesResource),
[Uses system under test](#usesSystemUnderTest),
[Uses benchmark task](#usesTask),

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

### Uses benchmark profile <a name="usesProfile"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#usesProfile`
Description | Indicates that the subject is using a specific RiverBench benchmark profile.
Super-properties |[Uses resource](#usesResource) (op)<br />
Range(s) |[Benchmark profile](#Profile) (c)<br />

### Uses resource <a name="usesResource"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#usesResource`
Description | Indicates that the subject is using the object (a dcat:Resource) in some way.
Super-properties |[dct:relation](http://purl.org/dc/terms/relation)<br />
Range(s) |[dcat:Resource](http://www.w3.org/ns/dcat#Resource) (c)<br />

### Uses system under test <a name="usesSystemUnderTest"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#usesSystemUnderTest`
Description | Indicates that the subject is using a specific system (e.g., an RDF store).
Super-properties |[Uses resource](#usesResource) (op)<br />
Range(s) |[System under test](#SystemUnderTest) (c)<br />

### Uses benchmark task <a name="usesTask"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#usesTask`
Description | Indicates that the subject is using a specific RiverBench benchmark task.
Super-properties |[irao:hasMethodology](http://ontology.ethereal.cz/irao/hasMethodology)<br />[Uses resource](#usesResource) (op)<br />
Range(s) |[Benchmark task](#Task) (c)<br />


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
[version](#version),
[Conformance property](#conformanceProperty),
[Conforms to W3C RDF 1.1 specification](#conformsToRdf11),
[Conforms to W3C RDF-star draft specification as of December 17, 2021](#conformsToRdfStarDraft_20211217),
[Has file name](#hasFileName),
[Has stream element count](#hasStreamElementCount),
[Has version (deprecated)](#hasVersion),
[Maximum](#maximum),
[Mean](#mean),
[Minimum](#minimum),
[Standard deviation](#standardDeviation),
[Statistical property](#statisticalProperty),
[Sum](#sum),
[Unique count](#uniqueCount),
[Unique count lower bound estimate](#uniqueCountLowerBound),
[Unique count upper bound estimate](#uniqueCountUpperBound),
[Uses generalized RDF datasets](#usesGeneralizedRdfDatasets),
[Uses generalized triples](#usesGeneralizedTriples),
[Uses metric](#usesMetric),
[Uses RDF-star](#usesRdfStar),

### version <a name="version"></a>
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#version`

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
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />

### Has version (deprecated) <a name="hasVersion"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#hasVersion`
Description | Version tag of an artifact. This property is deprecated since RiverBench schema release 2.2.0 and will be removed in version 2.3.0. Use dcat:version instead.
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />

### Maximum <a name="maximum"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#maximum`
Description | Maximum value of a distribution
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:double](http://www.w3.org/2001/XMLSchema#double) (c)<br />[xsd:long](http://www.w3.org/2001/XMLSchema#long) (c)<br />

### Mean <a name="mean"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#mean`
Description | Arithmetic mean of a distribution
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:double](http://www.w3.org/2001/XMLSchema#double) (c)<br />

### Minimum <a name="minimum"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#minimum`
Description | Minimum value of a distribution
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:long](http://www.w3.org/2001/XMLSchema#long) (c)<br />[xsd:double](http://www.w3.org/2001/XMLSchema#double) (c)<br />

### Standard deviation <a name="standardDeviation"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#standardDeviation`
Description | Standard deviation of a distribution
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:double](http://www.w3.org/2001/XMLSchema#double) (c)<br />

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
Range(s) |[xsd:long](http://www.w3.org/2001/XMLSchema#long) (c)<br />[xsd:double](http://www.w3.org/2001/XMLSchema#double) (c)<br />

### Unique count <a name="uniqueCount"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#uniqueCount`
Description | Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value may be estimated using a HyperLogLog sketch. In that case, rb:uniqueCountLowerBound and rb:uniqueCountLowerBound properties are also set on the subject.
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:long](http://www.w3.org/2001/XMLSchema#long) (c)<br />

### Unique count lower bound estimate <a name="uniqueCountLowerBound"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#uniqueCountLowerBound`
Description | Lower bound estimate of how many unique elements are in the entire dataset. The estimate is given for a 95% confidence interval.
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:long](http://www.w3.org/2001/XMLSchema#long) (c)<br />

### Unique count upper bound estimate <a name="uniqueCountUpperBound"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#uniqueCountUpperBound`
Description | Upper bound estimate of how many unique elements are in the entire dataset. The estimate is given for a 95% confidence interval.
Super-properties |[Statistical property](#statisticalProperty) (dp)<br />
Range(s) |[xsd:long](http://www.w3.org/2001/XMLSchema#long) (c)<br />

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

### Uses metric <a name="usesMetric"></a>
Property | Value
--- | ---
URI | `https://w3id.org/riverbench/schema/metadata#usesMetric`
Description | Indicates a benchmark metric that is used in a benchmark. Values of this property should be specified as the name of the metric, in the exact spelling as in the corresponding task definition. For example: "Loading throughput".
Super-properties |[owl:topDataProperty](http://www.w3.org/2002/07/owl#topDataProperty)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />

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
* **irao**
    * `http://ontology.ethereal.cz/irao/`
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