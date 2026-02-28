#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
毕设时间规划工具
根据答辩日期倒推各阶段时间节点
"""

import argparse
from datetime import datetime, timedelta
from typing import Dict, List


class ThesisPlanner:
    """毕设计划生成器"""
    
    # 各阶段时间占比（本科毕设）
    STAGES_UNDERGRAD = {
        '开题 + 文献综述': 0.15,
        '实验/开发': 0.35,
        '论文写作': 0.30,
        '答辩准备': 0.20,
    }
    
    # 各阶段时间占比（硕士毕设）
    STAGES_MASTER = {
        '开题报告': 0.10,
        '文献调研': 0.15,
        '实验研究': 0.40,
        '论文写作': 0.25,
        '答辩准备': 0.10,
    }
    
    # 各阶段详细任务
    TASKS = {
        '开题 + 文献综述': [
            '确定选题方向',
            '完成文献检索和阅读（至少 20 篇）',
            '撰写开题报告',
            '开题答辩',
        ],
        '实验/开发': [
            '需求分析 + 系统设计',
            '环境搭建',
            '编码实现',
            '单元测试 + 集成测试',
            '完成核心功能',
        ],
        '论文写作': [
            '撰写初稿（建议 1.5 万字以上）',
            '导师修改意见',
            '二稿修改',
            '格式审查',
            '查重检测',
        ],
        '答辩准备': [
            '论文定稿',
            '制作答辩 PPT',
            '预答辩演练',
            '正式答辩',
        ],
    }
    
    def __init__(self, defense_date: datetime, thesis_type: str = 'undergraduate'):
        self.defense_date = defense_date
        self.thesis_type = thesis_type
        
        if thesis_type == 'master':
            self.stages = self.STAGES_MASTER
        else:
            self.stages = self.STAGES_UNDERGRAD
    
    def calculate_stages(self) -> List[Dict]:
        """计算各阶段时间节点"""
        total_days = (self.defense_date - datetime.now()).days
        
        if total_days <= 0:
            raise ValueError("答辩日期必须是将来的日期")
        
        stages = []
        current_date = datetime.now()
        
        for stage_name, ratio in self.stages.items():
            stage_days = int(total_days * ratio)
            end_date = current_date + timedelta(days=stage_days)
            
            stages.append({
                'name': stage_name,
                'start': current_date,
                'end': end_date,
                'days': stage_days,
                'ratio': ratio,
                'tasks': self.TASKS.get(stage_name, []),
            })
            
            current_date = end_date
        
        return stages
    
    def generate_plan(self) -> str:
        """生成完整的毕设计划"""
        stages = self.calculate_stages()
        total_days = (self.defense_date - datetime.now()).days
        
        # 标题
        type_name = "硕士" if self.thesis_type == 'master' else "本科"
        output = []
        output.append(f"📅 {type_name}毕设计划（距离答辩还有 {total_days} 天）")
        output.append("")
        
        # 各阶段详情
        for i, stage in enumerate(stages, 1):
            start_str = stage['start'].strftime('%m-%d')
            end_str = stage['end'].strftime('%m-%d')
            
            output.append(f"【第{i}阶段】{stage['name']}（{start_str} - {end_str}）")
            for task in stage['tasks']:
                output.append(f"  - {task}")
            output.append("")
        
        # 关键节点提醒
        output.append("⚠️ 关键节点提醒：")
        if len(stages) >= 2:
            output.append(f"  - {stages[1]['end'].strftime('%m-%d')}：完成所有开发/实验工作")
        if len(stages) >= 3:
            output.append(f"  - {stages[2]['end'].strftime('%m-%d')}：提交论文终稿")
            output.append(f"  - 答辩前 7 天：查重截止")
        output.append(f"  - {self.defense_date.strftime('%m-%d')}：正式答辩")
        
        # 建议
        output.append("")
        output.append("💡 建议：")
        output.append("  - 每周向导师汇报进度")
        output.append("  - 提前 2 周开始准备答辩 PPT")
        output.append("  - 保留充足时间应对意外情况")
        
        return '\n'.join(output)


def parse_date(date_str: str) -> datetime:
    """解析日期字符串"""
    formats = [
        '%Y-%m-%d',
        '%Y/%m/%d',
        '%Y.%m.%d',
        '%m-%d',
        '%m/%d',
    ]
    
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            # 如果是月 - 日格式，补全年份
            if dt.year == 1900:
                dt = dt.replace(year=datetime.now().year)
            return dt
        except ValueError:
            continue
    
    raise ValueError(f"无法解析日期：{date_str}，请使用 YYYY-MM-DD 格式")


def main():
    parser = argparse.ArgumentParser(description='毕设时间规划工具')
    parser.add_argument('--defense-date', '-d', type=str, required=True, 
                       help='答辩日期 (YYYY-MM-DD)')
    parser.add_argument('--type', '-t', type=str, default='undergraduate',
                       choices=['undergraduate', 'master'],
                       help='论文类型 (undergraduate=本科，master=硕士)')
    
    args = parser.parse_args()
    
    try:
        defense_date = parse_date(args.defense_date)
        planner = ThesisPlanner(defense_date, args.type)
        print(planner.generate_plan())
    except Exception as e:
        print(f"错误：{e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
