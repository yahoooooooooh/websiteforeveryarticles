// js/script.js

document.addEventListener('DOMContentLoaded', () => {
    const navigationElement = document.getElementById('navigation');
    const articleContentElement = document.getElementById('article-content');
    const initialContentElement = document.getElementById('initial-content'); // 获取初始内容区域

    // --- Markdown 转换器 ---
    // 我们需要一个 Markdown 到 HTML 的转换器。
    // Marked.js 是一个流行的选择。您需要将它添加到您的项目中。
    // 您可以从 CDN 引入，或者下载 marked.min.js 并本地链接。
    // 例如，在 index.html 的 <head> 中添加:
    // <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    // 或者下载后: <script src="js/marked.min.js"></script>

    let articlesStructure = {}; // 将在这里存储从JSON加载的数据

    function renderNavigation() {
        if (!navigationElement) {
            console.error("Navigation element not found!");
            return;
        }
        navigationElement.innerHTML = ''; // 清空

        for (const theme in articlesStructure) {
            if (articlesStructure.hasOwnProperty(theme) && articlesStructure[theme].length > 0) {
                const themeLi = document.createElement('li');
                const themeSpan = document.createElement('span');
                themeSpan.textContent = theme;
                themeSpan.classList.add('theme-title');

                const articlesUl = document.createElement('ul');
                articlesUl.classList.add('article-list');

                articlesStructure[theme].forEach(article => {
                    const articleLi = document.createElement('li');
                    const articleLink = document.createElement('a');
                    articleLink.textContent = article.title;
                    articleLink.href = '#';
                    articleLink.dataset.path = article.path;
                    articleLink.addEventListener('click', (event) => {
                        event.preventDefault();
                        loadArticle(article.path);
                        // 可选: 更新活动链接样式
                        document.querySelectorAll('#navigation a').forEach(a => a.classList.remove('active'));
                        articleLink.classList.add('active');
                    });
                    articleLi.appendChild(articleLink);
                    articlesUl.appendChild(articleLi);
                });

                themeLi.appendChild(themeSpan);
                themeLi.appendChild(articlesUl);
                navigationElement.appendChild(themeLi);

                themeSpan.addEventListener('click', () => {
                    articlesUl.classList.toggle('open');
                });
            }
        }
    }

    async function loadArticle(path) {
        if (!articleContentElement) {
            console.error("Article content element not found!");
            return;
        }
        try {
            const response = await fetch(path);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status} for path: ${path}`);
            }
            const markdownText = await response.text();

            if (typeof marked === 'undefined') {
                articleContentElement.innerHTML = "<p>错误：Markdown 转换器 (marked.js) 未加载。</p>" +
                                                  "<p>请在 index.html 中引入 marked.js。例如：</p>" +
                                                  "<pre>&lt;script src=\"https://cdn.jsdelivr.net/npm/marked/marked.min.js\"&gt;&lt;/script&gt;</pre>";
                console.error("marked.js is not loaded. Please include it in your HTML.");
                return;
            }

            articleContentElement.innerHTML = marked.parse(markdownText); // 使用 marked.js 转换
            if(initialContentElement) initialContentElement.style.display = 'none'; // 加载文章后隐藏初始内容

        } catch (error) {
            console.error('加载文章失败:', error);
            articleContentElement.innerHTML = `<p>抱歉，加载文章失败: ${path}</p><p>${error.message}</p>`;
            if(initialContentElement) initialContentElement.style.display = 'none';
        }
    }

    // 获取导航数据并初始化
    async function initialize() {
        try {
            const response = await fetch('data/navigation_data.json'); // 从JSON文件加载
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            articlesStructure = await response.json();
            renderNavigation();
        } catch (error) {
            console.error('加载导航数据失败:', error);
            if (navigationElement) {
                navigationElement.innerHTML = '<li>加载导航失败!</li>';
            }
             if (articleContentElement && initialContentElement) {
                initialContentElement.innerHTML = `<p>无法加载导航结构，因此无法浏览文章。请确保 'data/navigation_data.json' 文件存在并且格式正确。</p><p>您可以尝试运行 'python generate_navigation.py' 来生成该文件。</p>`;
            }
        }
    }

    initialize(); // 调用初始化函数
});