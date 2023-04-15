# example-triples (development version)

This is an example dataset that is a triple stream.

## Dataset information

- **Title<sup>[?](## "A name given to the resource.")</sup>**: Example triples dataset
- **Identifier<sup>[?](## "An unambiguous reference to the resource within a given context.")</sup>**: example-triples
- **Has version<sup>[?](## "Version tag of an artifact")</sup>**: dev
- **Theme<sup>[?](## "A main category of the resource. A resource can have multiple themes.")</sup>**: Abstract ([rbt:abstract](https://riverbench.github.io/schema/theme#abstract))
- **Creator<sup>[?](## "An entity responsible for making the resource.")</sup>**: 
  - **Name<sup>[?](## "A name for some thing.")</sup>**: Piotr Sowiński
  - **Nickname<sup>[?](## "A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).")</sup>**: Ostrzyciel
  - **Homepage<sup>[?](## "A homepage for some thing.")</sup>**: https://github.com/Ostrzyciel
- **License<sup>[?](## "A legal document giving official permission to do something with the resource.")</sup>**: CC0-1.0 ([http://spdx.org/licenses/CC0-1.0](http://spdx.org/licenses/CC0-1.0))
- **Date Issued<sup>[?](## "Date of formal issuance of the resource.")</sup>**: 2023-03-13
- **Date Modified<sup>[?](## "Date on which the resource was changed.")</sup>**: 2023-03-13
- **Landing page<sup>[?](## "A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.")</sup>**: https://riverbench.github.io/datasets/example-triples/dev

## Technical metadata

- **Has stream element type<sup>[?](## "Indicates the type of contents of each stream element")</sup>**: Triples<sup>[?](## "Triple streams consist of elements, where each element is an RDF graph.")</sup> ([rb:triples](https://riverbench.github.io/schema/dataset#triples))
- **Has stream element count<sup>[?](## "Number of elements in the stream")</sup>**: 132432
- **Has stream element split**: 
  - **Type**: Stream elements split by time ([rb:TimeStreamElementSplit](https://riverbench.github.io/schema/dataset#TimeStreamElementSplit))
  - **Comment<sup>[?](## "A description of the subject resource.")</sup>**: The stream is split into 1 second intervals. Each element is one observation.
- **Uses ontology<sup>[?](## "Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.")</sup>**: https://name-example/p2
- **Conforms to W3C RDF 1.1 specification<sup>[?](## "Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.")</sup>**: yes
- **Conforms to W3C RDF-star draft specification as of December 17, 2021<sup>[?](## "Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.")</sup>**: yes
- **Uses generalized triples<sup>[?](## "Whether the dataset uses the non-standard generalized triples feature")</sup>**: no
- **Uses generalized RDF datasets<sup>[?](## "Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.")</sup>**: no
- **Uses RDF-star<sup>[?](## "Whether the dataset uses RDF-star features.")</sup>**: no
- **Temporal resolution<sup>[?](## "minimum time period resolvable in a dataset.")</sup>**: PT1S

## Distributions

### 100K elements flat distribution

- **Title<sup>[?](## "A name given to the resource.")</sup>**: 100K elements flat distribution
- **Has file name<sup>[?](## "Canonical file name of this distribution")</sup>**: `flat_100K.nt.gz`
- **Has distribution type<sup>[?](## "Indicates the type of RiverBench dataset distribution")</sup>**: 
  - Flat distribution<sup>[?](## "The dataset is distributed as a single flat file.")</sup> ([rb:flatDistribution](https://riverbench.github.io/schema/dataset#flatDistribution))
  - Partial distribution<sup>[?](## "A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.")</sup> ([rb:partialDistribution](https://riverbench.github.io/schema/dataset#partialDistribution))
- **Has stream element count<sup>[?](## "Number of elements in the stream")</sup>**: 100000
- **Byte size<sup>[?](## "The size of a distribution in bytes.")</sup>**: 9578677
- **Media type<sup>[?](## "The media type of the distribution as defined by IANA")</sup>**: application/n-triples
- **Compression format<sup>[?](## "The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.")</sup>**: application/gzip
- **Checksum<sup>[?](## "The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.")</sup>**: 
  - **Checksum (1)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `3fe30c6153d278e82f7080c90a86df20`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_md5<sup>[?](## "Indicates the algorithm used was MD5")</sup> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
  - **Checksum (2)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `4968c3133b7e8fbeac804d1dc392282e800f5af5`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_sha1<sup>[?](## "Indicates the algorithm used was SHA-1")</sup> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **Download URL<sup>[?](## "The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.")</sup>**: https://riverbench.github.io/datasets/example-triples/dev/flat_100K.nt.gz

#### Has statistics<sup>[?](## "Has a dataset statistics object")</sup>

##### Blank node count statistics

- **Type**: Blank node count statistics<sup>[?](## "Statistics about the number of blank nodes in the dataset.")</sup> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/dataset#BlankNodeCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Datatype literal count statistics

- **Type**: Datatype literal count statistics<sup>[?](## "Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.")</sup> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/dataset#DatatypeLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.50348
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 550348
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 550383
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.875703025279211
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Graph count statistics

- **Type**: Graph count statistics<sup>[?](## "Statistics about the number of RDF graphs in the dataset, including the default graph.")</sup> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/dataset#GraphCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### IRI count statistics

- **Type**: IRI count statistics<sup>[?](## "Statistics about the number of IRIs in the dataset.")</sup> ([rb:IriCountStatistics](https://riverbench.github.io/schema/dataset#IriCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 7.50348
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 750348
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 12
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.87570302527921
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 3
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 12

##### Language string count statistics

- **Type**: Language string count statistics<sup>[?](## "Statistics about the number of language literals in the dataset.")</sup> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/dataset#LanguageLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Literal count statistics

- **Type**: Literal count statistics<sup>[?](## "Statistics about the number of literals in the dataset.")</sup> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/dataset#LiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.50348
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 550348
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 550383
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.875703025279211
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Object count statistics

- **Type**: Object count statistics<sup>[?](## "Statistics about the number of objects in the dataset.")</sup> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/dataset#ObjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.751406050558422
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 11.00696
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 1100696
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Predicate count statistics

- **Type**: Predicate count statistics<sup>[?](## "Statistics about the number of predicates in the dataset.")</sup> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/dataset#PredicateCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 2.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 200000
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 2

##### Quoted triple count statistics

- **Type**: Quoted triple count statistics<sup>[?](## "Statistics about the number of quoted triples in the dataset.")</sup> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/dataset#QuotedTripleCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Simple literal count statistics

- **Type**: Simple literal count statistics<sup>[?](## "Statistics about the number of simple literals (of type xsd:string) in the dataset.")</sup> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/dataset#PlainLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Statement count statistics

- **Type**: Statement count statistics<sup>[?](## "Statistics about the number of RDF statements in the dataset.")</sup> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/dataset#StatementCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.751406050558422
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 11.00696
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 1100696
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Subject count statistics

- **Type**: Subject count statistics<sup>[?](## "Statistics about the number of subjects in the dataset.")</sup> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/dataset#SubjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.875703025279211
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.50348
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 550348
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

### 100K elements triple stream distribution

- **Title<sup>[?](## "A name given to the resource.")</sup>**: 100K elements triple stream distribution
- **Has file name<sup>[?](## "Canonical file name of this distribution")</sup>**: `stream_100K.tar.gz`
- **Has distribution type<sup>[?](## "Indicates the type of RiverBench dataset distribution")</sup>**: 
  - Partial distribution<sup>[?](## "A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.")</sup> ([rb:partialDistribution](https://riverbench.github.io/schema/dataset#partialDistribution))
  - Triple stream distribution<sup>[?](## "The dataset is distributed as a stream of RDF triples.")</sup> ([rb:tripleStreamDistribution](https://riverbench.github.io/schema/dataset#tripleStreamDistribution))
- **Has stream element count<sup>[?](## "Number of elements in the stream")</sup>**: 100000
- **Byte size<sup>[?](## "The size of a distribution in bytes.")</sup>**: 12562016
- **Media type<sup>[?](## "The media type of the distribution as defined by IANA")</sup>**: text/turtle
- **Packaging format<sup>[?](## "The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.")</sup>**: application/tar
- **Compression format<sup>[?](## "The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.")</sup>**: application/gzip
- **Checksum<sup>[?](## "The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.")</sup>**: 
  - **Checksum (1)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `f9fd45aba380d5a7e8b27fe8a9fdd6df`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_md5<sup>[?](## "Indicates the algorithm used was MD5")</sup> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
  - **Checksum (2)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `ccaf669b27560080e54df7a382992681d479526d`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_sha1<sup>[?](## "Indicates the algorithm used was SHA-1")</sup> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **Download URL<sup>[?](## "The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.")</sup>**: https://riverbench.github.io/datasets/example-triples/dev/stream_100K.tar.gz

#### Has statistics<sup>[?](## "Has a dataset statistics object")</sup>

##### Blank node count statistics

- **Type**: Blank node count statistics<sup>[?](## "Statistics about the number of blank nodes in the dataset.")</sup> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/dataset#BlankNodeCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Datatype literal count statistics

- **Type**: Datatype literal count statistics<sup>[?](## "Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.")</sup> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/dataset#DatatypeLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.50348
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 550348
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 550383
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.875703025279211
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Graph count statistics

- **Type**: Graph count statistics<sup>[?](## "Statistics about the number of RDF graphs in the dataset, including the default graph.")</sup> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/dataset#GraphCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### IRI count statistics

- **Type**: IRI count statistics<sup>[?](## "Statistics about the number of IRIs in the dataset.")</sup> ([rb:IriCountStatistics](https://riverbench.github.io/schema/dataset#IriCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 7.50348
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 750348
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 12
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.87570302527921
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 3
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 12

##### Language string count statistics

- **Type**: Language string count statistics<sup>[?](## "Statistics about the number of language literals in the dataset.")</sup> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/dataset#LanguageLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Literal count statistics

- **Type**: Literal count statistics<sup>[?](## "Statistics about the number of literals in the dataset.")</sup> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/dataset#LiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.50348
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 550348
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 550383
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.875703025279211
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Object count statistics

- **Type**: Object count statistics<sup>[?](## "Statistics about the number of objects in the dataset.")</sup> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/dataset#ObjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.751406050558422
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 11.00696
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 1100696
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Predicate count statistics

- **Type**: Predicate count statistics<sup>[?](## "Statistics about the number of predicates in the dataset.")</sup> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/dataset#PredicateCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 2.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 200000
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 2

##### Quoted triple count statistics

- **Type**: Quoted triple count statistics<sup>[?](## "Statistics about the number of quoted triples in the dataset.")</sup> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/dataset#QuotedTripleCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Simple literal count statistics

- **Type**: Simple literal count statistics<sup>[?](## "Statistics about the number of simple literals (of type xsd:string) in the dataset.")</sup> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/dataset#PlainLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Statement count statistics

- **Type**: Statement count statistics<sup>[?](## "Statistics about the number of RDF statements in the dataset.")</sup> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/dataset#StatementCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.751406050558422
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 11.00696
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 1100696
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Subject count statistics

- **Type**: Subject count statistics<sup>[?](## "Statistics about the number of subjects in the dataset.")</sup> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/dataset#SubjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.875703025279211
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.50348
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 550348
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

### 10K elements flat distribution

- **Title<sup>[?](## "A name given to the resource.")</sup>**: 10K elements flat distribution
- **Has file name<sup>[?](## "Canonical file name of this distribution")</sup>**: `flat_10K.nt.gz`
- **Has distribution type<sup>[?](## "Indicates the type of RiverBench dataset distribution")</sup>**: 
  - Flat distribution<sup>[?](## "The dataset is distributed as a single flat file.")</sup> ([rb:flatDistribution](https://riverbench.github.io/schema/dataset#flatDistribution))
  - Partial distribution<sup>[?](## "A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.")</sup> ([rb:partialDistribution](https://riverbench.github.io/schema/dataset#partialDistribution))
- **Has stream element count<sup>[?](## "Number of elements in the stream")</sup>**: 10000
- **Byte size<sup>[?](## "The size of a distribution in bytes.")</sup>**: 961030
- **Media type<sup>[?](## "The media type of the distribution as defined by IANA")</sup>**: application/n-triples
- **Compression format<sup>[?](## "The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.")</sup>**: application/gzip
- **Checksum<sup>[?](## "The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.")</sup>**: 
  - **Checksum (1)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `3484b1577c130c85b9b0f3cde426aa34`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_md5<sup>[?](## "Indicates the algorithm used was MD5")</sup> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
  - **Checksum (2)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `97087a2f6550a848e99d662f211ff88736a10e6f`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_sha1<sup>[?](## "Indicates the algorithm used was SHA-1")</sup> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **Download URL<sup>[?](## "The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.")</sup>**: https://riverbench.github.io/datasets/example-triples/dev/flat_10K.nt.gz

#### Has statistics<sup>[?](## "Has a dataset statistics object")</sup>

##### Blank node count statistics

- **Type**: Blank node count statistics<sup>[?](## "Statistics about the number of blank nodes in the dataset.")</sup> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/dataset#BlankNodeCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Datatype literal count statistics

- **Type**: Datatype literal count statistics<sup>[?](## "Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.")</sup> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/dataset#DatatypeLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.5272
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 55272
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 55277
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.884000721220438
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Graph count statistics

- **Type**: Graph count statistics<sup>[?](## "Statistics about the number of RDF graphs in the dataset, including the default graph.")</sup> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/dataset#GraphCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### IRI count statistics

- **Type**: IRI count statistics<sup>[?](## "Statistics about the number of IRIs in the dataset.")</sup> ([rb:IriCountStatistics](https://riverbench.github.io/schema/dataset#IriCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 7.5272
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 75272
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 12
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.884000721220439
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 3
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 12

##### Language string count statistics

- **Type**: Language string count statistics<sup>[?](## "Statistics about the number of language literals in the dataset.")</sup> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/dataset#LanguageLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Literal count statistics

- **Type**: Literal count statistics<sup>[?](## "Statistics about the number of literals in the dataset.")</sup> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/dataset#LiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.5272
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 55272
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 55277
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.884000721220438
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Object count statistics

- **Type**: Object count statistics<sup>[?](## "Statistics about the number of objects in the dataset.")</sup> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/dataset#ObjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.768001442440876
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 11.0544
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 110544
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Predicate count statistics

- **Type**: Predicate count statistics<sup>[?](## "Statistics about the number of predicates in the dataset.")</sup> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/dataset#PredicateCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 2.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 20000
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 2

##### Quoted triple count statistics

- **Type**: Quoted triple count statistics<sup>[?](## "Statistics about the number of quoted triples in the dataset.")</sup> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/dataset#QuotedTripleCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Simple literal count statistics

- **Type**: Simple literal count statistics<sup>[?](## "Statistics about the number of simple literals (of type xsd:string) in the dataset.")</sup> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/dataset#PlainLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Statement count statistics

- **Type**: Statement count statistics<sup>[?](## "Statistics about the number of RDF statements in the dataset.")</sup> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/dataset#StatementCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.768001442440876
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 11.0544
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 110544
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Subject count statistics

- **Type**: Subject count statistics<sup>[?](## "Statistics about the number of subjects in the dataset.")</sup> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/dataset#SubjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.884000721220438
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.5272
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 55272
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

### 10K elements triple stream distribution

- **Title<sup>[?](## "A name given to the resource.")</sup>**: 10K elements triple stream distribution
- **Has file name<sup>[?](## "Canonical file name of this distribution")</sup>**: `stream_10K.tar.gz`
- **Has distribution type<sup>[?](## "Indicates the type of RiverBench dataset distribution")</sup>**: 
  - Partial distribution<sup>[?](## "A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.")</sup> ([rb:partialDistribution](https://riverbench.github.io/schema/dataset#partialDistribution))
  - Triple stream distribution<sup>[?](## "The dataset is distributed as a stream of RDF triples.")</sup> ([rb:tripleStreamDistribution](https://riverbench.github.io/schema/dataset#tripleStreamDistribution))
- **Has stream element count<sup>[?](## "Number of elements in the stream")</sup>**: 10000
- **Byte size<sup>[?](## "The size of a distribution in bytes.")</sup>**: 1259418
- **Media type<sup>[?](## "The media type of the distribution as defined by IANA")</sup>**: text/turtle
- **Packaging format<sup>[?](## "The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.")</sup>**: application/tar
- **Compression format<sup>[?](## "The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.")</sup>**: application/gzip
- **Checksum<sup>[?](## "The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.")</sup>**: 
  - **Checksum (1)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `393698900f9b38168603b835290c3f61cc3ac09c`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_sha1<sup>[?](## "Indicates the algorithm used was SHA-1")</sup> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
  - **Checksum (2)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `3bbe5751b60b25af6e229dcfef1c45dc`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_md5<sup>[?](## "Indicates the algorithm used was MD5")</sup> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **Download URL<sup>[?](## "The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.")</sup>**: https://riverbench.github.io/datasets/example-triples/dev/stream_10K.tar.gz

#### Has statistics<sup>[?](## "Has a dataset statistics object")</sup>

##### Blank node count statistics

- **Type**: Blank node count statistics<sup>[?](## "Statistics about the number of blank nodes in the dataset.")</sup> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/dataset#BlankNodeCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Datatype literal count statistics

- **Type**: Datatype literal count statistics<sup>[?](## "Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.")</sup> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/dataset#DatatypeLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.5272
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 55272
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 55277
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.884000721220438
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Graph count statistics

- **Type**: Graph count statistics<sup>[?](## "Statistics about the number of RDF graphs in the dataset, including the default graph.")</sup> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/dataset#GraphCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### IRI count statistics

- **Type**: IRI count statistics<sup>[?](## "Statistics about the number of IRIs in the dataset.")</sup> ([rb:IriCountStatistics](https://riverbench.github.io/schema/dataset#IriCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 7.5272
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 75272
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 12
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.884000721220439
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 3
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 12

##### Language string count statistics

- **Type**: Language string count statistics<sup>[?](## "Statistics about the number of language literals in the dataset.")</sup> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/dataset#LanguageLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Literal count statistics

- **Type**: Literal count statistics<sup>[?](## "Statistics about the number of literals in the dataset.")</sup> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/dataset#LiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.5272
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 55272
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 55277
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.884000721220438
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Object count statistics

- **Type**: Object count statistics<sup>[?](## "Statistics about the number of objects in the dataset.")</sup> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/dataset#ObjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.768001442440876
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 11.0544
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 110544
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Predicate count statistics

- **Type**: Predicate count statistics<sup>[?](## "Statistics about the number of predicates in the dataset.")</sup> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/dataset#PredicateCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 2.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 20000
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 2

##### Quoted triple count statistics

- **Type**: Quoted triple count statistics<sup>[?](## "Statistics about the number of quoted triples in the dataset.")</sup> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/dataset#QuotedTripleCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Simple literal count statistics

- **Type**: Simple literal count statistics<sup>[?](## "Statistics about the number of simple literals (of type xsd:string) in the dataset.")</sup> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/dataset#PlainLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Statement count statistics

- **Type**: Statement count statistics<sup>[?](## "Statistics about the number of RDF statements in the dataset.")</sup> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/dataset#StatementCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.768001442440876
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 11.0544
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 110544
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Subject count statistics

- **Type**: Subject count statistics<sup>[?](## "Statistics about the number of subjects in the dataset.")</sup> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/dataset#SubjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.884000721220438
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.5272
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 55272
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

### Full flat distribution

- **Title<sup>[?](## "A name given to the resource.")</sup>**: Full flat distribution
- **Has file name<sup>[?](## "Canonical file name of this distribution")</sup>**: flat_full.nt.gz
- **Has distribution type<sup>[?](## "Indicates the type of RiverBench dataset distribution")</sup>**: 
  - Flat distribution<sup>[?](## "The dataset is distributed as a single flat file.")</sup> ([rb:flatDistribution](https://riverbench.github.io/schema/dataset#flatDistribution))
  - Full distribution<sup>[?](## "A full distribution, including all data in the dataset.")</sup> ([rb:fullDistribution](https://riverbench.github.io/schema/dataset#fullDistribution))
- **Has stream element count<sup>[?](## "Number of elements in the stream")</sup>**: 132432
- **Byte size<sup>[?](## "The size of a distribution in bytes.")</sup>**: 12675847
- **Media type<sup>[?](## "The media type of the distribution as defined by IANA")</sup>**: application/n-triples
- **Compression format<sup>[?](## "The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.")</sup>**: application/gzip
- **Checksum<sup>[?](## "The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.")</sup>**: 
  - **Checksum (1)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `2609cf12d67822ead11b3f615e72f22092935a00`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_sha1<sup>[?](## "Indicates the algorithm used was SHA-1")</sup> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
  - **Checksum (2)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `5b62463c88d1447956428e7930abc028`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_md5<sup>[?](## "Indicates the algorithm used was MD5")</sup> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **Download URL<sup>[?](## "The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.")</sup>**: https://riverbench.github.io/datasets/example-triples/dev/flat_full.nt.gz

#### Has statistics<sup>[?](## "Has a dataset statistics object")</sup>

##### Blank node count statistics

- **Type**: Blank node count statistics<sup>[?](## "Statistics about the number of blank nodes in the dataset.")</sup> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/dataset#BlankNodeCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Datatype literal count statistics

- **Type**: Datatype literal count statistics<sup>[?](## "Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.")</sup> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/dataset#DatatypeLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.498429382626555
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 728168
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 728308
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.8756098277330424
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Graph count statistics

- **Type**: Graph count statistics<sup>[?](## "Statistics about the number of RDF graphs in the dataset, including the default graph.")</sup> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/dataset#GraphCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### IRI count statistics

- **Type**: IRI count statistics<sup>[?](## "Statistics about the number of IRIs in the dataset.")</sup> ([rb:IriCountStatistics](https://riverbench.github.io/schema/dataset#IriCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 7.498429382626555
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 993032
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 12
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.8756098277330437
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 3
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 12

##### Language string count statistics

- **Type**: Language string count statistics<sup>[?](## "Statistics about the number of language literals in the dataset.")</sup> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/dataset#LanguageLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Literal count statistics

- **Type**: Literal count statistics<sup>[?](## "Statistics about the number of literals in the dataset.")</sup> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/dataset#LiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.498429382626555
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 728168
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 728308
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.8756098277330424
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Object count statistics

- **Type**: Object count statistics<sup>[?](## "Statistics about the number of objects in the dataset.")</sup> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/dataset#ObjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.751219655466085
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 10.99685876525311
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 1456336
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Predicate count statistics

- **Type**: Predicate count statistics<sup>[?](## "Statistics about the number of predicates in the dataset.")</sup> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/dataset#PredicateCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 2.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 264864
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 2

##### Quoted triple count statistics

- **Type**: Quoted triple count statistics<sup>[?](## "Statistics about the number of quoted triples in the dataset.")</sup> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/dataset#QuotedTripleCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Simple literal count statistics

- **Type**: Simple literal count statistics<sup>[?](## "Statistics about the number of simple literals (of type xsd:string) in the dataset.")</sup> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/dataset#PlainLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Statement count statistics

- **Type**: Statement count statistics<sup>[?](## "Statistics about the number of RDF statements in the dataset.")</sup> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/dataset#StatementCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.751219655466085
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 10.99685876525311
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 1456336
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Subject count statistics

- **Type**: Subject count statistics<sup>[?](## "Statistics about the number of subjects in the dataset.")</sup> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/dataset#SubjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.8756098277330424
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.498429382626555
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 728168
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

### Full triple stream distribution

- **Title<sup>[?](## "A name given to the resource.")</sup>**: Full triple stream distribution
- **Has file name<sup>[?](## "Canonical file name of this distribution")</sup>**: stream_full.tar.gz
- **Has distribution type<sup>[?](## "Indicates the type of RiverBench dataset distribution")</sup>**: 
  - Full distribution<sup>[?](## "A full distribution, including all data in the dataset.")</sup> ([rb:fullDistribution](https://riverbench.github.io/schema/dataset#fullDistribution))
  - Triple stream distribution<sup>[?](## "The dataset is distributed as a stream of RDF triples.")</sup> ([rb:tripleStreamDistribution](https://riverbench.github.io/schema/dataset#tripleStreamDistribution))
- **Has stream element count<sup>[?](## "Number of elements in the stream")</sup>**: 132432
- **Byte size<sup>[?](## "The size of a distribution in bytes.")</sup>**: 16626831
- **Media type<sup>[?](## "The media type of the distribution as defined by IANA")</sup>**: text/turtle
- **Packaging format<sup>[?](## "The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.")</sup>**: application/tar
- **Compression format<sup>[?](## "The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.")</sup>**: application/gzip
- **Checksum<sup>[?](## "The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.")</sup>**: 
  - **Checksum (1)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `46022478252e1ee532be8fdfe10dba1c`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_md5<sup>[?](## "Indicates the algorithm used was MD5")</sup> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
  - **Checksum (2)**  
    - **Type**: Checksum<sup>[?](## "A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.")</sup> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
    - **ChecksumValue<sup>[?](## "The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.")</sup>**: `86cfc424559079aa91c3782814cb67a681b74ca9`
    - **Algorithm<sup>[?](## "Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.")</sup>**: ChecksumAlgorithm_sha1<sup>[?](## "Indicates the algorithm used was SHA-1")</sup> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **Download URL<sup>[?](## "The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.")</sup>**: https://riverbench.github.io/datasets/example-triples/dev/stream_full.tar.gz

#### Has statistics<sup>[?](## "Has a dataset statistics object")</sup>

##### Blank node count statistics

- **Type**: Blank node count statistics<sup>[?](## "Statistics about the number of blank nodes in the dataset.")</sup> ([rb:BlankNodeCountStatistics](https://riverbench.github.io/schema/dataset#BlankNodeCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Datatype literal count statistics

- **Type**: Datatype literal count statistics<sup>[?](## "Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.")</sup> ([rb:DatatypeLiteralCountStatistics](https://riverbench.github.io/schema/dataset#DatatypeLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.498429382626555
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 728168
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 728308
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.8756098277330424
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Graph count statistics

- **Type**: Graph count statistics<sup>[?](## "Statistics about the number of RDF graphs in the dataset, including the default graph.")</sup> ([rb:GraphCountStatistics](https://riverbench.github.io/schema/dataset#GraphCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### IRI count statistics

- **Type**: IRI count statistics<sup>[?](## "Statistics about the number of IRIs in the dataset.")</sup> ([rb:IriCountStatistics](https://riverbench.github.io/schema/dataset#IriCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 7.498429382626555
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 993032
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 12
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.8756098277330437
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 3
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 12

##### Language string count statistics

- **Type**: Language string count statistics<sup>[?](## "Statistics about the number of language literals in the dataset.")</sup> ([rb:LanguageLiteralCountStatistics](https://riverbench.github.io/schema/dataset#LanguageLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Literal count statistics

- **Type**: Literal count statistics<sup>[?](## "Statistics about the number of literals in the dataset.")</sup> ([rb:LiteralCountStatistics](https://riverbench.github.io/schema/dataset#LiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.498429382626555
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 728168
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 728308
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.8756098277330424
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

##### Object count statistics

- **Type**: Object count statistics<sup>[?](## "Statistics about the number of objects in the dataset.")</sup> ([rb:ObjectCountStatistics](https://riverbench.github.io/schema/dataset#ObjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.751219655466085
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 10.99685876525311
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 1456336
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Predicate count statistics

- **Type**: Predicate count statistics<sup>[?](## "Statistics about the number of predicates in the dataset.")</sup> ([rb:PredicateCountStatistics](https://riverbench.github.io/schema/dataset#PredicateCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 2.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 264864
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 2

##### Quoted triple count statistics

- **Type**: Quoted triple count statistics<sup>[?](## "Statistics about the number of quoted triples in the dataset.")</sup> ([rb:QuotedTripleCountStatistics](https://riverbench.github.io/schema/dataset#QuotedTripleCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Simple literal count statistics

- **Type**: Simple literal count statistics<sup>[?](## "Statistics about the number of simple literals (of type xsd:string) in the dataset.")</sup> ([rb:PlainLiteralCountStatistics](https://riverbench.github.io/schema/dataset#PlainLiteralCountStatistics))
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 0.0
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 0
- **Unique count<sup>[?](## "Only used for count statistics. Indicates how many unique elements are in the entire dataset.")</sup>**: 0
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 0.0
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 0
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 0

##### Statement count statistics

- **Type**: Statement count statistics<sup>[?](## "Statistics about the number of RDF statements in the dataset.")</sup> ([rb:StatementCountStatistics](https://riverbench.github.io/schema/dataset#StatementCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 5.751219655466085
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 10.99685876525311
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 1456336
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 2
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 20

##### Subject count statistics

- **Type**: Subject count statistics<sup>[?](## "Statistics about the number of subjects in the dataset.")</sup> ([rb:SubjectCountStatistics](https://riverbench.github.io/schema/dataset#SubjectCountStatistics))
- **Standard deviation<sup>[?](## "Standard deviation of a distribution")</sup>**: 2.8756098277330424
- **Mean<sup>[?](## "Arithmetic mean of a distribution")</sup>**: 5.498429382626555
- **Sum<sup>[?](## "Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.")</sup>**: 728168
- **Minimum<sup>[?](## "Minimum value of a distribution")</sup>**: 1
- **Maximum<sup>[?](## "Maximum value of a distribution")</sup>**: 10

