import anthropic

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-4-7",
    system="You are a friendly assistant that specializes in answering questions about electronics.",
    messages=[{"role": "user", "content": "What is a diode?"}],
)

print(response.model_dump_json())
