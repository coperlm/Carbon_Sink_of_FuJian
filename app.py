#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import json
import os
from models.carbon_sink import CarbonSinkModel

app = Flask(__name__, 
            static_folder="static",
            template_folder="templates")

# 读取模拟数据
@app.route('/api/carbon_data')
def get_carbon_data():
    """获取福建省各地区碳汇量数据"""
    try:
        # 在实际应用中，这里会从数据库或文件中读取真实数据
        # 目前使用模拟数据
        carbon_model = CarbonSinkModel()
        data = carbon_model.get_all_regions_data()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/carbon_trend')
def get_carbon_trend():
    """获取碳汇量历史趋势数据"""
    try:
        region = request.args.get('region', '全省')
        start_year = request.args.get('start_year', '2015')
        end_year = request.args.get('end_year', '2025')
        
        carbon_model = CarbonSinkModel()
        trend_data = carbon_model.get_trend_data(region, start_year, end_year)
        
        return jsonify({"status": "success", "data": trend_data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/region_comparison')
def get_region_comparison():
    """获取地区碳汇量对比数据"""
    try:
        carbon_model = CarbonSinkModel()
        comparison_data = carbon_model.get_region_comparison()
        
        return jsonify({"status": "success", "data": comparison_data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/historical_data')
def get_historical_data():
    """返回历史碳汇数据趋势"""
    try:
        # 示例历史数据
        years = list(range(2015, 2025))
        data = {
            "years": years,
            "total_carbon_sink": [1900, 1950, 2000, 2050, 2100, 2150, 2200, 2220, 2240, 2250],  # 单位：万吨CO2当量
            "forest_carbon": [1500, 1520, 1550, 1580, 1600, 1630, 1650, 1670, 1680, 1700],
            "soil_carbon": [300, 310, 320, 330, 340, 350, 360, 370, 375, 380],
            "wetland_carbon": [100, 120, 130, 140, 160, 170, 190, 180, 185, 170]
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/environmental_factors')
def get_environmental_factors():
    """返回环境因素与碳汇关系的数据"""
    try:
        # 示例环境因素数据
        data = {
            "temperature": [15.2, 15.5, 15.7, 16.0, 16.2, 16.5, 16.7, 16.9, 17.1, 17.3],  # 年平均温度°C
            "precipitation": [1650, 1680, 1700, 1720, 1750, 1680, 1720, 1750, 1720, 1780],  # 年降水量mm
            "carbon_sink": [1900, 1950, 2000, 2050, 2100, 2150, 2200, 2220, 2240, 2250],  # 碳汇量（万吨CO2当量）
            "years": list(range(2015, 2025))
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    """渲染主页"""
    return render_template('index.html')

@app.route('/map')
def map_view():
    """渲染地图页面"""
    return render_template('map.html')

@app.route('/trends')
def trends_view():
    """渲染趋势分析页面"""
    return render_template('trends.html')

@app.route('/comparison')
def comparison_view():
    """渲染地区对比页面"""
    return render_template('comparison.html')

@app.route('/factors')
def factors_view():
    """渲染环境因素分析页面"""
    return render_template('factors.html')

if __name__ == '__main__':
    app.run(debug=True)