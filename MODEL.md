# Concepts

## Registration Authority
* Sponsor Data Standards Group
* CDISC SHARE 
* Medidata

## DataElementConcept

# Metamodel
* IdentifiedItem - retrieved directly (without relationships) such as PermissibleValue
* DesignatableItem - anything with a name attribute
* RegisteredItem - anything to be registered (Abstract)
  * AdministeredItem - 
  * AttachedItem - 

# AdministeredItem
## Definition
* A RegisteredItem for which administrative information is recorded by the Registration Authority
  * One or more registration associations with a registration authority
  * Exactly one stewardship association
## Attributes
* creation_date
* last_update_date
* change_description
* explanatory_comment
* origin

## AttachedItem
* A RegisteredItem where registration information is captured in another item (AdministeredItem) 

## Registrar

## Lifecycle

## Biomedical Concept
* Singleton
* Composite

## ConceptualDomain

## Domains

## Value Domains
* Standard
* Enhanced
* Custom

## Context
* Design
* Capture
* Reporting
* Analysis
* Submission

## Context:Capture
* DataFormat
* Question Text
* Description
