# DRAFT: OpenZaak codebase goverance

This document contains a draft proposal for the 'governance.md' file on the OpenZaak repository.

## Introduction

OpenZaak is:
a) an implementation the VNG Realisatie Standard APIs for Case Management (zaakgericht werken)
b) a component in a portfolio of components that together form the Zaakgericht Werken Platform

The development of OpenZaak is coordinated by the collaborative effort between municipalities leading zaakgericht werken.

The municipalities coordinate: 
* the identification of new features
* the prioritisation of backlogs and planning roadmaps 
* the financing and contracting of development and maintenance works
* the interdependencies and relationships between all components

## Governance principles

The OpenZaak community adheres to the following principles:

* Openzaak is open source.
* We're a welcoming and respectful community as mentioned in our [Code of Conduct](#Code-of-Conduct).
* Ideas and contributions accepted according to their technical merit and alignment with project objectives, scope, and design principles.
* We strive to document all changes to the OpenZaak organization, OpenZaak code repositories, and OpenZaak related activities (e.g. level, involvement, etc) in public.

That being said, it is possible some decisions may not be open or visible in this repo - particularly if they relate to other components.

It is expected that the majority of development is performed by parties that have been contractually appointed to do so.
As such, it is not currently the aim of this community to actively grow a community of contributors.

## Governance bodies

OpenZaak is governed by two bodies, a core group (kern groep) and a technical steering team.

## Core group

Responsibilities of the core group:

* Maintaining the mission, vision, values, and scope of the project
* Collecting planned features and presenting them in a unified view
* Refining the governance as needed
* Making codebase level decisions
* Resolving escalated project decisions when the subteam responsible is blocked
* Managing the OpenZaak brand
* Licensing and intellectual property changes
* Controlling access to OpenZaak assets such as hosting and project calendars
* Coordinating across componenets 

The core group is made up of representatives of the coordinating municipalities.
Representatives of market parties can be invited.

## Technical steering team

The OpenZaak technical steering team members are active contributors. As a team, they
have the joint responsibility to:

* Provide technical direction for the codebase
* Maintain a technical roadmap, an architecture and coding principles
* Resolve issues in development or conflicts between contributors
* Managing and planning releases
* Controlling rights to Open Zaak assets such as source repositories

The core group is made up of representatives of the parties contracted to do development and maintenance work, as well as representatives delegated by the coordinating municipalities.

The current team members are:

* Joeri Bekker, Maykin Media
* Sergei Maertens, Maykin Media

Any active member of the community can request to become a technical steering team
member by asking the core group.

On a day to day basis, these members are responsible for:

* Merging pull requests
* Overseeing the resolution and disclosure of security issues

If technical steering team members cannot reach consensus informally, the question at
hand should be forwarded to the technical steering team meeting.

The technical steering team meets regularly. Their agenda includes reivew of the
technical roadmap and issues that are at an impasse. The intention of the agenda is not
to review or approve all patches. This is mainly being done through the process
described in [the contributing guide](CONTRIBUTING.md#Reviews).

If more than one technical steering team member disagrees with a decision of the
technical steering team they may appeal to the core group who will make the
ultimate ruling.

## Code of Conduct

OpenZaak's Code of Conduct is explained in [this project's code of conduct](CODE_OF_CONDUCT.md).

Currently, the Technical Steering team handles Code of Conduct violations.

If the possible violation involves a team member that member will be recused from voting
on the issue. Such issues must be escalated to the core group contact, and
the core group choose to intervene.
