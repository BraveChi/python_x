最简单的爬虫小例子，用到了urllib.request、正则表达式、sorted排序，只有一个类。

map 和 lambda 的写法
sorted 的排序种子
正则表达式()分组


1、目标地址：
斗鱼王者荣耀类目
https://www.douyu.com/g_wzry

2、页面目标html内容：
<div class="mes">
    .....
    <p>
        <span class="dy-name ellipsis fl">冷未央丶</span>
        <span class="dy-num fr">26.4万</span>
    </p>
</div>
正则表达式：
(<div class="mes">[\s\S]*?<p>)([\s\S]*?)(</p>[\s\S*?]</div>)


3、输出结果示例：
rank 1 : 王者荣耀官方赛事   157万
rank 2 : 纯白   154万
rank 3 : 电视电子竞技G联赛   153万
rank 4 : 游弋   53万
rank 5 : 雷婷丶   39.3万
rank 6 : 渝万丶浮生   29.8万
rank 7 : 秀梦哒哒   28.4万
rank 8 : 皇玺丶瑞文   28万
rank 9 : 冷未央丶   26.4万
rank 10 : 雪下望月7   24.5万
rank 11 : AQ丶果粒   23.4万


遇到的错误信息：
1、HTTP Error 403: Forbidden
    添加header信息
2、urlopen() got an unexpected keyword argument 'headers'
   heades 信息组装在 request.Request 中，在通过urlopen 