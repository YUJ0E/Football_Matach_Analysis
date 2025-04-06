import pickle

# 打开一个文件用于读取
with open('track_stubs.pkl', 'rb') as f:
    # 使用pickle.load()从文件中读取序列化的对象并还原为原来的Python对象
    loaded_data = pickle.load(f)

# 打印加载的数据
print(loaded_data)
