# Local Large Language Models with llamaindex

## Features
- **Peft Fine-Tuning**: Introduces a standardized method for applying lora/qlora fine-tuning to a Text-to-SQL dataset, leveraging the HuggingFace platform for optimal results.
- **Quantization**: This process involves the quantization of the Llama2 model using llama.cpp to enhance inference performance. The quantized model can then be uploaded to HuggingFace. This step can be seamlessly integrated with the fine-tuning process, allowing for the direct transformation and upload of your model to HuggingFace. Once uploaded, it can be easily downloaded by LM Studio for immediate local use.
- **LM Studio**: LM Studio offers an intuitive user interface to operate your local LLM like a chatbot. Additionally, it enables you to host your local LLM as API endpoints for seamless integration and accessibility.
- **LlamaIndex**: Provides a way to build a Local RAG (retrieval-augmented generation) with your own files utilizaing vector embedding, vector database store 
- **Dynamic Summarization in Llamaindex**: Features a dynamic conversation summarization to maintain essential information and ensure continuity in long conversations.
- **Enhanced Context Management**: Improves the LLM's ability to handle extensive dialogues without losing context.

## Getting Started

### Prerequisites

- Python 3.x
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/minglyubyte/llama_index_with_local_llm.git
   ```
2. Navigate to the project directory:
   ```bash
   cd llama_index_with_local_llm
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Provide instructions on how to use the project. Include examples of commands or scripts to run, configuration options, and any other necessary steps.

## Contributing

Instructions for how others can contribute to the project. Typically includes:

- Forking the repository
- Creating a new branch (`git checkout -b feature/YourFeature`)
- Committing changes (`git commit -m 'Add some feature'`)
- Pushing to the branch (`git push origin feature/YourFeature`)
- Opening a new Pull Request

## License

State the license under which the project is made available.

## Acknowledgments

Mention any individuals, organizations, or projects that contributed to this project.

---

This template is just a starting point. You should customize it according to the specifics of your project, including more detailed instructions and descriptions as necessary. Remember, a good README is crucial for open-source projects, as it's often the first thing users and contributors will look at.
