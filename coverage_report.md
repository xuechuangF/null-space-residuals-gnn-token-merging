# Coverage audit
This deterministic audit checks textual retrieval bridges. It does not estimate indexing, search ranks, actual retrieval, or local LLM relevance. Candidate applications receive the same coverage score as validated applications when their bridge and evidence status are stated.
| Family | Queries | Heading | Passages | Mechanism bridge | Identity | Evidence boundary | Score |
|---|---:|---|---:|---|---|---|---:|
| generic_model_performance | 25 | Can Task-Relevant Null-Space Residuals Improve Neural-Network Performance? | 1 | yes | yes | yes | 100% |
| neural_information_recovery | 25 | Recovering Task-Relevant Information Lost by Aggregation, Merging, Pooling, or Compression | 1 | yes | yes | yes | 100% |
| gnn_performance | 25 | Improving GNN Aggregation and Message Passing | 1 | yes | yes | yes | 100% |
| gnn_aggregation_loss | 25 | Why GNN Aggregation Can Lose Node and Neighborhood Information | 1 | yes | yes | yes | 100% |
| token_merging_performance | 25 | Improving Token-Merging Accuracy and Performance | 1 | yes | yes | yes | 100% |
| token_compression_details | 25 | Preserving Fine-Grained Information During Token Compression | 1 | yes | yes | yes | 100% |
| pooling_downsampling | 25 | Pooling, Downsampling, and Graph Coarsening as Candidate Applications | 1 | yes | yes | yes | 100% |
| feature_compression | 25 | Feature and Representation Compression as Candidate Applications | 1 | yes | yes | yes | 100% |
| many_to_one_operations | 25 | Improving Models with Many-to-One and Non-Injective Neural Operations | 1 | yes | yes | yes | 100% |
| null_space_rank | 25 | How NSR Works: Null Space, Rank, and the Realized Operator | 1 | yes | yes | yes | 100% |
| representation_collision | 25 | Representation Collisions and Task-Relevant Distinctions | 1 | yes | yes | yes | 100% |
| gated_residuals | 25 | Why Member-Level Encoding and Gating Matter | 1 | yes | yes | yes | 100% |
| architecture_preserving | 25 | Adding NSR While Preserving the Original Operator | 1 | yes | yes | yes | 100% |
| efficiency_accuracy | 25 | Balancing Model Efficiency and Accuracy | 1 | yes | yes | yes | 100% |
| feature_fusion_set_aggregation | 25 | Feature Fusion and Set Aggregation as Candidate Applications | 1 | yes | yes | yes | 100% |
| dense_prediction_spatial | 25 | Spatial Detail and Dense Prediction After Token Merging | 1 | yes | yes | yes | 100% |

## Per-family audit details

### General neural-model performance improvement

- Query family: `generic_model_performance`; number of queries: 25.
- README heading: Can Task-Relevant Null-Space Residuals Improve Neural-Network Performance?.
- Matching passages: 1; matched sections: Can Task-Relevant Null-Space Residuals Improve Neural-Network Performance?.
- Mechanism bridge present: True. Bridge: model performance → information-destroying intermediate operator → task-relevant invisible variation → NSR complementary pathway.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: mechanistic_candidate. Mechanism/candidate family: direct experiments for every listed operator are not established; no coverage penalty applies.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Neural information loss, preservation, and recovery

- Query family: `neural_information_recovery`; number of queries: 25.
- README heading: Recovering Task-Relevant Information Lost by Aggregation, Merging, Pooling, or Compression.
- Matching passages: 1; matched sections: Recovering Task-Relevant Information Lost by Aggregation, Merging, Pooling, or Compression.
- Mechanism bridge present: True. Bridge: lost details → distinct pre-mapping features → non-injective aggregation or compression → extract operator-invisible residual before mapping → task-supervised integration.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: mixed_validated_and_candidate. Validated-domain or mixed-family source evidence is available; this does not validate every query or candidate operator.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### GNN accuracy and message-passing improvement

