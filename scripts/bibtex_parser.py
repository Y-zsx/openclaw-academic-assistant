#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BibTeX 文件解析工具 v1.2
支持解析 .bib 文件并转换为 GB/T 7714 格式
优化：英文作者解析、错误提示、统计信息
"""

import re
import sys
import argparse
from typing import Dict, List, Optional, Tuple


class BibTeXParser:
    """BibTeX 文件解析器"""
    
    TYPE_MAP = {
        'article': 'J',
        'inproceedings': 'C',
        'proceedings': 'C',
        'book': 'M',
        'inbook': 'M',
        'incollection': 'M',
        'phdthesis': 'D',
        'mastersthesis': 'D',
        'thesis': 'D',
        'techreport': 'R',
        'manual': 'R',
        'misc': 'EB/OL',
        'online': 'EB/OL',
        'www': 'EB/OL',
        'patent': 'P',
        'standard': 'S',
    }
    
    def __init__(self):
        self.entries = []
        self.errors = []
        self.stats = {'total': 0, 'success': 0, 'failed': 0}
    
    def parse_file(self, filepath: str) -> List[Dict]:
        """解析 BibTeX 文件"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.parse_string(content)
        except FileNotFoundError:
            self.errors.append(f"错误：文件不存在：{filepath}")
            return []
        except Exception as e:
            self.errors.append(f"错误：{e}")
            return []
    
    def parse_string(self, content: str) -> List[Dict]:
        """解析 BibTeX 字符串"""
        entries = []
        self.stats['total'] = 0
        
        # 移除注释
        content = re.sub(r'%.*$', '', content, flags=re.MULTILINE)
        
        # 匹配 BibTeX 条目 - 改进的正则
        pattern = r'@(\w+)\{([^,\s]+)\s*,(.+?)\n\}'
        matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
        
        for match in matches:
            self.stats['total'] += 1
            entry_type, cite_key, fields_str = match
            
            try:
                fields = self._parse_fields(fields_str)
                fields['type'] = entry_type.lower()
                fields['citekey'] = cite_key
                
                # 验证必填字段
                if not fields.get('title'):
                    self.errors.append(f"警告：{cite_key} 缺少标题字段")
                
                entries.append(fields)
                self.stats['success'] += 1
            except Exception as e:
                self.errors.append(f"解析 {cite_key} 失败：{str(e)}")
                self.stats['failed'] += 1
        
        self.entries = entries
        return entries
    
    def _parse_fields(self, fields_str: str) -> Dict:
        """解析字段字符串"""
        fields = {}
        
        # 匹配字段：name = {value} 或 name = "value" 或 name = number
        pattern = r'(\w+)\s*=\s*(?:\{([^}]*)\}|"([^"]*)"|(\d+)|([\w:/.-]+))'
        matches = re.findall(pattern, fields_str, re.DOTALL)
        
        for match in matches:
            name = match[0].lower()
            # value 可能在第 2、3、4 或 5 个组
            value = match[1] or match[2] or match[3] or match[4] or ''
            value = ' '.join(value.split())  # 清理多余空白
            fields[name] = value.strip()
        
        return fields
    
    def _format_author(self, author: str) -> str:
        """
        格式化作者姓名（优化版）
        支持多种 BibTeX 作者格式
        """
        if not author:
            return ""
        
        authors = []
        # BibTeX 作者格式：First Last and First Last 或 Last, First and Last, First
        author_list = re.split(r'\s+and\s+', author, flags=re.IGNORECASE)
        
        for a in author_list:
            a = a.strip()
            if not a:
                continue
            
            # 清理括号（如 {\L}ukasz）
            a = re.sub(r'\{\\[A-Za-z]+\}', lambda m: m.group().replace('{', '').replace('}', ''), a)
            
            # 处理 "Last, First" 格式
            if ',' in a:
                parts = a.split(',', 1)  # 只分割第一个逗号
                if len(parts) >= 2:
                    last = parts[0].strip().upper()
                    first = parts[1].strip()
                    # 名缩写
                    first_parts = first.split()
                    first_initials = ' '.join([p[0].upper() for p in first_parts if p and p not in [',', ';']])
                    if first_initials:
                        authors.append(f"{last} {first_initials}")
                    else:
                        authors.append(last)
                else:
                    authors.append(a.upper())
            else:
                # 处理 "First Last" 格式
                parts = a.split()
                if len(parts) >= 2:
                    # 最后一个是姓
                    last = parts[-1].upper()
                    # 前面是名
                    first_parts = parts[:-1]
                    first_initials = ' '.join([p[0].upper() for p in first_parts if p and p not in [',', ';']])
                    if first_initials:
                        authors.append(f"{last} {first_initials}")
                    else:
                        authors.append(last)
                elif len(parts) == 1:
                    authors.append(parts[0].upper())
        
        if len(authors) > 3:
            return ', '.join(authors[:3]) + ', et al.'
        return ', '.join(authors)
    
    def to_gbt7714(self, entry: Dict) -> str:
        """将 BibTeX 条目转换为 GB/T 7714 格式"""
        entry_type = entry.get('type', 'misc')
        ref_type = self.TYPE_MAP.get(entry_type, 'EB/OL')
        
        author = self._format_author(entry.get('author', ''))
        title = entry.get('title', '').strip()
        
        if not title:
            title = "无标题"
        
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
    
    def _format_journal_conference(self, entry: Dict, author: str, title: str, ref_type: str) -> str:
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
            pages = re.sub(r'^p\.?\s*', '', pages, flags=re.IGNORECASE)
            pages = re.sub(r'^pp\.?\s*', '', pages, flags=re.IGNORECASE)
            pages = pages.replace('--', '-')
            result += f": {pages}"
        
        result += "."
        return result
    
    def _format_book(self, entry: Dict, author: str, title: str, ref_type: str) -> str:
        publisher = entry.get('publisher', '').strip()
        address = entry.get('address', entry.get('location', '出版地不详')).strip()
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
        school = entry.get('school', entry.get('university', '')).strip()
        address = entry.get('address', entry.get('location', '地点不详')).strip()
        year = entry.get('year', '').strip()
        
        return f"{author}. {title}[{ref_type}]. {address}: {school}, {year}."
    
    def _format_electronic(self, entry: Dict, author: str, title: str, ref_type: str) -> str:
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
        journal = entry.get('journal', entry.get('booktitle', '')).strip()
        year = entry.get('year', '').strip()
        
        result = f"{author}. {title}[{ref_type}]"
        if journal:
            result += f". {journal}"
        if year:
            result += f", {year}"
        result += "."
        return result
    
    def format_all(self, show_citekey: bool = False) -> Tuple[List[str], Dict]:
        """格式化所有条目"""
        results = []
        for i, entry in enumerate(self.entries, 1):
            formatted = self.to_gbt7714(entry)
            citekey = entry.get('citekey', '')
            if formatted:
                if show_citekey and citekey:
                    results.append(f"[{i}] {citekey}: {formatted}")
                else:
                    results.append(f"[{i}] {formatted}")
        
        return results, self.stats
    
    def get_errors(self) -> List[str]:
        """获取错误列表"""
        return self.errors
    
    def get_stats_summary(self) -> str:
        """获取统计摘要"""
        total = self.stats['total']
        success = self.stats['success']
        failed = self.stats['failed']
        return f"共 {total} 篇文献，成功 {success} 篇" + (f"，失败 {failed} 篇" if failed > 0 else "")


