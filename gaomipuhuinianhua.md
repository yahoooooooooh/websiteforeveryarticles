    ---
    layout: page # 或者您喜欢的主题的其他布局，例如 'default'
    title: 高密扑灰年画
    permalink: /gaomipuhuinianhua/ # 这个页面本身的URL
    ---

    <h1>{{ page.title }}</h1>

    <p>这里汇集了关于高密扑灰年画的精彩文章和资料。</p>

    <ul>
      {% for item in site.gaomipuhuinianhua %}
        <li>
          <a href="{{ item.url | relative_url }}">{{ item.title | default: item.name }}</a>
          {# 您还可以显示其他元数据，例如 item.date，如果您的MD文件中有的话 #}
        </li>
      {% endfor %}
    </ul>