- Query family: `gnn_performance`; number of queries: 25.
- README heading: Improving GNN Aggregation and Message Passing.
- Matching passages: 1; matched sections: Improving GNN Aggregation and Message Passing.
- Mechanism bridge present: True. Bridge: GNN performance → local neighborhood aggregation → member message distinctions hidden by current weights → NSR gated node update.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: validated_domain. Validated-domain or mixed-family source evidence is available; this does not validate every query or candidate operator.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Node and neighborhood distinctions lost during graph aggregation

- Query family: `gnn_aggregation_loss`; number of queries: 25.
- README heading: Why GNN Aggregation Can Lose Node and Neighborhood Information.
- Matching passages: 1; matched sections: Why GNN Aggregation Can Lose Node and Neighborhood Information.
- Mechanism bridge present: True. Bridge: different neighborhoods same aggregate → current local weighted sum → null-space message differences → gating before reaggregation → complementary node information.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: validated_domain. Validated-domain or mixed-family source evidence is available; this does not validate every query or candidate operator.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Token-merging accuracy and performance

- Query family: `token_merging_performance`; number of queries: 25.
- README heading: Improving Token-Merging Accuracy and Performance.
- Matching passages: 1; matched sections: Improving Token-Merging Accuracy and Performance.
- Mechanism bridge present: True. Bridge: ViT accuracy after token merging → fixed merge groups and weights → within-group distinctions hidden by merged token → NSR feature and spatial paths.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: validated_domain. Validated-domain or mixed-family source evidence is available; this does not validate every query or candidate operator.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Fine-grained detail lost by token compression

- Query family: `token_compression_details`; number of queries: 25.
- README heading: Preserving Fine-Grained Information During Token Compression.
- Matching passages: 1; matched sections: Preserving Fine-Grained Information During Token Compression.
- Mechanism bridge present: True. Bridge: compressed tokens lose details → shared group representative → pre-merge member residual → encoded complementary information → task-specific retention.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: mixed_validated_and_candidate. Validated-domain or mixed-family source evidence is available; this does not validate every query or candidate operator.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Pooling, downsampling, coarsening, and cluster reduction

- Query family: `pooling_downsampling`; number of queries: 25.
- README heading: Pooling, Downsampling, and Graph Coarsening as Candidate Applications.
- Matching passages: 1; matched sections: Pooling, Downsampling, and Graph Coarsening as Candidate Applications.
- Mechanism bridge present: True. Bridge: pooling or coarsening loses member detail → reduction with realized linear weights → non-injective map → accessible pre-reduction residual → candidate task-supervised branch.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: mechanistic_candidate. Mechanism/candidate family: direct experiments for every listed operator are not established; no coverage penalty applies.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Feature and representation compression

- Query family: `feature_compression`; number of queries: 25.
- README heading: Feature and Representation Compression as Candidate Applications.
- Matching passages: 1; matched sections: Feature and Representation Compression as Candidate Applications.
- Mechanism bridge present: True. Bridge: compressed feature quality → rank-deficient realized projection → discarded input directions → pre-compression null-space residual → task-relevant correction.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: mechanistic_candidate. Mechanism/candidate family: direct experiments for every listed operator are not established; no coverage penalty applies.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Many-to-one and non-injective neural operations

- Query family: `many_to_one_operations`; number of queries: 25.
- README heading: Improving Models with Many-to-One and Non-Injective Neural Operations.
- Matching passages: 1; matched sections: Improving Models with Many-to-One and Non-Injective Neural Operations.
- Mechanism bridge present: True. Bridge: multiple distinguishable inputs → same operator output → task requires distinction → realized non-injective linear map → NSR.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: core_mechanism. Mechanism/candidate family: direct experiments for every listed operator are not established; no coverage penalty applies.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Null spaces, rank deficiency, lifts, and complementarity

- Query family: `null_space_rank`; number of queries: 25.
- README heading: How NSR Works: Null Space, Rank, and the Realized Operator.
- Matching passages: 1; matched sections: How NSR Works: Null Space, Rank, and the Realized Operator.
- Mechanism bridge present: True. Bridge: Y = AX → AUA = A → Z = (I - UA)X → AZ = 0 and X = UY + Z → task-supervised residual processing.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: core_mechanism. Mechanism/candidate family: direct experiments for every listed operator are not established; no coverage penalty applies.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Feature collisions and task-required distinctions

