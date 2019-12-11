import numpy as np
import numpy.linalg as LA

def e(n,i):
    #n次元ベクトルであってi番目に1、それ以外に0を持つベクトルを生成
    ans = [0 for j in range(n)]
    ans[i] = 1
    return ans

same_num = 0
n = 1000

wa = []

for i in range(n):
    # 2次元ベクトルax,ay
    ax = np.random.rand(2)
    ay = np.random.rand(2)

    # Aの3列目にかける定数
    d = np.random.rand()
    
    # Aの要素をlistに書き下したもの
    A_list = [[ax[0], ay[0], -ax[0], -ay[0]],
              [ax[1], ay[1], -ax[1], -ay[1]],
              [d    , d    ,  d    ,  d    ]]

    # 横長行列A
    A = np.array(A_list)
    
    # Aの下に4列の行ベクトルを配置する4×4正方行列を4種類作成
    B = [np.array(A_list + [e(4,i)]) for i in range(4)]

    # Bの各要素について、逆行列を計算
    Binv = [LA.inv(np.array(b)) for b in B]

    # Binvの平均でAの疑似逆行列を計算する
    # 4列目は本来存在しないのでカット（よりうまいカットの仕方あったら教えてください）
    Apinv_fromB = (0.25 * (Binv[0] + Binv[1] + Binv[2] + Binv[3])).transpose()[:3].transpose()
    
    Apinv = LA.pinv(A)

    # 相対誤差をnormで評価
    error = LA.norm(Apinv_fromB - Apinv) / LA.norm(Apinv)

    if error < 1e-10:
        print("num",i,"same")
        same_num += 1
    else:
        print("wa")
        wa.append([Apinv, Apinv_fromB])

print("[[fin]]")
print("tryail:",n)
print("same num:",same_num)
print("same ratio:",same_num/n)

if len(wa) > 0:
    print("wa:")
    for w in wa:
        print("Apinv:")
        print(w[0])
        print("Apinv_fromB:")
        print(w[1])
        print()
