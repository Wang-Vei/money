# Generated by Django 2.1.3 on 2019-01-13 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Con',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('gt_con', models.CharField(max_length=200, verbose_name='沟通内容')),
                ('talker', models.IntegerField(choices=[(0, '客户'), (1, '客服')], default=0, verbose_name='发言者')),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '客服记录',
                'verbose_name_plural': '客服记录',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('con', models.TextField(max_length=2000, verbose_name='资讯内容')),
                ('img', models.ImageField(default='', upload_to='financing/static/img/', verbose_name='图片')),
                ('author', models.CharField(max_length=10, verbose_name='作者')),
                ('s_id', models.IntegerField(choices=[(0, '未发布'), (1, '发布')], default=0, verbose_name='是否发布')),
            ],
            options={
                'verbose_name': '资讯',
                'verbose_name_plural': '资讯',
            },
        ),
        migrations.CreateModel(
            name='Kcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('outdate', models.IntegerField(choices=[(0, '已过期'), (1, '未使用'), (2, '已使用')], default=0, verbose_name='是否过期')),
                ('type', models.IntegerField(choices=[(0, '折扣券'), (1, '加息券')], default=0, verbose_name='卡片类型')),
                ('money', models.CharField(default=998, max_length=10, verbose_name='金额')),
                ('use_person', models.IntegerField(choices=[(0, '新手用户专享'), (1, '老用户专享')], default=0, verbose_name='使用分类')),
                ('tz_money', models.CharField(default=10000, max_length=10, verbose_name='投资金额')),
                ('tz_date', models.CharField(default=30, max_length=4, verbose_name='投资期限')),
                ('yxq_date', models.IntegerField(default=1, verbose_name='有效年限')),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '卡包',
                'verbose_name_plural': '卡包',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=50, verbose_name='消息标题')),
                ('con', models.TextField(max_length=2000, verbose_name='消息内容')),
                ('type', models.IntegerField(choices=[(0, '金额方面'), (1, '产品方面'), (2, '其他')], default=0, verbose_name='消息类型')),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '个人消息',
                'verbose_name_plural': '个人消息',
            },
        ),
        migrations.CreateModel(
            name='MyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=11, verbose_name='电话')),
                ('img', models.CharField(max_length=100, verbose_name='头像')),
                ('z_money', models.CharField(max_length=20, verbose_name='总资产')),
                ('d_money', models.CharField(max_length=20, verbose_name='待收收益')),
                ('lj_money', models.CharField(max_length=20, verbose_name='累计收益')),
                ('ky_money', models.CharField(max_length=20, verbose_name='可用余额')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=50, verbose_name='公告标题')),
                ('con', models.TextField(max_length=2000, verbose_name='公告内容')),
            ],
            options={
                'verbose_name': '平台公告',
                'verbose_name_plural': '平台公告',
            },
        ),
        migrations.CreateModel(
            name='Pl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('con', models.CharField(max_length=150, verbose_name='评论内容')),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='基金名称')),
                ('risk', models.IntegerField(choices=[(0, '高风险'), (1, '中风险'), (2, '低风险')], default=0, verbose_name='风险')),
                ('startmoney', models.CharField(max_length=10, verbose_name='起投金额(元)')),
                ('investment_date', models.CharField(max_length=10, verbose_name='投资期限(天)')),
                ('annual_income', models.CharField(max_length=10, verbose_name='年化收益(%)')),
                ('num', models.IntegerField(verbose_name='买过人数')),
                ('latest_val', models.CharField(max_length=10, verbose_name='最新净值')),
                ('drop_range', models.CharField(max_length=10, verbose_name='日涨跌幅(%)')),
                ('money', models.CharField(max_length=10, verbose_name='购买金额(元)')),
            ],
            options={
                'verbose_name': '产品信息',
                'verbose_name_plural': '产品信息',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(0, '2012'), (1, '2013'), (2, '2014'), (3, '2015'), (4, '2016'), (5, '2017'), (6, '2018')], default=0, verbose_name='年份')),
                ('rate', models.CharField(max_length=5, verbose_name='收益率(%)')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financing.Product', verbose_name='产品')),
            ],
            options={
                'verbose_name': '收益率',
                'verbose_name_plural': '收益率',
            },
        ),
        migrations.CreateModel(
            name='Selfproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('y_earning', models.CharField(max_length=50, verbose_name='昨日收益(元)')),
                ('h_earning', models.CharField(max_length=50, verbose_name='持有收益(元)')),
                ('dateLimit', models.IntegerField(default=0, verbose_name='到期期限')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financing.Product', verbose_name='产品')),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '持有产品',
                'verbose_name_plural': '持有产品',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('author', models.CharField(max_length=10, verbose_name='作者')),
                ('vid', models.FileField(default='', upload_to='financing/static/video/', verbose_name='视频地址')),
                ('s_id', models.IntegerField(choices=[(0, '未发布'), (1, '发布')], default=0, verbose_name='是否发布')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
        migrations.CreateModel(
            name='Ycard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=10, verbose_name='银行')),
                ('card_lx', models.IntegerField(choices=[(0, '储蓄卡'), (1, '信用卡')], default=0, verbose_name='银行卡类型')),
                ('card_number', models.CharField(max_length=16, verbose_name='卡号')),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '银行卡',
                'verbose_name_plural': '银行卡',
            },
        ),
        migrations.AddField(
            model_name='pl',
            name='v',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financing.Video', verbose_name='视频'),
        ),
    ]
