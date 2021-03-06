"""OpsManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from OpsManage.views import (index,assets,cron,deploy,
                             ansible,users,wssh,task,
                             database)
from rest_framework.urlpatterns import format_suffix_patterns
from OpsManage.restfull import (assets_api,cron_api,deploy_api,
                                ansible_api,users_api,logs_api,
                                db_api)


urlpatterns = [
    url(r'^$',index.index),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/',index.login),  
    url(r'^logout',index.logout), 
    url(r'^config',index.config), 
    url(r'^noperm',index.noperm), 
    url(r'^assets_config',assets.assets_config), 
    url(r'^assets_add',assets.assets_add), 
    url(r'^assets_list',assets.assets_list), 
    url(r'^assets_mod/(?P<aid>[0-9]+)/$',assets.assets_modf), 
    url(r'^assets_view/(?P<aid>[0-9]+)/$',assets.assets_view),
    url(r'^assets_facts',assets.assets_facts),
    url(r'^assets_log/(?P<page>[0-9]+)/$',assets.assets_log),
    url(r'^assets_import/',assets.assets_import),
    url(r'^assets_search/',assets.assets_search),
    url(r'^assets_server/',assets.assets_server),
    url(r'^assets/batch/',assets.assets_batch),
    url(r'^cron_add',cron.cron_add),
    url(r'^cron_list/(?P<page>[0-9]+)/$',cron.cron_list),
    url(r'^cron_config',cron.cron_config),
    url(r'^cron_log/(?P<page>[0-9]+)/$',cron.cron_log),
    url(r'^cron_mod/(?P<cid>[0-9]+)/$',cron.cron_mod),
    url(r'^deploy_add',deploy.deploy_add),
    url(r'^deploy_list',deploy.deploy_list),
    url(r'^deploy_log/(?P<page>[0-9]+)/$',deploy.deploy_log),
    url(r'^deploy_mod/(?P<pid>[0-9]+)/$',deploy.deploy_modf),
    url(r'^deploy_init/(?P<pid>[0-9]+)/$',deploy.deploy_init),
    url(r'^deploy_version/(?P<pid>[0-9]+)/$',deploy.deploy_version),    
    url(r'^deploy_run/(?P<pid>[0-9]+)/$',deploy.deploy_run),
    url(r'^deploy_result/(?P<pid>[0-9]+)/$',deploy.deploy_result),
    url(r'^deploy_ask/(?P<pid>[0-9]+)/$',deploy.deploy_ask),
    url(r'^deploy_order/(?P<page>[0-9]+)/$',deploy.deploy_order),
    url(r'^deploy_order/status/(?P<pid>[0-9]+)/$',deploy.deploy_order_status),
    url(r'^deploy_order/rollback/(?P<pid>[0-9]+)/$',deploy.deploy_order_rollback),
    url(r'^deploy_manage/(?P<pid>[0-9]+)/$',deploy.deploy_manage),
    url(r'^apps/$',ansible.apps_list),
    url(r'^apps/model/$',ansible.apps_model),
    url(r'^apps/script/online/$',ansible.apps_script_online),
    url(r'^apps/script/list/$',ansible.apps_script_list),
    url(r'^apps/script/file/(?P<pid>[0-9]+)/$',ansible.apps_script_file),
    url(r'^apps/script/run/(?P<pid>[0-9]+)/$',ansible.apps_script_online_run),
    url(r'^apps/run/$',ansible.ansible_run),
    url(r'^apps/log/$',ansible.ansible_log),
    url(r'^apps/log/(?P<model>[a-z]+)/(?P<id>[0-9]+)/$',ansible.ansible_log_view),
    url(r'^apps/playbook/upload/$',ansible.apps_upload),
    url(r'^apps/playbook/online/$',ansible.apps_online),
    url(r'^apps/playbook/file/(?P<pid>[0-9]+)/$',ansible.apps_playbook_file),  
    url(r'^apps/playbook/run/(?P<pid>[0-9]+)/$',ansible.apps_playbook_run),    
    url(r'^apps/playbook/modf/(?P<pid>[0-9]+)/$',ansible.apps_playbook_modf),   
    url(r'^apps/playbook/online/modf/(?P<pid>[0-9]+)/$',ansible.apps_playbook_online_modf), 
    url(r'^db/config/$',database.db_config), 
    url(r'^db/sql/order/audit/$',database.db_sqlorder_audit), 
    url(r'^db/sql/control/$',database.db_sql_control), 
    url(r'^db/sql/order/list/(?P<page>[0-9]+)/$',database.db_sqlorder_list),
    url(r'^db/sql/order/run/(?P<id>[0-9]+)/$',database.db_sqlorder_run),
    url(r'^db/sql/order/osc/(?P<id>[0-9]+)/$',database.db_sqlorder_osc),
    url(r'^db/sql/order/search/$',database.db_sqlorder_search),
    url(r'^db/ops/$',database.db_ops),
    url(r'^db/sql/dumps/$',database.db_sql_dumps),
    url(r'^db/sql/logs/(?P<page>[0-9]+)/$',database.db_sql_logs),
    url(r'^task_model/$',task.task_model),
    url(r'^task_view/$',task.task_view),
    url(r'^task_search/$',task.task_search),
    url(r'^users/manage$',users.user_manage),
    url(r'^register/',users.register),
    url(r'^user/(?P<uid>[0-9]+)/$',users.user),
    url(r'^user/center/$',users.user_center),
    url(r'^user/server/(?P<uid>[0-9]+)/$',users.user_server),
    url(r'^group/(?P<gid>[0-9]+)/$',users.group),
    url(r'^api/assets/$', assets_api.asset_list), 
    url(r'^api/assets/(?P<id>[0-9]+)/$', assets_api.asset_detail),
    url(r'^api/service/$', assets_api.service_list), 
    url(r'^api/service/(?P<id>[0-9]+)/$', assets_api.service_detail), 
    url(r'^api/project/$', assets_api.project_list), 
    url(r'^api/project/(?P<id>[0-9]+)/$', assets_api.project_detail),     
    url(r'^api/group/$', assets_api.group_list), 
    url(r'^api/group/(?P<id>[0-9]+)/$',assets_api.group_detail), 
    url(r'^api/user/$', users_api.user_list), 
    url(r'^api/user/(?P<id>[0-9]+)/$',users_api.user_detail), 
    url(r'^api/zone/$', assets_api.zone_list), 
    url(r'^api/zone/(?P<id>[0-9]+)/$',assets_api.zone_detail), 
    url(r'^api/line/$', assets_api.line_list), 
    url(r'^api/line/(?P<id>[0-9]+)/$',assets_api.line_detail),     
    url(r'^api/raid/$', assets_api.raid_list), 
    url(r'^api/raid/(?P<id>[0-9]+)/$',assets_api.raid_detail),     
    url(r'^api/server/$', assets_api.asset_server_list), 
    url(r'^api/server/(?P<id>[0-9]+)/$', assets_api.asset_server_detail), 
    url(r'^api/net/$', assets_api.asset_net_list), 
    url(r'^api/net/(?P<id>[0-9]+)/$', assets_api.asset_net_detail),  
    url(r'^api/cron/$', cron_api.cron_list),  
    url(r'^api/cron/(?P<id>[0-9]+)/$', cron_api.cron_detail),  
    url(r'^api/deploy/$', deploy_api.deploy_list),  
    url(r'^api/deploy/(?P<id>[0-9]+)/$', deploy_api.deploy_detail),    
    url(r'^api/playbook/$', ansible_api.playbook_list),  
    url(r'^api/playbook/(?P<id>[0-9]+)/$', ansible_api.playbook_detail),
    url(r'^api/order/(?P<username>.+)/$', deploy_api.OrderList.as_view()),
    url(r'^api/logs/assets/(?P<id>[0-9]+)/$', assets_api.assetsLog_detail),
    url(r'^api/logs/cron/(?P<id>[0-9]+)/$', cron_api.cronLogsdetail),
    url(r'^api/logs/ansible/model/(?P<id>[0-9]+)/$', ansible_api.modelLogsdetail),
    url(r'^api/logs/ansible/playbook/(?P<id>[0-9]+)/$', ansible_api.playbookLogsdetail),
    url(r'^api/logs/deploy/(?P<id>[0-9]+)/$', deploy_api.deployLogs_detail),
    url(r'^api/logs/search/model/$', logs_api.AnsibleModelLogsList),
    url(r'^api/logs/search/playbook/$', logs_api.AnsiblePlayBookLogsList),
    url(r'^api/logs/sql/(?P<id>[0-9]+)/$', db_api.sql_exec_logs),
    url(r'^api/inc/config/$', db_api.inc_list),
    url(r'^api/inc/config/(?P<id>[0-9]+)/$', db_api.inc_detail),
    url(r'^api/db/config/$', db_api.db_list),
    url(r'^api/db/config/(?P<id>[0-9]+)/$', db_api.db_detail),
    url(r'^api/sql/order/(?P<id>[0-9]+)/$', db_api.sql_order_detail),
    url(r'^api/sql/custom/$', db_api.sql_custom_list),
    url(r'^api/sql/custom/(?P<id>[0-9]+)/$', db_api.sql_custom_detail),
    url(r'^webssh/(?P<sid>[0-9]+)/$',wssh.wssh),
]

urlpatterns = format_suffix_patterns(urlpatterns)