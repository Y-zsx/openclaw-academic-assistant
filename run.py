#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学术助手 - 一键运行脚本 v1.2
简化使用流程，提供交互式界面
"""

import os
import sys
import subprocess
import argparse


def print_banner():
    print("=" * 60)
    print("       🎓 学术助手 v1.2 - Academic Assistant")
    print("=" * 60)
    print()


def run_script(cmd):
    """运行脚本并返回结果"""
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return result


def format_reference(text):
    """单篇文献格式化"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cmd = [sys.executable, os.path.join(script_dir, 'scripts/format_reference.py'), '-i', text]
    return run_script(cmd)


def parse_bibtex(filepath, output=None):
    """BibTeX 批量解析"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cmd = [sys.executable, os.path.join(script_dir, 'scripts/bibtex_parser.py'), '-i', filepath]
    if output:
        cmd.extend(['-o', output])
    return run_script(cmd)


def plan_thesis(date, thesis_type='undergraduate'):
    """毕设时间规划"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cmd = [sys.executable, os.path.join(script_dir, 'scripts/thesis_timeline.py'), '-d', date, '-t', thesis_type]
    return run_script(cmd)


def main():
    parser = argparse.ArgumentParser(description='学术助手 - 一键运行脚本')
    parser.add_argument('--mode', '-m', type=str, 
                       choices=['ref', 'bib', 'plan', 'auto'],
                       help='运行模式')
    parser.add_argument('--input', '-i', type=str, help='输入文件/文本')
    parser.add_argument('--output', '-o', type=str, help='输出文件路径')
    parser.add_argument('--type', '-t', type=str, default='undergraduate', help='论文类型（plan 模式用）')
    
    args = parser.parse_args()
    
    print_banner()
    
    # 命令行模式
    if args.mode and args.mode != 'auto':
        if args.mode == 'ref':
            if not args.input:
                print("❌ 请提供文献信息：-i '作者：张三，标题：...'")
                return
            result = format_reference(args.input)
            print(result.stdout)
            if result.stderr:
                print(f"⚠️  {result.stderr}")
        
        elif args.mode == 'bib':
            if not args.input:
                print("❌ 请提供 .bib 文件路径：-i references.bib")
                return
            result = parse_bibtex(args.input, args.output)
            print(result.stdout)
            if result.stderr:
                print(f"⚠️  {result.stderr}")
        
        elif args.mode == 'plan':
            if not args.input:
                print("❌ 请提供答辩日期：-i 2026-06-15")
                return
            result = plan_thesis(args.input, args.type)
            print(result.stdout)
            if result.stderr:
                print(f"⚠️  {result.stderr}")
        
        return
    
    # 交互模式
    print("请选择功能：")
    print("  1. 单篇文献格式化")
    print("  2. BibTeX 批量解析")
    print("  3. 毕设时间规划")
    print("  0. 退出")
    print()
    
    while True:
        choice = input("请输入选项（0-3）：").strip()
        
        if choice == '1':
            text = input("请输入文献信息：").strip()
            if text:
                result = format_reference(text)
                print("\n" + result.stdout)
        
        elif choice == '2':
            filepath = input("请输入 .bib 文件路径：").strip()
            if filepath and os.path.exists(filepath):
                output = input("输出文件路径（可选）：").strip() or None
                result = parse_bibtex(filepath, output)
                print("\n" + result.stdout)
            else:
                print("❌ 文件不存在")
        
        elif choice == '3':
            date = input("请输入答辩日期（2026-06-15）：").strip()
            if date:
                thesis_type = input("论文类型（1=本科，2=硕士）：").strip()
                type_arg = 'master' if thesis_type == '2' else 'undergraduate'
                result = plan_thesis(date, type_arg)
                print("\n" + result.stdout)
        
        elif choice == '0':
            print("\n👋 再见！")
            break
        else:
            print("❌ 无效选项")
        
        print()


if __name__ == '__main__':
    main()
