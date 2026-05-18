import dashscope
from dashscope import Generation
from docx import Document
import PyPDF2
import os

# ===================== 填写你的阿里云API KEY =====================
dashscope.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def read_txt(file_path):
    """读取 TXT 文件"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        with open(file_path, "r", encoding="gbk") as f:
            return f.read()


def read_docx(file_path):
    """读取 Word文档"""
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


def read_pdf(file_path):
    """读取 PDF文档"""
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def read_file(file_path):
    """自动识别文件类型并读取内容"""
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".txt":
        return read_txt(file_path)
    elif ext == ".docx":
        return read_docx(file_path)
    elif ext == ".pdf":
        return read_pdf(file_path)
    else:
        raise Exception("不支持的文件格式！仅支持TXT、DOCX、PDF")


def generate_chinese_summary(text, max_len=200):
    """生成中文摘要，适配长短文本"""
    prompt = f"""
    请对下面的文档内容进行专业、精炼的中文摘要：
    1. 保留所有核心观点与关键信息
    2. 语言通顺连贯，不直接照搬原文句子
    3. 控制摘要长度，尽量接近{max_len}字，不超过上限
    文档内容：
    {text}
    """

    response = Generation.call(
        model="qwen-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3  # 稍高温度，让AI能灵活扩写短句、优化表达
    )
    return response.output.text


def generate_english_summary(text, max_len=150):
    """生成英文摘要，适配长短文本"""
    prompt = f"""
    Please write a concise, professional English summary of the following document:
    1. Include all core information and key points
    2. Use fluent, natural academic English, do not just copy the original text
    3. Aim for around {max_len} words, do not exceed the limit
    Document content:
    {text}
    """

    response = Generation.call(
        model="qwen-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.output.text


# ===================== 主程序 =====================
if __name__ == "__main__":
    # 在这里修改你的文件名！支持.txt/.docx /.pdf
    FILE_NAME = "GPS.docx"

    # 1. 读取文档
    try:
        content = read_file(FILE_NAME)
        print(f"✅ 文档读取成功，原文共 {len(content)} 字")
    except Exception as e:
        print(f"❌ 读取文档失败：{e}")
        exit()

    # 2. 生成摘要
    print("\n正在生成中文摘要...")
    zh_summary = generate_chinese_summary(content)
    print("✅ 中文摘要生成完成")

    print("\n正在生成英文摘要...")
    en_summary = generate_english_summary(content)
    print("✅ 英文摘要生成完成")

    # 3. 输出结果（带字数统计）
    print("\n" + "=" * 60)
    print(f"📄 中文摘要（{len(zh_summary)} 字）")
    print("=" * 60)
    print(zh_summary)

    print("\n" + "=" * 60)
    print(f"📄 English Summary（{len(en_summary.split())} words）")
    print("=" * 60)
    print(en_summary)