from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """显示特定的主题"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries   }
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid(): #函数is_valid核实用户填写了所有必不可少的字段，且与要求的字段类型一致
            form.save() #将表单的数据写入数据库
            return HttpResponseRedirect(reverse('learning_logs:topics')) #重定向到页面topics
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """在特定主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id) # 从数据库中获取主题
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid(): 
            # 创建一个新的条目对象，存储到变量new_entry，不保存到数据库中
            new_entry = form.save(commit=False)# 传递实参commit=False
            new_entry.topic = topic 
            new_entry.save() #将表单的数据写入数据库
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id])) #重定向到页面topic
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """编辑条目"""
    entry = Entry.objects.get(id=entry_id) #获取要修改的条目对象
    topic = entry.topic #获取与条目关联的主题
    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry) #使用实参instance=entry创建一个EntryForm实例，创建一个表单
    else:
        # POST提交数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST) #同上，并根据request.POST中的数据修改
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


