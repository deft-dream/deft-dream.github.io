#!/usr/bin/env python3
"""
DARKSEC Blog - 文章生成器
用法: python3 new-post.py "文章标题" "分类" "标签1,标签2"
"""

import sys
import os
from datetime import datetime

def create_post(title, category, tags):
    # 生成文件名
    slug = title.lower()
    slug = slug.replace(' ', '-')
    slug = slug.replace('：', '-')
    slug = slug.replace('→', 'to')
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    filename = f"{slug}.html"
    
    # 读取模板
    with open('templates/article-template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 替换内容
    today = datetime.now().strftime('%Y-%m-%d')
    tags_html = '\n'.join([f'          <span class="tag">{tag.strip()}</span>' for tag in tags.split(',')])
    
    content = template.replace('文章标题', title)
    content = content.replace('分类 / 子分类', category)
    content = content.replace('YYYY-MM-DD', today)
    content = content.replace('标签1 / 标签2', ' / '.join([t.strip() for t in tags.split(',')]))
    content = content.replace('<span class="tag">标签1</span>\n          <span class="tag">标签2</span>', tags_html)
    
    # 保存文件
    filepath = f'posts/{filename}'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 文章已创建: {filepath}")
    print(f"📝 记得在 posts/index.html 和 index.html 中添加链接!")
    
    return filepath

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("用法: python3 new-post.py \"文章标题\" \"分类\" \"标签1,标签2\"")
        print("示例: python3 new-post.py \"SQL注入基础\" \"注入攻击\" \"SQLi,基础\"")
        sys.exit(1)
    
    title = sys.argv[1]
    category = sys.argv[2]
    tags = sys.argv[3]
    
    create_post(title, category, tags)