import tkinter as tk

# 创建窗口
window = tk.Tk()

# 设置窗口大小
window.geometry("600x400")

# 定义提示文本
placeholder_text_1 = "输入文本"
placeholder_text_2 = "请输入文件完整路径"
placeholder_text_3 = "输入声音voice"
placeholder_text_4 = "填写输入文件的保存路径"

# 创建四个文本框
input_entry1 = tk.Entry(window)
input_entry1.config(font=("Arial", 20))  # 设置字体和字号
input_entry1.pack()

input_entry2 = tk.Entry(window)
input_entry2.config(font=("Arial", 20))  # 设置字体和字号
input_entry2.pack()

input_entry3 = tk.Entry(window)
input_entry3.config(font=("Arial", 20))  # 设置字体和字号
input_entry3.pack()

input_entry4 = tk.Entry(window)
input_entry4.config(font=("Arial", 20))  # 设置字体和字号
input_entry4.pack()

# 定义绑定函数
def on_entry_click_1(event):
    if input_entry1.get() == placeholder_text_1:
        input_entry1.delete(0, "end")
        input_entry1.config(fg="black")  # 设置文本颜色为黑色

def on_focus_out_1(event):
    if input_entry1.get() == "":
        input_entry1.insert(0, placeholder_text_1)
        input_entry1.config(fg="gray")  # 设置文本颜色为灰色

def on_entry_click_2(event):
    if input_entry2.get() == placeholder_text_2:
        input_entry2.delete(0, "end")
        input_entry2.config(fg="black")  # 设置文本颜色为黑色

def on_focus_out_2(event):
    if input_entry2.get() == "":
        input_entry2.insert(0, placeholder_text_2)
        input_entry2.config(fg="gray")  # 设置文本颜色为灰色

def on_entry_click_3(event):
    if input_entry3.get() == placeholder_text_3:
        input_entry3.delete(0, "end")
        input_entry3.config(fg="black")  # 设置文本颜色为黑色

def on_focus_out_3(event):
    if input_entry3.get() == "":
        input_entry3.insert(0, placeholder_text_3)
        input_entry3.config(fg="gray")  # 设置文本颜色为灰色

def on_entry_click_4(event):
    if input_entry4.get() == placeholder_text_4:
        input_entry4.delete(0, "end")
        input_entry4.config(fg="black")  # 设置文本颜色为黑色

def on_focus_out_4(event):
    if input_entry4.get() == "":
        input_entry4.insert(0, placeholder_text_4)
        input_entry4.config(fg="gray")  # 设置文本颜色为灰色

# 绑定函数到文本框的事件
input_entry1.bind("<FocusIn>", on_entry_click_1)
input_entry1.bind("<FocusOut>", on_focus_out_1)

input_entry2.bind("<FocusIn>", on_entry_click_2)
input_entry2.bind("<FocusOut>", on_focus_out_2)

input_entry3.bind("<FocusIn>", on_entry_click_3)
input_entry3.bind("<FocusOut>", on_focus_out_3)

input_entry4.bind("<FocusIn>", on_entry_click_4)
input_entry4.bind("<FocusOut>", on_focus_out_4)

# 初始状态下显示提示文本
input_entry1.insert(0, placeholder_text_1)
input_entry1.config(fg="gray")  # 设置文本颜色为灰色

input_entry2.insert(0, placeholder_text_2)
input_entry2.config(fg="gray")  # 设置文本颜色为灰色

input_entry3.insert(0, placeholder_text_3)
input_entry3.config(fg="gray")  # 设置文本颜色为灰色

input_entry4.insert(0, placeholder_text_4)
input_entry4.config(fg="gray")  # 设置文本颜色为灰色


# 创建输出框
output_label = tk.Label(window, text="")
output_label.config(font=("Arial", 20))  # 设置字体和字号
output_label.pack()

# 定义处理函数
def process_input():
    num = input_entry1.get()  # 获取输入框中的文本
    file_path = input_entry2.get()
    voice = input_entry3.get()
    output_wav = input_entry4.get()

    # 进行处理，例如计算或其他操作
    output_text = "处理结果: " + num
    output_label.config(text=output_text)  # 更新输出框中的文本

# 创建处理按钮
process_button = tk.Button(window, text="处理", command=process_input)
process_button.config(font=("Arial", 20))  # 设置字体和字号
process_button.pack()

# 运行应用程序
window.mainloop()
