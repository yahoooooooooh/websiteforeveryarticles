# generate_navigation.py
import os
import json

def generate_navigation_data(articles_dir="articles", output_file="data/navigation_data.json"):
    """
    扫描 articles 目录，生成导航数据的 JSON 文件。
    """
    navigation_structure = {}
    articles_base_path = articles_dir

    if not os.path.isdir(articles_base_path):
        print(f"错误：找不到文章目录 '{articles_base_path}'")
        return

    # 确保输出目录存在
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建目录: {output_dir}")

    # 遍历 articles 目录下的每个主题文件夹
    for theme_name in os.listdir(articles_base_path):
        theme_path = os.path.join(articles_base_path, theme_name)
        if os.path.isdir(theme_path):
            navigation_structure[theme_name] = [] # 使用目录名作为主题名
            # 遍历主题文件夹下的每个 Markdown 文件
            for filename in os.listdir(theme_path):
                if filename.endswith(".md"):
                    article_title = os.path.splitext(filename)[0] # 使用文件名（不含.md）作为标题
                    # 你可以根据需要进一步处理 article_title，例如替换 "-" 为 " "，首字母大写等
                    # article_title = article_title.replace('-', ' ').title()

                    article_path = f"{articles_base_path}/{theme_name}/{filename}" # 保持 POSIX 风格的路径给 JS
                    navigation_structure[theme_name].append({
                        "title": article_title,
                        "path": article_path
                    })
            # 如果一个主题文件夹下没有 .md 文件，可以选择是否在导航中显示该主题
            # if not navigation_structure[theme_name]:
            #     del navigation_structure[theme_name]


    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(navigation_structure, f, ensure_ascii=False, indent=4)
        print(f"导航数据已成功生成到: {output_file}")
    except IOError as e:
        print(f"写入文件 {output_file} 时出错: {e}")
    except Exception as e:
        print(f"生成导航数据时发生意外错误: {e}")

if __name__ == "__main__":
    generate_navigation_data()