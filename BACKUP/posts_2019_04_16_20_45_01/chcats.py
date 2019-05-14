import glob
import os, sys
import glob
import shutil

CWD = os.getcwd()

trans = {
    "生信工具和算法": "bioinfo",
	"机器学习与算法基础": "ml",
	"统计学基础": "stat",
	"R统计语言": "R",
	"python编程": "python",
	"OS学习手册": "os",
	"快捷清单": "cargo",
	"深度学习": "dl",
	"IT开发笔记": "it",
	"小黄鸭调试法": "bug"
}

IGNORES = ['_ignore', '_bak', '_backup', '_backups', 'backup-link']

def get_meta(article):
    meta = {}
    stop = True
    for idx, line in enumerate(article.split('\n')):
        if idx == 0:
            assert '---' in line
        if '---' in line:
            if stop == False:
                break
            stop = not stop
            continue
        if ' - ' in line:
            continue
        arr = line.split(':', 1)
        k = arr[0].strip()
        v = arr[1].strip() if arr[1] else arr[1]
        meta[k] = v
    return meta

def chcats(direc, overwrite=False):
    for fp in glob.glob(direc + os.sep + "*"):
        
        is_ignored = False
        for kw in IGNORES:
            if kw in fp:
                is_ignored = True
                break
        if is_ignored:
            continue
        
        if os.path.isfile(fp):
            if fp.endswith('.md'):
                #print('正在处理 %s'%fp)
                with open(fp, 'r', encoding='utf-8') as reader:
                    article = reader.read()
                    new_article = article
                    meta = get_meta(article)
                    current_cat = meta['categories']
                    new_cat = trans.get(current_cat, False)
                    if new_cat:
                        _old = 'categories: %s'%current_cat
                        _new = 'categories: %s'%new_cat
                        new_article = article.replace(_old, _new)
                        #if 'latex' in fp: print(new_article.encode('utf-8'))
                
                if overwrite:
                    new_fp = fp
                else:
                    basename = os.path.basename(fp)
                    catename = os.path.basename(os.path.dirname(fp))
                    new_dir = "{1}{0}new{0}{2}".format(os.sep, CWD, catename)
                    if not os.path.exists(new_dir):
                        os.makedirs(new_dir)
                    new_fp = "{1}{0}{2}".format(os.sep, new_dir, basename)
                
                if ( not overwrite ) or ( overwrite and new_cat ):
                    with open(new_fp, 'w', encoding='utf-8') as writer:
                        print('修改 %s'%fp)
                        writer.write(new_article)
                else:
                    print('保持 %s'%fp)
                    pass
        else:
            chcats(fp, overwrite=True)
        
chcats(CWD, overwrite=True)
