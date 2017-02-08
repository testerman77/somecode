# coding=utf-8
import bs4
from bs4 import BeautifulSoup as bs

doc = """
<div style="position:relative;top:1px;font-weight:700;float:left;width:550px;font-size:20px;border-radius:8px;overflow:hidden;box-shadow:0 0 2px 0 rgba(0,0,0,.3);" class="panel panel-default" data-reactid=".0.0.0.1.0.1.0">
    <div class="panel-heading" data-reactid=".0.0.0.1.0.1.0.0">最新动态以及通知</div>
    <div class="page-home-notification list-group" fill="true" style="font-size:14px;" data-reactid=".0.0.0.1.0.1.0.1:$0">
        <a class="list-item-filled clearfix list-group-item" href="/static/document?plugin_name=MFileManager" data-reactid=".0.0.0.1.0.1.0.1:$0.$0/=1$0">
            <span style="width:100%;overflow:hidden;display:inline-block;white-space:nowrap;text-overflow:ellipsis;" data-reactid=".0.0.0.1.0.1.0.1:$0.$0/=1$0.0">1. 插件MFileManager更新到了1.2.8</span></a>
        <a class="list-item-filled clearfix list-group-item" href="/static/document?plugin_name=MDownloader" data-reactid=".0.0.0.1.0.1.0.1:$0.$1/=1$1">
            <span style="width:100%;overflow:hidden;display:inline-block;white-space:nowrap;text-overflow:ellipsis;" data-reactid=".0.0.0.1.0.1.0.1:$0.$1/=1$1.0">2. 插件MDownloader更新到了1.2.3</span></a>
        <a class="list-item-filled clearfix list-group-item" href="/static/document?plugin_name=MFeedback" data-reactid=".0.0.0.1.0.1.0.1:$0.$2/=1$2">
            <span style="width:100%;overflow:hidden;display:inline-block;white-space:nowrap;text-overflow:ellipsis;" data-reactid=".0.0.0.1.0.1.0.1:$0.$2/=1$2.0">3. 插件MFeedback更新到了1.0.2</span></a>
        <button type="button" class="list-item-filled clearfix list-group-item" data-reactid=".0.0.0.1.0.1.0.1:$0.$16/=1$16">
            <span style="width:100%;overflow:hidden;display:inline-block;white-space:nowrap;text-overflow:ellipsis;" data-reactid=".0.0.0.1.0.1.0.1:$0.$16/=1$16.0">17. 重要！ADP账户切换上线通知</span></button>
        <a class="list-item-filled clearfix list-group-item" href="/static/document?plugin_name=mgrowingio" data-reactid=".0.0.0.1.0.1.0.1:$0.$17/=1$17">
            <span style="width:100%;overflow:hidden;display:inline-block;white-space:nowrap;text-overflow:ellipsis;" data-reactid=".0.0.0.1.0.1.0.1:$0.$17/=1$17.0">18. 插件mgrowingio更新到了1.0.9</span></a>
        <button type="button" class="list-item-filled clearfix list-group-item" data-reactid=".0.0.0.1.0.1.0.1:$0.$18/=1$18">
            <span style="width:100%;overflow:hidden;display:inline-block;white-space:nowrap;text-overflow:ellipsis;" data-reactid=".0.0.0.1.0.1.0.1:$0.$18/=1$18.0">19. 重要：插件升级通知</span></button>
        <a class="list-item-filled clearfix list-group-item" href="/static/document?plugin_name=MBaiDuMap" data-reactid=".0.0.0.1.0.1.0.1:$0.$19/=1$19">
            <span style="width:100%;overflow:hidden;display:inline-block;white-space:nowrap;text-overflow:ellipsis;" data-reactid=".0.0.0.1.0.1.0.1:$0.$19/=1$19.0">20. 插件MBaiDuMap更新到了2.0.7</span></a>
    </div>
</div>
"""

dst= """
<div><div><a><span></span></a></div></div>
"""

def getHTMLConstructor(soup):
	for tag in soup:
		if isinstance(tag,bs4.Tag):
			yield '<{}>{}</{}>'.format(
				tag.name, "".join(getHTMLConstructor(tag)), tag.name)

def reduceChildByCss(soup, locator):
	reduceTags = soup.select(locator)[0]
	for idx,reduceTag in enumerate(reduceTags):
		if idx == 1:
			continue
		else:
			reduceTag.extract()
	return soup

def removeTagByCss(soup, locator):
	removeTags = soup.select(locator)
	for removeTag in removeTags:
		removeTag.extract()
	return soup

soup = bs(doc, 'html.parser')
soup = reduceChildByCss(soup, ".page-home-notification")
soup = removeTagByCss(soup, ".panel-heading")

dst_soup = bs(dst, 'html.parser')

src_constructor = ''.join(getHTMLConstructor(soup))
dst_constructor = ''.join(getHTMLConstructor(dst_soup))

print src_constructor == dst_constructor