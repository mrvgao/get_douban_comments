## Comment Spider 豆瓣电影评论爬虫程序

Author: Minchiuan(minchiuan.gao@gmail.com)

### Steps:

1. 因为豆瓣电影每个都有一个豆瓣自定义的movie-id, 所以首先用 BFS 搜索方式获得全网电影的movie-id；
2. 根据movie-id， 模拟手动浏览器行为获得comment页面；
3. 利用beautiful-soup进行解析。

### Requirements：

+ python >= 3.4
+ requests
+ beatifulsoup4


### How to Run:

1. 获取movie-id：

    ```bash
    $ python get_movie_id_bfs.py
    ```

2. 获得movie的评论;

    ```bash
    $ python douban+movie_comment_spider.py
    ```

### License:

MIT License
