#!/usr/bin/env python
# -*- coding:utf-8 -*-


from jd_assistant import Assistant

if __name__ == '__main__':
    asst = Assistant()      # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    asst.clear_cart()       # 清空购物车（可选）
    asst.add_item_to_cart(sku_ids='100001324422')  # 根据商品id添加购物车（可选）
    asst.submit_order_by_time(buy_time='2020-02-16 01:17:59.500', retry=4, interval=5)  # 定时提交订单
    # 3个参数：
    # buy_time: 下单时间，例如：'2019-02-16 01:17:59.500'
    # retry: 下单重复执行次数，可选参数，默认4次
    # interval: 下单执行间隔，可选参数，默认5秒
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒

 """   有货提交订单示例
from jd_assistant import Assistant

if __name__ == '__main__':
    sku_ids = '100001324422:1'  # 商品id
    area = '1_72_4211'          # 区域id
    asst = Assistant()          # 初始化
    asst.login_by_QRcode()      # 扫码登陆
    asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒"""
