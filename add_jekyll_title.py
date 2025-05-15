import os
import re
import yaml

def add_title_to_markdown_files(directory):
    """
    遍历指定目录下的Markdown文件，如果缺少title字段，则添加。
    """
    if not os.path.isdir(directory):
        print(f"错误：目录 {directory} 不存在。")
        return

    print(f"开始处理目录: {directory}")
    processed_count = 0

    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            print(f"处理文件: {filename}")

            try:
                with open(filepath, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    f.seek(0) # 回到文件开头

                    # 检查是否存在YAML Front Matter
                    # 匹配以 --- 开头和结尾的块
                    front_matter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)

                    if front_matter_match:
                        # 文件已有Front Matter
                        front_matter_str = front_matter_match.group(1)
                        front_matter = yaml.safe_load(front_matter_str)

                        if not isinstance(front_matter, dict):
                            print(f"警告：文件 {filename} 的Front Matter格式不正确或为空，跳过处理。")
                            continue

                        if 'title' not in front_matter:
                            # 没有title字段，添加
                            print(f"  - 添加 title 字段")
                            front_matter['title'] = os.path.splitext(filename)[0] # 使用文件名作为标题
                            # 重新构建完整的Front Matter字符串
                            updated_front_matter_str = "---\n" + yaml.dump(front_matter, allow_unicode=True, default_flow_style=False) + "---\n"
                            # 将更新后的内容写回文件
                            new_content = updated_front_matter_str + content[front_matter_match.end():]
                            f.write(new_content)
                            f.truncate() # Truncate any remaining original content if new content is shorter
                            processed_count += 1
                        else:
                            print(f"  - 已包含 title 字段，跳过。")

                    else:
                        # 文件没有Front Matter，添加新的Front Matter块
                        print(f"  - 添加新的 Front Matter 和 title 字段")
                        title = os.path.splitext(filename)[0] # 使用文件名作为标题
                        new_front_matter = {"title": title}
                        new_front_matter_str = "---\n" + yaml.dump(new_front_matter, allow_unicode=True, default_flow_style=False) + "---\n"
                        new_content = new_front_matter_str + content
                        f.write(new_content)
                        f.truncate()
                        processed_count += 1

            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")

    print(f"处理完成。共处理 {processed_count} 个文件。")

# 设置您的 _gaomipuhuinianhua 目录路径
# 请根据您的实际路径进行修改
gaomipuhuinianhua_dir = "_gaomipuhuinianhua" # 假设脚本在项目根目录运行

add_title_to_markdown_files(gaomipuhuinianhua_dir)