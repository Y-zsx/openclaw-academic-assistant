#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BibTeX 文件解析工具
支持解析 .bib 文件并转换为 GB/T 7714 格式
"""

import re
import sys
import argparse
from typing import Dict, List, Optional


class BibTeXParser:
    """BibTeX 文件解析器"""
    
    # BibTeX 类型映射到 GB/T 7714 类型
    TYPE_MAP = {
        'article': 'J',       # 期刊论文
        'inproceedings': 'C', # 会议论文
        'proceedings': 'C',
        'book': 'M',          # 专著
        'inbook': 'M',        # 书中章节
        'incollection': 'M',
        'phdthesis': 'D',     # 博士论文
        'mastersthesis': 'D', # 硕士论文
        'thesis': 'D',
        'techreport': 'R',    # 技术报告
        'manual': 'R',
        'misc': 'EB/OL',      # 其他
        'online': 'EB/OL',
        'www': 'EB/OL',
        'patent': 'P',        # 专利
        'standard': 'S',      # 标准
    }
    
    def __init__(self):
        self.entries = []
    
    def parse_file(self, filepath: str) -> List[Dict]:
        """解析 BibTeX 文件"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.parse_string(content)
        except FileNotFoundError:
            print(f"错误：文件不存在：{filepath}")
            return []
        except Exception as e:
            print(f"错误：{e}")
            return []
    
    def parse_string(self, content: str) -> List[Dict]:
        """解析 BibTeX 字符串"""
        entries = []
        
        # 移除注释
        content = re.sub(r'%.*$', '', content, flags=re.MULTILINE)
        
        # 匹配 BibTeX 条目
        pattern = r'@(\w+)\{([^,\s]+)\s*,\s*(.*?)\n\}'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for match in matches:
            entry_type, cite_key, fields_str = match
            
            # 解析字段
            fields = self._parse_fields(fields_str)
            fields['type'] = entry_type.lower()
            fields['citekey'] = cite_key
            
            entries.append(fields)
        
        self.entries = entries
        return entries
    
    def _parse_fields(self, fields_str: str) -> Dict:
        """解析字段字符串"""
        fields = {}
        
        # 匹配字段：name = {value} 或 name = "value" 或 name = number
        pattern = r'(\w+)\s*=\s*(?:\{([^}]*)\}|"([^"]*)"|(\d+))'
        matches = re.findall(pattern, fields_str, re.DOTALL)
        
        for match in matches:
            name = match[0].lower()
            # value 可能在第 2、3 或 4 个组
            value = match[1] or match[2] or match[3] or ''
            value = ' '.join(value.split())  # 清理多余空白
            fields[name] = value.strip()
        
        return fields
    
    def to_gbt7714(self, entry: Dict) -> str:
        """将 BibTeX 条目转换为 GB/T 7714 格式"""
        entry_type = entry.get('type', 'misc')
        ref_type = self.TYPE_MAP.get(entry_type, 'EB/OL')
        
        # 提取作者
        author = self._format_author(entry.get('author', ''))
        
        # 提取标题
        title = entry.get('title', '').strip()
        
        # 根据类型格式化
        if entry_type in ['article', 'inproceedings', 'proceedings']:
            return self._format_journal_conference(entry, author, title, ref_type)
        elif entry_type in ['book', 'inbook', 'incollection']:
            return self._format_book(entry, author, title, ref_type)
        elif entry_type in ['phdthesis', 'mastersthesis', 'thesis']:
            return self._format_thesis(entry, author, title, ref_type)
        elif entry_type in ['online', 'misc', 'www']:
            return self._format_electronic(entry, author, title, ref_type)
        else:
            return self._format_generic(entry, author, title, ref_type)
    
    def _format_author(self, author: str) -> str:
        """格式化作者"""
        if not author:
            return ""
        
        authors = []
        # BibTeX 作者格式：Last, First and Last, First
        author_list = re.split(r'\s+and\s+', author)
        
        for a in author_list:
            a = a.strip()
            if not a:
                continue
            
            # 处理 "Last, First" 格式
            if ',' in a:
                parts = a.split(',')
                if len(parts) >= 2:
                    last = parts[0].strip().upper()
                    first = parts[1].strip()
                    # 名缩写
                    first_parts = first.split()
                    first_initials = ' '.join([p[0].upper() for p in first_parts if p])
                    authors.append(f"{last} {first_initials}")
                else:
                    authors.append(a.upper())
            else:
                # 直接是大写的情况
                authors.append(a.upper())
        
        if len(authors) > 3:
            return ', '.join(authors[:3]) + ', et al.'
        return ', '.join(authors)
    
    def _format_journal_conference(self, entry: Dict, author: str, title: str, ref_type: str) -> str:
        """格式化期刊/会议论文"""
        journal = entry.get('journal', entry.get('booktitle', '')).strip()
        year = entry.get('year', '').strip()
        volume = entry.get('volume', '').strip()
        number = entry.get('number', entry.get('issue', '')).strip()
        pages = entry.get('pages', '').strip()
        publisher = entry.get('publisher', '').strip()
        
        if entry.get('type') == 'inproceedings':
            result = f"{author}. {title}[C]//{journal}"
            if publisher:
                result += f". {publisher}"
        else:
            result = f"{author}. {title}[{ref_type}]. {journal}"
        
        if year:
            result += f", {year}"
            if volume:
                if number:
                    result += f", {volume}({number})"
                else:
                    result += f", {volume}"
        
        if pages:
            # 清理页码格式（去除 p., pp. 等）
            pages = re.sub(r'^p\.?\s*', '', pages, flags=re.IGNORECASE)
            pages = re.sub(r'^pp\.?\s*', '', pages, flags=re.IGNORECASE)
            result += f": {pages}"
        
        result += "."
        return result
    
    def _format_book(self, entry: Dict, author: str, title: str, ref_type: str) -> str:
        """格式化专著"""
        publisher = entry.get('publisher', '').strip()
        address = entry.get('address', entry.get('location', '未知地点')).strip()
        year = entry.get('year', '').strip()
        edition = entry.get('edition', '').strip()
        pages = entry.get('pages', '').strip()
        
        result = f"{author}. {title}[{ref_type}]"
        if edition:
            result += f". {edition}版"
        result += f". {address}: {publisher}"
        if year:
            result += f", {year}"
        if pages:
            result += f": {pages}"
        result += "."
        return result
    
    def _format_thesis(self, entry: Dict, author: str, title: str, ref_type: str) -> str:
        """格式化学位论文"""
        school = entry.get('school', entry.get('university', '')).strip()
        address = entry.get('address', entry.get('location', '未知地点')).strip()
        year = entry.get('year', '').strip()
        
        return f"{author}. {title}[{ref_type}]. {address}: {school}, {year}."
    
    def _format_electronic(self, entry: Dict, author: str, title: str, ref_type: str) -> str:
        """格式化电子资源"""
        url = entry.get('url', '').strip()
        year = entry.get('year', '').strip()
        urldate = entry.get('urldate', entry.get('note', '')).strip()
        
        result = f"{author}. {title}[{ref_type}]"
        if url:
            result += f". {url}"
        if year:
            result += f", {year}"
        if urldate:
            result += f" ({urldate})"
        result += "."
        return result
    
    def _format_generic(self, entry: Dict, author: str, title: str, ref_type: str) -> str:
        """通用格式化"""
        journal = entry.get('journal', entry.get('booktitle', '')).strip()
        year = entry.get('year', '').strip()
        
        result = f"{author}. {title}[{ref_type}]"
        if journal:
            result += f". {journal}"
        if year:
            result += f", {year}"
        result += "."
        return result
    
    def format_all(self) -> List[str]:
        """格式化所有条目"""
        results = []
        for i, entry in enumerate(self.entries, 1):
            formatted = self.to_gbt7714(entry)
            if formatted:
                results.append(f"[{i}] {formatted}")
        return results
    
    def format_all_with_citekey(self) -> List[str]:
        """格式化所有条目（带引用键）"""
        results = []
        for i, entry in enumerate(self.entries, 1):
            formatted = self.to_gbt7714(entry)
            citekey = entry.get('citekey', '')
            if formatted:
                if citekey:
                    results.append(f"[{i}] {citekey}: {formatted}")
                else:
                    results.append(f"[{i}] {formatted}")
        return results


def main():
    parser = argparse.ArgumentParser(description='BibTeX 文件解析工具')
    parser.add_argument('--input', '-i', type=str, required=True, help='输入 .bib 文件路径')
    parser.add_argument('--output', '-o', type=str, help='输出文件路径（可选）')
    parser.add_argument('--with-citekey', action='store_true', help='显示引用键')
    parser.add_argument('--count', action='store_true', help='只显示数量')
    
    args = parser.parse_args()
    
    parser_obj = BibTeXParser()
    entries = parser_obj.parse_file(args.input)
    
    if not entries:
        print("未找到任何 BibTeX 条目")
        return
    
    if args.count:
        print(f"共 {len(entries)} 篇文献")
        return
    
    if args.with_citekey:
        results = parser_obj.format_all_with_citekey()
    else:
        results = parser_obj.format_all()
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            for result in results:
                f.write(result + '\n')
        print(f"已保存到：{args.output}")
    else:
        for result in results:
            print(result)


if __name__ == '__main__':
    main()
