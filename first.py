import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import numpy as np
import os

#默认差分为0
diff=0

#寻找ARIMA模型的最优p,q值
def ARI(window_lin):
    #定阶
    #一般阶数不超过length/10
    qmax=int(len(window_lin)/10)
    pmax=int(len(window_lin)/10)
    #bic矩阵
    bic_matrix=[]
    for p in range(pmax+1):
        tmp=[]
        for q in range(qmax+1):
            try:
                tmp.append(ARIMA(window_lin,(p,0,q)).fit().bic)
            except:
                tmp.append(None)
        bic_matrix.append(tmp)
    #从中可以找到最小值
    bic_matrix=pd.DataFrame(bic_matrix)
    #先用stack展平，然后用idxmin找出最小值
    p,q=bic_matrix.stack().idxmin()
    return p,q

# def DARIMA(dataPath,widows=50):
#     data = pd.read_table(dataPath, index_col=False, header=None, delim_whitespace=True)
#     length=len(data)
#     fd = []
#     # 开始时间
#     i = 50
#     while i <= 95:
#         # 从当前时间往前推50个点作为历史窗口进行预测
#         window_lin = data.iloc[i - 50:i, 1]
#         current_lin = data.iloc[i:i + 5, 1]
#         current_list = []
#         for o in current_lin:
#             current_list.append(o)
#         # window_lin=历史窗口的light intensity
#         p, q = ARI(window_lin)
#         model = ARIMA(window_lin, (p, 0, q)).fit()
#         f5 = model.forecast(5)[0]
#         fd5 = [abs(current_list[x] - f5[x]) for x in range(len(f5))]
#         fd = fd + fd5

#对一个文档进行数据处理
def DARIMA1(datapath):
    data = pd.read_table(datapath, index_col=False, header=None, delim_whitespace=True)
    time = data.iloc[:, 0]
    light_data = data.iloc[:, 1]
    anomaly_start = data.iloc[0, 3]
    anomaly_end = data.iloc[0, 4]
    # 异常平均位置
    t0 = (anomaly_start + anomaly_end) / 2
    # 异常时长
    t1 = anomaly_end - anomaly_start
    # ifsuccess判断本次报警是否成功,1成功，0失败
    ifsuccess = 0
    # sensitivity代表本次报警的灵敏度
    sensitivity = 0
    length = len(light_data)
    middle = length // 2
    # end即代表当前位置
    end = middle - 54
    # 历史窗口预测误差
    history_f = [[] for i in range(length)]
    windows_error = []
    while end <= (length - 1):
        windows_data = light_data[end - 50:end]
        p, q = ARI(windows_data)
        model = ARIMA(windows_data, (p, diff, q)).fit()
        f5 = model.forecast(5)[0]
        for i in range(5):
            history_f[end + i].append(f5[i])
        if len(history_f[end]) == 5:
            x = np.mean(history_f[end])
            er = x - light_data[end]
            if len(windows_error) < 50:
                windows_error.append(er)
            else:
                if er > np.max(windows_error):
                    if time[end] >= anomaly_start and time[end] <= anomaly_end:
                        ifsuccess = 1
                        sensitivity = (time[end] - t0) / t1
                    break
                else:
                    windows_error.pop(0)
                    windows_error.append(er)
        end = end + 1
    return ifsuccess,sensitivity

x,y=DARIMA1('C:\\Lianxi\\python\\data\\test\\TE.dat')