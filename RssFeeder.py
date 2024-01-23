import feedparser
import json
import time
#NewsFeed = feedparser.parse("https://tttang.com/rss.xml")

#获取博客地址：跳跳糖 - 安全与分享社区
#print(NewsFeed['feed']['title'])

#print(NewsFeed)

#检查是否是今日的rss更新
def check_rss_update(url:str)-> dict:
    Newfeed=feedparser.parse(url)
    data={}
    #计算文章的更新时间
    for i in range(len(Newfeed.entries)):
        #print(i)
        #print(Newfeed.entries[i]['title'])
        #文章题目、发布时间和文章连接
        articl=Newfeed.entries[i]['title']
        update=Newfeed.entries[i].published_parsed
        updatetime=f'{update.tm_year}年{update.tm_mon}月{update.tm_mday}日'
       # print(updatetime)
        link=Newfeed.entries[i]['link']
        #print(link)
        data.update({articl:link})
    for datum in data:
        print(data[datum])
        print(type(datum))

    return data

if __name__ == '__main__':
    print(check_rss_update("https://tttang.com/rss.xml"))
