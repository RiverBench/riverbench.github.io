{{ top_buttons() }}

# Release notes

This page lists all stable releases of RiverBench. You can switch between releases using the version selector in the top navigation bar. If you are looking for the development version of the documentation (which can be edited), click [here](https://w3id.org/riverbench/).

See also: [versioning and releases documentation](documentation/versioning.md).

## RiverBench 2.2.0

**Not released yet**

...

- Notable changes:
    - Updated the CI worker to Apache Jena 5, which came with minor changes to the dataset distribution format. ([#120](https://github.com/RiverBench/RiverBench/issues/120))
    - Introduced dataset distribution stability guarantees. ([#120](https://github.com/RiverBench/RiverBench/issues/120))
    - Changed the datatypes of some statistical properties in the metadata from `xsd:integer` and `xsd:decimal` to `xsd:long` and `xsd:double`. ([#134](https://github.com/RiverBench/RiverBench/issues/134))


## [RiverBench 2.1.0](https://w3id.org/riverbench/v/2.1.0)

**Release date: 2024-08-29**

Minor release focusing on improving the user experience and quality of the documentation. Most notably, it added a system for reporting benchmark results. One new dataset was added.

- Notable changes:
    - Introduced a system for reporting benchmark results with nanopublications. ([#101](https://github.com/RiverBench/RiverBench/issues/101), [#104](https://github.com/RiverBench/RiverBench/issues/104), [#105](https://github.com/RiverBench/RiverBench/issues/105))
    - Added a quick start guide. ([#73](https://github.com/RiverBench/RiverBench/issues/73))
    - Remodeled the main page layout. ([#109](https://github.com/RiverBench/RiverBench/issues/109))
    - Improved the contributor experience with new documentation and better UX (including the new "Edit this page" buttons). ([#53](https://github.com/RiverBench/RiverBench/issues/53), [#73](https://github.com/RiverBench/RiverBench/issues/73), [#87](https://github.com/RiverBench/RiverBench/issues/87), [#111](https://github.com/RiverBench/RiverBench/issues/111))
    - Made the permanent URLs of pages easier to find and access. ([#52](https://github.com/RiverBench/RiverBench/issues/52))
    - Added the release notes page. ([#88](https://github.com/RiverBench/RiverBench/issues/88))
    - Improved the accessibility of dataset download links. ([#86](https://github.com/RiverBench/RiverBench/issues/86))
    - Added statistics on the number of ASCII control characters in datasets. ([#115](https://github.com/RiverBench/RiverBench/issues/115))
    - Improved the clarity of many labels and descriptions.
    - Removed `*-nonstandard` profiles, as there were no matching datasets and the profiles were never used. ([#99](https://github.com/RiverBench/RiverBench/issues/99))
- Datasets:
    - Added a new dataset: `openaire-lod`. ([#95](https://github.com/RiverBench/RiverBench/issues/95))
    - Created a new PATCH release for the remaining datasets due to metadata updates.
- Resolved 29 issues – see the [full list](https://github.com/RiverBench/RiverBench/milestone/4?closed=1).

## [RiverBench 2.0.1](https://w3id.org/riverbench/v/2.0.1)

**Release date: 2024-06-07**

Patch release with minor improvements to the metadata.

- Notable changes:
    - Added unique subject/predicate/object counts to the dataset statistics. ([#89](https://github.com/RiverBench/RiverBench/issues/89))
    - Updated the `flat-rdf-store-loading` task description. ([#93](https://github.com/RiverBench/RiverBench/issues/93))
- Datasets:
    - Created a new PATCH release for all datasets due to metadata updates.
- Resolved 3 issues – see the [full list](https://github.com/RiverBench/RiverBench/milestone/5?closed=1).

## [RiverBench 2.0.0](https://w3id.org/riverbench/v/2.0.0)

**Release date: 2024-05-30**

Major release which restructured RiverBench, introducing the notions of categories and tasks.

- Notable changes:
    - Introduced benchmark categories (`flat` and `stream`). ([#62](https://github.com/RiverBench/RiverBench/issues/62))
    - Introduced the benchmark task system along with 9 new tasks. ([#63](https://github.com/RiverBench/RiverBench/issues/63))
    - Restructured the CI/CD pipelines and the metadata system to support tasks and categories. ([#65](https://github.com/RiverBench/RiverBench/issues/65))
    - Added a new metadata dump system. ([#42](https://github.com/RiverBench/RiverBench/issues/42))
    - Added [Jelly](https://w3id.org/jelly) as a new serialization format for dataset distributions and metadata. ([#45](https://github.com/RiverBench/RiverBench/issues/45), [#49](https://github.com/RiverBench/RiverBench/issues/49))
    to RiverBench's metadata. ([#55](https://github.com/RiverBench/RiverBench/issues/55), [#56](https://github.com/RiverBench/RiverBench/issues/56))
    - Added SHACL validation checks for user-editable metadata. ([#66](https://github.com/RiverBench/RiverBench/issues/66))
    - Added dataset previews to the dataset pages. ([#28](https://github.com/RiverBench/RiverBench/issues/28))
    - Improved the presentation of dataset statistics (tables instead of lists). ([#31](https://github.com/RiverBench/RiverBench/issues/31))
    - Changed the stream type system to [RDF-STaX](https://w3id.org/stax) and added the RDF-STaX ontology to RiverBench metadata. ([#55](https://github.com/RiverBench/RiverBench/issues/55), [#56](https://github.com/RiverBench/RiverBench/issues/56))
- Datasets:
    - Created a new PATCH release for all datasets due to metadata updates.
- Resolved 34 issues – see the [full list](https://github.com/RiverBench/RiverBench/milestone/2?closed=1).

## [RiverBench 1.0.0 / 1.0.1](https://w3id.org/riverbench/v/1.0.1)

**Release date: 2023-09-21**

Initial release of RiverBench.

- Added 12 initial datasets:
    - `assist-iot-weather` ([#25](https://github.com/RiverBench/RiverBench/issues/25))
    - `assist-iot-weather-graphs` ([#25](https://github.com/RiverBench/RiverBench/issues/25))
    - `citypulse-traffic` ([#21](https://github.com/RiverBench/RiverBench/issues/21))
    - `citypulse-traffic-graphs` ([#22](https://github.com/RiverBench/RiverBench/issues/22))
    - `dbpedia-live` ([#35](https://github.com/RiverBench/RiverBench/issues/35))
    - `digital-agenda-indicators` ([#24](https://github.com/RiverBench/RiverBench/issues/24))
    - `linked-spending` ([#18](https://github.com/RiverBench/RiverBench/issues/18))
    - `lod-katrina` ([#16](https://github.com/RiverBench/RiverBench/issues/16))
    - `muziekweb` ([#34](https://github.com/RiverBench/RiverBench/issues/34))
    - `nanopubs` ([#14](https://github.com/RiverBench/RiverBench/issues/14))
    - `politiquices` ([#17](https://github.com/RiverBench/RiverBench/issues/17))
    - `yago-annotated-facts` ([#15](https://github.com/RiverBench/RiverBench/issues/15))
- Resolved 26 issues – see the [full list](https://github.com/RiverBench/RiverBench/milestone/1?closed=1).    
