import random
def split_32bit_to_16bit(num):
    if not (-2**31 <= num < 2**31):
        raise ValueError("Input must be a 32-bit signed integer.")

    # 取出高 16 位和低 16 位
    high_16 = (num >> 16) & 0xFFFF  # 取高 16 位
    low_16 = num & 0xFFFF           # 取低 16 位

    # 轉換為有號整數
    if high_16 >= 0x8000:
        high_16 -= 0x10000
    if low_16 >= 0x8000:
        low_16 -= 0x10000

    return high_16, low_16

def combine_16bit_to_32bit(high_16, low_16):
    if not (-2**15 <= high_16 < 2**15) or not (-2**15 <= low_16 < 2**15):
        raise ValueError("Both inputs must be 16-bit signed integers.")

    # 將有號 16 位轉換為無號表示
    high_16 = high_16 & 0xFFFF
    low_16 = low_16 & 0xFFFF

    # 拼接為 32 位整數
    num = (high_16 << 16) | low_16

    # 處理有號的 32 位整數
    if num >= 0x80000000:
        num -= 0x100000000

    return num

# 測試範例
a = random.randint(-2147483648,2147483647)
b = random.randint(-2147483648,2147483647)
print(f"Original 32-bit integer a: {a}")

a_high, a_low = split_32bit_to_16bit(a)
'''
print(f"High 16 bits: {a_high}, Low 16 bits: {a_low}")

reconstructed_num = combine_16bit_to_32bit(a_high, a_low)
print(f"Reconstructed 32-bit integer: {reconstructed_num}")
'''
print(f"Original 32-bit integer b: {b}")
b_high, b_low = split_32bit_to_16bit(b)
'''
print(f"High 16 bits: {b_high}, Low 16 bits: {b_low}")

reconstructed_num = combine_16bit_to_32bit(b_high, b_low)
print(f"Reconstructed 32-bit integer: {reconstructed_num}")
'''
print(f"Main.add({a_high},{a_low},{b_high},{b_low});")

print(a+b)
high, low = split_32bit_to_16bit(a+b)
print(f"High 16 bits: {high}, Low 16 bits: {low}")
