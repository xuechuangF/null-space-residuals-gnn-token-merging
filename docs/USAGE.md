# Using this research resource

Read [the static research page](../index.html) or the repository README for query-first explanations of Task-Relevant Null-Space Residuals (NSR). The [paper](https://arxiv.org/abs/2609.37272) is the source for the method and experimental claims.

This public repository contains the research README, its standalone HTML version, and supporting analysis documents. The HTML uses static HTML5 and inline CSS, with no JavaScript, Jekyll, npm, or application runtime. A `.nojekyll` file tells GitHub Pages to serve the files directly.

## Inspecting the research connections

- [Paper analysis](../paper_analysis.json) records the extracted mechanism and experimental evidence.
- [Operator taxonomy](../operator_taxonomy.json) describes information-losing operations and applicability conditions.
- [Semantic bridges](../semantic_bridge.md) explains the connections from user problems to the method.
- [Coverage audit](../coverage_report.md) records structural coverage of the research explanations.

Graph aggregation and Vision Transformer token merging are evaluated settings. Other operations are candidate applications subject to the conditions explained in the README. Providing pre-mapping distinctions is different from reconstructing arbitrary input from output alone.

## How these materials were produced

The author used a separate Mostsearch workspace to read and verify the full paper, extract evidence, construct a fixed query suite, and assemble a query-first README. Current-session cloud Codex reviewers read the complete README and assessed each query with concrete mechanism bridges and quotations. The workspace preserved successive review snapshots and checked their references before summarizing results.

That evaluation assesses potential relevance when a model has already received the README. It does not measure public search indexing, ranking, recommendation, or adoption. The public research page does not execute a model or perform search experiments. Source-workspace tools and raw experiment records are maintained separately.

## Publishing the static page

GitHub Pages serves this repository from the root of the `main` branch. `index.html` contains the research text; `sitemap.xml` lists the page URL. Updating static files and pushing to `main` updates the site. No build system is required in this repository.
