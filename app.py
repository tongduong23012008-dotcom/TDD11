import pandas as pd
import matplotlib.pyplot as plt

du_lieu = {
    "Họ và tên": ["Nguyễn Văn Anh", "Trần Thị An", "Lê Hoàng Chi", "Phạm Minh Dũng", "Hoàng Thị Lam", "Vũ Quang Huy", "Đặng Thu Hà", "Bùi Duy Khang", "Ngô Thị Lan", "Đỗ Minh Nam" ],
    "Điểm chuyên cần": [9.0, 8.5, 10.0, 7.5, 8.0, 9.5, 8.5, 6.5, 9.0, 7.0],
    "Điểm giữa kỳ":   [8.0, 7.5, 9.5,  6.0, 7.0, 8.5, 7.5, 5.5, 8.0, 6.5],
    "Điểm cuối kỳ":   [7.5, 8.0, 9.0,  5.5, 6.5, 9.0, 8.0, 6.0, 8.5, 7.0]
}
df = pd.DataFrame(du_lieu)

df["Điểm tổng kết"] = (0.2 * df["Điểm chuyên cần"]) + (0.3 * df["Điểm giữa kỳ"]) + (0.5 * df["Điểm cuối kỳ"])
df["Điểm tổng kết"] = df["Điểm tổng kết"].round(2)

xep_loai = []

for diem in df["Điểm tổng kết"]:
    if diem >= 8.5:
        xep_loai.append("Giỏi")
    elif diem >= 7.0 and diem < 8.5:
        xep_loai.append("Khá")
    elif diem >= 5.0 and diem < 7.0:
        xep_loai.append("Trung Bình")
    else:
        xep_loai.append("Yếu")

df["Xếp loại"] = xep_loai

diem_trung_binh = sum(df["Điểm tổng kết"])/len(df["Điểm tổng kết"])

print(f"Điểm trung bình: {round(diem_trung_binh, 2)}")
idx_max = df["Điểm tổng kết"].idxmax()
idx_min = df["Điểm tổng kết"].idxmin()

print(f"Điểm tổng kết cao nhất: {df.loc[idx_max, 'Họ và tên']} ({df.loc[idx_max, 'Điểm tổng kết']} điểm)")
print(f"Điểm tổng kết thấp nhất: {df.loc[idx_min, 'Họ và tên']} ({df.loc[idx_min, 'Điểm tổng kết']} điểm)")

so_sinh_vien_dat_duoc = sum(1 for d in df["Điểm tổng kết"] if d >= 5.0)
print(f"Số sinh viên đạt: {so_sinh_vien_dat_duoc}\n")
#
plt.barh(df["Họ và tên"], df["Điểm tổng kết"])   
plt.xlabel("Điểm Tổng Kết")                     
plt.ylabel("Sinh Viên")                         
plt.title("Điểm tổng kết của 10 sinh viên")
plt.xlim(0, 10)                                 
plt.tight_layout()
plt.show()
