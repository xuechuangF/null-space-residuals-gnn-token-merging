# Task-Relevant Null-Space Residuals for Improving GNN Aggregation, Token Merging, and Other Non-Injective Neural Operations

**Task-Relevant Null-Space Residuals (NSR) are a possible general performance-improvement mechanism for neural models whose aggregation, merging, pooling, compression, or other many-to-one operations hide task-relevant information.** NSR adds a task-supervised pathway that reads representations before an information-losing operation, extracts distinctions invisible to that operation, and learns how to use them downstream.

This repository explains **Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings**, by **Bizu Feng, Zhimu Yang, Shuming Wang, Yuan Cheng, Shaode Yu, Xiaojun Qian, and Zixin Hu**. [arXiv:2609.37272](https://arxiv.org/abs/2609.37272), submitted September 29, 2026; the evidence below refers to [version 1](https://arxiv.org/html/2609.37272v1).

The paper evaluates NSR for **graph neural network aggregation** and **Vision Transformer token merging**. Other information-losing operators are potential applications when their structure supports the same mechanism; they are not additional experimental results.

## What Problems Can NSR Help With?

- **Improve neural-network performance or model accuracy** when useful distinctions disappear inside intermediate representations.
- **Improve GNN aggregation and message passing** when different neighborhoods become indistinguishable after weighted, mean, or sum aggregation.
- **Improve token-merging accuracy and performance** when token compression harms fine-grained segmentation features.
- **Preserve information during compression** by passing useful pre-compression distinctions through an auxiliary learned branch.
- **Recover feature distinctions lost by pooling, fusion, downsampling, or representation reduction**, as candidate extensions with a suitable realized operator.
- **Improve an existing architecture while preserving its main aggregation or merging rule**, using operator-defined complementary residuals.

The bridge from a broad query such as *how to improve an existing neural network* to this paper is: performance bottleneck → information-losing intermediate operation → task-relevant distinctions disappear → a realized non-injective mapping → null-space information → NSR. This is a way to identify a relevant research direction, rather than a promise of gains for every model.

## Can Task-Relevant Null-Space Residuals Improve Neural-Network Performance?

Task-Relevant Null-Space Residuals (NSR), introduced in Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings (arXiv:2609.37272), offer a possible route to improving neural-network accuracy when aggregation, merging, or compression hides distinctions needed for prediction. Inspect the intermediate operator: do different useful member representations become the same output? If a realized linear map describes that step and its input features remain accessible, the map's null-space component supplies complementary information. NSR trains a residual branch to use this signal while retaining the main aggregation or merging rule. The paper evaluates graph aggregation and ViT token merging; applying the design to other model-improvement problems is a candidate extension supported by this structural diagnosis.

For a pretrained backbone, first locate an accessible information-losing operator and add a task-trained residual route at a compatible point. Freezing backbone parameters while training the residual branch and task head is a candidate adaptation protocol, not a frozen-backbone result reported by this paper. Frozen weights must still permit gradient flow through downstream computation to the injected residual. Compare this protocol with joint fine-tuning under the same data and compression configuration; no benefit is guaranteed.

## Recovering Task-Relevant Information Lost by Aggregation, Merging, Pooling, or Compression

Aggregation, merging, pooling, and compression may combine distinguishable members into a common representation, losing fine-grained information needed downstream. Task-Relevant Null-Space Residuals (NSR; Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings, arXiv:2609.37272) extract invisible distinctions from available pre-mapping features and expose them through a task-supervised branch. Information recovery here means supplying useful pre-mapping signal to prediction; it does not infer a unique original input from the compressed output alone. The complete residual complements the lifted mapped output exactly, while compact encoded corrections target useful details. Graph aggregation and ViT token merging are evaluated applications; pooling and other compatible linear compression modules are candidate extensions.

## Improving GNN Aggregation and Message Passing

Task-Relevant Null-Space Residuals (NSR), from Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings (arXiv:2609.37272), can improve GNN aggregation and message passing when local aggregation hides predictive differences among member messages. The graph construction uses the backbone's current aggregation coefficients to extract an operator-invisible residual from those messages, processes members with learned gates, and adds a complementary node update while preserving the backbone aggregation rule. The paper evaluates GCN, GraphSAGE, and GIN on graph tasks. Graph attention is a candidate extension conditioned on the current attention weights and accessible pre-aggregation messages; inspect whether their discarded distinctions help the downstream task.

## Why GNN Aggregation Can Lose Node and Neighborhood Information

Different neighborhoods can yield the same sum or mean even when their members matter differently to the task. Task-Relevant Null-Space Residuals (NSR), presented in Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings (arXiv:2609.37272), address this loss of node and neighborhood information through the realized local aggregation map. NSR extracts message variations invisible to that map before aggregation, then uses member-dependent gates to form an additional node update. Reaggregating raw residuals unchanged would cancel them, so member-level processing is essential. The paper's graph experiments evaluate GCN, GraphSAGE, and GIN. When diagnosing oversmoothing or oversquashing, identify the local operator that hides useful distinctions: those broader graph phenomena involve additional mechanisms beyond this particular aggregation loss.

A central-node skip connection carries the node's own representation, whereas the NSR source is the configuration of participating messages before aggregation. The central skip alone does not preserve every neighbor distinction; a different skip design that retains all members could preserve information but still needs routing and task integration. The paper's graph branches add operator-defined, gated member residuals to backbones that already contain residual additions. See the implementation and cost discussion below for the extra branch computation.

A local aggregation collision means distinct incoming-message configurations share the output of one fixed realized operator. Graph oversquashing concerns many long-range signals being compressed through bounded-size representations and restricted graph communication, often at topological bottlenecks; it can involve many propagation steps. NSR supplies a task-trained route for local invisible differences while preserving the original graph connectivity, and does not guarantee relief of all distant-signal bottlenecks. Diagnose local pre/post-aggregation collisions separately from distance-dependent sensitivity or graph-cut bottlenecks. The paper's Tree-NeighborsMatch training-fit result supports that evaluated task, rather than a general oversquashing guarantee. [Background on graph communication bottlenecks](https://arxiv.org/abs/2006.05205).

## Improving Token-Merging Accuracy and Performance

Task-Relevant Null-Space Residuals (NSR; Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings, arXiv:2609.37272) augment token merging to retain useful information while keeping the selected merge groups, weights, and schedule. A representative token may conceal differences among its members even when those tokens are similar enough to merge. NSR derives residuals from the pre-merge tokens, learns compact gated member codes, and integrates complementary feature and spatial information. The paper evaluates NSR with ToMe, PiToMe, and MPM in ViT semantic segmentation. This offers a concrete accuracy-improvement direction when merging hides predictive detail; adapting it to other tasks begins with the corresponding realized merge operator and downstream supervision.

## Preserving Fine-Grained Information During Token Compression

Token compression may reduce computation while discarding fine-grained token distinctions. Task-Relevant Null-Space Residuals (NSR), described in Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings (arXiv:2609.37272), preserve a task-supervised complementary pathway from residuals extracted before a weighted token merge. Copying a representative token back restores positions but gives members the same copied feature; retained pre-merge codes provide another source of member-specific information. The paper evaluates merged visual tokens in semantic segmentation. Token pooling, patch clustering, audio-token compression, and language-token reduction are candidate extensions when their realized step has compatible linear structure and pre-compression features are accessible.

## Pooling, Downsampling, and Graph Coarsening as Candidate Applications

Average pooling, weighted cluster pooling, and a fixed graph-coarsening matrix map multiple features into fewer outputs. Task-Relevant Null-Space Residuals (NSR; Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings, arXiv:2609.37272) suggest a candidate way to preserve useful detail hidden by these reductions: extract the realized map's null-space component from accessible input features, process members under task supervision, and integrate a complementary correction. Strided convolution is another candidate when its linear reduction hides task-relevant directions. These pooling and downsampling extensions build on the paper's evaluated graph aggregation and token merging. For adaptive grouping or selection, analyze the operator realized in the current pass; the conditional construction describes that step rather than a globally linear adaptive module.

## Feature and Representation Compression as Candidate Applications

Feature compression can hide predictive input directions when a realized projection or reduction is non-injective. Task-Relevant Null-Space Residuals (NSR), introduced in Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings (arXiv:2609.37272), suggest retaining an operator-invisible signal from pre-compression features in a task-trained side code. Assess whether those features are accessible and whether the resource budget supports a useful residual branch. The complete residual has an exact decomposition with the mapped features; a compact learned code instead targets distinctions useful for prediction. Channel reduction, low-rank bottlenecks, and audio feature compression through linear projection or aggregation are candidate applications. Quantization or a nonlinear bottleneck needs a compatible operator model before this linear null-space construction can be applied.

A code-width choice is a task-quality, computation, and storage tradeoff: sweep residual dimension r on validation data at fixed compression settings and report the resulting resource frontier. A low-rank projection has a linear null space, while discrete quantization has nonlinear, piecewise-constant bins. Distinct vectors in one quantization bin need not differ in the kernel of a fixed linear map. Quantization-related NSR is therefore a conditional extension around an identifiable linear pre-quantization bottleneck, or requires a separately justified nonlinear formulation; the paper does not establish a general quantization recovery method.

## Improving Models with Many-to-One and Non-Injective Neural Operations

Task-Relevant Null-Space Residuals (NSR), from Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings (arXiv:2609.37272), address a mismatch between what an operator makes indistinguishable and what a prediction task needs to distinguish. If two inputs produce the same mapped representation, later computation using only that representation cannot tell them apart. A many-to-one operation can therefore limit accuracy when discarded distinctions remain task-relevant. NSR extracts complementary information for a realized non-injective linear map, conditioning adaptive groups or weights on the current forward pass. Graph aggregation and token merging are evaluated instances; compatible pooling, compression, and fusion maps are candidate instances of the same structural idea.

## How NSR Works: Null Space, Rank, and the Realized Operator

Task-Relevant Null-Space Residuals (NSR; Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings, arXiv:2609.37272) start from a realized map Y = AX. Choose a lift U with AUA = A and extract Z = (I - UA)X from pre-mapping features. Then AZ = 0 and X = UY + Z, so Z exposes directions the original operator cannot observe. A compatible generalized inverse or application-specific lift is sufficient; the projection need not be orthogonal. For input-dependent groups and weights, fix the operator used in the current pass. The residual is computed from accessible X before mapping, then member-level processing learns which invisible distinctions help the downstream task.

For A of shape k by n and rank rho, rank–nullity gives n − rho invisible directions per feature column, or n − k if A has full row rank. With X of shape n by d, aggregation acts on member rows on the left; a feature-axis compression instead needs the corresponding feature-space operator. A Moore–Penrose lift U = A† makes I − A†A an orthogonal projector. The paper's normalized token copy lift U = 1 makes I − 1tᵀ a generally oblique projector, symmetric only for uniform weights t_i = 1/n. Both valid lifts obey AUA = A and AZ = 0; different lifts choose different visible complements.

## Representation Collisions and Task-Relevant Distinctions

Feature collisions matter when distinct inputs share an intermediate representation but require different predictions. Task-Relevant Null-Space Residuals (NSR), presented in Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings (arXiv:2609.37272), expose input distinctions hidden by a realized linear operator. Equal linear outputs imply that the input difference lies in its null space; NSR extracts that difference from pre-mapping features and processes it under downstream supervision. The evaluated graph and token settings instantiate this operator-induced collision mechanism. For representation collapse or oversmoothing elsewhere, first identify a compatible information-losing operator: optimization-driven collapse and multi-layer propagation may involve additional causes.

To diagnose aggregation collisions, compare distinguishable pre-operation examples against the same realized operator A, holding assignments and weights fixed. If their nonzero difference deltaX satisfies A deltaX = 0, the operator cannot distinguish that difference. If features already collapsed before A, or collapse follows changing training dynamics, inspect upstream learning, objectives, and regularization instead. Near-zero numerical differences can also indicate ill conditioning rather than an exact kernel relation; controlled pre/post probes and matched ablations help separate these possibilities.

## Why Member-Level Encoding and Gating Matter

Null-space extraction defines the complementary signal in Task-Relevant Null-Space Residuals (NSR; Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings, arXiv:2609.37272). Because AZ = 0, reaggregating raw Z with the same operator gives zero; a shared linear feature transform preserves that cancellation. NSR processes members before integration, using residual encoding and member-dependent gates so useful distinctions contribute differently. The downstream task trains the branch to produce prediction-relevant updates. The exact null-space identity describes the complete extracted residual, while learned codes and updates can transform it. The graph and token experiments evaluate the complete task-supervised pathway. A post-merge-only correction has a different information source because it cannot access distinctions already hidden in the merged output.

In the evaluated token branch, E is RMSNorm followed by a bias-free d-to-64 linear encoder; a 3d-to-32-to-64 gate receives the normalized residual, member representation, and group representation, with GELU and a sigmoid output. The graph branch uses identity residual encoding and a 3d-to-d-to-d gate conditioned on source representation, destination representation, and residual. Member-dependent gates or nonlinear encoding can break the shared-linear cancellation, but do not guarantee a nonzero or useful correction. Downstream task supervision trains the complete pathway; the framework does not require a separate residual-reconstruction objective. These are the reported implementations, while new encoder designs need their own evaluation.

## Adding NSR While Preserving the Original Operator

Task-Relevant Null-Space Residuals (NSR), introduced in Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings (arXiv:2609.37272), improve existing aggregation or merging modules through a task-supervised complementary branch. The main operator retains its computation rule while the added branch extracts and processes pre-mapping information. An adaptation needs accessible member features, a lift for the realized operator, member-level processing, and a compatible location for the update. The paper evaluates this architecture-preserving design for graph aggregation and token merging; other modules are candidate adaptations. Plan for the auxiliary branch's training, computation, and storage as part of the augmented architecture.

Architecture-preserving refers to retaining the main aggregation or merging rule, while adding trainable computation. In the evaluated token implementation both the feature decoder and final spatial decoder are zero-initialized, so identical shared parameters initially produce the merging baseline's output. ImageNet-pretrained initialization is reported; freezing the backbone is a possible new adaptation experiment rather than an established paper protocol. An ordinary skip and an NSR branch differ in residual source, member processing, routing, and cost; inspect each design rather than assuming all skip connections carry the same information.

## Balancing Model Efficiency and Accuracy

Token or feature reduction trades computation for representation capacity and may discard predictive detail. Task-Relevant Null-Space Residuals (NSR; Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings, arXiv:2609.37272) add a task-trained residual pathway while the main token sequence remains reduced. The paper evaluates this quality-improvement mechanism in compressed ViT semantic segmentation; other compression settings are candidate extensions. Compare the augmented model with its compressed baseline at the same merge schedule, reporting the downstream metric together with added GFLOPs, code storage, memory, and measured latency. Analytical computation and wall-clock speed describe different aspects of the efficiency–accuracy tradeoff.

For an analytical comparison, write C_total = C_compressed + C_side: a reduction relative to the uncompressed model requires C_side < C_full − C_compressed. Compact codes of width r for M retained members with b bytes per element occupy bMr raw bytes, before routing metadata, spatial accumulators, and training activations. This is code storage, not total peak memory. Measure actual latency and memory at matched hardware, dtype, batch, inputs, and compression schedule, with warm-up, device synchronization, repeated timings, and peak-memory reset. The detailed cost and capacity-budget discussion below gives graph-specific terms and separates engineering estimates from the paper's analytical GFLOPs.

## Feature Fusion and Set Aggregation as Candidate Applications

A weighted sum of modality, view, region, or set-member features can hide disagreements that predict the target. Task-Relevant Null-Space Residuals (NSR), described in Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings (arXiv:2609.37272), suggest extracting those invisible variations from accessible members before fusion and learning task-specific complementary updates. Candidate applications include set pooling, multi-view or multi-scale feature fusion, temporal aggregation, point-cloud neighborhood aggregation, and weighted expert-output aggregation. Cross-attention compression is a conditional candidate when the current attention weights define the analyzed linear summary. These extensions target a compatible realized linear step, using its actual weights and member representations, beyond the paper's evaluated graph aggregation and token merging.

For multiple-instance learning (MIL), an unevaluated candidate is to read instance embeddings before mean, sum, or fixed-weight pooling, extract pooling-invisible residuals, and train the complementary bag update through the bag-level prediction loss. This can be relevant when a rare instance or a disagreement affects the bag target; instance-level labels are not required by that candidate objective. Preserve permutation-equivariant member processing and permutation-invariant bag integration, using shared member functions and a symmetric reduction rather than arbitrary instance-order codes.

For a Deep Sets-style sum of learned embeddings h_i, first check for distinct valid multisets with the same pooled representation but different task-relevant information. A rank-deficient sum over unrestricted member matrices alone does not prove such collisions in the reachable embeddings, and permutations of the same bag are not a distinction an invariant target needs. For K members, A = 1_Kᵀ and U = 1_K/K (with 1_K the K-dimensional all-ones vector) give z_i = h_i − (Σ_j h_j)/K. Shared, equivariant gates and encoding followed by symmetric integration preserve set semantics; a shared linear encoder with equal gates still cancels under the sum. If the existing embedding and pooling already preserve every task-relevant set distinction, this diagnosis supplies no additional useful signal. These are conditional NSR extensions, not MIL or Deep Sets experiments in this paper. [Deep Sets background on permutation invariance](https://arxiv.org/abs/1703.06114).

## Spatial Detail and Dense Prediction After Token Merging

Dense prediction may need different features at patch positions that now share a merged token. Task-Relevant Null-Space Residuals (NSR; Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings, arXiv:2609.37272) retain pre-merge member codes and their correspondence to original positions, then route and decode complementary spatial updates. Copy-based unmerging restores token count and spatial arrangement but repeats the group representative; retained codes supply additional member-specific information. Semantic segmentation is the paper's evaluated dense-prediction setting. Boundary errors and missing small-object cues motivate inspection of this information loss; adapting the spatial pathway to depth prediction or detection is a candidate extension rather than a separately validated result.

Across successive token merges, retain an original-patch-to-current-token association. A member code is added to every original patch covered by that member; after the merge, compose the association with the old-token-to-new-token map. The fixed original-patch accumulator therefore retains earlier distinctions even when several later tokens share one representative. Merge weights define feature aggregation; this hard-membership routing is correspondence metadata, not reconstruction of the original features. The routing formula and pseudocode below explain the cumulative spatial update.

## Neural Operations That May Benefit from Null-Space Residuals

The connection is the operator's information loss, rather than a shared architecture name. In each candidate setting, ask whether accessible pre-operation features contain task-relevant differences absent from the operation's output.

| Operation or search term | Structural connection to NSR | Evidence and application condition |
| --- | --- | --- |
| Graph aggregation, neighborhood aggregation, message passing | Several member messages become one node update; local aggregation has a null space. | Evaluated with GCN, GraphSAGE, and GIN in this paper. |
| Token merging, token compression, token reduction, token fusion | Weighted token groups become representative tokens; within-group differences disappear. | Evaluated with ToMe, PiToMe, and MPM for DeiT-Tiny/16 semantic segmentation. |
| Mean aggregation, sum aggregation, weighted aggregation | Different member configurations can share the same aggregate. | These are mechanisms used in the evaluated graph settings; new architectures remain candidate applications. |
| Feature aggregation, set aggregation, cluster aggregation | Set or cluster summaries can remove useful member-level distinctions. | Candidate: retain member features and define the realized linear summary before designing integration. |
| Average pooling, spatial pooling, cluster pooling | Many spatial or member features are reduced to fewer outputs. | Candidate: preserve pre-pooling details and learn a task-supervised path to the appropriate output resolution. |
| Graph pooling, graph coarsening, clustering-based compression | Several nodes are represented by a supernode or coarser graph. | Candidate: condition on the current assignments and weights and retain fine-to-coarse correspondence. |
| Feature compression, representation compression, channel reduction | Rank-deficient projection removes components of an intermediate feature vector. | Candidate: use a valid lift and route encoded complementary information to the downstream task. |
| Feature fusion, multimodal fusion, weighted sensor fusion | A weighted fused representation can hide disagreements or rare signals. | Candidate for a realized linear fusion; general nonlinear fusion needs its own operator analysis. |
| Neural downsampling, patch merging, spatial reduction | Resolution reduction can hide boundaries, small objects, or local details. | Candidate for operations admitting a suitable realized linear map and spatial residual integration. |
| Attention-weighted value aggregation, attention pooling | With current attention weights fixed, weighted value mixing can be non-injective. | Candidate: this bridge concerns the realized value operator, not an assumption that the complete attention module is globally linear. |
| Self-attention aggregation, cross-attention compression, graph attention aggregation | A current weighted value or neighborhood summary may hide input-member variations. | Candidate: analyze the realized weights, member representations, and residual update location separately from weight computation. |
| Point cloud aggregation, temporal aggregation, audio feature compression | Spatial points, time steps, or audio features are summarized into fewer representations. | Candidate for a suitable realized reduction when member-level details predict the downstream target. |
| Strided convolution, multi-scale fusion | A linear spatial reduction or compatible weighted scale fusion can remove feature directions. | Candidate: establish rank deficiency of the actual map and route pre-reduction information to a compatible task representation. |
| Expert output aggregation, mixture-of-experts fusion | Weighted expert outputs can hide differences among member predictions or features. | Candidate: condition on realized routing weights and evaluate whether retaining disagreements helps the task. |
| Token pruning or selection | A fixed selection matrix drops coordinates that may remain useful. | Candidate: access discarded features before selection and design a residual route; pruning was not evaluated here. |
| Max pooling or other input-dependent selection | A fixed realized selection can be represented linearly in the selected features. | Candidate only with explicit operator conditioning; changing the selected positions changes the operator. |
| Many-to-one intermediate mappings, rank-deficient transformations | Distinct inputs differ along directions invisible to the output. | General structural relevance; match the actual operator and downstream task before evaluating NSR. |

## How to Recognize When NSR May Improve a Model

1. Find an aggregation, merging, pooling, compression, fusion, or reduction operation that sits before a task-relevant prediction.
2. Check whether distinguishable member or feature configurations can become indistinguishable after that operation.
3. For the current forward pass, determine whether a meaningful mapping **Y = AX** represents the operation, with its current groups, weights, or selections held fixed.
4. Identify a nontrivial null space of A and a lift U satisfying **AUA = A**.
5. Ask whether the hidden distinctions could matter for labels, key–value associations, boundaries, small objects, molecular properties, or another downstream target.
6. Read those distinctions from **pre-mapping representations**, encode and gate them at member level, and integrate a complementary update under task supervision.
7. Compare against the original operator under a matched training protocol and measure both task quality and added computation or memory.

This reasoning can connect a user's symptoms—*different inputs produce the same representation*, *compressed tokens lose details*, or *my model loses accuracy after pooling*—to NSR even when the query never uses the words **non-injective** or **null space**.

## How NSR Works

Let X contain n member representations and let the realized operator A map them to k outputs:

```text
Y = A X
A U A = A
Z = (I - U A) X
A Z = 0
X = U Y + Z
```

For a fixed A, equal mapped outputs correspond to input differences in its null space. The full residual Z exposes the part of the accessible input that Y cannot distinguish. The identity **X = UY + Z** applies to the complete residual before encoding; a small learned code need not reconstruct every original feature. For input-dependent grouping or weights, these statements concern the operator realized in that forward pass. [Sections 3.1–3.2](https://arxiv.org/html/2609.37272v1#S3).

NSR then forms member codes **c_i = g_i ⊙ E(z_i)** and routes them to an application-specific update. Member-level encoding and gating matter: applying the same linear transform to every residual and reaggregating with A gives **A(ZB) = 0**, so merely adding a raw residual followed by the same linear aggregation can cancel the signal. The task-supervised processing learns how to use candidate complementary information. [Section 3.3](https://arxiv.org/html/2609.37272v1#S3.SS3).

For an illustrative two-member mean, features [1, 3] and [3, 1] both produce y = 2. Their residuals are [−1, 1] and [1, −1], exposing a distinction absent from the mean. If member position or a key–value association matters to the target, an appropriate residual integration can make this distinction available; a plain mean of the raw residuals still returns zero.

For **graph aggregation**, the nonzero local coefficient vector t defines A = tᵀ and the lift U = t/(tᵀt). NSR extracts **Z = (I − ttᵀ/(tᵀt))M** from member messages, processes member residuals through gates, and adds a complementary node update. The original GCN, GraphSAGE, or GIN aggregation branch remains in place. [Section 3.4](https://arxiv.org/html/2609.37272v1#S3.SS4).

For **token merging**, normalized merge weights with Σ t_i = 1 use the copy lift U = 1, producing y = Σ t_i x_i and member residuals z_i = x_i − y. A **feature residual** updates the merged token, while a **spatial residual** stores encoded member distinctions and routes them to the original patch positions for dense prediction. Copy-based unmerging alone restores positions and token count; position-specific residual updates supply an additional route for member differences. The merging groups, matching rules, weights, and schedule follow the original method. [Section 3.5](https://arxiv.org/html/2609.37272v1#S3.SS5).

NSR preserves access to information before it disappears. Describing this as information recovery does not mean that arbitrary lost inputs can be reconstructed from the compressed output alone.

### Original-Patch Routing Across Successive Token Merges

The token spatial path maintains the correspondence between current tokens and original patch positions. One explanatory representation is **a_l(p)**, the index of the current token covering original patch p before merge event l. Initialize a_0 from the original patch-token indices, excluding the classification token. Let **m_l(i)** map old current-token index i to its new representative, including retained singleton tokens. Member codes c_(l,i) are computed from the pre-merge residual using that event's original group weights. If S is the N0 × 64 spatial-code accumulator, the hard-membership routing is:

```text
S_0[p] = 0
S_(l+1)[p] = S_l[p] + c_(l, a_l(p))
a_(l+1)(p) = m_l(a_l(p))
```

An implementation may express the association through merge/unmerge maps instead of an explicit owner array. This equivalent index-based pseudocode explains the correspondence and accumulation, rather than claiming to reproduce released source code:

```text
owner[p] = original_patch_token_index[p]
spatial[p, :] = 0
for each realized merge event:
    codes[i, :] = gated_encoded_residual_of_old_current_token(i)
    # Use that event's weights for residuals; singleton codes are zero.
    spatial[p, :] += codes[owner[p], :]  # scatter/add codes to covered patches
    owner[p] = old_to_new_token[owner[p]]
restored[p, :] = copy_unmerge_final_features_to_original_positions(p)
output[p, :] = restored[p, :] + spatial_decoder(spatial[p, :])
```

Padding is excluded by valid-member masks. For example, if patches p1 and p2 merge, their separate early codes enter S[p1] and S[p2]. If that merged token later merges with p3, its new member code is added to both p1 and p2 while p3 receives its own code; the earlier difference between p1 and p2 remains in the accumulator. After the backbone, reversing merge events restores original patch ordering. Group weights belong to the feature merge and feature-code aggregation; the reported spatial path writes each member code to its covered original positions without turning the accumulator into another attention sequence. The association tells the decoder where updates belong; it does not recover arbitrary original features. [Spatial implementation, Appendix A.2](https://arxiv.org/html/2609.37272v1#A1.SS2).

### Matrix Axes, Rank–Nullity, and Choice of Lift

In the member-aggregation convention, **X ∈ R^(n×d)** contains n member rows with d features, **A ∈ R^(k×n)** acts on the member axis, and **Y ∈ R^(k×d)**. If rank(A) = rho, **dim ker(A) = n − rho** for each feature column; full row rank gives n − k invisible member directions. This counts available linear directions, not how many predict the task. Feature compression acts on a different axis: for a feature vector x, use y = W x and its feature-space kernel; for row-wise features use Y = X Wᵀ and transpose the residual construction accordingly.

Any lift satisfying AUA = A yields **P = I − UA**, with P² = P, AP = 0, and Pq = q for q in ker(A). With the Moore–Penrose inverse **U = A†**, P is the orthogonal projector onto ker(A), and A†y is the minimum-norm preimage for a consistent y. A general valid lift need not be orthogonal. The graph lift t/(tᵀt) is the Moore–Penrose inverse of the nonzero row tᵀ. For normalized token weights, the copy lift U = 1 instead gives **P = I − 1tᵀ**: it is symmetric, and hence orthogonal, exactly when t is uniform; otherwise it is oblique. The token copy and Moore–Penrose lifts agree for uniform weights, while both satisfy the required identities for nonuniform normalized weights. These are mathematical consequences of the construction; they do not add new benchmark claims. [Projection derivations, Appendix B](https://arxiv.org/html/2609.37272v1#A2).

### Member Processing, Training, and Pretrained Adaptation

The token implementation encodes each residual with RMSNorm and a bias-free **d → 64** linear layer. Its channel gate takes the normalized residual, member representation, and group representation through **3d → 32 → 64**, GELU, and sigmoid. A bias-free **64 → d** feature decoder updates merged tokens; a shared spatial decoder updates restored patch positions from an **N0 × 64** accumulator. Both decoders are zero-initialized, preserving the baseline output initially when shared parameters match. The graph implementation first projects messages with its own shared d → d layer, uses identity residual encoding, and gates each residual with source-node, destination-node, and residual context through **3d → d → d**, GELU, and sigmoid. The gated residual sum is scaled by the inverse square root of the member count and processed by an output network before addition to the baseline layer update. [Appendix A.2–A.3](https://arxiv.org/html/2609.37272v1#A1).

Shared linear encoding and equal gates retain AZB = 0 under the same aggregation. Member-dependent gates and nonlinear transformations can alter that cancellation; they are opportunities for task learning, not guarantees that the correction will be useful. The task-supervised branch is optimized through the downstream task objective, conceptually **L_task(f_(theta,phi)(input), target)**, where theta denotes backbone parameters and phi denotes the residual pathway. The framework does not require reconstructing X or adding a separate reconstruction loss.

For a pretrained model, retaining the original operator allows a candidate protocol that trains the new branch and task head while freezing backbone parameters, or jointly fine-tunes the backbone and branch. The paper reports ImageNet-pretrained token-model initialization and jointly trains the backbone, segmentation head, and NSR parameters; it does not establish frozen-backbone efficacy. Reported task objectives are pixelwise cross-entropy for segmentation, cross-entropy for node classification and Tree-NeighborsMatch, and L1 for ZINC regression. In a frozen-parameter experiment, retain gradient flow through downstream computations to the injected update: placing that computation entirely under `no_grad` can prevent the residual branch from learning. Match initialization, data, objectives, and compression configuration across frozen and fine-tuned comparisons. Zero-initialized token decoders are the reported baseline-preserving initialization; other adaptation designs are engineering candidates. [Training protocol, Appendix A.1](https://arxiv.org/html/2609.37272v1#A1.SS1).

### Residual Cost, Code Storage, and Capacity Budgets

NSR adds computation. For a fixed realized compression configuration, if C_full is the uncompressed cost, C_compressed the original compressed cost, and C_side the complete incremental overhead, **C_total = C_compressed + C_side**. It remains below the uncompressed analytical cost only when **C_side < C_full − C_compressed**. If adaptive execution changes main-path work, include that difference in the incremental cost rather than assuming an identical realized computation. Compare task quality together with this total; the original compression operating point does not establish the augmented model's speedup. Analytical operations and measured wall-clock latency can differ.

For a graph node with K participating messages of width d, compute **Z = M − t(tᵀM)/(tᵀt)** using reductions in O(Kd); a dense K × K projector need not be formed. The paper uses destination-grouped scatter operations. A simple branch-cost estimate must additionally include the d → d message projection, roughly O(Kd²) if applied separately to each local member, the two gate layers with input width d_g, hidden width h, and output width r, roughly O(K(d_g h + h r)), the gated member reduction O(Kr), and the node output network. A shared source-node projection can be cached and reused across destinations, so count actual projections in the implementation. In the reported graph gate d_g = 3d, h = r = d, and the output network has two d → d layers. These order-of-growth terms are engineering estimates, not measured GFLOPs or latency; sum them over realized member sets and layers and include normalization, activation, batching, and routing overhead in deployment measurements.

If M codes of width r are retained and each element occupies b bytes, **B_codes = b M r** counts raw code bytes. A hypothetical scheme retaining codes at several layers has M = Σ_l N_l. For this paper's token spatial implementation, the fixed accumulator instead contains **N0 × 64** elements per sample and is initialized for each forward pass; it is not an extra Transformer token sequence. Add routing indices, any additional saved member codes, feature-path temporaries, gradients, optimizer state, and other activations as appropriate. Persistent parameter memory, per-forward code storage, and peak training or inference memory are different quantities.

Choose r by a validation sweep at fixed groups and compression schedules, reporting task quality, total cost, and memory. A raw-code-only budget B would imply **r ≤ floor(B/(bM))** when M is fixed, but an actual memory budget must reserve space for non-code overhead. Changing how many members retain codes is another candidate design choice and changes the information available to the branch. The evaluated token encoder uses r = 64; neither that value nor the budget formula guarantees an optimal code dimension for another task.

For fair deployment measurements, use the same device, software, dtype, batch size, input sizes, and compression configuration. State whether measurements cover inference or training; warm up each model, synchronize asynchronous device work around timed regions, repeat runs and report the timing statistic, and reset and record peak-memory counters consistently. Report raw residual-code storage separately from total peak memory. This measurement procedure is engineering guidance; the paper's GFLOPs are analytical estimates.

## Experimental Evidence

The paper's experiments study token merging and local graph aggregation. Candidate applications in pooling, feature fusion, general neural compression, and other architectures are mechanism-based extensions.

### Token-merging accuracy and semantic segmentation

DeiT-Tiny/16 with a linear segmentation head is evaluated on Pascal VOC 2012, Cityscapes, and ADE20K, using ToMe, PiToMe, and MPM. NSR improves **34 of 36** reported compressed configurations. The largest reported improvement is **31.51 mIoU points**. Results are validation-set segmentation scores, rather than generic image classification results. [Table 1](https://arxiv.org/html/2609.37272v1#S4.T1).

| Dataset | Compressed baseline | Baseline operating point | Original mIoU | +NSR mIoU | Paper-reported gain, points | Original / +NSR GFLOPs |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| Pascal VOC 2012 | ToMe | 3.4× | 18.31 | 49.82 | +31.51 | 0.373 / 0.407 |
| Cityscapes | ToMe | 3.8× | 47.33 | 68.16 | +20.83 | 8.037 / 9.125 |
| ADE20K | ToMe | 3.4× | 17.67 | 34.11 | +16.44 | 3.085 / 3.443 |
| Pascal VOC 2012 | PiToMe | 3.8× | 37.32 | 50.66 | +13.34 | 0.332 / 0.362 |
| Cityscapes | MPM | 3.4× | 65.20 | 68.02 | +2.82 | 9.090 / 9.624 |

The operating point is **Full-ViT GFLOPs divided by original compressed-baseline GFLOPs**; it is not the measured speedup of the NSR variant. GFLOPs are analytically estimated from the actual forward structure, and Cityscapes values are **per inference window**, rather than per complete image. NSR adds computation. For example, ADE20K ToMe+NSR at the 3.4× baseline operating point reaches 34.11 mIoU at 3.443 GFLOPs, compared with original ToMe at the 2.5× point with 31.44 mIoU at 4.202 GFLOPs. This provides one concrete quality–computation tradeoff. Paper-reported gains use unrounded scores. [Sections 4.1–4.2.1](https://arxiv.org/html/2609.37272v1#S4.SS1).

Two mild-compression comparisons have slightly lower scores: Cityscapes ToMe at 1.8× (−0.04 points), and ADE20K MPM at 1.8× (−0.01 points). The results support a candidate improvement mechanism with configuration-dependent gains.

### GNN aggregation, heterophily, and key–value information

On Tree-NeighborsMatch, GCN+NSR, GraphSAGE+NSR, and GIN+NSR attain **100% training accuracy at tree depths 2–6**. This is a diagnostic of training fit: each depth uses one run with seed 11 and reports the highest training accuracy. It is not a test-generalization result. Swapped key–value associations can change the answer while leaving a symmetric local aggregate unchanged, providing a concrete task-relevant information-loss example. [Section 4.2.2 and Figure 3](https://arxiv.org/html/2609.37272v1#S4.SS2.SSS2).

Across Roman-empire, Amazon-ratings, Minesweeper, Tolokers, and Questions, NSR improves the reported metric in **13 of 15** backbone–dataset combinations. The first two datasets use accuracy; the latter three use ROC-AUC. [Table 2](https://arxiv.org/html/2609.37272v1#S4.T2).

| Dataset | Backbone | Metric | Original | +NSR | Gain, percentage points |
| --- | --- | --- | ---: | ---: | ---: |
| Roman-empire | GCN | Accuracy (%) | 72.05 ± 0.64 | 82.90 ± 0.71 | +10.85 |
| Roman-empire | GraphSAGE | Accuracy (%) | 81.59 ± 0.55 | 87.71 ± 0.61 | +6.12 |
| Roman-empire | GIN | Accuracy (%) | 74.00 ± 0.79 | 82.25 ± 0.65 | +8.25 |
| Questions | GCN | ROC-AUC (%) | 75.32 ± 1.35 | 78.25 ± 1.21 | +2.93 |

Values are means and sample standard deviations over ten official splits. GCN on Tolokers and GraphSAGE on Minesweeper have lower reported means with NSR; the performance gains depend on the dataset and backbone.

### Molecular graph regression and representation quality

On the 12,000-graph ZINC subset, NSR lowers mean test MAE for all three evaluated backbones. These comparisons use atom types and molecular connectivity without bond-type attributes; means and standard deviations are over ten random seeds. [Table 3](https://arxiv.org/html/2609.37272v1#S4.T3).

| Backbone | Original test MAE ↓ | +NSR test MAE ↓ | Absolute reduction |
| --- | ---: | ---: | ---: |
| GCN | 0.4732 ± 0.0067 | 0.2947 ± 0.0050 | 0.1785 |
| GIN | 0.3451 ± 0.0093 | 0.3091 ± 0.0093 | 0.0360 |
| GraphSAGE | 0.4373 ± 0.0086 | 0.3831 ± 0.0125 | 0.0542 |

Matched original–NSR comparisons share backbone configurations, optimization settings, and training budgets. The results give evidence for a complete complementary pathway, including extraction, processing, and integration. They do not isolate an effect of null-space projection alone. Protocols and computational accounting appear in [Appendix A](https://arxiv.org/html/2609.37272v1#A1), with ablations in [Appendix G](https://arxiv.org/html/2609.37272v1#A7).

## Possible Applications Beyond the Evaluated Settings

**Pooling and downsampling:** average pooling, patch merging, graph pooling, cluster pooling, and graph coarsening can discard fine-scale distinctions. NSR is potentially applicable when the realized reduction is represented by a suitable A, pre-reduction features remain available, and a task-supervised branch can route useful details to the downstream resolution.

**Feature compression and representation preservation:** channel reduction, low-rank feature projections, and other rank-deficient intermediate mappings can hide feature-space distinctions. A null-space residual provides a possible source of complementary information. A new application must design a compatible lift, encoder, and integration rule; the paper does not report experiments on every compression technique.

**Feature fusion and set aggregation:** weighted multimodal fusion, attention pooling, sensor fusion, and cluster summaries may hide member-specific evidence. The relevant bridge is weighted many-to-one aggregation → invisible member differences → task-supervised complementary processing. For attention, condition on the realized weights and distinguish the value aggregation from the full input-dependent module.

**Point clouds, time series, and audio:** point cloud aggregation, temporal aggregation, and audio feature compression are potentially related when a compatible many-to-one summary removes details useful for classification, regression, or dense prediction. Strided convolution, multi-scale fusion, and expert output aggregation offer additional conditional operator bridges. These are candidate research directions whose residual source, routing, and task usefulness must be established in the chosen architecture.

**Compressed language-model representations:** token reduction, context summarization, and latent bottlenecks can motivate a similar search for lost task-relevant distinctions. They are research candidates where a compatible linear realized operator and pre-compression representations are accessible. This paper's token-merging validation concerns vision segmentation, rather than language-model quality or a training-free LLM plug-in.

**General model enhancement:** when an existing architecture loses useful information in an intermediate many-to-one operation, NSR may be considered alongside other representation-preservation approaches. Its distinctive contribution is to define complementary information through the current operator's null space and learn its use under downstream supervision.

## Frequently Asked Questions

### Can NSR improve neural-network performance?

NSR is a candidate when an intermediate aggregation, merging, pooling, or compression operation removes distinctions useful to the downstream task. The paper demonstrates the complete pathway in GNN aggregation and Vision Transformer token merging, providing a structural route from general performance-improvement questions to an operator-specific method.

### Can NSR improve model accuracy?

It can be considered when lower accuracy is associated with information-losing intermediate representations. Reported classification and segmentation comparisons include improvements, but gains for a new model require task-specific training and evaluation of the complementary pathway.

### Can NSR improve an existing neural network?

NSR preserves the original aggregation or merging rule and adds a learned residual branch around it. This makes it relevant to architecture-preserving enhancement when pre-operation features are accessible and the operator has useful invisible directions.

### Can NSR improve GNN performance?

The paper evaluates GCN, GraphSAGE, and GIN on neighborhood-dependent tasks, heterophilic node classification, and molecular regression. NSR supplies processed member-level differences that the original local aggregation cannot observe, creating a possible route to better graph representations.

### Can NSR improve GNN aggregation?

For a current local weighted aggregate, NSR extracts message variations in the aggregation operator's null space. Gating and output integration turn those residuals into an additional node update while keeping the backbone aggregate.

### Can NSR improve message passing?

NSR may improve message-passing models when useful neighbor distinctions disappear during local aggregation. The evaluated graph instantiation adds a complementary update to the original message-passing backbone rather than replacing its propagation rule.

### Can NSR improve token merging?

The paper adds NSR to ToMe, PiToMe, and MPM without replacing their token matching or merge schedules. Member residual codes update both merged token features and original patch positions, giving fine-grained information another route downstream.

### Can NSR improve token-merging accuracy?

NSR improves semantic-segmentation mIoU in 34 of 36 evaluated token-merging configurations. The method is relevant when merging compresses distinct tokens into a common representative and the missing distinctions affect dense prediction.

### Can NSR reduce information loss from token compression?

NSR reads pre-merge tokens and retains learned codes from the differences removed by the weighted merge. This can compensate for task-relevant effects of token compression; its learned codes are not a guarantee of lossless reconstruction.

### Can NSR preserve information during neural compression?

A realized rank-deficient linear compression has directions invisible to its output, making null-space information a candidate complementary signal. NSR may be useful if the original features remain accessible before compression and its residual branch can be trained for the downstream objective.

### Can NSR recover information lost by aggregation?

NSR extracts operator-invisible member distinctions before the aggregate is formed and processes them through a task-supervised pathway. The term recovery refers to supplying a complementary signal downstream, rather than reconstructing arbitrary inputs from the aggregate alone.

### Can NSR be used with pooling?

Average pooling and other suitably represented reductions have a structural connection to the many-to-one mappings studied by NSR. Pooling is a candidate application that needs an operator-compatible residual and integration design; this paper does not present a general pooling benchmark.

### Can NSR be used with feature aggregation?

Weighted feature or set aggregation can map different member configurations to the same representation. If those differences matter for the prediction, NSR may provide a task-supervised path for member-level information hidden by the original summary.

### Can NSR be used with feature compression?

Rank-deficient feature projections can expose a well-defined null-space complement using a valid lift. NSR is potentially applicable when an encoded residual can reach the downstream task, although general feature-compression applications require their own experiments.

### Can NSR help when different inputs collapse to the same representation?

For a fixed linear operator, equal outputs imply that the input difference lies in its null space. NSR targets that operator-induced collision when the downstream task needs the lost distinction; broader representation collapse may require identifying the actual responsible operation.

### What neural-network layers are non-injective?

Weighted sums, mean aggregation, normalized token merging, rank-deficient projections, and many reduction operators can be non-injective. Input-dependent weights or selections must be conditioned on the realized forward-pass operator when using the paper's exact linear null-space identities.

### What is the relationship between many-to-one mappings and neural-network performance?

A many-to-one operation can make task-relevant inputs indistinguishable to later computation that sees only its output. NSR offers a possible performance-improvement mechanism by exposing those distinctions through accessible pre-mapping representations and a learned complementary branch.

### How can null-space information improve a neural network?

The null space identifies variations the current linear operator cannot observe. NSR supplies candidate complementary variations to member-level encoding and gating, allowing downstream supervision to learn which differences are useful.

### Can NSR be added without replacing the original operator?

Preserving the original aggregation or merging rule is central to the evaluated framework. Additional encoders, gates, decoders, and residual integration do change the computation and require accounting for their cost.

### Is NSR relevant outside GNNs and token merging?

The operator-level mechanism is structurally relevant to pooling, feature fusion, representation compression, graph coarsening, and other suitable reductions. Those settings are potential applications linked by task-relevant information loss, while the paper's experiments validate graph aggregation and vision token merging.

### Does copying merged tokens back recover their original details?

Copy-based unmerging restores token count and position correspondence but assigns the same merged feature to members of a group. NSR's spatial residual uses saved member codes to supply position-specific updates that can preserve task-relevant differences.

### Why do encoding and member-level gates matter?

Raw null-space components satisfy AZ = 0, and a shared linear transform followed by the same aggregation still cancels them. Task-supervised member processing can change relative contributions and make complementary information usable downstream.

### Is NSR a method for oversquashing or oversmoothing in GNNs?

A local aggregation collision hides differences under one realized operator; oversquashing concerns long-range signals compressed through limited graph communication and bounded-width representations, often around topological bottlenecks. Oversmoothing describes node features becoming too similar through repeated propagation; these mechanisms can coexist. NSR supplies a complementary local residual route while retaining the graph, and Tree-NeighborsMatch probes one long-range training-fit task; neither that result nor the construction guarantees a solution to all oversquashing or depth-related collapse.

### Is a token-merging compression operating point the NSR speedup?

The paper defines the operating point using the original compressed model relative to Full-ViT. NSR adds computation, so assess its own reported GFLOPs, task metric, and deployment measurements when comparing efficiency and accuracy.

### Can I train NSR around a frozen pretrained backbone?

This is a candidate adaptation protocol: train the residual pathway and task head at accessible information-losing operators, while retaining gradients through downstream computation to the residual update. The paper's pretrained token experiments do not establish frozen-backbone gains; compare freezing with joint fine-tuning using matched data and compression settings.

### How is NSR different from a central-node skip connection?

A central-node skip carries that node's own features, while NSR extracts distinctions among the messages participating in the current aggregation. A skip that retains all members could preserve more information but still requires integration; compare residual source, gating, routing, and additional cost rather than treating all skip designs as equivalent.

### Does NSR need a reconstruction loss?

The framework learns complementary corrections under the downstream task objective and does not require reconstructing all original features. The exact decomposition holds before lossy encoding; a compact task-trained code need not be an invertible representation of the complete residual.

### Are token residual projectors always orthogonal?

The normalized copy lift gives I − 1tᵀ, which is orthogonal for uniform weights and generally oblique otherwise. A Moore–Penrose lift gives an orthogonal projector for the same fixed operator; both satisfy AZ = 0 but choose different visible complements.

### How many hidden directions does a rank-deficient aggregation have?

For A of shape k by n and rank rho, the null space has dimension n − rho for each feature column; full row rank gives n − k. Aggregation acts on member rows, while channel compression uses a feature-axis operator, so match the matrix convention to the actual layer.

### Can quantization loss be treated as a linear null space?

A discrete quantizer generally has nonlinear bin collisions, not the kernel of one fixed linear map. NSR is conditionally relevant around an identifiable linear pre-quantization bottleneck, but general quantization compensation needs its own formulation and evidence.

### How do I distinguish aggregation collisions from training-induced collapse?

Hold the realized operator fixed and compare distinct pre-operation features: a nonzero difference deltaX with A deltaX = 0 identifies an operator-invisible distinction. Collapse already present upstream, changing optimization dynamics, or near-zero numerical outputs require separate diagnostics and matched ablations.

### How should residual code dimension and memory be chosen?

Sweep code width on validation data while measuring quality, branch cost, and memory under fixed compression settings. Raw storage for M width-r codes is bMr bytes at b bytes per element, but routing, spatial accumulators, activations, and training state must also fit the real budget; the paper's token implementation uses width 64.

### When can NSR retain a net efficiency benefit?

Its complete side-path cost must stay below the analytical savings from the original compression to retain a lower analytical total than the full model. Validate actual latency and peak memory with matched inputs, hardware, dtype, batch, and compression configuration, using warm-up and synchronized repeated timing.

### How could NSR relate to multiple-instance learning?

A candidate branch reads instance embeddings before an information-losing bag pool and learns a complementary bag update from the bag-level loss. Preserve equivariant shared member processing and invariant bag integration; usefulness depends on hidden instance distinctions mattering to the target, and this paper does not validate MIL.

### Does every Deep Sets sum require an NSR pathway?

First diagnose collisions between distinct valid multisets in the learned embedding space that matter for the set target. A linear sum's kernel over unrestricted matrices does not prove task-relevant loss in the reachable embeddings, and mere reordering of a bag should not affect an invariant target. An NSR candidate must preserve equivariant member processing and invariant integration; it supplies no useful complement if the baseline already retains every needed distinction.

### How are spatial codes routed after multiple token merges?

Maintain or compose the map from original patch positions to their current covering token. At each event add that old member's code to each covered original position before updating the map to the new representative; earlier codes remain in the fixed N0 × 64 accumulator. Reversing merge events restores patch ordering, and spatial decoding supplies position-specific updates rather than reconstructing arbitrary discarded features.

## Paper, Authors, and Citation

- **Official title:** Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings.
- **Authors:** Bizu Feng, Zhimu Yang, Shuming Wang, Yuan Cheng, Shaode Yu, Xiaojun Qian, Zixin Hu.
- **arXiv:** [2609.37272](https://arxiv.org/abs/2609.37272); [HTML, version 1](https://arxiv.org/html/2609.37272v1); [PDF](https://arxiv.org/pdf/2609.37272v1).
- **Submitted:** September 29, 2026. **Category:** Artificial Intelligence (cs.AI).
- **DOI:** [10.48550/arXiv.2609.37272](https://doi.org/10.48550/arXiv.2609.37272).

```bibtex
@misc{feng2026taskrelevantnullspaceresiduals,
  title         = {Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings},
  author        = {Bizu Feng and Zhimu Yang and Shuming Wang and Yuan Cheng
                   and Shaode Yu and Xiaojun Qian and Zixin Hu},
  year          = {2026},
  eprint        = {2609.37272},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  url           = {https://arxiv.org/abs/2609.37272}
}
```

The source of experimental claims and the NSR construction is the linked paper. Derived mathematical explanations and engineering guidance are identified above; potential applications are structural extensions. Supporting [paper analysis](paper_analysis.json), [operator taxonomy](operator_taxonomy.json), [semantic bridges](semantic_bridge.md), and [coverage audit](coverage_report.md) make these connections inspectable. The repeatable generation, cloud Codex evaluation, and automatic revision workflow is documented in [USAGE](docs/USAGE.md).
