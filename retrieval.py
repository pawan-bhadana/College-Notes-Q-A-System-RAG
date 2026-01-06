from sentence_transformers import util
from embeddings import model,embeddings
import numpy as np
from chunking import new_chunks

query=input()
embedding=model.encode([query])
embeddings_sim=[];
j=0
for i in embeddings:
    similarity=util.cos_sim(embedding,i)
    embeddings_sim.append([similarity.item(),j])
    j+=1
embeddings_sim.sort(reverse=True)

context=[]

for i,j in embeddings_sim:
    context.append([new_chunks[j],i])

# print(context[:5])







