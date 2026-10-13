# ---------------------------------------------------------------
# Ask Your PDF - a small RAG (Retrieval Augmented Generation) app
#
# Flow:
#   PDF -> text -> small chunks -> embeddings -> FAISS index
#   question -> find the most similar chunks -> send them + question to the LLM
# ---------------------------------------------------------------

from dotenv import load_dotenv                                   # reads secrets (API key) from a .env file
import streamlit as st                                           # builds the web UI
from PyPDF2 import PdfReader                                     # reads text out of PDF files
from langchain.text_splitter import CharacterTextSplitter        # cuts long text into small pieces
from langchain.embeddings.openai import OpenAIEmbeddings         # turns text into number vectors (meaning)
from langchain.vectorstores import FAISS                         # fast "search by meaning" database
from langchain.chains.question_answering import load_qa_chain    # ready-made "answer using these documents" chain
from langchain.llms import OpenAI                                # the language model that writes the answer


def main():
    # Load OPENAI_API_KEY from the .env file into the environment.
    # OpenAIEmbeddings and OpenAI pick it up automatically.
    load_dotenv()

    # Page settings: browser tab title and centered layout
    st.set_page_config(
        page_title="Ask your pdf",
        layout="centered",
        initial_sidebar_state="auto",
    )
    st.header("Ask your pdf (OpenAI)")

    # ----------------------------------------------------------
    # STEP 1: Upload the PDF
    # ----------------------------------------------------------
    # Shows an upload button. Returns None until the user picks a file.
    pdf = st.file_uploader("Upload your pdf", type="pdf")

    # Everything below only runs once a PDF has been uploaded
    if pdf is not None:

        # ------------------------------------------------------
        # STEP 2: Extract text from every page
        # ------------------------------------------------------
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            # extract_text() can return None for scanned/image pages,
            # so "or ''" prevents a crash when joining strings
            text += page.extract_text() or ""

        # ------------------------------------------------------
        # STEP 3: Split the text into chunks
        # ------------------------------------------------------
        # The LLM has a limited input size, so we cut the text into small pieces.
        text_splitter = CharacterTextSplitter(
            separator="\n",       # prefer to cut at line breaks
            chunk_size=1000,      # max characters per chunk
            chunk_overlap=200,    # share 200 characters between neighbours so no sentence loses context
            length_function=len,  # measure size by number of characters
        )
        chunks = text_splitter.split_text(text)

        # ------------------------------------------------------
        # STEP 4: Create embeddings and the search index
        # ------------------------------------------------------
        # An embedding is a list of numbers that represents the meaning of a text.
        embeddings = OpenAIEmbeddings()

        # Convert every chunk to an embedding and store them in FAISS,
        # so we can later search "by meaning" instead of by exact words.
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # ------------------------------------------------------
        # STEP 5: Get the user's question
        # ------------------------------------------------------
        user_question = st.text_input("Ask a question about the PDF: ")

        # Only continue when the user has typed something
        if user_question:

            # --------------------------------------------------
            # STEP 6: Find the chunks most similar to the question
            # --------------------------------------------------
            # Returns the closest chunks, best match first (default is 4 chunks)
            similar_chunks = knowledge_base.similarity_search(user_question)

            # Keep only the top k chunks. Fewer chunks = cheaper and more focused.
            k = 3
            top_k_chunks = similar_chunks[:k]

            # --------------------------------------------------
            # STEP 7: Ask the LLM, giving it only the relevant chunks
            # --------------------------------------------------
            llm = OpenAI()

            # chain_type="stuff" means: paste all chunks into ONE prompt together
            # with the question. Simple and fast for small amounts of text.
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=top_k_chunks, question=user_question)

            # Length of each top chunk (just for information/debugging)
            k_values = [len(str(chunk)) for chunk in top_k_chunks]

            # --------------------------------------------------
            # STEP 8: Show everything on the page
            # --------------------------------------------------
            st.subheader("Similarity Search Results:")
            st.write("Chunks with similar context/meaning as the question:")
            for i, chunk in enumerate(similar_chunks):
                st.write(f"Chunk {i + 1}:", chunk)

            st.subheader(f"Top {k} Chunks Similar to the Question:")
            for i, chunk in enumerate(top_k_chunks):
                st.write(f"Chunk {i + 1}:", chunk)

            st.subheader("Answer from LLM:")
            st.write(response)

            st.subheader("Length of each retrieved chunk:")
            for i, k_value in enumerate(k_values):
                st.write(f"Chunk {i + 1}: {k_value}")


# Run main() only when this file is executed directly (not when imported)
if __name__ == "__main__":
    main()
