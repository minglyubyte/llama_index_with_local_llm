# Local Large Language Models with llamaindex

## Features
- **Peft Fine-Tuning**: Introduces a standardized method for applying lora/qlora fine-tuning to a Text-to-SQL dataset, leveraging the HuggingFace platform for optimal results.
- **Quantization**: This process involves the quantization of the Llama2 model using llama.cpp to enhance inference performance. The quantized model can then be uploaded to HuggingFace. This step can be seamlessly integrated with the fine-tuning process, allowing for the direct transformation and upload of your model to HuggingFace. Once uploaded, it can be easily downloaded by LM Studio for immediate local use.
- **LM Studio**: LM Studio offers an intuitive user interface to operate your local LLM like a chatbot. Additionally, it enables you to host your local LLM as API endpoints for seamless integration and accessibility.
- **LlamaIndex**: Offers a solution for creating a Local Retrieval-Augmented Generation (RAG) system using your personal files. It utilizes vector embedding and vector database storage for efficient nearest document retrieval.
- **Dynamic Summarization in Llamaindex**: Features a dynamic conversation summarization to maintain essential information and ensure continuity in long conversations.
- **ChainLit**: ChainLit offers a web interface for local llm, resembling the appearance of ChatGPT.
