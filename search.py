import sys
import getopt

from absl import flags
from musicdl import musicdl



default_srcs = ['baiduFlac', 'kugou', 'kuwo', 'qq', 'qianqian', 'netease', 'migu', 'xiami', 'joox', 'yiting']
config = {'logfilepath': 'musicdl.log', 'savedir': 'downloaded', 'search_size_per_source': 20, 'proxies': {}}

FLAGS = flags.FLAGS
flags.DEFINE_string("src",
        "baiduFlac,kugou,kuwo,qq,qianqian,netease,migu,xiami,joox,yiting", "输入目标站点")
flags.DEFINE_string("query", "赵雷", "输入查询关键词")

def print_lines(lines):
    for line in lines:
        print (line)

def search_and_download(query, srcs):
    client = musicdl.musicdl(config=config)
    search_results = client.search(query, srcs)
    index = 1 
    items = []
    lines = []
    for key, value in search_results.items():
        for item in value:
            line = "|index:%d\t|singers:%s\t|songname:%s|" % (index, item["singers"], item["songname"])
            lines.append(line)
            index = index+1
            items.append(item)
    while 1:
        print_lines(lines)
        num_str = input("input download num(input 0 to exit):")
        num = 0
        try:
            num = int(num_str)
        except:
            print ("convert num to int failed")
            continue
        if num == 0 or num > 20:
            sys.exit()
        print (items[num-1])
        client.download([items[num-1]])

def main(argv):
    srcs = []
    query = ""

    FLAGS(sys.argv)
    source = FLAGS.src
    query = FLAGS.query
    srcs = source.rstrip().split(",")
    if len(srcs) == 0:
        srcs = default_srcs

    search_and_download(query, srcs)

if __name__=="__main__":
    main(sys.argv)
