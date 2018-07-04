# Contributing to bfa-shadow-priest

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to bfa-shadow-priest, which are part of efforts made by the HowToPriest Shadow Theorycrafting team. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

What should I know before I get started?
  * [SimulationCraft](https://github.com/simulationcraft/simc)
  * [Python Scripting](https://medium.com/the-renaissance-developer/python-101-the-basics-441136fb7cc3)

[How Can I Contribute?](#how-can-i-contribute)
  * [Creating Issues](#before-submitting-an-issue)
  * [Pull Requests](#pull-requests)

[Styleguides](#styleguides)
  * [Git Commit Messages](#git-commit-messages)
  * [Python Styleguide](#python-styleguide)

[Additional Notes](#additional-notes)
  * [Issue and Pull Request Labels](#issue-and-pull-request-labels)

## Code of Conduct

This project and everyone participating in it is governed by the [bfa-shadow-priest Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [publik@exiledpower.com](mailto:publik@exiledpower.com).

## I don't want to read this whole thing I just have a question!!!

* [Discord](https://discuss.atom.io)
* [HowToPriest](https://howtopriest.com/)

## How Can I Contribute?

### Creating Issues

This section guides you through submitting an issue for bfa-shadow-priest. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating issues, please check [this list](#before-submitting-an-issue) as you might find out that you don't need to create one. When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-an-issue?). Fill out [the required template](ISSUE_TEMPLATE.md), the information it asks for helps us resolve issues faster.

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

#### Before Submitting an Issue

* **Check the [FAQs on the forum](https://discuss.atom.io/c/faq)** for a list of common questions and problems.
* **Check the [SimC repo for known issues](https://github.com/simulationcraft/simc/issues)** for a list of common questions and problems.
* **Check the [WoW-BugTracker repo for known issues](https://github.com/SimCMinMax/WoW-BugTracker/issues)**

#### How Do I Submit an Issue?

Issues are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue and provide the following information by filling in [the template](ISSUE_TEMPLATE.md).

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. For example, start by explaining how you started SimC, e.g. which command exactly you used in the terminal, or the exact profile used. When listing steps, **don't just say what you did, but explain how you did it**. For example, if ran a profile, explain the settings used to run it.
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Provide relevant comparrisons between SimC behavior and in-game behavior with matching stats**
* **If the problem wasn't triggered by a specific action**, describe what you were doing before the problem happened and share more information using the guidelines below.

Provide more context by answering these questions:

* **Did the problem start happening recently** (e.g. after updating to a new version of SimC) or was this always a problem?
* If the problem started happening recently, **can you reproduce the problem in an older version of SimC?** What's the most recent version in which the problem doesn't happen? You can download older versions of SimC from [the releases page](http://downloads.simulationcraft.org/?C=M;O=D).
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.

### Pull Requests

* Fill in [the required template](PULL_REQUEST_TEMPLATE.md)
* Follow the [Python style guide](#python-styleguide).

## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Python Styleguide

* Follow [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/?)

## Additional Notes

### Issue and Pull Request Labels

This section lists the labels we use to help us track and manage issues and pull requests.

The labels are loosely grouped by their purpose, but it's not required that every issue have a label from every group or that an issue can't have more than one label from the same group.

Please open an issue if you have suggestions for new labels, and if you notice some labels are missing on some repositories, then please open an issue on that repository.

#### Type of Issue and Issue State

| Label name | Link | Description |
| ---------- | ---- | ----------- |
| `enhancement` | [search][search-bfa-shadow-priest-repo-label-enhancement] | Feature requests. |
| `bug` | [search][search-bfa-shadow-priest-repo-label-bug] | Confirmed bugs or reports that are very likely to be bugs. |
| `question` | [search][search-bfa-shadow-priest-repo-label-question] | Question inside the issue needs to be answered. |
| `help-wanted` | [search][search-bfa-shadow-priest-repo-label-help-wanted] | Needs someone to work on the issue |
| `needs-reproduction` | [search][search-bfa-shadow-priest-repo-label-needs-reproduction] | Likely bugs, but haven't been reliably reproduced. |
| `blocked` | [search][search-bfa-shadow-priest-repo-label-blocked] | Issues blocked on other issues. |
| `duplicate` | [search][search-bfa-shadow-priest-repo-label-duplicate] | Issues which are duplicates of other issues, i.e. they have been reported before. |
| `wontfix` | [search][search-bfa-shadow-priest-repo-label-wontfix] | The Priest team has decided not to fix these issues for now, either because they're working as intended or for some other reason. |
| `analysis` | [search][search-bfa-shadow-priest-repo-label-analysis] | The type of the issue requires analysis work. |
| `apl` | [search][search-bfa-shadow-priest-repo-label-apl] | The type of the issue requires APL work. |
| `simc module` | [search][search-bfa-shadow-priest-repo-label-simc-module] | The type of the issue requires simc module work. |
