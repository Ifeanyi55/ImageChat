# pip install google-generativeai grpcio grpcio-tools gradio

import google.generativeai as genai
import gradio as gr
import numpy as np
import PIL.Image

genai.configure(api_key="input your Google AI Studio API key")

def ImageChat(image, prompt):

  # load model
  model = genai.GenerativeModel("gemini-pro-vision")

  # check image file and convert to a Numpy array
  if isinstance(image, np.ndarray):

        img = PIL.Image.fromarray(image)
  else:
        img = PIL.Image.open(image)

  response =  model.generate_content([prompt, img])

  return response.text

# build gradio frontend
app = gr.Interface(ImageChat,
                   inputs = [gr.Image(), gr.Text()],
                   outputs = gr.Text(),
                   title = "Image Chat",
                   theme = gr.themes.Soft())

app.launch(debug = True)
