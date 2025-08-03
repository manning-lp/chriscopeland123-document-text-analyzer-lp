def simple_example_call():
    client = openai.OpenAI(api_key=userdata.get('OPENAI_API_KEY'))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "What are the main parts of a contract?"}],
        max_tokens=50
    )

    print(response.choices[0].message.content)
