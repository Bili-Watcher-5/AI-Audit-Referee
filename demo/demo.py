"""
演示：偏离度计算公式
仅数学演示，无真实行业数据，不可直接商用
"""

def calc_deviation(reported_saving, audit_saving, base_price):
    deviation = (reported_saving - audit_saving) / base_price
    return round(deviation,4)

if __name__ == "__main__":
    # 示例模拟数字
    reported = 500000
    audit_result = 320000
    base = 10000000
    dev = calc_deviation(reported, audit_result, base)
    print(f"厂商上报节约：{reported}")
    print(f"第三方审计核算节约：{audit_result}")
    print(f"偏离度：{dev:.2%}")
