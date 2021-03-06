from django.conf.urls import patterns, include, url
from django.contrib.auth.views import password_reset
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                           # Examples:
                           # url(r'^$', 'pms.views.home', name='home'),
                           # url(r'^pms/', include('pms.foo.urls')),

                           # Uncomment the admin/doc line below to enable admin documentation:
                           # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                           # Uncomment the next line to enable the admin:
                           url(r'^admin/', include(admin.site.urls)),
                           url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),
                           
                           url(r'^ckeditor/', include('ckeditor.urls')),

                           url(r'^home/$', 'client.views.home', name='home'),

                           url(r'^documents/', include('documents.urls')),
                          #url(r'^resest/password/',
                               #include('password_reset.urls')),
                           url(r'^password/reset/$', password_reset,
                               {'is_admin_site': True, 'template_name': 'people/my_password_reset_form.html'}),
                           url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done',
                               {'template_name': 'people/my_password_reset_done.html'}),
                           url(r'^reset/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm',
                               {'template_name': 'people/my_password_reset_confirm.html'}),
                           url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
                               {'template_name': 'people/my_password_reset_complete.html'}),

                           # ---------------------------------Client----------------------------------------------#

                           url(r'^client/(?P<task>(:?add|:?edit|:?delete|:?active))/(?P<id>[0-9]+)/$',
                               'client.views.client_details', name='client_details'),
                           url(r'^clients/$', 'client.views.client_list',
                               name='client_list'),
                           url(r'^client/view/(?P<id_disp>\d+)/$',
                               'client.views.display_client', name='display_client'),
                           url(r'^import/data/', 'client.views.import_data',
                               name='import_data'),
                           url(r'^client/dashboard/(?P<id_disp>\d+)/$',
                               'client.views.dash_client', name='dash_client'),
                           url('^recently/viewed/$', 'client.views.recently_viewed',
                               name='recently_viewed'),

                           # ---------------------------------Project---------------------------------------------#

                           url(r'^project/(?P<task>(:?add))/$',
                               'projects.views.project_details', name='project_add'),
                           url(r'^project/(?P<task>(:?add|:?edit|:?delete|:?active))/(?P<id>[0-9]+)/$',
                               'projects.views.project_details', name='project_details'),
                           url(r'^projects/$', 'projects.views.project_list',
                               name='project_list'),
                           url(r'^manager/(?P<task>(:?add|:?edit|:?delete|:?active))/$',
                               'projects.views.project_manager', name='project_manager'),
                           url(r'^managers/$', 'projects.views.managers_details',
                               name='managers_details'),
                           url(r'^project/view/(?P<id_disp>\d+)/$',
                               'projects.views.project_profile', name='project_profile'),
                           url(r'^getprojects/$', 'projects.views.getprojects',
                               name='getprojects'),
                           url(r'^modules/$', 'projects.views.getmodules',
                               name='modules_home'),
                           url('^project/dashboard/(?P<id_disp>\d+)/$',
                               'projects.views.project_dashboard', name='project_dashboard'),
                           #url(r'^tasks/view/(?P<id_disp>\d+)/$', 'projects.views.project_dashboard', name= 'task_with_no_assignees'),


                           #----------------------------------PEOPLE----------------------------------------------#

                           url(r'^person/(?P<task>(:?add))/$',
                               'people.views.people_details', name='people_details'),
                           url(r'^persons/$', 'people.views.person_list',
                               name='person_list'),
                           url(r'^person/view/(?P<id_disp>\d+)/$',
                               'people.views.display_people', name='display_people'),
                           url(r'^person/(?P<task>(:?edit|:?delete|:?active))/(?P<id>[0-9]+)/$',
                               'people.views.useredit', name='useredit'),
                           url(r'^$', 'people.views.login_user',
                               name='login_user'),
                           url(r'^login/$', 'people.views.login_user',
                               name='login_user'),
                           url(r'^logout/$', 'people.views.logout_user',
                               name='logout'),
                           url(r'^person/add-user/(?P<unval>.*)/$',
                               'people.views.person_add', name="person-add"),
                           url(r'^assign-projects-to-people/(?P<id_assign>\d+)/$', 'people.views.assigning_projects_to_persons', name="assigning_projects_to_persons"),
                           # url(r'^employers-home/$','people.views.employer_disp',name='employer_disp'),
                           # url(r'^project/permission/(?P<task>(:?add|:?edit|:?delete|:?active))/$','people.views.employee_details',name='employee_details'),
                           # url(r'^employer/(?P<task>(:?add|:?edit|:?delete|:?active))/$','people.views.employer',name='employer'),
                           # url(r'^project/permissions/$','people.views.employees_list',name='employees_list'),
                           #url(r'^person/add/$', 'people.views.add_user_for_client', name='add_user_for_client'),
                           # url(r'^import/data/','people.views.import_data',name='import_data'),




                           url(r'^admin/', include(admin.site.urls)),

                           url(r'^task/add-document/(?P<tid>\d+)/$',
                               'documents.views.add_document', name='add-document'),
                           url(r'^task/edit-document/(?P<tid>\d+)/$',
                               'documents.views.edit_document', name='edit-document'),
                           url(r'^task/delete-document/(?P<tid>\d+)/$',
                               'documents.views.delete_document', name='delete-document'),
                           url(r'^task/activate-document/(?P<tid>\d+)/$',
                               'documents.views.activate_document', name='activate-document'),
                           url(r'^task/add/$',
                               'tasks.views.task_add', name='add'),
                           url(r'^task/addmultiple/$',
                               'tasks.views.add_multiple_tasks', name='addm'),
                           url(r'task/overdue/$', 'tasks.views.task_overdue',
                               name='task_overdue'),
                           url(r'^tasks/$', 'tasks.views.task_home',
                               name='task'),
                           url(r'^tasks/view/(?P<id_disp>\d+)/$',
                               'tasks.views.task_detail_view', name='detail'),
                           url(r'^task/assigned/$',
                               'tasks.views.task_assigned', name='assign'),
                           url(r'^task/ownedby/$',
                               'tasks.views.task_ownedby', name='task'),
                           url(r'^task/following/$', 'tasks.views.task_following',
                               name='task_following'),
                           url(r'^gettasks/$', 'tasks.views.gettasks',
                               name='gettasks'),
                           url(r'^getmilestones/$', 'tasks.views.getmilestones',
                               name='getmilestones'),
                           url(r'^getmodules/$', 'tasks.views.getmodules',
                               name='getmodules'),
                           url(r'^getclients/$', 'projects.views.getclients',
                               name='getclients'),
                           url(r'^search/$', 'tasks.views.search',
                               name='search'),
                           url(r'^task/requests/$', 'tasks.views.task_requests',
                               name='task_requests'),
                           url(r'^task/request/add/$', 'tasks.views.task_request_add',
                               name='task_request_add'),
                           url(r'^task/request/view/(?P<id_disp>\d+)/$',
                               'tasks.views.task_request_view', name='task_request_view'),
                           url(r'^task/edit/(?P<id_edit>\d+)/$',
                               'tasks.views.task_edit', name='edit'),
                           url(r'^task/request/edit/(?P<id_edit>\d+)/$',
                               'tasks.views.task_request_edit', name='task_request_edit'),
                           url(r'^task/assign/(?P<id_disp>[0-9]+)/$',
                               'tasks.views.add_task_request_to_new_task', name='add_task_request_to_new_task'),
                           url(r'^task-commend/$', 'tasks.views.task_commend',
                               name="task-commend"),
                           #    url(r'^deletetasks/(?P<id_delete>\d+)/$','documents.views.deletetasks', name='deletetasks'),
                           url(r'^tasks/view/$', 'tasks.views.task_with_no_assignees',
                               name='task_with_no_assignees'),



                           # url for milestones
                           url(r'^milestone/view/(?P<id_disp>\d+)/$',
                               'milestones.views.view', name='view'),
                           url(r'^milestones/$',
                               'milestones.views.mile', name='mile'),
                           url(r'^milestones/view/(?P<id_disp>\d+)/$',
                               'milestones.views.milestone_view', name='milestone_view'),
                           url(r'^milestones/(?P<task>(:?add|:?edit))/(?P<id>[0-9]+)/$',
                               'milestones.views.addmilestone', name='addmilestone'),
                           url(r'^milestones/owned by me/$',
                               'milestones.views.milestone_owned_by', name='milestone_owned_by'),
                           url(r'^milestones/deactive/(?P<id_delete>\d+)/$',
                               'milestones.views.deletemilestones', name='deletemilestones'),
                           url(r'^milestones/active/(?P<id_active>\d+)/$',
                               'milestones.views.activemilestones', name='activemilestones'),
                           url(r'^gettasks/$', 'milestones.views.gettasks',
                               name='gettasks'),
                           url(r'^getstatus/S', 'milestones.views.getstatus',
                               name='getstatus'),
                           url(r'^getmilestones/$', 'milestones.views.getmilestones',
                               name='getmilestones'),
                           url(r'^getpeople/$', 'milestones.views.getpeople',
                               name='getpeople'),
                           url(r'^milestones/import/$',
                               'milestones.views.import_data_m', name='import_data_m'),
                           #url(r'^milestones/documents/$','milestones.views.milestone_documents', name='milestone_documents'),
                           #url(r'^addmilestonedocument/$', 'milestones.views.addmilestonedocument', name='addmilestonedocument'),
                           #url(r'^editmilestonedocument/(?P<id_edit>\d+)/$','milestones.views.editmilestonedocument', name='editmilestonedocument'),
                           url(r'^milestones/overdue/$',
                               'milestones.views.overdueview', name='overdueview'),
                           url(r'^milestones/search/$',
                               'milestones.views.search', name='search'),
                           url(r'^mile-comment/', 'milestones.views.milestone_comment',
                               name="mile_comment"),
                           url(r'^od/$', 'milestones.views.od', name='od'),
                           url(r'^gettasks_list', 'milestones.views.gettasks_list',
                               name="gettasks_list"),
                           url(r'^get_id_avaliable_task/$', 'milestones.views.addmilestone', name='addmilestone'),



                           #---------------------------Times----------------------------------------#
                           url(r'^times/$', 'times.views.times_home',
                               name='times_home'),
                           url(r'^addtimes/$', 'times.views.addtimes',
                               name='addtimes'),
                           url(r'^addmtimes/$', 'times.views.addmtimes',
                               name='addmtimes'),
                           url(r'^edittimes/(?P<id_edit>\d+)/$',
                               'times.views.edittimes', name='edittimes'),
                           url(r'^time view/$', 'times.views.timeview',
                               name='timeview'),
                           url(r'^Weekly hour graph/$',
                               'times.views.whg', name='whg'),
                           url(r'^times/manage/timesheets/(?P<task>(:?submit|:?approve|:?reject))/$',
                               'times.views.manage_time_sheets', name='manage_time_sheets'),
                           url(r'^times/manage/timesheets/',
                               'times.views.manage_timesheets', name='manage_timesheets'),
                           url(r'^Active timers/$',
                               'times.views.activetimer', name='activetimer'),
                           url(r'^Missing timesheets/$',
                               'times.views.missingtime', name='missingtime'),
                           url(r'^Submitted/$', 'times.views.sub', name='sub'),
                           #url(r'^Manage time/(?P<id_submit>\d+)/$','times.views.current_week', name='current_week'),
                           url(r'^Manage_time/$', 'times.views.current_week',
                               name='current_week'),
                           url(r'^get_project_tasks/$', 'projects.views.get_project_tasks', name='get_project_tasks'),
                           url(r'^add-times-sheets/$', 'times.views.times_sheet', name='times_sheet'),
                           url(r'^time-sheets/$', 'times.views.weekly_time_sheets', name='weekly_time_sheets'),



                           #----------------mastermodule-----------------------
                           url(r'^budgets/$', 'mastermodule.views.budget_details',
                               name='budget_details'),
                           url(r'^budget/(?P<task>(:?add|:?edit|:?delete|:?active))/$',
                               'mastermodule.views.budget', name='budget'),
                           url(r'^task-stauses-home/$', 'mastermodule.views.task_staus_details',
                               name='task_staus_details'),
                           url(r'^task-statuses/(?P<task>(:?add|:?edit|:?delete|:?active))/$',
                               'mastermodule.views.task_statuses', name='task_statuses'),
                           url(r'^modules-home/$', 'mastermodule.views.modules_details',
                               name='modules_details'),
                           url(r'^modules/(?P<task>(:?add|:?edit|:?delete|:?active))/$',
                               'mastermodule.views.modules', name='modules'),
                           url(r'^add settings/$', 'mastermodule.views.addsettings',
                               name='addsettings'),
                           url(r'^Settings & Defaults/$', 'mastermodule.views.settings_and_defaults',
                               name='settings_and_defaults'),
                           url(r'^editsettings/(?P<id_edit>\d+)/$',
                               'mastermodule.views.editsettings', name='editsettings'),
                           url(r'^settings/resource/categorization/(?P<task>(:?add|:?edit|:?delete|:?active))/(?P<id>[0-9]+)/$',
                               'mastermodule.views.resource_categorizations_details', name='resource_categorizations_details'),
                           url(r'^settings/resource/categorizations/$',
                               'mastermodule.views.resource_categorization_list', name='resource_categorization_list'),
                           url(r'^settings/project/categorization/(?P<task>(:?add|:?edit|:?delete|:?active))/(?P<id>[0-9]+)/$',
                               'mastermodule.views.project_categorization_details', name='project_categorizations_details'),
                           url(r'^settings/project/categorizations/$',
                               'mastermodule.views.project_categorization_list', name='project_categorization_list'),
                           url(r'^settings/task/priorities/(?P<task>(:?add|:?edit|:?delete|:?active))/(?P<id>[0-9]+)/$',
                               'mastermodule.views.task_priorities_details', name='task_priorities_details'),
                           url(r'^settings/task/priorities/$',
                               'mastermodule.views.task_priorities_list', name='task_priorities_list'),
                           url(r'^settings/statuses/$', 'mastermodule.views.task_staus_details',
                               name='task_staus_details'),
                           url(r'^settings/statuses/(?P<task>(:?add|:?edit|:?delete|:?active))/(?P<id>[0-9]+)/$',
                               'mastermodule.views.task_statuses', name='task_statuses'),


                           # --------------------Invoices ----------------------------------#
                           url(r'^invoices-home/$', 'invoice.views.invoices_details',
                               name='invoices_details'),
                           url(r'^invoice/$', 'invoice.views.invoice_add',
                               name='invoice_add'),
                           url(r'^invoice_edit/(?P<id_edit>\d+)/$',
                               'invoice.views.invoice_edit', name='invoice_edit'),
                           url(r'^invoice_delete/(?P<id_delete>\d+)/$',
                               'invoice.views.invoice_delete', name='invoice_delete'),
                           url(r'^import/invoice/',
                               'invoice.views.import_data', name='import_data'),
                               
                           url(r'^leavecalender/(?P<task>(:?add|:?edit|:?delete|:?active))/$', 'leavecalender.views.calender_details', name='calender_details'),
                           url(r'^leavecalender/$', 'leavecalender.views.clander_list', name='leavecalender-list'),
                           url(r'^leavecalender/view/$', 'leavecalender.views.clander_list', name='leavecalender-list'),
                           url(r'^resource/leavecalender/(?P<task>(:?add|:?edit|:?delete|:?active))/$', 'leavecalender.views.resource_calender_details', name='resource_calender_details'),
                           url('^resource/leavecalender/$', 'leavecalender.views.resource_leave_calender_list', name='resource_leave_calender_list'),
                           
                       )

#-------------Static files---------------------------------------#
urlpatterns += patterns('', (r'^static/(?P<path>,*)$',
                             'django.views.static.serve', {'document_root': 'static'}),)
