import torch
import random
def synthetic_data(w, b, num_examples):  #@save
    """
    生成y=Xw+b+噪声：
    数据集有1000条数据，每一条数据有2个特征，标签y是一个实数，
    因此X为1000行2列，y为1000行1列，噪声是1000行1列，
    y=Xw+b+噪声
    w是权重，2行1列，b是偏差，1行1列

    """
    X = torch.normal(0, 1, (num_examples, len(w))) 
    #生成一个num_examples行，len(w)列的矩阵，也就是1000*2
    y = torch.matmul(X, w) + b
    #矩阵乘法，b是一个标量，y是一个1000行1列的矩阵，相加的时候是广播机制

    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))#-1的意思是根据其他维度自动计算这一维的大小，y.reshape((-1, 1))是将y变成1000行1列的矩阵

true_w = torch.tensor([2.19, 3.33])
true_b = 4.077
features, labels = synthetic_data(true_w, true_b, 1000)
print(features[:10,0:2],'\n',labels[:10,0:1])

def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    # 这些样本是随机读取的，没有特定的顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]


batch_size = 10

for X, y in data_iter(batch_size, features, labels):
    print(X, '\n', y)
    break

w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
##初始化，权重w从正态分布中取，b为0
def linreg(X, w, b):  ##定义模型，实际上就是根据线性回归的公式y=Xw+b来计算预测值
    """线性回归模型"""
    return torch.matmul(X, w) + b
def squared_loss(y_hat, y):  ##y_hat为预测值，y为真实值
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2
##公式为0.5*(y_hat - y)**2，y.reshape(y_hat.shape)是将y变成和y_hat一样的形状

#优化算法与训练
def sgd(params, lr, batch_size):  #@save
    """小批量随机梯度下降"""
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()


lr = 0.03
num_epochs = 10
net = linreg
loss = squared_loss

for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)  # X和y的小批量损失
        # 因为l形状是(batch_size,1)，而不是一个标量。l中的所有元素被加到一起，
        # 并以此计算关于[w,b]的梯度
        l.sum().backward()
        ##！！！！注意，这里不能直接使用l.backward()，因为l是一个向量，backward()默认只对标量求导，所以需要先对l求和得到一个标量，再进行反向传播
        sgd([w, b], lr, batch_size)  # 使用参数的梯度更新参数
    with torch.no_grad():##一轮结束后，计算所有1000条数据的损失，来观察模型的训练情况
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')


print(f'w的估计误差: {true_w - w.reshape(true_w.shape)}')
print(f'b的估计误差: {true_b - b}')