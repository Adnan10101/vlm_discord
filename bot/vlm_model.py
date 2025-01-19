from io import BytesIO
from PIL import Image
from jinja2 import Template
from unsloth import FastVisionModel


class Model:
    def __init__(self, model_name = "Prince12f/Llava_spatial_reasoning"):
        model, tokenizer = FastVisionModel.from_pretrained(
            model_name = self.model_name, 
            load_in_4bit = True,
        )
    
    def formate_input(self, image, user_text):
        formated_message = self.template(user_text)
        templated_message = self.tokenizer.apply_chat_template(formated_message)
        inputs = self.tokenizer(
            image,
            templated_message,
            add_special_tokens = False,
            return_tensors = "pt",
        ).to("cuda")
        
    def pred(self, image_bytes, user_text):
        image = Image.open(BytesIO(image_bytes))
        inputs = self.formate_input(image, user_text)
        response = self.model.generate(
            **inputs,
            max_new_tokens=1024,
            do_sample=False,  # Use greedy decoding
            temperature=0.0,  # Deterministic
        )
        response_text = self.tokenizer.decode(response[0], skip_special_tokens=True)
        return response_text
    
    def template(self, user_text):
        instruction = (
            "Please provide a direct and specific response to the following question, "
            "avoiding feedback-style comments:\n" 
            + user_text
        )
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image"},  # Indicate the presence of an image
                    {"type": "text", "text": instruction},
                ],
            }
        ]
        return messages