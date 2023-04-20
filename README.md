# 📰DailyPaper

这个项目是一个论文summary库，旨在通过简单高效的方式来了解学界的最新研究成果。

```
📎workflow:
通过爬虫每日抓取arXiv上指定关键词的最新论文，然后使用chatgpt总结论文内容，汇总更新。

🎃tips:
1. 本脚本中arXiv识别key words的方法是对论文中的abstract做分词，然后匹配（匹配度大于2/3就会被认定匹配成功），所以难免会抓取到少量非本领域的论文（比如diffusion关键词中经常抓到天体物理相关的论文）；
2. summary并不完全准确，只能作为基本的参考；
3. chatgpt有时会不听话的输出英文内容;
4. arXiv周六周日不更新论文。
```

## example

> 一个实例：
>
> 1. Title: Efficient and Effective Text Encoding for Chinese LLaMA and Alpaca.
> 2. Authors: Yiming Cui, Ziqing Yang, Xin Yao.
> 3. Affiliation: 无.
> 4. Keywords: Large Language Models, natural language processing, Chinese language, open-source software.
> 5. Urls: arXiv:2304.08177v1, Github: https://github.com/ymcui/Chinese-LLaMA-Alpaca.
> 6. Summary:
>
> - (1): 本文研究背景为大型语言模型在自然语言处理领域的广泛应用以及其对透明和开放的学术研究所带来的挑战。
> - (2): 过去的方法存在着专有限制和高昂的训练费用等问题，导致整个研究社区在此基础上无法进行细粒度的进一步研究。作者提出的方法侧重于对中国巨型语言模型进行二次预训练，并使用中国数据进行微调，从而显著提高模型的理解能力和指令执行能力。
> - (3): 作者提出了二次预训练和微调技术并在中国指令数据集上进行微调和测试，以评估模型的性能和理解能力。
> - (4): 该方法在中国巨型语言模型上进行了全面的评测，取得了良好的性能表现，支持了开源软件的目标。
> - (5): 本文的主要动机是为了推动自然语言处理领域的开放研究并提高巨型语言模型的透明度和可理解性。

## 📍目前的关键词

| query                | key words                                |
| :------------------- | :--------------------------------------- |
| chatgpt              | chatgpt                                  |
| multimodal           | multimoal, text, image, video            |
| dialogue system      | dialogue system, chatbot, chat-bot       |
| empathetic dialogue  | empathetic dialogue, ed                  |
| humorous dialogue    | humorous dialogue                        |
| diffusion            | diffusion, image, text, image generation |
| large language model | LLM, large language model                |

## ✏参考项目

> chatpaper: https://github.com/kaixindelele/ChatPaper
>
> chatgpt academic: https://github.com/binary-husky/chatgpt_academic
