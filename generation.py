from retrieval_faiss import context,query
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")   # not enough credits right now
client=OpenAI(api_key=api_key)

context_text="\n\n".join([f'chunk{i}:\n{chunk}' for i,chunk in enumerate(context)])
context_text+=f'Question:\n{query}\n\nAnswer:'
prompt=f'{context_text}'



response=client.chat.completions.create(model="gpt-4o-mini",
    messages=[{"role":"system","content":"You are a assistant. Answer the question based ONLY on provided context."},
              {"role":"user","content":prompt}],
    temperature=0.2)
# for chunk in context:
#     prompt+=f'chunk {i}:\n{chunk}\n\n'
#     i+=1
# prompt+=f'Question:\n{query}\n\nAnswer:'

