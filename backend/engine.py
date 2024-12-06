import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
# 从环境变量中读取api_key
api_key = os.getenv('ZHIPU_API_KEY')
base_url = "https://open.bigmodel.cn/api/paas/v4/"
chat_model = "glm-4-flash"
emb_model = "embedding-2"

from llama_index.llms.zhipuai import ZhipuAI
llm = ZhipuAI(
    api_key = api_key,
    model = chat_model,
)

from llama_index.embeddings.zhipuai import ZhipuAIEmbedding
embedding = ZhipuAIEmbedding(
    api_key = api_key,
    model = emb_model,
)


from llama_index.core import SimpleDirectoryReader,Document
documents = SimpleDirectoryReader(input_files=['../docs/问答手册.txt']).load_data()
from llama_index.core import VectorStoreIndex
index = VectorStoreIndex.from_documents(documents,embed_model=embedding)



query_engine = index.as_query_engine(
    streaming=True, 
    similarity_top_k=3,
    llm=llm)