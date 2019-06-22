
import time
from flask import render_template, jsonify, url_for

from . import main_bp


@main_bp.route('/')
def index():
    return render_template('main/index.html')


@main_bp.route('/news')
def news():
    return render_template('main/news.html')


@main_bp.route('/news_content/<int:page>')
def news_content(page):
    time.sleep(1)
    content_list = [{'img': url_for('static', filename='img/dt.jpg'),
                     'title': '武侯祠旁读《蜀相》，这一次诵读如此美妙',
                     'content': '不要以为孩子们静不下来，在精心制作的冥想音乐中，他们如此专心专注，甚至像个小菩萨，内心是安定的，缓缓的告别浮躁，找寻自我心底的宁静。'}]
    return jsonify({'content': render_template('main/news_content.html', content_list=content_list),
                    'next_url': url_for('.news_content', page=page+1) if page < 5 else ''})


@main_bp.route('/activities')
def activities():
    return render_template('main/activities.html')


@main_bp.route('/activities_content/<int:page>')
def activities_content(page):
    time.sleep(1)
    content_list = [{'img': url_for('static', filename='img/hd.jpg'),
                     'title': '陪伴成长——妈妈的坚持，转移到孩子的坚持',
                     'content': '亲子陪读有门道——挖掘中华经典的力量系列活动将于6月15日迎来第八期——陪伴成长——妈妈的坚持，转移到孩子的坚持，海光老师将与大家分享影响孩子坚持的几大因素。'}]
    return jsonify({'content': render_template('main/activities_content.html', content_list=content_list),
                    'next_url': url_for('.activities_content', page=page+1) if page < 5 else ''})


@main_bp.route('/works')
def works():
    return render_template('main/works.html')


@main_bp.route('/products')
def products():
    return render_template('main/products.html')


@main_bp.route('/about')
def about():
    return render_template('main/about.html')
