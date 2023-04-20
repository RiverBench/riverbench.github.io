# example-triples (development version)

This is an example dataset that is a triple stream. Each element in the stream is an RDF graph. The dataset is entirely synthetic and was generated for demonstration purposes.

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Example triples dataset
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: example-triples
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: <abbr title="Datasets with abstract information (unrelated to the real world).">Abstract data</abbr> ([rbt:abstract](https://riverbench.github.io/schema/theme#abstract))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
    - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
    - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://github.com/Ostrzyciel](https://github.com/Ostrzyciel)
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: CC0-1.0 ([http://spdx.org/licenses/CC0-1.0](http://spdx.org/licenses/CC0-1.0))
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-03-13
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2023-04-18
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [example-triples (dev)](https://riverbench.github.io/datasets/example-triples/dev)

## Technical metadata

- **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Triple streams consist of elements, where each element is an RDF graph.">Triples</abbr> ([rb:triples](https://riverbench.github.io/schema/metadata#triples))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 132432
- **Has stream element split**: 
    - **Type**: Stream elements split by time ([rb:TimeStreamElementSplit](https://riverbench.github.io/schema/metadata#TimeStreamElementSplit))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The stream is split into 1 second intervals. Each element is one observation.
- **<abbr title="Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.">Uses ontology</abbr>**: [https://name-example/p2](https://name-example/p2)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no
- **<abbr title="minimum time period resolvable in a dataset.">Temporal resolution</abbr>**: PT1S

## Distributions

### 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://riverbench.github.io/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://riverbench.github.io/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 9578677
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3fe30c6153d278e82f7080c90a86df20`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `4968c3133b7e8fbeac804d1dc392282e800f5af5`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://riverbench.github.io/datasets/example-triples/dev/files/flat_100K.nt.gz](https://riverbench.github.io/datasets/example-triples/dev/files/flat_100K.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 550348
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 550383
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.50348
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.875703025279211
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://riverbench.github.io/schema/metadata#IriCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 750348
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.50348
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.87570302527921
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/metadata#LiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 550348
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 550383
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.50348
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.875703025279211
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1100696
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.00696
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.751406050558422
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 200000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1100696
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.00696
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.751406050558422
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 550348
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.50348
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.875703025279211
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

### 100K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements triple stream distribution
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://riverbench.github.io/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://riverbench.github.io/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 12559445
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `99204f4d626d5239c812af4be19bc172`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a63cb1ce815a7aec00b8c8aa7b744bfe73001cf3`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://riverbench.github.io/datasets/example-triples/dev/files/stream_100K.tar.gz](https://riverbench.github.io/datasets/example-triples/dev/files/stream_100K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 550348
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 550383
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.50348
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.875703025279211
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://riverbench.github.io/schema/metadata#IriCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 750348
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.50348
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.87570302527921
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/metadata#LiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 550348
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 550383
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.50348
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.875703025279211
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1100696
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.00696
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.751406050558422
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 200000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1100696
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.00696
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.751406050558422
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 550348
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.50348
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.875703025279211
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

### 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://riverbench.github.io/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://riverbench.github.io/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 961030
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3484b1577c130c85b9b0f3cde426aa34`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `97087a2f6550a848e99d662f211ff88736a10e6f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://riverbench.github.io/datasets/example-triples/dev/files/flat_10K.nt.gz](https://riverbench.github.io/datasets/example-triples/dev/files/flat_10K.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 55272
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 55277
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.5272
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.884000721220438
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://riverbench.github.io/schema/metadata#IriCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 75272
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.5272
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.884000721220439
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/metadata#LiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 55272
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 55277
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.5272
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.884000721220438
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 110544
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0544
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.768001442440876
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 110544
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0544
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.768001442440876
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 55272
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.5272
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.884000721220438
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

### 10K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements triple stream distribution
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://riverbench.github.io/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://riverbench.github.io/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1259357
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `92aeaa53be65446ba3b70abce9576a36102c4a46`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b24a17687595c84580633e7521e72f6d`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://riverbench.github.io/datasets/example-triples/dev/files/stream_10K.tar.gz](https://riverbench.github.io/datasets/example-triples/dev/files/stream_10K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 55272
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 55277
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.5272
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.884000721220438
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://riverbench.github.io/schema/metadata#IriCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 75272
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.5272
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.884000721220439
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/metadata#LiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 55272
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 55277
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.5272
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.884000721220438
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 110544
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0544
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.768001442440876
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 110544
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0544
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.768001442440876
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 55272
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.5272
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.884000721220438
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

### Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: flat_full.nt.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://riverbench.github.io/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://riverbench.github.io/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 132432
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 12675847
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5b62463c88d1447956428e7930abc028`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `2609cf12d67822ead11b3f615e72f22092935a00`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://riverbench.github.io/datasets/example-triples/dev/files/flat_full.nt.gz](https://riverbench.github.io/datasets/example-triples/dev/files/flat_full.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 728168
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 728308
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.498429382626555
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.8756098277330424
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://riverbench.github.io/schema/metadata#IriCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 993032
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.498429382626555
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.8756098277330437
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/metadata#LiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 728168
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 728308
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.498429382626555
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.8756098277330424
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1456336
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.99685876525311
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.751219655466085
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 264864
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1456336
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.99685876525311
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.751219655466085
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 728168
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.498429382626555
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.8756098277330424
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

### Full triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full triple stream distribution
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: stream_full.tar.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://riverbench.github.io/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://riverbench.github.io/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 132432
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 16623228
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `280f6e503e0566bcfb08f69d5deadab4`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `2decbc68dadc17e0d705a027cea90a1b4da7d0a6`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://riverbench.github.io/datasets/example-triples/dev/files/stream_full.tar.gz](https://riverbench.github.io/datasets/example-triples/dev/files/stream_full.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 728168
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 728308
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.498429382626555
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.8756098277330424
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://riverbench.github.io/schema/metadata#IriCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 993032
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.498429382626555
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.8756098277330437
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/metadata#LiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 728168
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 728308
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.498429382626555
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.8756098277330424
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1456336
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.99685876525311
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.751219655466085
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 264864
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 20
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1456336
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.99685876525311
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.751219655466085
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 728168
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.498429382626555
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.8756098277330424
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1

