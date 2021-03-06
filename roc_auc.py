# encoding: utf-8
import numpy as np


def cal_rate(result, thres):
    all_number = len(result[0])
    # print all_number
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for item in range(all_number):
        disease = result[0][item]
        if disease >= thres:
            disease = 1
        if disease == 1:
            if result[1][item] == 1:
                TP += 1
            else:
                FP += 1
        else:
            if result[1][item] == 0:
                TN += 1
            else:
                FN += 1
    # print TP+FP+TN+FN
    accracy = float(TP+FP) / float(all_number)
    if TP+FP == 0:
        precision = 0
    else:
        precision = float(TP) / float(TP+FP)
    TPR = float(TP) / float(TP+FN)
    TNR = float(TN) / float(FP+TN)
    FNR = float(FN) / float(TP+FN)
    FPR = float(FP) / float(FP+TN)
    # print accracy, precision, TPR, TNR, FNR, FPR
    return accracy, precision, TPR, TNR, FNR, FPR

#prob是样本正确率的array，label则是样本label的array
threshold_vaule = sorted(prob)
threshold_num = len(threshold_vaule)
accracy_array = np.zeros(threshold_num)
precision_array = np.zeros(threshold_num)
TPR_array = np.zeros(threshold_num)
TNR_array = np.zeros(threshold_num)
FNR_array = np.zeros(threshold_num)
FPR_array = np.zeros(threshold_num)
# calculate all the rates
for thres in range(threshold_num):
    accracy, precision, TPR, TNR, FNR, FPR = cal_rate((prob,label), threshold_vaule[thres])
    accracy_array[thres] = accracy
    precision_array[thres] = precision
    TPR_array[thres] = TPR
    TNR_array[thres] = TNR
    FNR_array[thres] = FNR
    FPR_array[thres] = FPR

AUC = np.trapz(TPR_array, FPR_array)
threshold = np.argmin(abs(FNR_array - FPR_array))
EER = (FNR_array[threshold]+FPR_array[threshold])/2
plt.plot(FPR_array, TPR_array)
plt.title('roc')
plt.xlabel('FPR_array')
plt.ylabel('TPR_array')
plt.show()
