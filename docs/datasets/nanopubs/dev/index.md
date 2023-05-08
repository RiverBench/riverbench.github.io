# nanopubs (development version)

Nanopublications are small units of publishable information, used for scientific results and more. This dataset is based on a subset of [a dump of all available nanopublications](https://zenodo.org/record/1213293) as of April 5, 2018. Only the first 5M of freely-licensed nanopubs were included. Each nanopub consists of several RDF graphs and thus is an RDF dataset. The included data is primarily from the biomedical domain. More information: [paper](https://arxiv.org/abs/1809.06532), [website](https://nanopub.net/).

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/datasets/nanopubs/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/datasets/nanopubs/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/datasets/nanopubs/dev.rdf)**
    <br>Source repository: **[nanopubs](https://github.com/RiverBench/dataset-nanopubs)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Nanopublications
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: nanopubs
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - <abbr title="Datasets with bibliographical information.">Bibliographical</abbr> ([rbt:bibliographical](https://w3id.org/riverbench/schema/theme#bibliographical))
    - <abbr title="Datasets with biomedical information.">Biomedical</abbr> ([rbt:biomedical](https://w3id.org/riverbench/schema/theme#biomedical))
    - <abbr title="Datasets with scientific information.">Scientific</abbr> ([rbt:scientific](https://w3id.org/riverbench/schema/theme#scientific))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **Authors of the included nanopublications (cited within the dataset) (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Authors of the included nanopublications (cited within the dataset)
    - **Tobias Kuhn (2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Tobias Kuhn
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://orcid.org/0000-0002-1267-0234](https://orcid.org/0000-0002-1267-0234)
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: Author of the [nanopublications dump](https://zenodo.org/record/1213293)
    - **Piotr Sowiński (3)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**:     
            -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
            - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC-BY-SA-3.0](https://spdx.org/licenses/CC-BY-SA-3.0)
- **<abbr title="A related resource from which the described resource is derived.">Source</abbr>**: [https://doi.org/10.5281/zenodo.1213293](https://doi.org/10.5281/zenodo.1213293)
- **<abbr title="Information about rights held in and over the resource.">Rights</abbr>**: This dataset only includes freely-licensed publications (CC BY, CC BY-SA, or ODbL licenses). Each nanopublication includes information about its original authors and is self-citing. The dataset is marked as under CC BY-SA, as this is the most restrictive license in the dataset.
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-04-30
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2023-05-08
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

## Technical metadata

- **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Quad streams consist of elements, where each element is an RDF dataset.">Quads</abbr> ([rb:quads](https://w3id.org/riverbench/schema/metadata#quads))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5,000,000
- **<abbr title="Indicates how the stream was split into elements.">Has stream element split</abbr>**: 
    - **Type**: <abbr title="The elements correspond to different topics/subjects in the dataset.">Stream elements split by topic</abbr> ([rb:TopicStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each stream element is one nanopublication.
- **<abbr title="Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.">Uses ontology</abbr>**: 
    - [http://purl.org/dc/terms/](http://purl.org/dc/terms/)
    - [http://www.nanopub.org/nschema#](http://www.nanopub.org/nschema#)
    - [https://www.w3.org/ns/prov-o](https://www.w3.org/ns/prov-o)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no

## Distributions

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-100k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nq.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 35.73 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b38c9d95416a30a353ac46192f6ab18accc77084`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `7180fd388408b9e48075afa559dacf89`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_100K.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_100K.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 400,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,207,266
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 32.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.94
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 27
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 33

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,100,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 21
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 21

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,307,350
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.94
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 29
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 925,880
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.26
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.55
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 400,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 158
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,907,266
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 671,463
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 49.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.94
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 44
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 50

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 300,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 60,104
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 700,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 60,262
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 7

##### PlainLiteralCountStatistics

- **Type**: PlainLiteralCountStatistics ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nq.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3.47 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e2415dd8ec272c94922beb79f2a025146d2db319`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `6d6e1ec6871a259250b61bab84d0d810`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_10K.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_10K.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 40,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 330,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 33
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 33

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 210,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 21
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 21

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 340,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 34.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 34
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 10
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 40,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 17
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 500,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 73,219
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 50.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 50
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 50

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 30,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 6,857
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 70,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 6,874
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 7

##### PlainLiteralCountStatistics

- **Type**: PlainLiteralCountStatistics ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="flat-1m"></a> 1M elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-1m
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_1M.nq.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 384.61 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1e2dec57fc8ceb1c212c994d0c8ea04c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `9171cabf2cca60d5180de3ddfb0438115b65121f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_1M.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_1M.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,000,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 32,151,723
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 32.15
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.09
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 27
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 89

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20,738,344
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 20.74
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.94
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 17
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 33,423,542
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.42
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 4.64
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 28
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 135

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9,350,387
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.35
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.33
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 52

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,266,443
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 89,864
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.27
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.94
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 48,861,863
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 7,017,131
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 48.86
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.03
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 40
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 100

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,763,885
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 530,740
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.76
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.81
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 7,030,328
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 620,603
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.03
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.24
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22

##### PlainLiteralCountStatistics

- **Type**: PlainLiteralCountStatistics ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: flat_full.nq.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.68 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `387dc1e1adc92f2fd91b6c315fdf9436`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `110d9c128ca0d9e48f806086a373ea3639cf94f4`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_full.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_full.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20,000,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 159,866,280
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 31.97
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.03
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 14
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 157

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 97,782,581
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 19.56
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.81
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 171,885,662
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 34.38
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 9.93
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 16
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 196

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 46,588,350
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.32
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 4.43
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 68

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 27,015,713
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2,243,795
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.40
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.74
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 236,997,015
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 47,162,247
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 47.40
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.68
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 25
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 142

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 8,627,838
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 1,033,269
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.73
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.48
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 32

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 35,643,551
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 3,277,169
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.13
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34

##### PlainLiteralCountStatistics

- **Type**: PlainLiteralCountStatistics ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="stream-100k"></a> 100K elements quad stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements quad stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 25.59 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1ec474e8cf6f413927ad75c236fb37cf`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5686c28882ff1c322214e418d461ab932fc952c5`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 400,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,207,266
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 32.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.94
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 27
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 33

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,100,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 21
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 21

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,307,350
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.94
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 29
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 925,880
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.26
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.55
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 400,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 158
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,907,266
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 671,463
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 49.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.94
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 44
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 50

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 300,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 60,104
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 700,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 60,262
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 7

##### PlainLiteralCountStatistics

- **Type**: PlainLiteralCountStatistics ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="stream-10k"></a> 10K elements quad stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements quad stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 2.55 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5bae0e97c5462ec43bf8c00551e10456254d92c5`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c1ee0262644d85f9a514cf243a297212`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 40,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 330,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 33
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 33

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 210,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 21
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 21

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 340,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 34.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 34
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 10
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 40,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 17
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 500,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 73,219
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 50.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 50
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 50

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 30,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 6,857
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 70,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 6,874
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 7

##### PlainLiteralCountStatistics

- **Type**: PlainLiteralCountStatistics ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="stream-1m"></a> 1M elements quad stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements quad stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-1m
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_1M.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 277.16 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `eac1b7777fd273e2276d308ea529caa9`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3b0946513e3c376ab69e7c1ab5749b6912dd4493`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,000,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 32,151,723
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 32.15
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.09
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 27
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 89

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20,738,344
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 20.74
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.94
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 17
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 33,423,542
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.42
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 4.64
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 28
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 135

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9,350,387
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.35
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.33
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 52

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,266,443
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 89,864
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.27
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.94
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 48,861,863
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 7,017,131
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 48.86
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.03
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 40
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 100

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,763,885
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 530,740
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.76
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.81
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 7,030,328
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 620,603
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.03
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.24
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22

##### PlainLiteralCountStatistics

- **Type**: PlainLiteralCountStatistics ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="stream-full"></a> Full quad stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full quad stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: stream_full.tar.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.02 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `cff09e24cdf0aae097d18164065cbea9f61d4eba`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a6c475b30bd2cdffe9304747414b2154`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20,000,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 159,866,280
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 31.97
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.03
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 14
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 157

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 97,782,581
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 19.56
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.81
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 171,885,662
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 34.38
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 9.93
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 16
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 196

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 46,588,350
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.32
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 4.43
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 68

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 27,015,713
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2,243,795
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.40
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.74
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 236,997,015
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 47,162,247
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 47.40
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.68
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 25
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 142

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 8,627,838
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 1,033,269
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.73
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.48
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 32

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 35,643,551
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 3,277,169
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.13
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34

##### PlainLiteralCountStatistics

- **Type**: PlainLiteralCountStatistics ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

