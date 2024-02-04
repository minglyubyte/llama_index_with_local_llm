import os
from openai import OpenAI

from llama_index.query_engine.retriever_query_engine import RetrieverQueryEngine
from llama_index.callbacks.base import CallbackManager
from llama_index import (
    LLMPredictor,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
    set_global_service_context
)
from llama_index.llms import ChatMessage, OpenAILike  
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.agent import ReActAgent
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.core.llms.types import ChatMessage, MessageRole
import chainlit as cl

llm = OpenAILike(  
    api_base="http://localhost:1234/v1",  
    timeout=600,  # secs  
    api_key="loremIpsum",  
    is_chat_model=True,  
    context_window=4048,
    temperature = 0.1
)

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

def generate_conversation(chat_history):
    output = ""
    for chatmessage in chat_history:
        if chatmessage['role'] == MessageRole.USER:
            output += "User: {}\n\n".format(chatmessage['content'])
        elif chatmessage['role'] == MessageRole.SYSTEM:
            output += "System: {}\n\n".format(chatmessage['content'])
        else:
            output += "System summarization: {}\n\n".format(chatmessage['content'])
    return output


@cl.on_chat_start
async def factory():
    service_context = ServiceContext.from_defaults(
        llm=llm,
        chunk_size=512,
        embed_model = "local",
        callback_manager=CallbackManager([cl.LlamaIndexCallbackHandler()]),
    )

    set_global_service_context(service_context)

    try:
        # rebuild storage context
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        # load index
        index = load_index_from_storage(storage_context)
    except:
        documents = SimpleDirectoryReader("./data").load_data()
        index = VectorStoreIndex.from_documents(documents, service_context = service_context)
        index.storage_context.persist()

    index_engine = index.as_query_engine(
        similarity_top_k=5, 
        service_context=service_context
    )
    
    index_tool = QueryEngineTool(
        query_engine = index_engine,
        metadata=ToolMetadata(
            name="index_engine",
            description=(
                "Provides information about experimental design."
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    )

    query_engine_tools = [index_tool]
    
    chat_agent = ReActAgent.from_tools(
        tools = query_engine_tools, 
        llm=llm, 
        verbose=True,
    )
    cl.user_session.set("chat_agent", chat_agent)


@cl.on_message
async def main(message: cl.Message):
    chat_agent = cl.user_session.get("chat_agent") 
    response = await cl.make_async(chat_agent.chat)(message.content)

    response_message = cl.Message(content="")
    
    for token in response.response:
        await response_message.stream_token(token=token)

    if response.response:
        response_message.content = response.response

    chat_history = chat_agent.memory.to_dict()
    num_token_length = 0
    
    for chatmessage in chat_history['chat_store']['store']['chat_history']:
        num_token_length += len(chatmessage['content'])

    if num_token_length >= 1000:
        previous_conversation = generate_conversation(chat_history['chat_store']['store']['chat_history'])
        prompt = """Your task is to create a concise summary of the following conversation. 
        This summary should be structured, short and informative, enabling a chatbot to extract relevant and useful information 
        for addressing future queries. Please find conversation below: {}""".format(previous_conversation)
        completion = llm.complete(prompt, temperature=0.1)
        chat_history['chat_store']['store']['chat_history'] = [
            {'role':MessageRole.SYSTEM, 'content': "Here is the brief summary of the previous conversation: {}".format(completion.text)}
        ]
        chat_agent.memory = chat_agent.memory.from_dict(chat_history)
    
    print(chat_agent.memory.chat_store)
    await response_message.send()









