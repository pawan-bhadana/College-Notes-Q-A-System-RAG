from faiss import IndexFlatIP
import numpy as np
from embeddings import model,embeddings
from chunking import new_chunks


c_embeddings=np.array(embeddings).astype("float32")
dim=c_embeddings.shape[1]
# print(dim)
index=IndexFlatIP(dim)
index.add(c_embeddings)

query=input()
query_em=model.encode([query])
k=3
distances,indices=index.search(query_em,k)
context=[]
for i in range(k):
    # print(new_chunks[indices[0][i]],distances[0][i])
    context.append(new_chunks[indices[0][i]])







