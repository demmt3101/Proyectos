import openai

openai.api_key = "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"

class ChatGPTHandler:
    def __init__(self) -> None:
        pass
    
    def askChatGPT(self, userPrompt):
        try:
            response = openai.Completion.create(
                model = "text-davinci-003",
                prompt = userPrompt, 
                temperature = 0, 
                max_tokens = 500,
                top_p = 1.0,
                frequency_penalty = 0.0,
                presence_penalty = 0.0
            )
            return response.choices[0].text
        except Exception as e: 
            print(e)
            return "No puedo conectar con GPT"