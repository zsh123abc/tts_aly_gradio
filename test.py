# import gradio as gr
# import numpy as np
# import time
 
# def fake_diffusion(steps):
#     for i in range(steps):
#         time.sleep(1)
#         image = '。'*i
#         yield image
#     image = "cute_dog.jpg"
#     yield image
 
# #官方例子这里的滑动块是浮点数，需要整数，不然迭代次数出错，加一个step，每次是1即可
# demo = gr.Interface(fake_diffusion, inputs=gr.Slider(1, 10, 3,step=1), outputs="text")
 
# demo.queue()
# demo.launch()



import gradio as gr
import time
import tts_run
def input_text(text,voice,output_wav):

    tts_run.tts_input_text(text,voice,output_wav)
    return f"Welcome to Gradio, !"

def upload_file(file_path,voice,output_wav):

    tts_run.tts_upload_file(file_path,voice,output_wav)
    return f"Welcome to Gradio, !"

def input_file_name(file_path,voice,output_wav):

    tts_run.tts_upload_file(file_path,voice,output_wav)
    return f"Welcome to Gradio, !"
# Define a real-time updating function
def fake_diffusion(steps):
    for i in range(steps):
        time.sleep(1)
        image = '。' * i
        yield image
    image = "cute_dog.jpg"
    yield image

# Create Gradio user interface
demo = gr.Interface(
    fake_diffusion,  # Use the real-time updating function as the callback
    inputs=gr.Slider(1, 10, 3, step=1),
    outputs="text"
)

# Create the first input interface elements
voice = gr.Textbox("voice", placeholder="Input voc value")
output_wav = gr.Textbox("output_wav", placeholder="Input save path")

# Create the second input interface elements
inp1 = gr.Textbox("input_text", placeholder="Text")
file_path = gr.File("file_path", file_types=["file"])
file_path_2 = gr.Textbox("file_path_2", placeholder="File name")

# Create buttons for each input interface
btn1 = gr.Button("Run", fn=input_text, inputs=[inp1, voice, output_wav])
btn2 = gr.Button("Run", fn=upload_file, inputs=[file_path, voice, output_wav])
btn3 = gr.Button("Run", fn=input_file_name, inputs=[file_path_2, voice, output_wav])

# Display all elements in a layout
with demo:
    gr.Row(
        gr.Markdown("输入voc和保存路径"),
        gr.Tab("文本生成语音", gr.Row(inp1, btn1)),
        gr.Tab("上传文本生成语音", gr.Row(file_path, btn2)),
        gr.Tab("输入文件路径，生成语音", gr.Row(file_path_2, btn3))
    )

# Launch the user interface
demo.launch()