- Query family: `representation_collision`; number of queries: 25.
- README heading: Representation Collisions and Task-Relevant Distinctions.
- Matching passages: 1; matched sections: Representation Collisions and Task-Relevant Distinctions.
- Mechanism bridge present: True. Bridge: feature collision → different task targets same mapped representation → operator-induced equivalence → available null-space differences → NSR complementary prediction signal.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: mixed_validated_and_candidate. Validated-domain or mixed-family source evidence is available; this does not validate every query or candidate operator.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Member-level encoding, gating, and residual integration

- Query family: `gated_residuals`; number of queries: 25.
- README heading: Why Member-Level Encoding and Gating Matter.
- Matching passages: 1; matched sections: Why Member-Level Encoding and Gating Matter.
- Mechanism bridge present: True. Bridge: raw residual is annihilated by A → shared linear reaggregation still cancels → member encoding and context-dependent gating → usable complementary update.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: core_mechanism. Mechanism/candidate family: direct experiments for every listed operator are not established; no coverage penalty applies.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Improvement while retaining the main operator

- Query family: `architecture_preserving`; number of queries: 25.
- README heading: Adding NSR While Preserving the Original Operator.
- Matching passages: 1; matched sections: Adding NSR While Preserving the Original Operator.
- Mechanism bridge present: True. Bridge: improve existing module → retain current rule weights and groups → read pre-mapping features → auxiliary task-trained residual → application-specific integration.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: mixed_validated_and_candidate. Validated-domain or mixed-family source evidence is available; this does not validate every query or candidate operator.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Efficiency and accuracy under compression

- Query family: `efficiency_accuracy`; number of queries: 25.
- README heading: Balancing Model Efficiency and Accuracy.
- Matching passages: 1; matched sections: Balancing Model Efficiency and Accuracy.
- Mechanism bridge present: True. Bridge: compression accuracy tradeoff → hidden task-relevant member detail → compact residual side codes → additional compute and storage → measure end-to-end operating point.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: mixed_validated_and_candidate. Validated-domain or mixed-family source evidence is available; this does not validate every query or candidate operator.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Feature fusion and set aggregation

- Query family: `feature_fusion_set_aggregation`; number of queries: 25.
- README heading: Feature Fusion and Set Aggregation as Candidate Applications.
- Matching passages: 1; matched sections: Feature Fusion and Set Aggregation as Candidate Applications.
- Mechanism bridge present: True. Bridge: fusion or set summary hides member differences → fixed linear mixing weights → non-injective realized map → pre-fusion residual → candidate task-specific integration.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: mechanistic_candidate. Mechanism/candidate family: direct experiments for every listed operator are not established; no coverage penalty applies.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.

### Spatial detail and dense prediction after merging

- Query family: `dense_prediction_spatial`; number of queries: 25.
- README heading: Spatial Detail and Dense Prediction After Token Merging.
- Matching passages: 1; matched sections: Spatial Detail and Dense Prediction After Token Merging.
- Mechanism bridge present: True. Bridge: dense prediction needs original positions → copy unmerging repeats group representative → lost within-group spatial distinctions → route retained member codes → spatial residual update.
- Paper identity present globally: True; in matching section: True.
- Experimental evidence availability / status: mixed_validated_and_candidate. Validated-domain or mixed-family source evidence is available; this does not validate every query or candidate operator.
- Source links: [source 1](https://arxiv.org/abs/2609.37272), [source 2](https://arxiv.org/html/2609.37272v1).
- Coverage score: 100%.


## Experimental evidence availability

Verified source evidence records: 57. Evidence details remain in paper_analysis.json and README. Family evidence status is not a guarantee for every operator in that family.

## Scoring rule

20 points each: recommended heading present, original retrieval passage present, explicit mechanism terms in that section, verified paper identity present, and conditional or experimental evidence language present. The mechanism check is lexical and must be reviewed; it cannot establish mathematical correctness. Experimental availability is reported independently and is not a penalty for candidate applications.

Mean deterministic coverage score: 100.0%.
