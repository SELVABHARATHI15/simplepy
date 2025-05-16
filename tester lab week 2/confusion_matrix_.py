import numpy as np
def cal_mat(c_matrix):
    tp = c_matrix[0,0]
    tn = c_matrix[1,1]
    fp = c_matrix[0,1]
    fn = c_matrix[1,0]
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    recall = tp/(tp+fn)
    precision = tp/(tp+fp)
    F1 = 2*precision*recall/(precision+recall)
    return accuracy,recall,precision,F1

c_m =np.array([[80,20],[10,90]])
ac,re,pr,f1 = cal_mat(c_m)
print(f"accuracy  : {ac:.2f},\nrecall    : {re:.2f},\nprecision : {pr:.2f},\nF1 Score  : {f1:.2f}.")
