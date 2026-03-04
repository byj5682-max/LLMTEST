from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/workspaces/LLMTEST/Owners_Manual.pdf') 
pages = loader.load_and_split()

print(pages[0])