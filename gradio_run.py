import gradio as gr
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


with gr.Blocks(theme=gr.themes.Soft()) as demo: # 设置主题
    gr.Markdown("输入voc和保存路径")
    with gr.Row():
        voice = gr.Textbox(placeholder="输入voc值",label="voice")
        output_wav = gr.Textbox(placeholder="输入保存路径",label="保存路径")

    with gr.Tab("文本生成语音"):
        gr.Markdown("输入文本")
        with gr.Row():
            inp1 = gr.Textbox(placeholder="文本",label="路径")
            # out1 = gr.Textbox(placeholder="文本")
        btn1 = gr.Button("Run")
        btn1.click(fn=input_text, inputs=[inp1,voice,output_wav])

    with gr.Tab("上传文本生成语音"):
        gr.Markdown("上传文件")
        with gr.Row():
            file_path = gr.File(file_types = ["file"],label="文件")
        btn2 = gr.Button("Run")
        btn2.click(fn=upload_file, inputs=[file_path,voice,output_wav])

    with gr.Tab("输入文件路径，生成语音"):
        gr.Markdown("输入文件名")
        with gr.Row():
            file_path_2 = gr.Textbox(placeholder="文本",label="文件名")
        btn3 = gr.Button("Run")
        btn3.click(fn=input_file_name, inputs=[file_path_2,voice,output_wav])

    outputs=[gr.Textbox(label="完成消息")]
demo.launch()



