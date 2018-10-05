import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import numpy as np

diff=0
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


data=pd.read_table('C:\\Lianxi\\python\\data\\test\\0.068_0.030_0.200_0.320_1.280_5.236.dat', index_col=None,header=None, delim_whitespace=True)
time = data.iloc[:, 0]
light_data = data.iloc[:, 1]
anomaly_start = data.iloc[0,3]
anomaly_end = data.iloc[0,4]
# 异常平均位置
t0 = (anomaly_start+anomaly_end) / 2
# 异常时长
t1 =anomaly_end-anomaly_start
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
print(ifsuccess)
print(sensitivity)
