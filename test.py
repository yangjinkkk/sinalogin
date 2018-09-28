import re
ra = r'<a.+?href=\"(.+?)\".+?nm.*>'
user_name = re.findall(ra, '<a bpfilter=\"main\" href=\"\/\/weibo.com\/u\/2786328714\/home?topnav=1&wvr=6\" nm=\"home\" class=\"S_txt1 home\" suda-uatrack=\"key=topnav_tab&value=homepage\"><em class=\"W_ficon ficon_home S_ficon\">E<\/em><em class=\"S_txt1\">首页<\/em><\/a>', re.S)[0]
print(user_name)