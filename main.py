import langsmith
from langchain import chat_models

# Define your runnable or chain below.
prompt = prompts.ChatPromptTemplate.from_messages(
  [
    ("system", "You are a helpful AI assistant."),
    ("human", "{your_input_key}")
  ]
)
llm = chat_models.ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = prompt | llm | output_parser.StrOutputParser()

client = langsmith.Client()
chain_results = client.run_on_dataset(
    dataset_name="<dataset-name>",
    llm_or_chain_factory=chain,
    project_name="test-false-floozie-93",
    concurrency_level=5,
    verbose=True,
)