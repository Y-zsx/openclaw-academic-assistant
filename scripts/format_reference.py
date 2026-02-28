#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
参考文献格式化工具 - GB/T 7714-2015 标准
"""

import re
import sys
import argparse
from typing import Dict, List


class ReferenceFormatter:
    def __init__(self):
        pass
    
    def parse_author(self, author_str: str) -> str:
        """解析作者姓名"""
        if not author_str:
            return ""
        
        authors = []
        for author in re.split(r'[，,;；]', author_str):
            author = author.strip()
            if not author:
                continue
            
            if re.match(r'^[\u4e00-\u9fa5]+$', author):
                authors.append(author)
            else:
                parts = author.strip().split()
                if len(parts) >= 1:
                    surname = parts[-1].upper().rstrip(',;:')
                    given_names = ' '.join([p[0].upper() for p in parts[:-1] if p])
                    if given_names:
                        authors.append(f"{surname} {given_names}")
                    else:
                        authors.append(surname)
        
        if len(authors) > 3:
            return ', '.join(authors[:3]) + ', et al.'
        return ', '.join(authors)
    
    def format_journal(self, data: Dict) -> str:
        author = self.parse_author(data.get('author', ''))
        title = data.get('title', '').strip()
        journal = data.get('journal', '').strip()
        year = data.get('year', '').strip()
        volume = data.get('volume', '').strip()
        issue = data.get('issue', '').strip()
        pages = data.get('pages', '').strip()
        
        if not author and not title:
            return ""
        
        result = f"{author}. {title}[J]. {journal}"
        if year:
            result += f", {year}"
            if volume:
                if issue:
                    result += f", {volume}({issue})"
                else:
                    result += f", {volume}"
        if pages:
            result += f": {pages}"
        result += "."
        return result
    
    def format_thesis(self, data: Dict) -> str:
        author = self.parse_author(data.get('author', ''))
        title = data.get('title', '').strip()
        school = data.get('school', '').strip()
        location = data.get('location', '未知地点').strip()
        year = data.get('year', '').strip()
        
        if not author and not title:
            return ""
        
        return f"{author}. {title}[D]. {location}: {school}, {year}."
    
    def format_book(self, data: Dict) -> str:
        author = self.parse_author(data.get('author', ''))
        title = data.get('title', '').strip()
        publisher = data.get('publisher', '').strip()
        location = data.get('location', '未知地点').strip()
        year = data.get('year', '').strip()
        
        if not author and not title:
            return ""
        
        result = f"{author}. {title}[M]. {location}: {publisher}"
        if year:
            result += f", {year}"
        result += "."
        return result
    
    def _extract_field(self, text: str, markers: List[str], next_markers: List[str] = None) -> str:
        """提取字段值"""
        for marker in markers:
            idx = text.find(marker)
            if idx != -1:
                start = idx + len(marker)
                # 找到下一个标记的位置
                end = len(text)
                if next_markers:
                    for nm in next_markers:
                        nm_idx = text.find(nm, start)
                        if nm_idx != -1 and nm_idx < end:
                            end = nm_idx
                
                value = text[start:end].strip()
                # 清理末尾的标点
                value = re.sub(r'[，,;:：]+$', '', value)
                if value:
                    return value
        return ""
    
    def _parse_text(self, text: str) -> Dict:
        """解析文本"""
        data = {}
        
        # 定义字段标记
        author_markers = ['作者：', '作者:', 'Authors:', 'Author:']
        title_markers = ['标题：', '标题:', '题名：', '题名:', 'Title:', '题目:']
        journal_markers = ['期刊：', '期刊:', '杂志：', 'Journal:', '来源:']
        year_markers = ['年份：', '年份:', '年:', 'Year:']
        volume_markers = ['卷：', '卷:', 'Volume:']
        issue_markers = ['期：', '期:', 'Number:']
        pages_markers = ['页码：', '页码:', '页:', 'Pages:']
        publisher_markers = ['出版社：', '出版社:', '出版者:', 'Publisher:']
        school_markers = ['学校：', '学校:', '单位:', 'School:', 'University:']
        
        data['author'] = self._extract_field(text, author_markers, title_markers)
        data['title'] = self._extract_field(text, title_markers, journal_markers)
        data['journal'] = self._extract_field(text, journal_markers, year_markers)
        data['year'] = self._extract_field(text, year_markers, volume_markers)
        data['volume'] = self._extract_field(text, volume_markers, issue_markers)
        data['issue'] = self._extract_field(text, issue_markers, pages_markers)
        data['pages'] = self._extract_field(text, pages_markers)
        data['publisher'] = self._extract_field(text, publisher_markers, year_markers)
        data['school'] = self._extract_field(text, school_markers, year_markers)
        
        return data
    
    def format_reference(self, text: str) -> str:
        text = text.strip()
        data = self._parse_text(text)
        
        if data.get('school'):
            return self.format_thesis(data)
        elif data.get('publisher') and not data.get('journal'):
            return self.format_book(data)
        else:
            return self.format_journal(data)


def main():
    parser = argparse.ArgumentParser(description='参考文献格式化工具')
    parser.add_argument('--input', '-i', type=str, help='输入文献信息')
    parser.add_argument('--file', '-f', type=str, help='输入文件')
    
    args = parser.parse_args()
    
    formatter = ReferenceFormatter()
    
    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    result = formatter.format_reference(line.strip())
                    if result:
                        print(result)
    elif args.input:
        result = formatter.format_reference(args.input)
        print(result)
    else:
        print("参考文献格式化工具 (GB/T 7714-2015)")
        print("输入 'quit' 退出")
        
        while True:
            try:
                text = input("\n请输入：").strip()
                if text.lower() in ['quit', 'q']:
                    break
                result = formatter.format_reference(text)
                print(f"结果：{result}")
            except:
                break


if __name__ == '__main__':
    main()
