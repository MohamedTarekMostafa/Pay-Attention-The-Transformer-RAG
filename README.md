#  Pay Attention: A Deep Dive into Transformers with RAG

I built this project because I wanted to do more than just read the "Attention Is All You Need" paper—I wanted to talk to it. 

**Pay Attention** is a RAG-based research assistant that understands the architecture, the math, and the logic behind the original Transformer model. Whether you're stuck on Multi-Head Attention or curious about Positional Encodings, this tool acts as a bridge between a dense 15-page PDF and your technical questions.

---

##  Why This Project?

Reading academic papers is hard. Building a RAG system to query them is easy, but making it **accurate** is the real challenge. In this project, I focused on high-precision retrieval to ensure that when you ask about a formula, you get an answer backed by the actual paper, not a hallucination.

---

##  How it's Put Together

I divided the logic into three simple parts:

* **The LLM  (Gemini 2.5 Flash):** I chose this model for its speed and its ability to handle technical academic context without breaking a sweat.
* **The Memory (ChromaDB + BGE Embeddings):** I used `BGE-small` because it's a heavyweight in the embedding world. It understands the "semantics" of AI research much better than standard models.
* **The Filter (Custom Splitting):** I went with a **512 chunk size**. Why? Because it’s the "sweet spot." It’s small enough to be precise but large enough to keep a mathematical definition intact.



---

##  Real-World Limitations (The Honest Part)

Let’s be real—Standard RAG has its ceilings:

* **The "K" Struggle:** Right now, the system pulls the top 5 chunks. But what if the answer is spread across 10? Or what if it's only in 1? A static "K" is sometimes a bit rigid.
* **Missing the Big Picture:** While 512 chunks are great for specific details, they sometimes miss the broader "narrative" of the paper.
* **No Fact-Checking:** If the retriever picks up a noisy chunk, the LLM might still try to make sense of it. It lacks a "Wait, this doesn't look right" step.

---

##  The Future: Moving to Agentic RAG

This is where it gets exciting. My next goal is to turn this into an **Agentic System**. 

Instead of just searching and answering, an **Agentic RAG** would:
1.  **Critique itself:** "Did I actually find the answer or just some random text?"
2.  **Iterate:** If the first search fails, it will rephrase the question and try again.
3.  **Reason:** It would look at the architecture diagram and the text simultaneously to give a 360-degree answer.

---

##  Setup & Run

1.  **Clone & Install:**
    ```bash
    pip install langchain-huggingface langchain-google-genai langchain-chroma fastapi streamlit python-dotenv
    ```
2.  **Fire up the Server:**
    ```bash
    uvicorn main:app --reload
    ```
3.  **Talk to the Paper:**
    ```bash
    streamlit run ui.py
    ```

---
###  The User Interface
<img width="860" height="569" alt="Capture" src="https://github.com/user-attachments/assets/c0ef4c67-4a04-42da-bd33-83e91616df22" />
<img width="825" height="470" alt="2" src="https://github.com/user-attachments/assets/63b446d8-1a6b-401e-b27a-7aa0dfd3aaf7" />
<img width="859" height="429" alt="3" src="https://github.com/user-attachments/assets/6e83ed96-4b57-4248-814f-03b49198d80a" />


*If you're into Transformers or just want to geek out over RAG architectures, feel free to reach out!*
