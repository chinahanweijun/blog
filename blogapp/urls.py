
from django.conf.urls import url
from blogapp.views import *

urlpatterns = [
    url(r'^$', Index, name='index'),
    # 映射到归档页面
    url(r'^archive/', Archive, name='archive'),
    # 映射到文章页面
    url(r'^article/$', Article, name='article'),
    # 映射到提交评论页面
    url(r'^comment/post/$', Comment_post, name='comment_post'),
    # 映射到标签页面
    url(r'^tag/', Tag, name='tag'),
    # 映射到分类页面
    url(r'^category/$', Category, name='category'),
    # 登录注册注销
    url(r'^logout/$', Logout, name='logout'),
    url(r'^login/$', Login, name='login'),
    url(r'^reg/$', Reg, name='reg'),
]