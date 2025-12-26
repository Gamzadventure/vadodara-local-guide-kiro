def vadodara_local_guide(user_query):
    with open(".kiro/product.md", "r", encoding="utf-8") as file:
        local_context = file.read()

    response = f"""
Using Vadodara Local Context:

{local_context}

User Question:
{user_query}

AI Response:
Based on Vadodara's local culture and food habits, here is a helpful answer.
"""
    return response


if __name__ == "__main__":
    question = input("Ask about Vadodara city: ")
    print(vadodara_local_guide(question))
