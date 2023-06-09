# Data Governance Schema and Taxonomy

## Introduction

This scheme is based on the [Data Beliefs](https://www.linkedin.com/pulse/data-beliefs-eugene-morozov/) I outlined in the LinkedIn article back in 2022. It formalises Concepts, Data Containers, Data Elements, Data Ownership, Transformations and Controls. It also provides a set of common hierarchies for things such as Data Quality Dimensions and Controls.

## Usage

Import the schema into [Confluence](https://www.atlassian.com/software/confluence) with [Taxonomies for Confluence](https://dalstonsemantics.com/services/taxonomies-for-confluence/) add-on and use it to govern your organisation's data.

![Data Governance RDFS Schema in Taxonomies for Confluence](data-governance-rdfs-schema.png)

![Data Governance SKOS Taxonomy in Taxonomies for Confluence](data-governance-skos-concept-scheme.png)

## References

1. [Data](https://www.isko.org/cyclo/data) and [Information](https://www.isko.org/cyclo/information) entries in the [ISKO Encyclopedia of Knowledge Organization](https://www.isko.org/cyclo/) by Birger Hjørland.
1. [Data and Reality](https://www.goodreads.com/en/book/show/1753248.Data_and_Reality) by William Kent.
1. [Metaphors We Live By](https://www.goodreads.com/book/show/34459.Metaphors_We_Live_By) by George Lakoff and Mark Johnson.
1. [Creating a Structured Vocabulary](https://www.meetup.com/Knowledge-Organisation-London/events/284319067/) by Leonard Will.
1. [Data on the Outside vs. Data on the Inside](https://queue.acm.org/detail.cfm?id=3415014) by Pat Helland.
1. [Why not one big database? Principles for data ownership](https://www.sciencedirect.com/science/article/abs/pii/0167923694000424) by Marshall Van Alstyne, Erik Brynjolfsson, and Stuart Madnick.

## Design Decisions

1. For common properties follow schema.org naming convention for Properties (e.g., `classification` rather than `hasClassification`) to increase readability and adoption.
1. Only use "has" and "is" in property URIs and labels when it helps make the meaning clear (e.g., `hasBroaderConcept` rather than `broader` as in SKOS) to increase readability and adoption.
1. Doing away with domain and range and using names of the classes in the UIRs of the properties and, in most cases, in the labels.
1. TTL file combines the RDFS-based schema and the SKOS-based taxonomy.
1. Do away with `Term` Class for the time being to simplify the scheme. Terms are only useful when we want to specify context where the term is used explicitly (e.g., in specific business unit).
1. Do away with `DataTransferContainer` and `DataStorageContainer` classes. Data Containers are not intrinsically transfer or storage, e.g. Excel file can be used to enter, process, transfer and store data.
1. No `CriticalDataElement` Class, rather just criticality taxonomy.
1. `Control` Class is for Resources corresponding to control instances, taxonomy for types can be created to specify types of controls and their hierarchy.
1. When documenting Data Elements on Confluence people typically assume one-to-one relationship between Data Container, Concept and Data Element. To simplify data entry, yet allow query and integration with other Data Governance tools, separate set of properties were created for each of the Classes (e.g., `dataContainerCategory`, `controlCategory`)

## Attributions and Disclaimers

### APRA

Part of this work, "Data Governance Taxonomy", is a derivative of [Prudential Practice Guide CPG 235 - Managing Data Risk (September 2013)](https://www.apra.gov.au/managing-data-risk) by [Australian Prudential Regulation Authority (APRA)](https://www.apra.gov.au/) used under [Creative Commons Attribution 3.0 Australia Licence (CCBY 3.0)](www.creativecommons.org/licenses/by/3.0/au/)

This prudential practice guide is not legal advice and users are encouraged to obtain professional advice about the application of any legislation or prudential standard relevant to their particular circumstances and to exercise their own skill and care in relation to any material contained in this guide.

APRA disclaims any liability for any loss or damage arising out of any use of this prudential practice guide.

APRA do not endorse this derivative work or its author.

### World Wide Web Consortium

"The RDF Concepts Vocabulary (RDF)" and "The RDF Schema vocabulary (RDFS)" are distributed with the release without changes under [W3C® Software and Document License](https://www.w3.org/Consortium/Legal/2023/software-license).  

The RDF Concepts Vocabulary (RDF): [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#)  
Copyright © 2004-2014 World Wide Web Consortium. All Rights Reserved. This work is distributed under the [W3C® Software and Document License](https://www.w3.org/Consortium/Legal/copyright-software) in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

The RDF Concepts Vocabulary (RDF): [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#)  
Copyright © 2019 World Wide Web Consortium. All Rights Reserved. This work is distributed under the [W3C® Software and Document License](https://www.w3.org/Consortium/Legal/copyright-software) in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.