import openai

class GPTResponder:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, transcript):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or another model
                messages=[
                    {"role": "user", "content": transcript}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"Error getting response: {e}")
            return "Error retrieving response"
