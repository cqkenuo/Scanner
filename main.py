#!/usr/bin/python
# -*- coding:utf8 -*-
#author:Jinhao

from dict import *
import argparse,sys,os
import re
import func_spider,func_scan

class Scanner():
    def __init__(self):
        self.info = self.terminal_input()
        self.parser_dump()         # 自动解析参数
        self.url_check(self.opt['url'])           # 检查url合法性
        self.run()


    def terminal_input(self):
        '''
        接收命令行参数
        :return: 解析后的参数键值对
        '''
        ter_opt={}
        if len(sys.argv) == 1:
            sys.argv.append('-h')
        parser = argparse.ArgumentParser()
        parser.add_argument('-u','--url',help='扫描对象的url')
        parser.add_argument('--cookies',default=None,help='目标网站的cookies')
        parser.add_argument('--spider',help='爬取网站上的网页链接',action='store_true')
        parser.add_argument('--scan',help='扫描网站后台',action='store_true')
        parser.add_argument('--sqlscan',help='网站SQL注入检测',action='store_true')
        args = parser.parse_args()
        for x, y in args._get_kwargs():
            ter_opt[x] = y    # 保存为键值对
        return ter_opt


    def parser_dump(self):
        '''
        自动把参数添加进dict
        :return:
        '''
        self.opt={}
        for x in self.info:
            # print(x)
            self.opt[x] = self.info[x]
            # print(self.opt[x])


    def url_check(self,url):
        '''
        很随意的URL合理性检测
        :param url: 待检测的URL
        :return: bool值
        '''
        if re.match('(http|https)://(.*?)\.(.*)',url):     # 匹配以http|https开头的网站
            return
        elif re.match('(.*?)\.(.*)',url):                  # 匹配xxx.xxx...规则的网站
            self.opt['url'] = "http://"+url                # 添加协议头
            return
        else:
            print("URL格式出错!")
            sys.exit(1)


    def base_report(self):
        print('>>>>>base_report'+'-'*40)
        for i in self.opt:
            if self.opt[i]:
                print("{0} : {1}".format(i,self.opt[i]))
        print('-'*40+'<<<<<base_report'+'\n')


    def run(self):
        '''
        调用模块
        :return:
        '''
        self.base_report()
        if self.opt['spider']:
            func_spider.Spider(self.opt['url'],self.opt['cookies'])
        if self.opt['scan']:
            func_scan.Scan(self.opt['url'],self.opt['cookies'])
        else:
            # print("Nothing to do...")
            pass






def main():
    x = Scanner()

if __name__ == "__main__":
    main()
