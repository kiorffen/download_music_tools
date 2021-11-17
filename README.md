比较好用的音乐下载工具，根据musicdl做了一些包装，使用之前先安装依赖。

安装依赖

```
pip install musicdl --upgrade
pip install absl-py
```

使用方法

```
python search.py --src="qq" --query="刘德华"
--src="目标站点"，支持站点参考[https://github.com/CharlesPikachu/musicdl](https://github.com/CharlesPikachu/musicdl)
--query="搜索关键词"，人名或者歌名都可以，最多展示20个结果
```
