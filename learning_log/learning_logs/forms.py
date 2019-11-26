from django import forms #导入form模块
from .models import Topic, Entry #导入Topic.Entry模型
class TopicForm(forms.ModelForm): #定义TopicForm类，继承forms.ModelFrom
    # 最简单的ModelFrom，只有一个内嵌的Meta类，让Django根据某个模型创建表单
    class Meta:
        model = Topic #根据Topic模型创建一个表单
        fields = ['text'] #表单只包含text字段
        labels = {'text': ''} #不要为字段创建标签

class EntryForm(forms.ModelForm): #定义EntryForm类，继承forms.ModelFrom
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        # 小部件widget是一个html表单元素，如单行文本框、多行文本框区域、下拉列表
        # 设置widget，可覆盖Django选择的默认小部件
        # 使用form.Textarea，定制字段'text'的输入小部件
        # 将文本区域的宽度设置为80列（默认40）
