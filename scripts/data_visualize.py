#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实验数据可视化脚本
支持 CSV/Excel 文件生成常见图表
"""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='实验数据可视化工具')
    parser.add_argument('--input', '-i', type=str, required=True, help='输入数据文件 (CSV/Excel)')
    parser.add_argument('--type', '-t', type=str, default='line',
                       choices=['line', 'bar', 'scatter', 'heatmap', 'box'],
                       help='图表类型')
    parser.add_argument('--output', '-o', type=str, default='output.png', help='输出文件路径')
    parser.add_argument('--x', type=str, help='X 轴列名')
    parser.add_argument('--y', type=str, help='Y 轴列名')
    
    args = parser.parse_args()
    
    # 检查依赖
    try:
        import pandas as pd
        import matplotlib.pyplot as plt
    except ImportError as e:
        print(f"错误：缺少依赖库，请运行：pip install pandas matplotlib openpyxl")
        print(f"详情：{e}")
        sys.exit(1)
    
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    
    try:
        # 读取数据
        if args.input.endswith('.xlsx') or args.input.endswith('.xls'):
            df = pd.read_excel(args.input)
        else:
            df = pd.read_csv(args.input)
        
        print(f"✓ 成功读取数据：{len(df)} 行，{len(df.columns)} 列")
        print(f"  列名：{list(df.columns)}")
        
        # 创建图表
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if args.type == 'line':
            if args.x and args.y:
                ax.plot(df[args.x], df[args.y], marker='o')
                ax.set_xlabel(args.x)
                ax.set_ylabel(args.y)
            else:
                df.plot(ax=ax, marker='o')
            ax.set_title('趋势图')
            
        elif args.type == 'bar':
            if args.x and args.y:
                ax.bar(df[args.x], df[args.y])
                ax.set_xlabel(args.x)
                ax.set_ylabel(args.y)
            else:
                df.plot(kind='bar', ax=ax)
            ax.set_title('柱状图')
            plt.xticks(rotation=45)
            
        elif args.type == 'scatter':
            if args.x and args.y:
                ax.scatter(df[args.x], df[args.y])
                ax.set_xlabel(args.x)
                ax.set_ylabel(args.y)
            else:
                print("错误：散点图需要指定 --x 和 --y 参数")
                sys.exit(1)
            ax.set_title('散点图')
            
        elif args.type == 'heatmap':
            import seaborn as sns
            corr = df.corr()
            sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
            ax.set_title('相关性热力图')
            
        elif args.type == 'box':
            df.plot(kind='box', ax=ax)
            ax.set_title('箱线图')
            plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.savefig(args.output, dpi=150, bbox_inches='tight')
        print(f"✓ 图表已保存至：{args.output}")
        
    except FileNotFoundError:
        print(f"错误：文件不存在：{args.input}")
        sys.exit(1)
    except Exception as e:
        print(f"错误：{e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
