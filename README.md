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

## ☀️本月快速导航

|Sum|Mon|Tue|Wed|Thu|Fri|Sat|
|:-|:-|:-|:-|:-|:-|:-|
|||||||**[1](./2023/4月/2023_04_01.md)** |
|**[2](./2023/4月/2023_04_02.md)** |**[3](./2023/4月/2023_04_03.md)** |**[4](./2023/4月/2023_04_04.md)** |**[5](./2023/4月/2023_04_05.md)** |**[6](./2023/4月/2023_04_06.md)** |**[7](./2023/4月/2023_04_07.md)** |**[8](./2023/4月/2023_04_08.md)** |
|**[9](./2023/4月/2023_04_09.md)** |**[10](./2023/4月/2023_04_10.md)** |**[11](./2023/4月/2023_04_11.md)** |**[12](./2023/4月/2023_04_12.md)** |**[13](./2023/4月/2023_04_13.md)** |**[14](./2023/4月/2023_04_14.md)** |**[15](./2023/4月/2023_04_15.md)** |
|**[16](./2023/4月/2023_04_16.md)** |**[17](./2023/4月/2023_04_17.md)** |**[18](./2023/4月/2023_04_18.md)** |**[19](./2023/4月/2023_04_19.md)** |**[20](./2023/4月/2023_04_20.md)** |**[21](./2023/4月/2023_04_21.md)** |**[22](./2023/4月/2023_04_22.md)** |
|**[23](./2023/4月/2023_04_23.md)** |**[24](./2023/4月/2023_04_24.md)** |**[25](./2023/4月/2023_04_25.md)** |**[26](./2023/4月/2023_04_26.md)** |**[27](./2023/4月/2023_04_27.md)** |**[28](./2023/4月/2023_04_28.md)** |**[29](./2023/4月/2023_04_29.md)** |
|**[30](./2023/4月/2023_04_30.md)** |||||||

## 📝Example

> 1. Title: Efficient and Effective Text Encoding for Chinese LLaMA and Alpaca.
> 2. Authors: Yiming Cui, Ziqing Yang, Xin Yao.
> 3. Affiliation: 无
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
| multimodal           | multimodal, text, image, video            |
| dialogue system      | dialogue system, chatbot, chat-bot       |
| empathetic dialogue  | empathetic dialogue, ed                  |
| humorous dialogue    | humorous dialogue                        |
| diffusion            | diffusion, image, text, image generation |
| large language model | LLM, large language model                |
| contrastive learning | contrastive learning, text generation, negative response, negative example, attention mask, multi-modal, dialog |
| reinforcement learning | rl, reinforcement learning, reinforcement learning from human feedback |

## ⌨代码

本项目的代码是用api2d做了中转，如果要直接使用chatgpt的服务，只需要修改 `api2d.py`文件的请求链接和请求头。

```python
# 基本配置信息, 保存apikey, email, query, key words等信息
config.ini 
# arxiv爬虫
get_arxiv.py
# 本地数据库
database.py
# 发送邮件
send_email.py
# 处理pdf
process_pdf.get_summary.py, prompt_convert_json.py 
# 🧠大脑
NavigoX.py
```

## ✏参考项目

> chatpaper: https://github.com/kaixindelele/ChatPaper
>
> chatgpt academic: https://github.com/binary-husky/chatgpt_academic
