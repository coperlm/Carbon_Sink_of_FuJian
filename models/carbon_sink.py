#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import json
import os
import random
from datetime import datetime

class CarbonSinkModel:
    """福建碳汇量数据模型类"""
    
    def __init__(self):
        """初始化模型，加载数据"""
        self.regions = [
            '福州市', '厦门市', '莆田市', '三明市', '泉州市', 
            '漳州市', '南平市', '龙岩市', '宁德市', '平潭综合试验区'
        ]
        self.forest_types = ['常绿阔叶林', '常绿针叶林', '落叶阔叶林', '针阔混交林', '竹林', '红树林', '灌木林']
        
        # 在实际应用中，这里应该从数据库或数据文件加载真实数据
        # 目前使用模拟数据进行演示
        self._generate_mock_data()
    
    def _generate_mock_data(self):
        """生成模拟数据"""
        # 1. 生成各地区碳汇基础数据
        self.base_data = {}
        for region in self.regions:
            # 每个地区的森林覆盖率 (40%-70%)
            forest_coverage = round(random.uniform(40, 70), 2)
            
            # 每个地区的森林面积 (单位: 万公顷, 范围: 20-150)
            forest_area = round(random.uniform(20, 150), 2)
            
            # 每个地区的碳汇总量 (单位: 万吨, 范围根据面积按比例计算)
            carbon_sink = round(forest_area * random.uniform(3.5, 5.0), 2)
            
            # 各森林类型占比
            forest_type_ratio = {}
            remaining = 100.0
            for i, forest_type in enumerate(self.forest_types):
                if i == len(self.forest_types) - 1:
                    ratio = remaining
                else:
                    ratio = round(random.uniform(5, remaining - 5 * (len(self.forest_types) - i - 1)), 1)
                    remaining -= ratio
                forest_type_ratio[forest_type] = ratio
            
            self.base_data[region] = {
                'forest_coverage': forest_coverage,
                'forest_area': forest_area,
                'carbon_sink': carbon_sink,
                'forest_type_ratio': forest_type_ratio
            }
        
        # 2. 生成历史趋势数据 (2015-2025年)
        self.trend_data = {}
        for region in self.regions + ['全省']:
            yearly_data = {}
            # 基准值，全省取平均
            if region == '全省':
                base_carbon = sum(data['carbon_sink'] for data in self.base_data.values()) / len(self.regions)
                base_area = sum(data['forest_area'] for data in self.base_data.values()) / len(self.regions)
            else:
                base_carbon = self.base_data[region]['carbon_sink'] * 0.8  # 2015年基准值为当前的80%
                base_area = self.base_data[region]['forest_area'] * 0.9    # 2015年基准值为当前的90%
            
            for year in range(2015, 2026):
                # 每年增长1-3%
                growth_rate = 1 + random.uniform(0.01, 0.03)
                base_carbon *= growth_rate
                
                # 面积每年增长0.5-1%
                area_growth_rate = 1 + random.uniform(0.005, 0.01)
                base_area *= area_growth_rate
                
                yearly_data[year] = {
                    'carbon_sink': round(base_carbon, 2),
                    'forest_area': round(base_area, 2)
                }
            
            self.trend_data[region] = yearly_data
    
    def get_all_regions_data(self):
        """获取所有地区的碳汇量数据"""
        result = {
            'regions': [],
            'forest_coverage': [],
            'forest_area': [],
            'carbon_sink': []
        }
        
        for region, data in self.base_data.items():
            result['regions'].append(region)
            result['forest_coverage'].append(data['forest_coverage'])
            result['forest_area'].append(data['forest_area'])
            result['carbon_sink'].append(data['carbon_sink'])
            
        return result
    
    def get_region_data(self, region):
        """获取特定地区的详细数据"""
        if region in self.base_data:
            return self.base_data[region]
        else:
            return None
    
    def get_trend_data(self, region='全省', start_year='2015', end_year='2025'):
        """获取特定地区和时间范围内的趋势数据"""
        if region not in self.trend_data:
            return None
            
        try:
            start = int(start_year)
            end = int(end_year)
        except ValueError:
            start = 2015
            end = 2025
            
        result = {
            'years': [],
            'carbon_sink': [],
            'forest_area': []
        }
        
        for year in range(start, end + 1):
            if year in self.trend_data[region]:
                result['years'].append(year)
                result['carbon_sink'].append(self.trend_data[region][year]['carbon_sink'])
                result['forest_area'].append(self.trend_data[region][year]['forest_area'])
                
        return result
    
    def get_region_comparison(self):
        """获取各地区碳汇量对比数据"""
        return {
            'regions': list(self.base_data.keys()),
            'values': [data['carbon_sink'] for data in self.base_data.values()]
        }