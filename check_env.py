# 导入我们刚才安装的包
import torch
import transformers

# 打印一下版本号，确认安装成功
print("PyTorch version:", torch.__version__)
print("Transformers version:", transformers.__version__)

# 复习一下基础语法：变量与f-string（格式化字符串）
device_name = "cuda" if torch.cuda.is_available() else "cpu"
print(f"当前使用的设备是: {device_name}")

# 如果是 cuda，说明你的 3060 显卡被 Python 识别到了
if device_name == "cuda":
    print("恭喜！你的 3060 显卡已经就绪！")
else:
    print("注意：目前在使用 CPU，没关系，暂时够用。")