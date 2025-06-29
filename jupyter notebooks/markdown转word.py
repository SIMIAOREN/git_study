import pypandoc


def convert_md_to_docx(md_file_path, output_docx_path):
    """
    将Markdown文件转换为Word文档
    :param md_file_path: 输入的Markdown文件路径
    :param output_docx_path: 输出的Word文档路径
    """
    try:
        # 转换核心代码
        output = pypandoc.convert_file(
            source_file=md_file_path,  # 输入Markdown文件
            to='docx',  # 输出格式为Word
            format='markdown',  # 输入格式为Markdown
            outputfile=output_docx_path,  # 输出文件路径
            extra_args=['--standalone']  # 生成完整的Word文档结构
        )
        return True
    except Exception as e:
        print(f"转换失败: {str(e)}")
        return False


# 示例用法
if __name__ == "__main__":
    input_file = "E:/vscode/github_my/git_study/jupyter notebooks/python3学习笔记.md"  # 输入的Markdown文件
    output_file = "E:/vscode/github_my/git_study/jupyter notebooks/python3学习笔记3.docx"  # 输出的Word文档

    success = convert_md_to_docx(input_file, output_file)

    if success:
        print(f"转换成功! Word文档已保存至: {output_file}")
    else:
        print("转换失败，请检查错误信息")