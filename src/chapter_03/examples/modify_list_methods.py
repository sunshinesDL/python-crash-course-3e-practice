# Created Time: 2026/07/09
# Author: sunshinesDL (sunshinesDL@163.com)

"""Review how to modify the list."""


dishes = ['hotpot', 'da_pan_ji', 'roast_meat']
print(dishes)

# 指定位置插入元素
dishes.insert(0, 'dao_xiao_mian')
print(dishes)

# 删除指定位置的元素
del dishes[0]
print(dishes)

# 弹出列表末尾的元素
dinner_next_celebration = dishes.pop()
print(f"下次庆祝时吃：{dinner_next_celebration}")
print(dishes)

# 弹出其他位置的元素
dinner_winter_celebration = dishes.pop(0)
print(f"今年冬天庆祝时吃：{dinner_winter_celebration}")
print(dishes)

# 根据值删除元素
oily_dishes = "da_pan_ji"
dishes.remove(oily_dishes)
print(f'删除太油的菜后：{dishes}')