def main():
    parser = argparse.ArgumentParser(description='BibTeX 文件解析工具 v1.2')
    parser.add_argument('--input', '-i', type=str, required=True, help='输入 .bib 文件路径')
    parser.add_argument('--output', '-o', type=str, help='输出文件路径（可选）')
    parser.add_argument('--with-citekey', action='store_true', help='显示引用键')
    parser.add_argument('--quiet', '-q', action='store_true', help='静默模式（不显示统计信息）')
    
    args = parser.parse_args()
    
    parser_obj = BibTeXParser()
    entries = parser_obj.parse_file(args.input)
    
    if not entries:
        print("❌ 未找到任何 BibTeX 条目")
        if parser_obj.get_errors():
            for err in parser_obj.get_errors():
                print(f"  {err}")
        return
    
    results, stats = parser_obj.format_all(show_citekey=args.with_citekey)
    
    # 输出结果
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            for result in results:
                f.write(result + '\n')
        print(f"✅ 已保存到：{args.output}")
    else:
        for result in results:
            print(result)
    
    # 显示统计信息
    if not args.quiet:
        print(f"\n📊 {parser_obj.get_stats_summary()}")
        
        # 显示警告/错误
        errors = parser_obj.get_errors()
        if errors:
            print(f"\n⚠️ 警告信息：")
            for err in errors:
                print(f"  {err}")


if __name__ == '__main__':
    main()
