# Misinfo Reaction Frames

Even to a simple and short news headline, readers react in a multitude of ways: cognitively (e.g., inferring the writer's intent), emotionally (e.g., feeling distrust), and behaviorally (e.g., sharing the news with their friends). Such reactions are instantaneous and yet complex, as they rely on factors that go beyond interpreting the factual content the news headline. We propose Misinfo Reaction Frames, a pragmatic formalism for modeling how readers might react to a news headline.

![alt text](https://github.com/misinfo-belief/misinfo-modeling/blob/main/Misinfo_Reaction_Frames.png)

We release the Misinfo Reaction Frames corpus, which covers over 200k headline/implication pairs capturing the writer intents, potential reader perceptions and reader actions associated with Covid-19, climate and cancer misinfo/real news, as well as likelihood of a reader sharing the headline, perceived labels and fact-checked gold labels.  

[**Misinfo Reaction Frames: Reasoning about Readers' Reactions to News Headlines**.](https://arxiv.org/abs/2104.08790) 
Saadia Gabriel, Skyler Hallinan, Maarten Sap, Pemi Nguyen, Franziska Roesner, Eunsol Choi and Yejin Choi. 2021. 

## Data 

Each data split is in a .tsv file with the following header format:

| headline      | writer_intent | effect_on_reader | reader_action | spread | pred_label | gold_label | date | source | type | 
| ------------- | ------------- | ---------------- | ------------- | ------ | ---------- | ---------- | ---- | ------ | ---- | 

Link to [data splits](https://drive.google.com/drive/folders/1RGrwbnj-Z25OeU4S6Di_JzX07P_2TdtZ?usp=sharing) 

Link to [current version of data statement](https://github.com/misinfo-belief/misinfo-modeling/blob/main/data_statement.txt) 

## Pretrained Models 

We emphasize that annotations (and model generations) reflect perceptions and beliefs of annotators, rather than universal
truths. We urge caution in generalizing beliefs or taking beliefs held in certain social/cultural contexts to be factual knowledge.

The goal of publicly releasing this work is to aid in misinformation detection efforts and countering misinformation, as well as research aimed at better understanding intent of written text. We do not condone use of this work in unethical technology applications like purposefully generating deceptive text. 

These models can be loaded using huggingface implementations for GPT-2 [link](https://huggingface.co/transformers/model_doc/gpt2.html) and T5 [link](https://huggingface.co/transformers/model_doc/t5.html) with the following special tokens added:

["writer_intent", "effect_on_reader", "reader_action","pred_label","gold_label","spread","climate","covid","cancer","Other"]

Link to [GPT-2 (small)](https://drive.google.com/drive/u/0/folders/1Z_HQ4MEZ3p6hD4uf1u4sKnaojY1YZXnH)

Link to [GPT-2 (large)](https://drive.google.com/drive/u/0/folders/1Uqm19zGsCykafWR1tXLGLGkArfn8VaD9)

Link to [T5-base](https://drive.google.com/drive/u/0/folders/1JQmWmC_1he6Ng7ght_Y12foUipI2lzi8) 

Link to [T5-large](https://drive.google.com/drive/u/0/folders/1jBkrhhMgai2Sk57oRDeLx8Hsw3ErAoGK) 

## Full repo coming soon! 

## If you use this work, please cite us: 

```
@article{Gabriel2021MisinfoRF,
  title={Misinfo Reaction Frames: Reasoning about Readers' Reactions to News Headlines},
  author={Saadia Gabriel and Skyler Hallinan and Maarten Sap and Pemi Nguyen and Franziska Roesner and Eunsol Choi and Yejin Choi},
  journal={ArXiv},
  year={2021},
  volume={abs/2104.08790}
}
```

If you have questions, please email skgabrie@cs.washington.edu or open a new issue. 
