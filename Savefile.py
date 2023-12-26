import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os
# dulieux=[("['__label__sức_khỏe']", 'cao răng cặn cứng muối vô_cơ cặn mềm mảnh vụn thức_ăn chất_khoáng miệng lắng_đọng huyết_thanh gây lấy cao răng định_kỳ tháng tránh bệnh viêm nướu nha chu nhiễm_trùng chân_răng tuy_nhiên tiện cơ_sở nha_khoa có_thể loại_bỏ cao răng nhà một_số'), ("['__label__âm_nhạc']", 'dường_như gần thị_trường game việt nam sôi_nổi bao_giờ hết liên_tiếp tựa game mua game fly high nữ thần chi ca trường_hợp ngoại_lệ'), ("['__label__xe_360']", 'bối_cảnh sức_mua ô_tô đà sụt_giảm doanh_số bán chưa cải_thiện dù nhà_sản_xuất đại_lý ô_tô áp_dụng ưu_đãi _liệu chính_sách giảm 50 lệ_phí trước_bạ tiếp_tục áp_dụng đủ sức vực dậy thị_trường ô_tô'), ("['__label__kinh_doanh']", 'thời_điểm cuối nhận lương lao_động luôn trông_chờ tiền thưởng công_ty _vậy nhân_viên công_ty game hoạt_động mảng esports thì thưởng tết'), ("['__label__xuất_bản']", 'miền trung tận cà_mau sinh_sống 30 tôi chưa trò_chuyện quê_hương thứ làm_sao cất lời gượng sáo đọc tác_phẩm dự thi nghĩa_tình miền tây'), ("['__label__sức_khỏe']", 'mặc_dù cực_kỳ hiếm triệu_chứng giống parkinson xảy một_số covid 19'), ("['__label__thể_thao']", 'tay_vợt tuổi teen shang juncheng lịch_sử 16 trở_thành tay_vợt nam_trung_quốc đầu_tiên giành chiến_thắng trận đấu đơn giải quần_vợt úc mở_rộng')]
def luuexcel(dulieu):
    data = pd.DataFrame(dulieu)
    root = tk.Tk()
    root.withdraw()


    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    data.to_excel(file_path, index=False)
def chonfile():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("Excel files", "*.xlsx*")))
    file_ext = os.path.splitext(filename)[1]
    if file_ext.endswith('.txt'):
        #  Đọc file txt
        with open(filename, 'r',encoding="utf-8") as f:
            data = f.read()
    elif file_ext.endswith('.xlsx'):
        # Đọc file Excel
        with open(filename, 'r',errors='ignore') as f:
            data = pd.read_excel(f)
    return data