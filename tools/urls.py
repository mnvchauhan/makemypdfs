from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('tool/<str:tool_id>', views.show_tool, name='show_tool'),
    path('api/merge', views.process_merge, name='process_merge'),
    path('api/split', views.process_split, name='process_split'),
    path('api/compress', views.process_compress, name='process_compress'),
    path('api/pdf-to-word', views.process_pdf_to_word, name='process_pdf_to_word'), 
    path('download/<str:filename>', views.download_file, name='download_file'),
    path('api/pdf-to-jpg', views.process_pdf_to_jpg, name='process_pdf_to_jpg'),
    path('api/unlock-pdf', views.process_unlock_pdf, name='process_unlock_pdf'),
    path('api/word-to-pdf', views.process_word_to_pdf, name='process_word_to_pdf'),
    path('api/protect-pdf', views.process_protect_pdf, name='process_protect_pdf'),
    path('api/rotate-pdf', views.process_rotate_pdf, name='process_rotate_pdf'),
    path('api/pdf-to-powerpoint', views.process_pdf_to_powerpoint, name='process_pdf_to_powerpoint'),
    path('api/pdf-to-excel', views.process_pdf_to_excel, name='process_pdf_to_excel'),
    path('api/jpg-to-pdf', views.process_jpg_to_pdf, name='process_jpg_to_pdf'),
    path('api/excel-to-pdf', views.process_excel_to_pdf, name='process_excel_to_pdf'),
    path('api/watermark', views.process_watermark, name='process_watermark'),
    path('api/powerpoint-to-pdf', views.process_powerpoint_to_pdf, name='process_powerpoint_to_pdf'),
    path('api/organize-pdf', views.process_organize_pdf, name='process_organize_pdf'),
    path('api/pdf-to-pdfa', views.process_pdf_to_pdfa, name='process_pdf_to_pdfa'),
    path('api/sign-pdf', views.process_sign_pdf, name='process_sign_pdf'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]