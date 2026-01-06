with open('PROJECT_NOTES.txt', 'r') as file:
    text = file.read()

# print(text[:50])

chunks=text.split("\n\n")

# print(chunks[:10])

overlap=20
size=100
new_chunks=[]

for chunk in chunks[:10]:
    words=chunk.split()
    n=len(words)
    if(n==0):continue
    prev=""
    for i in range(len(words)//size +1):
        temp=words[i*size:min(n,(i+1)*size)]
        new_chunks.append(prev + " " + " ".join(temp))
        prev=" ".join(temp[-overlap:])

# print(new_chunks[:10])




